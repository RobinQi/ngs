#!/usr/bin/python

import os,sys
import logging
########################################
# __author__ = 'Robin Qi'              #
#__email__ = 'yanbingqi6@outlook.com'  #
########################################

LOG_FORMAT = '%(asctime)s [%(levelname)s - %(module)s] %(message)s'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
FORMATTER = logging.Formatter(LOG_FORMAT,TIME_FORMAT)
def add_file_handler(logger, log_file = 'pipeline.log',log_level = logging.INFO):
    fh = logging.FileHandler(log_file)
    fh.setFormatter(FORMATTER)
    fh.setLevel(log_level)
    logger.addHandler(fh)
def add_stream_handler(logger, stream = sys.stdout, log_level = logging.INFO):
    sh = logging.StreamHandler(stream = stream)
    sh.setFormatter(FORMATTER)
    sh.setLevel(log_level)
    logger.addHandler(sh)

def initialize_logger(logger, log_file = None, stream = None, debug = False):
    if debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    logger.setLevel(log_level)
    if log_file:
        add_file_handler(logger, log_file = log_file, log_level = log_level)
    if stream:
        add_stream_handler(logger, log_file = log_file, log_level = log_level)