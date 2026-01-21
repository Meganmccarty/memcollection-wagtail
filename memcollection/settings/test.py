from .base import *  # noqa: F403, F401

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Using af Fake key for testing
SECRET_KEY = "fake-key"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),  # noqa: F405
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "test",
        "USER": "test",
        "PASSWORD": "test",
        "HOST": "localhost",
        "PORT": 5432,
    }
}
