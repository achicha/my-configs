from raven import Client

client = Client('http://<key>:<secret>@0.0.0.0:9000/1')

try:
    1 / 0
except ZeroDivisionError:
	client.captureException()

##############################################################
from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging
import logging

# add handler
handler = SentryHandler('http://<key>:<secret>@0.0.0.0:9000/1')
handler.setLevel(logging.ERROR)
setup_logging(handler)

# create logger
logger = logging.getLogger(__name__)

# If you're actually catching an exception, use `exc_info=True`
logger.error('There was an error, with a stacktrace!', exc_info=True)

# If you don't have an exception, but still want to capture a
# stacktrace, use the `stack` arg
logger.error('There was an error, with a stacktrace!', extra={'stack': True,})

#############################################################
# load config from dict
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)6s] %(name)s '
                      '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',

            'datefmt': '%Y/%m/%d %H:%M:%S',
            },
        },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
            },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'console',
            'when': 'D',
            'interval': 30,
            'filename': 'folder/filename.log'
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': 'http://<key>:<secret>@0.0.0.0:9000/1',
            },
        },

    'loggers': {
        '': {
            'handlers': ['console', 'file', 'sentry'],
            'level': 'DEBUG',
            'propagate': False,
            },
        'your_app': {
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

