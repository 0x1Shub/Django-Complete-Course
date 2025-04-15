import os

env = os.getenv("DJANGO_ENV") or "dev"
if env == "prod":
    from .settings.prod import *
else:
    from .settings.dev import *
