import logging
from logging.handlers import RotatingFileHandler
import sys
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s|%(filename)s|%(asctime)s|%(message)s")

# STDERR (everything above and including WARN)
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setFormatter(formatter)
stderr_handler.setLevel(logging.WARN)
logger.addHandler(stderr_handler)

class MakeRotatingFileHandler(RotatingFileHandler):
    def __init__(self, filename, **kwargs):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        super().__init__(filename, **kwargs)

try:
    stats_handler = MakeRotatingFileHandler('logs/stats.log', backupCount=2, maxBytes=1000)
    stats_handler.setFormatter(formatter)
    stats_handler.setLevel(logging.INFO)
    logger.addHandler(stats_handler)
except PermissionError:
    logger.warn("Could not set the stats_FileHandler due to a permission error. Don't use both local and docker")
    pass
