
CSRF_ENABLED = True
SECRET_KEY = 'isnt-foobar-pretty-secret-for-you'

try:
    from local_config import *
except ImportError:
    print(" * Using default config")
    pass
