import logging
import sys
from logging import StreamHandler


def init(app):
    log_handler = StreamHandler(sys.stdout)
    formatter = logging.Formatter(app.config['LOG_FORMAT'])
    log_handler.setFormatter(formatter)

    # set the app logger level
    app.logger.setLevel(app.config['LOG_LEVEL'])

    app.logger.addHandler(log_handler)
