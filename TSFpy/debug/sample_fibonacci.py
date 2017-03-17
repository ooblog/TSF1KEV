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
    "\t".join(["UTF-8","#TSF_encoding","200","#TSF_calcPR","N-Fibonacci:","#TSF_this","0","#TSF_fin."]),
    TSF_style="T")
TSF_Forth_setTSF("N-Fibonacci:",
    "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[Fibcount:0]~[TSF_argvs:0]","#TSF_calcDC","Fibcount:","0","#TSF_pokethe","Fibonacci:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("Fibonacci:",
    "\t".join(["[Fibcount:1]Z1~[Fibcount:1]","#TSF_calcDC","((2&(([0]+3)*[0]+2)^)/((2&(2*[0]+2)^)-(2&([0]+1)^)-1)\\1)#(2&([0]+1)^)","#TSF_calcDC","1","#TSF_echoN","[Fibcount:1]+1","#TSF_calcDC","Fibcount:","1","#TSF_pokethe","Fibjump:","[Fibcount:0]-([Fibcount:1]+1)o0~1","#TSF_calcDC","#TSF_peekthe","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("Fibcount:",
    "\t".join(["20","-1"]),
    TSF_style="T")
TSF_Forth_setTSF("Fibjump:",
    "\t".join(["Fibonacci:","#exit"]),
    TSF_style="T")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_run()

