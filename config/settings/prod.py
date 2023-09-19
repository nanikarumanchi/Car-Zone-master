from .base import *

DEBUG = True  # for serving media files

ALLOWED_HOSTS = ['.herokuapp.com']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
