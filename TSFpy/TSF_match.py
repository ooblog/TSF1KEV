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
    TSF_words["#TSF_charslen"]=TSF_match_charslen; TSF_words["#文字数取得"]=TSF_match_charslen
    TSF_words["#TSF_replacestacks"]=TSF_match_replacestacks; TSF_words["#スタックを文字列群で置換"]=TSF_match_replacestacks
    TSF_words["#TSF_resubstacks"]=TSF_match_resubstacks; TSF_words["#スタックを正規表現群で置換"]=TSF_match_resubstacks
    TSF_words["#TSF_matchgrade"]=TSF_match_matchgrade; TSF_words["#文字列類似の合格点"]=TSF_match_matchgrade
    TSF_words["#TSF_countstacks"]=TSF_match_countstacks; TSF_words["#スタックの該当箇所を数える"]=TSF_match_countstacks
    TSF_words["#TSF_casestacks"]=TSF_match_casestacks; TSF_words["#スタックの該当箇所のエイリアス"]=TSF_match_casestacks
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

def TSF_match_split():   #TSF_doc:[string,spliter]文字列を分割する。2スタック積み下ろし、分割された文字列+分割数1スタック積み込み。
    TSF_tsvP=TSF_Forth_popthat()
    TSF_tsvQ=TSF_Forth_popthat()
    TSF_tsvK=TSF_tsvQ.split(TSF_tsvP)
    for TSF_tsvA in TSF_tsvK:
        TSF_Forth_pushthat(TSF_tsvA)
    TSF_Forth_pushthat(str(len(TSF_tsvK)))
    return None

def TSF_match_chars():   #TSF_doc:[string]文字列を一文字ずつに分割する。1スタック積み下ろし、分割された文字+文字列長1スタック積み込み。
    TSF_tsvQ=TSF_Forth_popthat()
    for TSF_tsvA in TSF_tsvQ:
        TSF_Forth_pushthat(TSF_tsvA)
    TSF_Forth_pushthat(str(len(TSF_tsvQ)))
    return None

def TSF_match_charslen():   #TSF_doc:[string]文字列長を取得する。1スタック積み下ろし、1スタック積み込み。
    TSF_tsvQ=TSF_Forth_popthat()
    TSF_Forth_pushthat(str(len(TSF_tsvQ)))
    return None

def TSF_match_replacestacks():   #TSF_doc:[stackS,stackO,stackN]SスタックをテキストとみなしてOスタックの文字列群をNスタックの文字列群に置換。
    TSF_tsvN=TSF_Forth_popthat(); TSF_strsN=TSF_Forth_stackvalue(TSF_tsvN)
    TSF_tsvO=TSF_Forth_popthat(); TSF_strsO=TSF_Forth_stackvalue(TSF_tsvO)
#    print("TSF_tsvO",TSF_tsvO,TSF_tsvO)
#    print("TSF_strsN",TSF_tsvN,TSF_strsN)
    TSF_strsN.extend([""]*(max(len(TSF_strsO)-len(TSF_strsN),0)))
    TSF_tsvS=TSF_Forth_popthat()
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_Forth_stackvalue(TSF_tsvS)))
#    print("TSF_tsvO",TSF_tsvO)
#    print("TSF_strsN",TSF_strsN)
    for TSF_peek,TSF_strO in enumerate(TSF_strsO):
        TSF_text=TSF_text.replace(TSF_strO,TSF_strsN[TSF_peek])
    TSF_Forth_setTSF(TSF_tsvS,TSF_text,TSF_style="N")
    return None

def TSF_match_resubstacks():   #TSF_doc:[stackS,stackO,stackN]SスタックをテキストとみなしてOスタックの文字列群をNスタックの文字列群に正規表現で置換。
    TSF_tsvN=TSF_Forth_popthat(); TSF_strsN=TSF_Forth_stackvalue(TSF_tsvN)
    TSF_tsvO=TSF_Forth_popthat(); TSF_strsO=TSF_Forth_stackvalue(TSF_tsvO)
    if len(TSF_strsN) < len(TSF_strsO):
        TSF_strsN.extend([""]*(len(TSF_strsO)-len(TSF_strsN)))
    TSF_tsvS=TSF_Forth_popthat()
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_Forth_stackvalue(TSF_tsvS)))
    for TSF_peek,TSF_strO in enumerate(TSF_strsO):
        TSF_text=re.sub(re.compile(TSF_strO,re.MULTILINE),TSF_strsN[TSF_peek],TSF_text)
    TSF_Forth_setTSF(TSF_tsvS,TSF_text,TSF_style="N")
    return None

TSF_matchgrade=5/6
def TSF_match_matchgrade():   #TSF_doc:[grade]文字列一致とみなすグレード値を変更。1スタック積み下ろし。
    global TSF_matchgrade
    TSF_tsvG=TSF_Forth_popthat()
    TSF_matchgrade=float(TSF_tsvG)
    return None

def TSF_match_research(TSF_matcher,TSF_string):   #TSF_doc:正規表現で文字列比較
    try:
        TSF_research=re.search(re.compile(TSF_matcher),TSF_string)
    except re.error:
        TSF_research=None
    return 1 if TSF_research else 0
TSF_match_case=OrderedDict([
    ('equal',(lambda TSF_matcher,TSF_string:1 if matcher == string else 0)),
    ('in',(lambda TSF_matcher,TSF_string:1 if matcher in string else 0)),
    ('research',(lambda TSF_matcher,TSF_string:TSF_match_research(TSF_matcher,TSF_string))),
    ('matcher',(lambda TSF_matcher,TSF_string:1 if difflib.SequenceMatcher(None,unicodedata.normalize('NFKC',TSF_matcher),unicodedata.normalize('NFKC',TSF_string)).ratio() >= TSF_matchgrade else 0)),
])

def TSF_match_countstacks():   #TSF_doc:[matcher,algo,stackO]Oスタックに該当するmatcherの数を数える。algoは文字列の比較方法。
    TSF_tsvO=TSF_Forth_popthat(); TSF_strsO=TSF_Forth_stackvalue(TSF_tsvO)
    TSF_algo=TSF_Forth_popthat()
    TSF_matcher=TSF_Forth_popthat()
    TSF_count=0
    for TSF_strO in TSF_strsO:
        if TSF_match_case.get(TSF_algo,TSF_match_case['equal'])(TSF_matcher,TSF_strO):
            TSF_count+=1
    TSF_Forth_pushthat(str(TSF_count))
    return None

def TSF_match_casestacks():   #TSF_doc:[matcher,algo,stackO,stackN]Oスタックに該当するmatcherがあった場合、stackNのエイリアスを呼び出す。algoは文字列の比較方法。
    TSF_tsvN=TSF_Forth_popthat()
    TSF_tsvO=TSF_Forth_popthat()
    TSF_algo=TSF_Forth_popthat()
    TSF_matcher=TSF_Forth_popthat()
    TSF_case=""
    for TSF_peek,TSF_strO in enumerate(TSF_strsO):
        if TSF_match_case.get(TSF_algo,TSF_match_case['equal'])(TSF_matcher,TSF_strO):
            TSF_case=TSF_Forth_peekthe(TSF_tsvN,TSF_peek)
            break
    TSF_Forth_pushthat(str(TSF_case))
    return None



def TSF_match_matchcasethe():   #TSF_doc:[stack,matcher,func,string]スタックの文字列検索などの組み合わせを1つのワードに集約予定。
    TSF_tsvS=TSF_Forth_popthat()
    TSF_tsvF=TSF_Forth_popthat()
    if '-' in TSF_tsvF:
        TSF_matchF,TSF_matchC=TSF_tsvF.split('-')[0],TSF_tsvF.split('-')[-1]
    else:
        TSF_matchF,TSF_matchC=TSF_tsvF,"first"
    TSF_tsvM=TSF_Forth_popthat()
    TSF_the=TSF_Forth_popthat()
    TSF_matchcases=TSF_Forth_stackvalue(TSF_the)
    if TSF_matchC == "first":
        TSF_count=-1
        for TSF_matchcount,TSF_matchcase in enumerate(TSF_matchcases):
            if TSF_match_case.get(TSF_tsvF,TSF_match_case[TSF_matchF])(TSF_text,TSF_matcher,TSF_string):
                TSF_count=TSF_matchcount; break
    else:  #TSF_matchC == "count":
        TSF_count=0
        for TSF_matchcase in TSF_matchcases:
            TSF_count+=TSF_match_case.get(TSF_tsvF,TSF_match_case[TSF_matchF])(TSF_text,TSF_matcher,TSF_string)
    TSF_Forth_pushthat(str(TSF_count))
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
