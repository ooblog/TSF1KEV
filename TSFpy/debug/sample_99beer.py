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
    "\t".join(["UTF-8","#TSF_encoding","N-BottlesofBeer:","#TSF_this","0","#TSF_fin."]),
    TSF_style="T")
TSF_Forth_setTSF("N-BottlesofBeer:",
    "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[onthewallint:0]~[TSF_argvs:0]","#TSF_calcDC","onthewallint:","0","#TSF_pokethe","onthewallint:","#TSF_that","#TSF_carbonthat","#TSF_carbonthat","drinkbottles:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("drinkbottles:",
    "\t".join(["#TSF_swapBAthat","1","#TSF_popNthat","[onthewallint:1]-1","#TSF_calcDC","countbottles:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("countbottles:",
    "\t".join(["bottlesreplace:","bottlescall:","onthewallint:","1","#TSF_peekthe","#TSF_peeklimitthe","#TSF_clonethe","bottlesreplace:","onthewallstr:","onthewallint:","#TSF_replacestacks","bottlesreplace:","#TSF_echothe","lopbottles:","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("lopbottles:",
    "\t".join(["bottlesjump:","[onthewallint:2]O0~1","#TSF_calcDC","#TSF_peekthe","#TSF_this"]),
    TSF_style="T")
TSF_Forth_setTSF("bottlesjump:",
    "\t".join(["drinkbottles:","#exit"]),
    TSF_style="T")
TSF_Forth_setTSF("onthewallstr:",
    "\t".join(["{buybottles}","{drink}","{drinked}"]),
    TSF_style="T")
TSF_Forth_setTSF("onthewallint:",
    "\t".join(["99"]),
    TSF_style="N")
TSF_Forth_setTSF("bottlescall:",
    "\t".join(["nomorebottles:","1bottle:","2bottles:","3ormorebottles:"]),
    TSF_style="T")
TSF_Forth_setTSF("3ormorebottles:",
    "\t".join(["{drink} bottles of beer on the wall, {drink} bottles of beer.",
    "Take one down and pass it around, {drinked} bottles of beer on the wall."]),
    TSF_style="N")
TSF_Forth_setTSF("2bottles:",
    "\t".join(["{drink} bottles of beer on the wall, {drink} bottles of beer.",
    "Take one down and pass it around, 1 bottle of beer on the wall."]),
    TSF_style="N")
TSF_Forth_setTSF("1bottle:",
    "\t".join(["{drink} bottle of beer on the wall, {drink} bottle of beer.",
    "Take one down and pass it around, no more bottles of beer on the wall."]),
    TSF_style="N")
TSF_Forth_setTSF("nomorebottles:",
    "\t".join(["No more bottles of beer on the wall, no more bottles of beer.",
    "Go to the store and buy some more, {buybottles} bottles of beer on the wall."]),
    TSF_style="N")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_run()
