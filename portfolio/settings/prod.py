from decouple import config

from .base import *

DEBUG = config("DEBUG", False, cast=bool)

ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "format_1": {
            "format": "{asctime} : {levelname} : {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(
                BASE_DIR,
                config("LOG_FILE_FOLDER"),
                config("LOG_FILE_NAME"),
            ),
            "formatter": "format_1",
        },
    },
    "loggers": {
        "general": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

try:
    from .local import *
except ImportError:
    pass
