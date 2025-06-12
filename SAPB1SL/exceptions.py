################################################
#                   BLPG                       #   
################################################

class SAPServiceLayerError(Exception):
    pass

class AuthenticationError(SAPServiceLayerError):
    pass

class SAPRequestError(SAPServiceLayerError):
    def __init__(self, status_code, message):
        super().__init__(f"Error {status_code}: {message}")
        self.status_code = status_code
        self.message = message
