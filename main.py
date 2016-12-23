#!/usr/bin/python

######################################
#__authour__ = 'Robin Qi'            #
#__email__ = 'yanbingqi6@outlook.com'#
######################################

import os,sys
import yaml
import logging
import argparse
from io.args import parse_args,args
import subprocess
from  log.log import initialize_logger
from pipeline.qc import qc

log = logging.getLogger()

class main( object ):
    def __init__(self):
        parse_args()
        self.__dict__.update(vars(args))
        self.config_file = args.config
        with open(self.config_file) as handle:
            self.config = yaml.load(handle)
        self.initiate_log_output()
        initialize_logger(log,log_file = self.log_file )
    def initiate_log_output(self):
        log_dir = self.config['log']['dir']
        if os.path.exists(log_dir):
            pass
        else:
            try:
                os.mkdir(log_dir + '/log')
            except OSError:
                pass
        log_name = str(self.config['pipeline']) + '.log'
        self.log_file = os.path.join(log_dir,log_name)
    def run_pipeline(self):
        if self.config['pipeline'] == 'qc':
            self.run_qc()
        elif self.config['pipeline'] == 'alignment':
            self.run_alignment()
    def run_qc(self):
        qc(dir = self.config['softwares']['fastx_toolkit']['dir'],input = self.config['input']['dir'],output = self.config['output']['dir'])
    def run_alignment(self):
        pass

if __name__ == '__main__':
    test = main()
    test.run_pipeline()

