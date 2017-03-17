#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import sys
import os
os.chdir(sys.path[0])
sys.path.append('/mnt/sda2/github/TSF1KEV/TSFpy')
from TSF_io import *
#from TSF_Forth import *
from TSF_shuffle import *
from TSF_match import *
from TSF_calc import *
from TSF_time import *

TSF_Forth_init(TSF_io_argvs(),[TSF_shuffle_Initwords,TSF_match_Initwords,TSF_calc_Initwords,TSF_time_Initwords])

TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
    "\t".join(["UTF-8","#TSF_encoding","calender:","#TSF_this","0","#TSF_fin."]),
    TSF_style="T")
TSF_Forth_setTSF("calender:",
    "\t".join(["testorargvs:","TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z1~0","#TSF_calcDC","#TSF_peekthe","#TSF_carbonthe","#TSF_calender","1","#TSF_echoN"]),
    TSF_style="T")
TSF_Forth_setTSF("calendertest:",
    "\t".join(["@000y@0m@0dm@wdec@0h@0n@0s"]),
    TSF_style="N")
TSF_Forth_setTSF("testorargvs:",
    "\t".join(["TSF_argvs:","calendertest:"]),
    TSF_style="T")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_run()
