from decouple import config

if config('ENV') == 'local':
    from .local import *
else:
    from .prod import *
