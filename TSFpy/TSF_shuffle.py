#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import datetime
import os
import copy
import random
from TSF_Forth import *


def TSF_shuffle_Initwords(TSF_words):    #TSF_doc:スタック並び替え関連のワードを追加する(TSFAPI)。
    TSF_words["#TSF_swapBAthat"]=TSF_shuffle_swapBAthat; TSF_words["#スタックBA交換"]=TSF_shuffle_swapBAthat
    TSF_words["#TSF_swapCAthat"]=TSF_shuffle_swapCAthat; TSF_words["#スタックCA交換"]=TSF_shuffle_swapCAthat
    TSF_words["#TSF_swapCBthat"]=TSF_shuffle_swapCBthat; TSF_words["#スタックCB交換"]=TSF_shuffle_swapCBthat
    TSF_words["#TSF_lenthe"]=TSF_shuffle_lenthe; TSF_words["#スタック個数"]=TSF_shuffle_lenthe
    TSF_words["#TSF_lenthis"]=TSF_shuffle_lenthis; TSF_words["#実行中スタック個数"]=TSF_shuffle_lenthis
    TSF_words["#TSF_lenthat"]=TSF_shuffle_lenthat; TSF_words["#積込先スタック個数"]=TSF_shuffle_lenthat
    TSF_words["#TSF_lenthey"]=TSF_shuffle_lenthey; TSF_words["#スタック一覧個数"]=TSF_shuffle_lenthey
    TSF_words["#TSF_peekthe"]=TSF_shuffle_peekthe; TSF_words["#スタック読込"]=TSF_shuffle_peekthe
    TSF_words["#TSF_peekthis"]=TSF_shuffle_peekthis; TSF_words["#実行中スタック読込"]=TSF_shuffle_peekthis
    TSF_words["#TSF_peekthat"]=TSF_shuffle_peekthat; TSF_words["#積込先スタック読込"]=TSF_shuffle_peekthat
    TSF_words["#TSF_peekrndthe"]=TSF_shuffle_peekrndthe; TSF_words["#スタック乱択"]=TSF_shuffle_peekrndthe
    TSF_words["#TSF_peekrndthis"]=TSF_shuffle_peekrndthis; TSF_words["#実行中スタック乱択"]=TSF_shuffle_peekrndthis
    TSF_words["#TSF_peekrndthat"]=TSF_shuffle_peekrndthat; TSF_words["#積込先スタック乱択"]=TSF_shuffle_peekrndthat
    TSF_words["#TSF_shufflethe"]=TSF_shuffle_shufflethe; TSF_words["#スタックシャッフル"]=TSF_shuffle_shufflethe
    TSF_words["#TSF_shufflethat"]=TSF_shuffle_shufflethat; TSF_words["#積込先スタックシャッフル"]=TSF_shuffle_shufflethat
#    TSF_words["#TSF_carbonthe"]=TSF_shuffle_carbonthe; TSF_words["#スタックの表面を複製"]=TSF_shuffle_carbonthe
#    TSF_words["#TSF_carbonthis"]=TSF_shuffle_carbonthis; TSF_words["#実行中スタックの表面を複製"]=TSF_shuffle_carbonthis
#    TSF_words["#TSF_carbonthat"]=TSF_shuffle_carbonthat; TSF_words["#積込先スタックの表面を複製"]=TSF_shuffle_carbonthat
    return TSF_words
#        "#TSF_pokethe":TSF_Forth_pokethe,  "番目のスタックに上書き":TSF_Forth_pokethe,
#        "#TSF_rndseed":TSF_Forth_rndseed,  "を乱数の種":TSF_Forth_rndseed,
#        "#TSF_shuffle":TSF_Forth_shuffle,  "をシャッフル":TSF_Forth_shuffle,
#        "#TSF_rndpeekthe":TSF_Forth_rndpeekthe,  "からランダムに読み込む":TSF_Forth_rndpeekthe,
#        "#TSF_pushthe":TSF_Forth_pushthe,  "スタックを積む":TSF_Forth_pushthe,
#        "#TSF_pushthis":TSF_Forth_pushthis,  "実行中スタックを自身に積む":TSF_Forth_pushthis,
#        "#TSF_pushthat":TSF_Forth_pushthat,  "積込先スタックから積む":TSF_Forth_pushthat,
#        "#TSF_pushthey":TSF_Forth_pushthey,  "スタック名一覧を積む":TSF_Forth_pushthey,
#        "#TSF_clonethe":TSF_Forth_clonethe,  "スタックを複製する":TSF_Forth_clonethe,
#        "#TSF_clonethis":TSF_Forth_clonethis,  "実行中スタックを複製する":TSF_Forth_clonethis,
#        "#TSF_clonethat":TSF_Forth_clonethat,  "積込先スタック複製する":TSF_Forth_clonethat,
#        "#TSF_clonethey":TSF_Forth_clonethey,  "スタック名一覧をスタックとして複製する":TSF_Forth_clonethey,
#        "#TSF_popthe":TSF_Forth_popthe,  "スタックから拾う":TSF_Forth_popthe,
#        "#TSF_popthis":TSF_Forth_popthis,  "実行中スタックから拾う":TSF_Forth_popthis,
#        "#TSF_popthat":TSF_Forth_popthat,  "積込先スタックから除く":TSF_Forth_popthat,
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

def TSF_shuffle_lenthe():   #TSF_doc:[stack]指定したスタックの数を数える。1スタック積み上げ。
    TSF_Forth_pushthat(str(TSF_Forth_stacklen(TSF_Forth_popthat())))
    return None

def TSF_shuffle_lenthis():   #TSF_doc:[]thisスタック(実行中スタック)の数を数える。1スタック積み上げ。
    TSF_Forth_pushthat(str(TSF_Forth_stacklenthis()))
    return None

def TSF_shuffle_lenthat():   #TSF_doc:[]thatスタック(積込先スタック)の数を数える。1スタック積み上げ。
    TSF_Forth_pushthat(str(TSF_Forth_stacklenthat()))
    return None

def TSF_shuffle_lenthey():   #TSF_doc:[]スタック名一覧の数を数える。1スタック積み上げ。
    TSF_Forth_pushthat(str(TSF_Forth_stackslen()))
    return None

def TSF_shuffle_peekthe():   #TSF_doc:[stack,counter]スタックから読み込む。2スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_pintthat()
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_Forth_popthat(),TSF_count))
    return None

def TSF_shuffle_peekthis():   #TSF_doc:[counter]実行中スタックから読み込む。1スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_pintthis()
    TSF_Forth_pushthat(TSF_Forth_peekthis(TSF_count))
    return None

def TSF_shuffle_peekthat():   #TSF_doc:[counter]積込先スタックから読み込む。1スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_pintthat()
    TSF_Forth_pushthat(TSF_Forth_peekthat(TSF_count))
    return None

def TSF_shuffle_peekrndthe():   #TSF_doc:[stack]スタックから読み込む。1スタック積み下ろして、1スタック積み上げ。
    TSF_the=TSF_Forth_popthat()
    TSF_count=random.randint(1,TSF_Forth_stacklen(TSF_the))-1
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_the,TSF_count))
    return None

def TSF_shuffle_peekrndthis():   #TSF_doc:[]実行中スタックから読み込む。1スタック積み上げ。
    TSF_count=random.randint(1,TSF_Forth_stacklenthis())-1
    TSF_Forth_pushthat(TSF_Forth_peekthis(TSF_count))
    return None

def TSF_shuffle_peekrndthat():   #TSF_doc:[]積込先スタックから読み込む。1スタック積み上げ。
    TSF_count=random.randint(1,TSF_Forth_stacklenthat())-1
    TSF_Forth_pushthat(TSF_Forth_peekthat(TSF_count))
    return None

def TSF_shuffle_shufflethe():   #TSF_doc:[stack]スタックをシャッフル。1スタック積み下ろし。
    TSF_Forth_shufflethe(TSF_Forth_popthat())
    return None

def TSF_shuffle_shufflethat():   #TSF_doc:[]積込先スタックをシャッフル。0スタック積み下ろし。
    TSF_Forth_shufflethe(TSF_Forth_stacklenthat())
    return None

def TSF_shuffle_carbonthe():   #TSF_doc:[stack]スタックの一番上のスタックを複製する。
#    TSF_peekdata=TSF_Forth_peekthe(TSF_Forth_popthat(),-1)
#    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
#    TSF_carbon=TSF_stacks[TSF_thename][-1] if len(TSF_stacks[TSF_thename]) > 0 else ""
#    TSF_Forth_push(TSF_thatstack_name,TSF_carbon)
    return None

def TSF_shuffle_carbonthis():   #TSF_doc:[]実行中スタックの一番上のスタックを複製する。
#    TSF_carbon=TSF_stacks[TSF_thisstack_name][-1] if len(TSF_stacks[TSF_thisstack_name]) > 0 else ""
#    TSF_Forth_push(TSF_thatstack_name,TSF_carbon)
    return None

def TSF_shuffle_carbonthat():   #TSF_doc:[]積込先スタックの一番上のスタックを複製する。
#    TSF_carbon=TSF_stacks[TSF_thatstack_name][-1] if len(TSF_stacks[TSF_thatstack_name]) > 0 else ""
#    TSF_Forth_push(TSF_thatstack_name,TSF_carbon)
    return None

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
