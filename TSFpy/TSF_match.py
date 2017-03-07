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

def TSF_match_Initwords(TSF_words):    #TSF_doc:スタック並び替え関連のワードを追加する(TSFAPI)。
    TSF_words["#TSF_joinN"]=TSF_match_TSF_joinN; TSF_words["#N個連結"]=TSF_match_TSF_joinN
    TSF_words["#TSF_betweenN"]=TSF_match_TSF_betweenN; TSF_words["#挟んでN個連結"]=TSF_match_TSF_betweenN
    TSF_words["#TSF_split"]=TSF_match_split; TSF_words["#文字で分割"]=TSF_match_split
    TSF_words["#TSF_chars"]=TSF_match_chars; TSF_words["#一文字ずつに分離"]=TSF_match_chars
    TSF_words["#TSF_requalS"]=TSF_match_equalS; TSF_words["#文字列一致"]=TSF_match_equalS
    TSF_words["#TSF_inS"]=TSF_match_inS; TSF_words["#文字列に含む"]=TSF_match_inS
    TSF_words["#TSF_searchS"]=TSF_match_searchS; TSF_words["#正規表現に該当"]=TSF_match_searchS
    TSF_words["#TSF_matcherS"]=TSF_match_matcherS; TSF_words["#文字列のそれっぽさ"]=TSF_match_matcherS
    TSF_words["#TSF_matchgrade"]=TSF_match_matchgrade; TSF_words["#文字列類似の合格点"]=TSF_match_matchgrade
    TSF_words["#TSF_matchif"]=TSF_match_matchif; TSF_words["#文字列のそれっぽさ"]=TSF_match_matchif
    TSF_words["#TSF_matchelse"]=TSF_match_matchelse; TSF_words["#文字列のそれっぽさ"]=TSF_match_matchelse
    TSF_words["#TSF_matchifelse"]=TSF_match_matchifelse; TSF_words["#文字列のそれっぽさ"]=TSF_match_matchifelse
    TSF_words["#TSF_matchcasethe"]=TSF_match_matchcasethe; TSF_words["#文字列とスタックの一致箇所"]=TSF_match_matchcasethe
    TSF_words["#TSF_matchthe"]=TSF_match_replacethe; TSF_words["#スタックをテキストとみなして置換"]=TSF_match_replacethe
    TSF_words["#TSF_matchthat"]=TSF_match_replacethat; TSF_words["#積込先スタックをテキストとみなして置換"]=TSF_match_replacethat
    TSF_words["#TSF_resubthe"]=TSF_match_resubthe; TSF_words["#スタックをテキストとみなして正規表現で置換"]=TSF_match_resubthe
    TSF_words["#TSF_resubthat"]=TSF_match_resubthat; TSF_words["#積込先スタックをテキストとみなして正規表現で置換"]=TSF_match_resubthat
    return TSF_words

def TSF_match_TSF_joinN():   #TSF_doc:[stackN…stackB,stackA,count]スタックを連結する。count自身とcountの回数分スタック積み下ろし。
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_joinlist=[""]*TSF_countlen
    for TSF_count in range(TSF_countlen):
        TSF_joinlist[TSF_count]=TSF_Forth_popthat()
    TSF_Forth_pushthat("".join(reversed(TSF_joinlist)))
    return None

def TSF_match_TSF_betweenN():   #TSF_doc:[stackN…stackB,stackA,count,joint]スタックAとスタックBを交換する。接続子とcount自身およびcountの回数分スタック積み下ろし。
    TSF_joint=TSF_Forth_stackthat()
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_joinlist=[""]*TSF_countlen
    for TSF_count in range(TSF_countlen):
        TSF_joinlist[TSF_count]=TSF_Forth_popthat()
    TSF_Forth_pushthat(TSF_joint.join(reversed(TSF_joinlist)))
    return None

def TSF_match_split():   #TSF_doc:[string,spliter]文字列を分割する。2スタック積み下ろし、分割された文字列分スタック積み込み。
    TSF_tsvP=TSF_Forth_popthat()
    TSF_tsvQ=TSF_Forth_popthat()
    TSF_tsvK=TSF_tsvQ.split(TSF_tsvP)
    for TSF_tsvA in TSF_tsvK:
        TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_match_chars():   #TSF_doc:[string]文字列を一文字ずつに分割する。1スタック積み下ろし、分割された文字分スタック積み込み。
    TSF_tsvQ=TSF_Forth_popthat()
    for TSF_tsvA in TSF_tsvQ:
        TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_match_equalS():   #TSF_doc:[equal,string]文字列が一致すれば1、不一致なら0を残す。2スタック積み下ろし、1スタック積み込み。
    TSF_tsvS=TSF_Forth_popthat()
    TSF_tsvE=TSF_Forth_popthat()
    TSF_tsvA="1" if TSF_tsvS == TSF_tsvE else "0"
    TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_match_inS():   #TSF_doc:[in,string]文字列が含まれれば1、含まれないなら0を残す。2スタック積み下ろし、1スタック積み込み。
    TSF_tsvS=TSF_Forth_popthat()
    TSF_tsvE=TSF_Forth_popthat()
    TSF_tsvA="1" if TSF_tsvS in TSF_tsvE else "0"
    TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_match_searchS():   #TSF_doc:[search,string]正規表現に該当すれば1、含まれないなら0を残す。2スタック積み下ろし、1スタック積み込み。
    TSF_tsvS=TSF_Forth_popthat()
    TSF_tsvE=TSF_Forth_popthat()
    TSF_research=None
    TSF_tsvA="0"
    try:
        TSF_research=re.search(re.compile(TSF_tsvS),TSF_tsvE)
    except re.error:
        TSF_research=None
    if LTsvDOC_research:
        TSF_tsvA="1"
    TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_match_matcherS():   #TSF_doc:[matcher,string]文字列が完全一致すれば1.0、不一致なら0.0、そこそこ惜しい場合は類似度を小数値で残す。2スタック積み下ろし、1スタック積み込み。
    TSF_tsvS=TSF_Forth_popthat(); TSF_tsvS=unicodedata.normalize('NFKC',TSF_tsvS)
    TSF_tsvE=TSF_Forth_popthat(); TSF_tsvE=unicodedata.normalize('NFKC',TSF_tsvE)
    TSF_tsvA=str(difflib.SequenceMatcher(None,TSF_tsvS,TSF_tsvE).ratio())
    TSF_Forth_pushthat(TSF_tsvA)
    return None

TSF_matchgrade=5/6
def TSF_match_matchgrade():   #TSF_doc:[grade]文字列一致とみなすグレード値を変更。1スタック積み下ろし。
    global TSF_matchgrade
    TSF_tsvG=TSF_Forth_popthat()
    TSF_matchgrade=float(TSF_tsvG)
    return None

def TSF_match_matchif():   #TSF_doc:[then,score]類似度がグレード値を満たせばthenスタックを実行。2スタック積み下ろし。
    TSF_matchscore=TSF_io_floatstr(TSF_Forth_popthat())
    TSF_then=TSF_Forth_popthat()
    TSF_then=TSF_then if TSF_matchscore >= TSF_matchgrade else None
    return TSF_then

def TSF_match_matchelse():   #TSF_doc:[else,score]類似度がグレード値を満たせなかった場合にelseスタックを実行。2スタック積み下ろし。
    TSF_matchscore=TSF_io_floatstr(TSF_Forth_popthat())
    TSF_else=TSF_Forth_popthat()
    TSF_else=TSF_else if TSF_matchscore < TSF_matchgrade else None
    return TSF_else

def TSF_match_matchifelse():   #TSF_doc:[else,then,score]類似度がグレード値を満たせばthenスタック、満たせなかった場合にelseスタックを実行。3スタック積み下ろし、1スタック積み込み。
    TSF_matchscore=TSF_io_floatstr(TSF_Forth_popthat())
    TSF_then=TSF_Forth_popthat()
    TSF_else=TSF_Forth_popthat()
    TSF_ifelse=TSF_then if TSF_matchscore >= TSF_matchgrade else TSF_else
    return TSF_ifelse

def TSF_match_matchcasethe():   #TSF_doc:[stack,matcher,func,string]スタックの文字列置換・カウント・検索などの組み合わせを1つのワードに集約予定。
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_stackvalue(TSF_the)
    return None

def TSF_match_replacethe():   #TSF_doc:[stack,old,new]スタックをテキストとみなして文字列置換する。3スタック積み下ろし。
    TSF_tsvN=TSF_Forth_popthat()
    TSF_tsvO=TSF_Forth_popthat()
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_style(TSF_the,TSF_style="N")
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_Forth_stackvalue(TSF_the)))
    TSF_text=TSF_text.replace(TSF_tsvO,TSF_tsvN)
    TSF_Forth_setTSF(TSF_the,TSF_text,TSF_style="N")
    return None

def TSF_match_replacethat():   #TSF_doc:[old,new]積込先スタックをテキストとみなして文字列置換する。2スタック積み下ろし。
    TSF_tsvN=TSF_Forth_popthat()
    TSF_tsvO=TSF_Forth_popthat()
    TSF_the=TSF_Forth_stackthat()
    TSF_Forth_style(TSF_the,TSF_style="N")
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_Forth_stackvalue(TSF_the)))
    TSF_text=TSF_text.replace(TSF_tsvO,TSF_tsvN)
    TSF_Forth_setTSF(TSF_the,TSF_text,TSF_style="N")
    return None

def TSF_match_resubthe():   #TSF_doc:[stack,old,new]スタックをテキストとみなして文字列置換する。3スタック積み下ろし。
    TSF_tsvN=TSF_Forth_popthat()
    TSF_tsvO=TSF_Forth_popthat()
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_style(TSF_the,TSF_style="N")
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_Forth_stackvalue(TSF_the)))
    TSF_text=re.sub(re.compile(TSF_tsvO,re.MULTILINE),TSF_tsvN,TSF_text)
    TSF_Forth_setTSF(TSF_the,TSF_text,TSF_style="N")
    return None

def TSF_match_resubthat():   #TSF_doc:[old,new]積込先スタックをテキストとみなして文字列置換する。2スタック積み下ろし。
    TSF_tsvN=TSF_Forth_popthat()
    TSF_tsvO=TSF_Forth_popthat()
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_style(TSF_the,TSF_style="N")
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_Forth_stackvalue(TSF_the)))
    TSF_text=re.sub(re.compile(TSF_tsvO,re.MULTILINE),TSF_tsvN,TSF_text)
    TSF_Forth_setTSF(TSF_the,TSF_text,TSF_style="N")
    return None


def TSF_match_debug():    #TSF_doc:「TSF/TSF_shuffle.py」単体テスト風デバッグ関数。
    TSF_tsvS="いいまちがいやうろおぼえ"
    TSF_tsvE="いいまつがいやうるおぼえ"
    TSF_tsvA=str(difflib.SequenceMatcher(None,TSF_tsvS,TSF_tsvE).ratio())
    TSF_io_printlog("{0}:{1}={2}/{3}".format(TSF_tsvS,TSF_tsvE,TSF_tsvA,str(TSF_matchgrade)))

if __name__=="__main__":
    from collections import OrderedDict
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/TSF_match_debug.txt"
    TSF_debug_log=TSF_match_debug()
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
