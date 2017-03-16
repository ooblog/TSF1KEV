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
    "\t".join(["UTF-8","#TSF_encoding","N-FizzBuzz:","#TSF_this","0","#TSF_fin."]),
    TSF_style="T")
TSF_Forth_setTSF("N-FizzBuzz:",
    "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[FZcount:4]~[TSF_argvs:0]","#TSF_calcDC","FZcount:","4","#TSF_pokethe","FizzBuzz:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("FizzBuzz:",
    "\t".join(["[FZcount:0]+1","#TSF_calcDC","FZcount:","0","#TSF_pokethe","FZcount:","([FZcount:0]#3Z1~0)+([FZcount:0]#5Z2~0)","#TSF_calcDC","#TSF_peekthe","1","#TSF_echoN","FZjump:","[FZcount:0]-[FZcount:4]O1~0","#TSF_calcDC","#TSF_peekthe","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("FZcount:",
    "\t".join(["0","Fizz","Buzz","Fizz&Buzz","20"]),
    TSF_style="T")
TSF_Forth_setTSF("FZjump:",
    "\t".join(["FizzBuzz:","#exit"]),
    TSF_style="T")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_run()
