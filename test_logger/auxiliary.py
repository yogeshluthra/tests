import logging
from logging.handlers import RotatingFileHandler
import os

def add_file_log(log_file_name, logger=None):
    FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    handler = RotatingFileHandler(log_file_name, maxBytes=3 * 1024 * 1024, backupCount=5, encoding='utf-8')
    handler.setFormatter(FORMATTER)
    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
    logger.parent.addHandler(handler)
    print(logger.parent.name)
    logger.info("in auxiliary.py")
    return logger