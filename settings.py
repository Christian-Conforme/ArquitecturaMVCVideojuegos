# settings.py

# ...existing code...

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # Si estás usando un backend personalizado para el correo electrónico, agrégalo aquí
)

# Eliminar la configuración de LOGIN_URL
# LOGIN_URL = 'iniciar_sesion'

# ...existing code...