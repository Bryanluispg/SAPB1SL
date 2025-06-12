import uiautomator2 as u2

d = u2.connect()

# Instala los servicios necesarios si no están aún
d.app_install("https://github.com/openatx/atx-agent/releases/download/0.10.0/atx-agent.apk")

# Inicia uiautomator
d.uiautomator.start()

# Opcional: comprueba que responde
print(d.info)
