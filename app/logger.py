import logging
from logging.handlers import RotatingFileHandler
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s|%(filename)s|%(asctime)s|%(message)s")

# STDERR (everything above and including WARN)
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setFormatter(formatter)
stderr_handler.setLevel(logging.WARN)
logger.addHandler(stderr_handler)

try:
    stats_handler = RotatingFileHandler('logs/stats.log', backupCount=2, maxBytes=1000)
    stats_handler.setFormatter(formatter)
    stats_handler.setLevel(logging.INFO)  # type:ignore
    # stats_handler.addFilter(lambda record: record.levelno == logging.INFO)  # type:ignore
    logger.addHandler(stats_handler)
except PermissionError:
    logger.warn("Could not set the stats_FileHandler due to a permission error. Don't use both local and docker")
    pass
