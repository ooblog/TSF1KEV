#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import datetime
import os
import re
import difflib
import unicodedata
from TSF_Forth import *

def TSF_replace_Initwords(TSF_words):    #TSF_doc:スタック並び替え関連のワードを追加する(TSFAPI)。
    TSF_words["#TSF_joinN"]=TSF_replace_TSF_joinN; TSF_words["#N個連結"]=TSF_replace_TSF_joinN
    TSF_words["#TSF_betweenN"]=TSF_replace_TSF_betweenN; TSF_words["#挟んでN個連結"]=TSF_replace_TSF_betweenN
    return TSF_words
#        "#TSF_replacethe":TSF_Forth_replacethe,  "スタックをテキストとみなして置換する":TSF_Forth_replacethe,
#        "#TSF_resubthe":TSF_Forth_resubthe,  "スタックをテキストとみなして正規表現で置換する":TSF_Forth_resubthe,
#        "#TSF_replacethat":TSF_Forth_replacethat,  "一行を置換する":TSF_Forth_replacethat,
#        "#TSF_resubthat":TSF_Forth_resubthat,  "一行を正規表現で置換する":TSF_Forth_resubthat,
#        "#TSF_split":TSF_Forth_split,  "文字で分割":TSF_Forth_split,
#        "#TSF_chars":TSF_Forth_chars,  "一文字ずつに分離":TSF_Forth_chars,
#        "#TSF_strequal":TSF_Forth_chars,  "文字列一致":TSF_Forth_chars,
#        "#TSF_strmatcher":TSF_Forth_chars,  "文字列のそれっぽさ":TSF_Forth_chars,

def TSF_replace_TSF_joinN():   #TSF_doc:[stackN…stackB,stackA,count]スタックを連結する。count自身とcountの回数分スタック積み下ろし。
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_joinlist=[""]*TSF_countlen
    for TSF_count in range(TSF_countlen):
        TSF_joinlist[TSF_count]=TSF_Forth_popthat()
    TSF_Forth_pushthat("".join(reversed(TSF_joinlist)))
    return None

def TSF_replace_TSF_betweenN():   #TSF_doc:[stackN…stackB,stackA,count,joint]スタックAとスタックBを交換する。接続子とcount自身およびcountの回数分スタック積み下ろし。
    TSF_joint=TSF_Forth_stackthat()
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_joinlist=[""]*TSF_countlen
    for TSF_count in range(TSF_countlen):
        TSF_joinlist[TSF_count]=TSF_Forth_popthat()
    TSF_Forth_pushthat(TSF_joint.join(reversed(TSF_joinlist)))
    return None


#def TSF_Forth_split():   #TSF_doc:[…stackB,stackA,string,spliter]文字列を分割する。stringとspliter分スタック積み下ろし、分割された文字列分スタック積み込み。
#    TSF_tsvP=TSF_Forth_pop(TSF_thatstack_name)
#    TSF_tsvQ=TSF_Forth_pop(TSF_thatstack_name)
#    TSF_tsvK=TSF_tsvQ.split(TSF_tsvP)
#    for TSF_tsvA in TSF_tsvK:
#        TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
#    return None

#def TSF_Forth_chars():   #TSF_doc:[…stackB,stackA,string]文字列を一文字ずつに分割する。stringスタック積み下ろし、分割された文字分スタック積み込み。
#    TSF_tsvQ=TSF_Forth_pop(TSF_thatstack_name)
#    for TSF_tsvA in TSF_tsvQ:
#        TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
#    return None



def TSF_replace_debug():    #TSF_doc:「TSF/TSF_shuffle.py」単体テスト風デバッグ関数。
    pass

if __name__=="__main__":
    from collections import OrderedDict
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/TSF_replace_debug.txt"
    TSF_debug_log=TSF_replace_debug()
#    TSF_io_savetext(TSF_debug_savefilename,TSF_debug_log)
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
