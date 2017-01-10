#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Forth import *

def TSF_debug():    #TSF_doc:「TSF/TSF.py」単体テスト風デバッグ関数。
    TSF_stacks=TSF_Forth_stacks()
    print("TSF_debug",TSF_stacks)
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog(TSF_Forth_1ststack(),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    for TSF_stackK,TSF_stackV in TSF_stacks.items():
        if TSF_stackK == TSF_Forth_1ststack(): continue;
        TSF_debug_log=TSF_io_printlog(TSF_stackK,TSF_log=TSF_debug_log)
        TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_stackV)),TSF_log=TSF_debug_log)
#    print(TSF_stacks)


TSF_Forth_Init()
if len(sys.argv) < 2 or sys.argv[1] in "--":
    TSF_Forth_settext("about:",
        "「TSF_Tab-Separated-Forth:」の文法暫定案。\n"
        "\n")
else:
    pass

TSF_debug()
sys.exit()
