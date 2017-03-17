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
    "\t".join(["UTF-8","#TSF_encoding","replace:","#TSF_this","help:","#TSF_echothe","0","#TSF_fin."]),
    TSF_style="T")
TSF_Forth_setTSF("help:",
    "\t".join(["usage: ./TSF.py [command|file.tsf] [argv] ...",
    "commands:",
    "  --help        this commands view",
    "  --about       about TSF UTF-8 text (Japanese) view\" ",
    "  --python      TSF.tsf to Python.py view or save\" ",
    "  --helloworld  \"Hello world  1  #TSF_echoN\" sample",
    "  --quine       TSF_Forth_viewthey() Quine (self source) sample",
    "  --99beer      99 Bottles of Beer sample",
    "  --fizzbuzz    ([0]#3Z1~0)+([0]#5Z2~0) Fizz Buzz Fizz&Buzz sample",
    "  --zundoko     Zun Zun Zun Zun Doko VeronCho sample",
    "  --fibonacci   Fibonacci number 0,1,1,2,3,5,8,13,21,55... sample",
    "  --prime       prime numbers 2,3,5,7,11,13,17,19,23,29... sample",
    "  --calcFX      fractions calculator \"1/3-m1|2\"-> p5|6 sample",
    "  --calcDC      fractions calculator \"1/3-m1|2\"-> 0.8333... sample",
    "  --calcKN      fractions calculator \"1/3-m1|2\"-> 6 bunno 5 sample",
    "  --calender    \"@000y@0m@0dm@wdec@0h@0n@0s\"-> TSF_time_getdaytime() sample"]),
    TSF_style="N")
TSF_Forth_setTSF("replace:",
    "\t".join(["replaceN:","#TSF_carbonthe","#TSF_calender","replaceN:","0","#TSF_pokethe","help:","replaceO:","replaceN:","#TSF_replacestacks"]),
    TSF_style="T")
TSF_Forth_setTSF("replaceO:",
    "\t".join(["TSF_time_getdaytime()"]),
    TSF_style="N")
TSF_Forth_setTSF("replaceN:",
    "\t".join(["@000y@0m@0dm@wdec@0h@0n@0s"]),
    TSF_style="N")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_run()
