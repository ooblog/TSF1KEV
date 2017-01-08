#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_io import *
from TSF_txt import *

def TSF_Forth_debug(TSF_argv=[]):
    TSF_debug_log=""
    print("Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print(TSF_argv)
    TSF_debug_log=TSF_printlog("TSF_Tab-Separated-Forth",TSF_log=TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    TSF_debug_log=TSF_Forth_debug(sys.argv)
    TSF_debug_savefilename="TSF_Forth_debug.txt"
    print(TSF_debug_log)
    sys.exit()
