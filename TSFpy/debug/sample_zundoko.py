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
    "\t".join(["UTF-8","#TSF_encoding","N-ZunDoko:","#TSF_this","0","#TSF_fin."]),
    TSF_style="T")
TSF_Forth_setTSF("N-ZunDoko:",
    "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[Zcount:0]~[TSF_argvs:0]","#TSF_calcDC","Zcount:","0","#TSF_pokethe","Zreset:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("Zreset:",
    "\t".join(["0","Zcount:","1","#TSF_pokethe","ZDdice:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("ZDdice:",
    "\t".join(["ZDjump:","#TSF_shufflethe","ZDjump:","#TSF_carbonthe","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("ZDjump:",
    "\t".join(["Zun:","Doko:"]),
    TSF_style="T")
TSF_Forth_setTSF("Zun:",
    "\t".join(["Zun","1","#TSF_echoN","[Zcount:1]+1","#TSF_calcDC","Zcount:","1","#TSF_pokethe","ZDdice:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("Doko:",
    "\t".join(["Doko","1","#TSF_echoN","VCjump:","[Zcount:0]-[Zcount:1]Z1~0","#TSF_calcDC","#TSF_peekthe","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("VCjump:",
    "\t".join(["Zreset:","VeronCho:"]),
    TSF_style="T")
TSF_Forth_setTSF("VeronCho:",
    "\t".join(["VeronCho","1","#TSF_echoN"]),
    TSF_style="T")
TSF_Forth_setTSF("Zcount:",
    "\t".join(["4","0"]),
    TSF_style="T")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_run()
