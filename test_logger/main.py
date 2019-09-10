import logging.config

from test_logger.auxiliary import *

def log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger

print(log().name)
add_file_log('{}/{}_job_{}_worker_{}.log'.format('.', "tests", 1, 1))
log().info("in main.py")
