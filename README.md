#  sap_service_layer

Cliente Python ligero para conectarse al **Service Layer de SAP Business One** utilizando `requests`. Esta librería facilita la autenticación, el manejo de sesiones, la reconexión automática y la ejecución de peticiones HTTP de forma robusta, sencilla y limpia.

##  Características

-  Autenticación al Service Layer de SAP B1
-  Reconexión automática cuando la sesión expira
-  Métodos simplificados: `get()`, `post()`, `patch()`, `delete()`
-  Código limpio y mantenible, ideal para entornos productivos
-  Útil para integraciones backend, automatizaciones o servicios web

##  Instalación

Puedes instalar esta librería directamente desde PyPI (una vez publicada):

```bash
pip install sap-service-layer
```
---
## 🚀 Ejemplo de uso

```python
from sap_service_layer import SAPServiceLayerClient

client = SAPServiceLayerClient(
    base_url="https://mi-servidor-sap:50000/b1s/v1",
    company_db="SBODemoCL",
    username="manager",
    password="1234"
)

response = client.get("BusinessPartners?$top=5")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
```
---
## Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT. Ver archivo LICENSE para más detalles.

---

## Autor
Bryan Luis Pineda
Linkedin: https://www.linkedin.com/in/blpg/

---

## Contribuciones
Este proyecto es de código abierto, pero cualquier cambio debe ser aprobado previamente por el autor. Si deseas colaborar, abre un issue primero o contáctame directamente por LinkedIn.
