GOOGLE_OAUTH2_CLIENT_ID = '<your-client-id>'
GOOGLE_OAUTH2_CLIENT_SECRET = '<your-client-secret>'
GOOGLE_OAUTH2_REDIRECT_URI = 'http://localhost:8000/rest/v1/calendar/redirect/'
import os

SECRET_KEY = os.environ['SECRET_KEY']
import secrets

print(secrets.token_hex(24))

SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/tmp/django_sessions'
INSTALLED_APPS = [
    ...
    'calendar_integration',
    'django.contrib.sessions',
]

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
]
