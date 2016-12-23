#!/usr/bin/python

import os,sys
import logging
import argparse

args = argparse.Namespace()
log = logging.getLogger()

def parse_args():
    desc = 'pipeline to process ngs sequencing data'
    parser = argparse.ArgumentParser(description=desc)
    add_argument = parser.add_argument
    add_argument('-c','--config',
                 metavar='config_file',
                 help='configure file')
    parser.parse_args( namespace=args )








