#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import os
from TSF_Forth import *

def TSF_uri_Initwords(TSF_words):    #TSF_doc:URLとファイルパス関連のワードを追加する(TSFAPI)。
    TSF_words["#TSF_mainfile"]=TSF_uri_mainfile; TSF_words["#メインファイル名"]=TSF_uri_mainfile
    TSF_words["#TSF_fileext"]=TSF_uri_fileext; TSF_words["#ファイルの拡張子"]=TSF_uri_fileext
    return TSF_words

def TSF_uri_mainfile():   #TSF_doc:[filepath]実行メインファイル名を取得する。1スタック積み下ろし。
    TSF_Forth_pushthat(TSF_Forth_mainfile())
    return None

def TSF_uri_fileext():   #TSF_doc:[filepath]ファイルの拡張子を取得する。1スタック積み下ろし、1スタック積み上げ。
    TSF_tsvU=TSF_Forth_popthat()
    TSF_tsvU=os.path.splitext(TSF_tsvU)[1]
    TSF_Forth_pushthat(TSF_tsvU)
    return None


def TSF_uri_debug(TSF_argvs):    #TSF_doc:「TSF/TSF_shuffle.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_Forth_init(TSF_argvs,[TSF_uri_Initwords])
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","TSF_fileexttest:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("TSF_uri.py:","\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout]))
    TSF_Forth_setTSF("TSF_fileexttest:","\t".join(["debug/sample_quine.tsf","#TSF_fileext","1","#TSF_echoN"]))
    TSF_Forth_addfin(TSF_argvs)
    TSF_Forth_run()
    for TSF_thename in TSF_Forth_stackskeys():
        TSF_debug_log=TSF_Forth_view(TSF_thename,True,TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    from collections import OrderedDict
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/debug_uri.log"
    TSF_debug_log=TSF_uri_debug(TSF_argvs)
    TSF_io_savetext(TSF_debug_savefilename,TSF_debug_log)
    print("")
    try:
        print("--- {0} ---\n{1}".format(TSF_debug_savefilename,TSF_debug_log))
    except:
        print("can't 'print(TSF_debug_savefilename,TSF_debug_log)'")
    finally:
        pass
    sys.exit()

# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
