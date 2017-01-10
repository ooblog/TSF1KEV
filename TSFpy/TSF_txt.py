#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import re

from TSF_io import *


def TSF_txt_debug(TSF_argv=[]):    #TSF_doc:「TSF/TSF_txt.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog("TSF_Tab-Separated-Forth:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_argv:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argv)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    print("")
    print("--- {0} ---".format(sys.argv[0]))
    TSF_debug_savefilename="debug/TSF_txt_debug.txt"
    TSF_debug_log=TSF_txt_debug(sys.argv)
    TSF_io_savetext(TSF_debug_savefilename,TSF_debug_log)
    TSF_debug_log=TSF_io_loadtext(TSF_debug_savefilename)
    print("")
    try:
        print("--- {0} ---".format(TSF_debug_savefilename))
    except:
       print("can't 'print(TSF_debug_savefilename)'")
    finally:
        pass
    try:
        print(TSF_debug_log)
    except:
       print("can't 'print(TSF_debug_log)'")
    finally:
        pass
    sys.exit()
