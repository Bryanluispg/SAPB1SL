##############################################
#                   BLPG                     #   
##############################################

import requests
from .exceptions import AuthenticationError, SAPRequestError
import urllib3

urllib3.disable_warnings()
class SAPB1SL:
    def __init__(self, base_url, username, password, company_db, max_retries=1):
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.company_db = company_db
        self.max_retries = max_retries

        self.session = requests.Session()
        self.session_id = None
        self.route_id = None

        self._login()

    def _login(self):
        url = f"{self.base_url}/Login"
        data = {
            "UserName": self.username,
            "Password": self.password,
            "CompanyDB": self.company_db
        }
        response = self.session.post(url, json=data, verify=False)
        if response.status_code != 200:
            raise AuthenticationError(f"Login failed: {response.text}")

        result = response.json()
        self.session_id = result.get("SessionId")
        self.route_id = result.get("RouteId")
        self.session.headers.update({
            "Cookie": f"B1SESSION={self.session_id}; ROUTEID={self.route_id}"
        })

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        attempt = 0

        while attempt <= self.max_retries:
            response = self.session.request(method, url, **kwargs, verify=False)

            if response.status_code == 401 or "Session" in response.text:
                attempt += 1
                if attempt > self.max_retries:
                    raise AuthenticationError("Sesión expirada y reintento fallido.")
                self._login()
                continue

            if not response.ok:
                raise SAPRequestError(response.status_code, response.text)
            return response.json() if response.content else None

    def get(self, endpoint, params=None):
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint, data):
        return self._request("POST", endpoint, json=data)

    def patch(self, endpoint, data):
        return self._request("PATCH", endpoint, json=data)

    def delete(self, endpoint):
        return self._request("DELETE", endpoint)

    def logout(self):
        try:
            self.session.post(f"{self.base_url}/Logout")
        except Exception:
            pass
