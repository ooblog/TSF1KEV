#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import datetime
import os
import copy
import random

from TSF_Forth import *


def TSF_shuffle_Initwords(TSF_words):    #TSF_doc:TSF_words(ワード)を初期化する(TSFAPI)。
    TSF_words["#TSF_swapBAthat"]=TSF_Forth_swapBAthat; TSF_words["#スタックBA交換"]=TSF_Forth_swapBAthat
    TSF_words["#TSF_swapCAthat"]=TSF_Forth_swapCAthat; TSF_words["#スタックCA交換"]=TSF_Forth_swapCAthat
    TSF_words["#TSF_swapCBthat"]=TSF_Forth_swapCBthat; TSF_words["#スタックCB交換"]=TSF_Forth_swapCBthat
    return TSF_words
#        "#TSF_lenthe":TSF_Forth_lenthe,  "スタック個数":TSF_Forth_lenthe,
#        "#TSF_lenthis":TSF_Forth_lenthis,  "実行中スタックの個数":TSF_Forth_lenthis,
#        "#TSF_lenthat":TSF_Forth_lenthat,  "積込先スタックの個数":TSF_Forth_lenthat,
#        "#TSF_lenthey":TSF_Forth_lenthey,  "スタック名一覧の個数":TSF_Forth_lenthey,
#        "#TSF_pushthe":TSF_Forth_pushthe,  "スタックを積む":TSF_Forth_pushthe,
#        "#TSF_pushthis":TSF_Forth_pushthis,  "実行中スタックを自身に積む":TSF_Forth_pushthis,
#        "#TSF_pushthat":TSF_Forth_pushthat,  "積込先スタックから積む":TSF_Forth_pushthat,
#        "#TSF_pushthey":TSF_Forth_pushthey,  "スタック名一覧を積む":TSF_Forth_pushthey,
#        "#TSF_carbonthe":TSF_Forth_carbonthe,  "スタックの一番上を複製する":TSF_Forth_carbonthe,
#        "#TSF_carbonthis":TSF_Forth_carbonthis,  "実行中スタックの一番上を複製する":TSF_Forth_carbonthis,
#        "#TSF_carbonthat":TSF_Forth_carbonthat,  "積込先スタックの一番上を複製する":TSF_Forth_carbonthat,
#        "#TSF_clonethe":TSF_Forth_clonethe,  "スタックを複製する":TSF_Forth_clonethe,
#        "#TSF_clonethis":TSF_Forth_clonethis,  "実行中スタックを複製する":TSF_Forth_clonethis,
#        "#TSF_clonethat":TSF_Forth_clonethat,  "積込先スタック複製する":TSF_Forth_clonethat,
#        "#TSF_clonethey":TSF_Forth_clonethey,  "スタック名一覧をスタックとして複製する":TSF_Forth_clonethey,
#        "#TSF_popthe":TSF_Forth_popthe,  "スタックから拾う":TSF_Forth_popthe,
#        "#TSF_popthis":TSF_Forth_popthis,  "実行中スタックから拾う":TSF_Forth_popthis,
#        "#TSF_popthat":TSF_Forth_popthat,  "積込先スタックから除く":TSF_Forth_popthat,
#        "#TSF_peekthe":TSF_Forth_peekthe,  "番目のスタックから読み込む":TSF_Forth_peekthe,
#        "#TSF_rndseed":TSF_Forth_rndseed,  "を乱数の種":TSF_Forth_rndseed,
#        "#TSF_shuffle":TSF_Forth_shuffle,  "をシャッフル":TSF_Forth_shuffle,
#        "#TSF_rndpeekthe":TSF_Forth_rndpeekthe,  "からランダムに読み込む":TSF_Forth_rndpeekthe,
#        "#TSF_pokethe":TSF_Forth_pokethe,  "番目のスタックに上書き":TSF_Forth_pokethe,
#        "#TSF_delthe":TSF_Forth_delthe,  "のスタック削除":TSF_Forth_delthe,
#        "#TSF_delthis":TSF_Forth_delthat,  "実行中スタックを削除":TSF_Forth_delthis,
#        "#TSF_delthat":TSF_Forth_delthat,  "積込先スタックを削除":TSF_Forth_delthat,
#        "#TSF_join":TSF_Forth_join,  "個分連結":TSF_Forth_join,
#        "#TSF_joinC":TSF_Forth_joinC,  "で回数分挟んで連結":TSF_Forth_joinC,
#        "#TSF_split":TSF_Forth_split,  "の文字で分離":TSF_Forth_split,
#        "#TSF_chars":TSF_Forth_chars,  "一文字ずつに分離":TSF_Forth_chars,
#        "#TSF_replacethe":TSF_Forth_replacethe,  "スタックをテキストとみなして置換する":TSF_Forth_replacethe,
#        "#TSF_resubthe":TSF_Forth_resubthe,  "スタックをテキストとみなして正規表現で置換する":TSF_Forth_resubthe,
#        "#TSF_replacethat":TSF_Forth_replacethat,  "一行を置換する":TSF_Forth_replacethat,
#        "#TSF_resubthat":TSF_Forth_resubthat,  "一行を正規表現で置換する":TSF_Forth_resubthat,

def TSF_shuffle_swapBAthat():   #TSF_doc:[stackB,stackA]スタックAとスタックBを交換する。
    TSF_tsvA=TSF_Forth_popthat()
    TSF_tsvB=TSF_Forth_popthat()
    TSF_Forth_pushthat(TSF_tsvA)
    TSF_Forth_pushthat(TSF_tsvB)

def TSF_shuffle_swapCAthat():   #TSF_doc:[stackC,stackB,stackA]スタックAとスタックCを交換する。
    TSF_tsvA=TSF_Forth_popthat()
    TSF_tsvB=TSF_Forth_popthat()
    TSF_tsvC=TSF_Forth_popthat()
    TSF_Forth_pushthat(TSF_tsvA)
    TSF_Forth_pushthat(TSF_tsvB)
    TSF_Forth_pushthat(TSF_tsvC)

def TSF_shuffle_swapCBthat():   #TSF_doc:[stackC,stackB,stackA]スタックBとスタックCを交換する。
    TSF_tsvA=TSF_Forth_popthat()
    TSF_tsvB=TSF_Forth_popthat()
    TSF_tsvC=TSF_Forth_popthat()
    TSF_Forth_pushthat(TSF_tsvB)
    TSF_Forth_pushthat(TSF_tsvC)
    TSF_Forth_pushthat(TSF_tsvA)


if __name__=="__main__":
    from collections import OrderedDict
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/TSF_shuffle_debug.txt"
#    TSF_debug_log=TSF_shuffle_debug()
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
