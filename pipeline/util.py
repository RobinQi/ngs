#!/usr/bin/python
import os,sys
import logging

log = logging.getLogger()

def stdout_stderr(output=None,pipeline=None):
    try:
        os.mkdir(str(output) + '/' + str(pipeline))
    except OSError:
        log.error('can not create %s folder' % str(pipeline))
    stdout = os.path.join(str(output), pipeline, 'stdout.txt')
    stderr = os.path.join(str(output), pipeline, 'stderr.txt')
    stdout_h = open(stdout, 'a')
    stderr_h = open(stderr, 'a')
    return stdout_h, stderr_h