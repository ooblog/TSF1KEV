#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Forth import *

def TSF_debug():    #TSF_doc:「TSF/TSF.py」単体テスト風デバッグ関数。
    TSF_Forth_Init()
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog(TSF_Forth_1ststack(),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_stacks[TSF_Forth_1ststack()])),TSF_log=TSF_debug_log)

TSF_Forth_Init()
if sys.argv > 2:
    pass
else:
    pass

TSF_debug()
sys.exit()
