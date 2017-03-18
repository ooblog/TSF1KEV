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
from TSF_uri import *
from TSF_calc import *
from TSF_time import *

TSF_Forth_init(TSF_io_argvs(),[TSF_shuffle_Initwords,TSF_match_Initwords,TSF_uri_Initwords,TSF_calc_Initwords,TSF_time_Initwords])

TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
    "\t".join(["UTF-8","#TSF_encoding","/mnt/sda2/github/TSF1KEV/TSFpy","#TSF_viewpythonappend","#TSF_popNthat","quine_ext:","#TSF_this","0","#TSF_fin."]),TSF_style="T")
TSF_Forth_setTSF("quine_ext:",
    "\t".join(["#TSF_mainfile","#TSF_fileext","equal","quine_match:","quine_jump:","#TSF_casestacks","#TSF_this"]),TSF_style="T")
TSF_Forth_setTSF("quine_match:",
    "\t".join([".tsf",".py"]),TSF_style="T")
TSF_Forth_setTSF("quine_jump:",
    "\t".join(["quine_tsf:","quine_python:"]),TSF_style="T")
TSF_Forth_setTSF("quine_tsf:",
    "\t".join(["#TSF_viewthey"]),TSF_style="N")
TSF_Forth_setTSF("quine_python:",
    "\t".join(["#TSF_viewpython"]),TSF_style="N")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_mainfile(TSF_io_argvs()[0])
TSF_Forth_run()
