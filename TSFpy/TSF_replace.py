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
    TSF_words["#TSF_split"]=TSF_replace_split; TSF_words["#文字で分割"]=TSF_replace_split
    TSF_words["#TSF_chars"]=TSF_replace_chars; TSF_words["#一文字ずつに分離"]=TSF_replace_chars
    TSF_words["#TSF_input"]=TSF_replace_input; TSF_words["#文字列入力"]=TSF_replace_input
    TSF_words["#TSF_strequal"]=TSF_replace_strequal; TSF_words["#文字列一致"]=TSF_replace_strequal
    TSF_words["#TSF_strmatcher"]=TSF_replace_strmatcher; TSF_words["#文字列のそれっぽさ"]=TSF_replace_strmatcher
    return TSF_words
#        "#TSF_replacethe":TSF_Forth_replacethe,  "スタックをテキストとみなして置換する":TSF_Forth_replacethe,
#        "#TSF_replacethat":TSF_Forth_replacethat,  "一行を置換する":TSF_Forth_replacethat,
#        "#TSF_resubthe":TSF_Forth_resubthe,  "スタックをテキストとみなして正規表現で置換する":TSF_Forth_resubthe,
#        "#TSF_resubthat":TSF_Forth_resubthat,  "一行を正規表現で置換する":TSF_Forth_resubthat,

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

def TSF_replace_split():   #TSF_doc:[string,spliter]文字列を分割する。2スタック積み下ろし、分割された文字列分スタック積み込み。
    TSF_tsvP=TSF_Forth_popthat()
    TSF_tsvQ=TSF_Forth_popthat()
    TSF_tsvK=TSF_tsvQ.split(TSF_tsvP)
    for TSF_tsvA in TSF_tsvK:
        TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_replace_chars():   #TSF_doc:[string]文字列を一文字ずつに分割する。1スタック積み下ろし、分割された文字分スタック積み込み。
    TSF_tsvQ=TSF_Forth_popthat()
    for TSF_tsvA in TSF_tsvQ:
        TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_replace_input():   #TSF_doc:[]文字列を入力させる。1スタック積み込み。
    TSF_tsvA=raw_input()
    TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_replace_strequal():   #TSF_doc:[equal,string]文字列が一致すれば1、不一致なら0を残す。2スタック積み下ろし、1スタック積み込み。
    TSF_tsvS=TSF_Forth_popthat()
    TSF_tsvE=TSF_Forth_popthat()
    TSF_tsvA="1" if TSF_tsvS == TSF_tsvE else "0"
    TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_replace_strmatcher():   #TSF_doc:[matcher,string]文字列が完全一致すれば1.0、不一致なら0.0、そこそこ惜しい場合は類似度を小数値で残す。2スタック積み下ろし、1スタック積み込み。
    TSF_tsvS=TSF_Forth_popthat(); TSF_tsvS=unicodedata.normalize('NFKC',TSF_tsvS)
    TSF_tsvE=TSF_Forth_popthat(); TSF_tsvE=unicodedata.normalize('NFKC',TSF_tsvE)
    TSF_tsvA=str(difflib.SequenceMatcher(None,TSF_tsvS,TSF_tsvE).ratio())
    TSF_Forth_pushthat(TSF_tsvA)
    return None

TSF_matchgrade=0.9
def TSF_replace_matchgrade():   #TSF_doc:[grade]文字列一致とみなすグレード値を変更。1スタック積み下ろし。
    TSF_tsvG=TSF_Forth_popthat()
    TSF_matchgrade=float(TSF_tsvG)
    return None

def TSF_replace_matchif():   #TSF_doc:[then,score]文字列が一致すれば1、不一致なら0を残す。2スタック積み下ろし、1スタック積み込み。
    return None

def TSF_replace_matchifelse():   #TSF_doc:[else,then,score]文字列が一致すれば1、不一致なら0を残す。2スタック積み下ろし、1スタック積み込み。
    return None

def TSF_replace_debug():    #TSF_doc:「TSF/TSF_shuffle.py」単体テスト風デバッグ関数。
    TSF_tsvS="いいまちがい"
    TSF_tsvE="いいまつがい"
    TSF_tsvA=str(difflib.SequenceMatcher(None,TSF_tsvS,TSF_tsvE).ratio())
    TSF_io_printlog("{0}:{1}={2}".format(TSF_tsvS,TSF_tsvE,TSF_tsvA))

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
