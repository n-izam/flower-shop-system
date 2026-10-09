from .base import *

DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

# Allow cross-origin requests for local web/mobile development
CORS_ALLOW_ALL_ORIGINS = True