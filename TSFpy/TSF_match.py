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
    TSF_words["#TSF_joinN"]=TSF_match_joinN; TSF_words["#N個連結"]=TSF_match_joinN
    TSF_words["#TSF_betweenN"]=TSF_match_betweenN; TSF_words["#挟んでN個連結"]=TSF_match_betweenN
    TSF_words["#TSF_split"]=TSF_match_split; TSF_words["#文字で分割"]=TSF_match_split
    TSF_words["#TSF_chars"]=TSF_match_chars; TSF_words["#一文字ずつに分離"]=TSF_match_chars
    TSF_words["#TSF_charslen"]=TSF_match_charslen; TSF_words["#文字数取得"]=TSF_match_charslen
    TSF_words["#TSF_replacestacks"]=TSF_match_replacestacks; TSF_words["#スタックを文字列群で置換"]=TSF_match_replacestacks
    TSF_words["#TSF_resubstacks"]=TSF_match_resubstacks; TSF_words["#スタックを正規表現群で置換"]=TSF_match_resubstacks
    TSF_words["#TSF_matcher"]=TSF_match_matcher; TSF_words["#文字列類似度"]=TSF_match_matcher
    TSF_words["#TSF_matchgrade"]=TSF_match_matchgrade; TSF_words["#文字列類似の合格点"]=TSF_match_matchgrade
    TSF_words["#TSF_countstacks"]=TSF_match_countstacks; TSF_words["#スタックの該当箇所を数える"]=TSF_match_countstacks
    TSF_words["#TSF_casestacks"]=TSF_match_casestacks; TSF_words["#スタックの該当箇所で置換"]=TSF_match_casestacks
    TSF_words["#TSF_tagcyclestack"]=TSF_match_tagcyclestack; TSF_words["#タグ名スタックで周択置換"]=TSF_match_tagcyclestack
    TSF_words["#TSF_taglimitstack"]=TSF_match_taglimitstack; TSF_words["#タグ名スタックで囲択置換"]=TSF_match_taglimitstack
    return TSF_words

def TSF_match_joinN():   #TSF_doc:[stackN…stackB,stackA,count]スタックを連結する。count自身とcountの回数分スタック積み下ろし。
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_joinlist=[""]*TSF_countlen
    for TSF_count in range(TSF_countlen):
        TSF_joinlist[TSF_count]=TSF_Forth_popthat()
    TSF_Forth_pushthat("".join(reversed(TSF_joinlist)))
    return None

def TSF_match_betweenN():   #TSF_doc:[stackN…stackB,stackA,count,joint]スタックAとスタックBを交換する。接続子とcount自身およびcountの回数分スタック積み下ろし。
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
    TSF_strsN.extend([""]*(max(len(TSF_strsO)-len(TSF_strsN),0)))
    TSF_tsvS=TSF_Forth_popthat()
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_Forth_stackvalue(TSF_tsvS)))
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

def TSF_match_matcher():   #TSF_doc:[matcher,string]文字列一致とみなすグレード値を変更。2スタック積み下ろし、1スタック積み上げ。
    TSF_tsvM=TSF_Forth_popthat()
    TSF_tsvS=TSF_Forth_popthat()
    TSF_tsvD=difflib.SequenceMatcher(None,TSF_tsvM,TSF_tsvS).ratio()
    TSF_Forth_pushthat(str(TSF_tsvD))

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
    ('equal',(lambda TSF_matcher,TSF_string:1 if TSF_matcher == TSF_string else 0)),
    ('in',(lambda TSF_matcher,TSF_string:1 if TSF_matcher in TSF_string else 0)),
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
    TSF_tsvO=TSF_Forth_popthat(); TSF_strsO=TSF_Forth_stackvalue(TSF_tsvO)
    TSF_algo=TSF_Forth_popthat()
    TSF_matcher=TSF_Forth_popthat()
    TSF_case=""
    for TSF_peek,TSF_strO in enumerate(TSF_strsO):
        if TSF_match_case.get(TSF_algo,TSF_match_case['equal'])(TSF_matcher,TSF_strO):
            TSF_case=TSF_Forth_peekthe(TSF_tsvN,TSF_peek)
            break
    TSF_Forth_pushthat(str(TSF_case))
    return None

def TSF_match_tagcyclestack():   #TSF_doc:[stackT,tag,peek]tagsスタック名で周択置換。3スタック積み下ろし。
    TSF_peek=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_tsvT=TSF_Forth_popthat(); TSF_tsvsT=TSF_Forth_stackvalue(TSF_tsvT)
    TSF_tsvM=TSF_Forth_popthat(); 
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_Forth_stackvalue(TSF_tsvM)))
    for TSF_tag in TSF_tsvsT:
        TSF_text=TSF_text.replace(TSF_tag,TSF_Forth_peekcyclethe(TSF_tag,TSF_peek))
    TSF_Forth_setTSF(TSF_tsvM,TSF_text,TSF_style="N")
    return None

def TSF_match_taglimitstack():   #TSF_doc:[stackT,tag,peek]tagsスタック名で囲択置換。3スタック積み下ろし。
    TSF_peek=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_tsvT=TSF_Forth_popthat(); TSF_tsvsT=TSF_Forth_stackvalue(TSF_tsvT)
    TSF_tsvM=TSF_Forth_popthat(); 
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_Forth_stackvalue(TSF_tsvM)))
    for TSF_tag in TSF_tsvsT:
        TSF_text=TSF_text.replace(TSF_tag,TSF_Forth_peeklimitthe(TSF_tag,TSF_peek))
    TSF_Forth_setTSF(TSF_tsvM,TSF_text,TSF_style="N")
    return None


def TSF_match_debug(TSF_argvs):    #TSF_doc:「TSF/TSF_shuffle.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_Forth_init(TSF_argvs,[TSF_match_Initwords])
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","0.8","#TSF_matchgrade","TSF_matchtest:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("TSF_match.py:","\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout]))
    TSF_Forth_setTSF("TSF_matchtest:","\t".join(["TSF_matchBF:","#TSF_that","いいまちがいやうろおぼえ","いいまつがいやうるおぼえ","TSF_matchAF:","#TSF_that","いいまちがいやうろおぼえ","いいまつがいやうるおぼえ","#TSF_matcher"]))
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
    TSF_debug_savefilename="debug/debug_match.log"
    TSF_debug_log=TSF_match_debug(TSF_argvs)
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
