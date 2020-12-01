import sys
import logging


class LogFormatter(logging.Formatter):
    """
        Custom log formatting
        (https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output)
    """
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;1m"
    blue = "\x1b[36;1m"
    red = "\x1b[31;1m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey,
        logging.INFO: blue,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red
    }

    def __init__(self, fmt="%(asctime)s | %(message)s"):
        super(LogFormatter, self).__init__()
        self.fmt = fmt


    def format(self, record):
        log_fmt_color = self.FORMATS.get(record.levelno)
        log_fmt = log_fmt_color + self.fmt + self.reset
        formatter = logging.Formatter(log_fmt)

        return formatter.format(record)

class DefaultLogger():

    @staticmethod
    def get_log():
        log = logging.getLogger(__name__)
        log.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(LogFormatter())

        log.addHandler(handler)

        return log