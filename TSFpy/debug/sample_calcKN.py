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
    "\t".join(["UTF-8","#TSF_encoding","calcKN:","#TSF_this","0","#TSF_fin."]),
    TSF_style="T")
TSF_Forth_setTSF("calcKN:",
    "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[calcKNtest:0]~[TSF_argvs:0]","#TSF_calcKN","1","#TSF_echoN"]),
    TSF_style="T")
TSF_Forth_setTSF("calcKNtest:",
    "\t".join(["1/3-m1|2"]),
    TSF_style="N")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_run()
