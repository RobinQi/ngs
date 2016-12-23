#!/usr/bin/python

import os,sys
import logging
import subprocess
from util import stdout_stderr

log = logging.getLogger()

def qc(dir=None,input=None,output=None):
    log.info('start to run qc step using fastx_toolkit software')
    stdout_h,stderr_h = stdout_stderr(output=output,pipeline='QC')

    cmd = ['/opt/software/fastax_toolkit/bin/fastq_to_fasta','-i','/userdata/PB/raw_data/ngs/demo.fastq',
           '-o','/userdata/PB/raw_data/ngs/demo.fasta','-Q 33']
    p = subprocess.Popen(cmd,stdout=stdout_h,stderr=stderr_h)
    stdout,stderr = p.communicate()
    log.info('qc successfully finished')

