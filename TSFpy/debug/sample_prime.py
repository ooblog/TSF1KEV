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
    "\t".join(["UTF-8","#TSF_encoding","N-prime:","#TSF_this","0","#TSF_fin."]),
    TSF_style="T")
TSF_Forth_setTSF("N-prime:",
    "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[Pcount:0]~[TSF_argvs:0]","#TSF_calcDC","Pcount:","0","#TSF_pokethe","primeskip:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("primeskip:",
    "\t".join(["Pstep:","[Pcount:1]","#TSF_calcDC","#TSF_peekcyclethe","Pcount:","#TSF_carbonthe","[0]+[1]","#TSF_calcDC","Pcount:","2","#TSF_pokethe","[Pcount:1]+1","#TSF_calcDC","Pcount:","1","#TSF_pokethe","primewhile:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("primewhile:",
    "\t".join(["Pwhilejump:","[Pcount:0]-[Pcount:2]O0~1","#TSF_calcDC","#TSF_peekthe","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("Pwhilejump:",
    "\t".join(["prime2chk:","primeecho:"]),
    TSF_style="T")
TSF_Forth_setTSF("prime2chk:",
    "\t".join(["P2chkjump:","Pcount:","#TSF_carbonthe","2F[0]~[0])-2Z0~1","#TSF_calcDC","#TSF_peekthe","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("P2chkjump:",
    "\t".join(["primeMchk:","primeskip:"]),
    TSF_style="T")
TSF_Forth_setTSF("primeMchk:",
    "\t".join(["primeadd:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("PMchkjump:",
    "\t".join(["primeadd:","primeskip:"]),
    TSF_style="T")
TSF_Forth_setTSF("primeadd:",
    "\t".join(["Ppool:","Pcount:","#TSF_carbonthe","1","#TSF_addNthe","primeskip:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("primeecho:",
    "\t".join(["[Pcount:0]-1U3~(6-[Pcount:0])/2","#TSF_calcDC","Ppool:","#TSF_popNthe","Ppool:","#TSF_echothe"]),
    TSF_style="T")
TSF_Forth_setTSF("Pcount:",
    "\t".join(["100","0","1"]),
    TSF_style="T")
TSF_Forth_setTSF("Ppool:",
    "\t".join(["2","3","5"]),
    TSF_style="T")
TSF_Forth_setTSF("Pstep:",
    "\t".join(["6","4","2","4","2","4","6","2"]),
    TSF_style="T")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_run()
