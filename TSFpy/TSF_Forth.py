#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_io import *


def TSF_Forth_1ststack():    #TSF_doc:TSF_初期化に使う1ststack名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSF_doc:TSF_初期化に使うバージョン(ブランチ)名(TSFAPI)。
    return "20170301W224954"

TSF_Initcalls=[]
TSF_stacks,TSF_styles,TSF_callptrs,TSF_words=OrderedDict(),OrderedDict(),OrderedDict(),OrderedDict()
TSF_stackthis,TSF_stackthat,TSF_stackcount=TSF_Forth_1ststack(),TSF_Forth_1ststack(),0
def TSF_Forth_run(TSF_argvs=[],TSF_addcalls=[]):    #TSF_doc:TSF_stacks,TSF_styles,TSF_callptrs,TSF_wordsなどをまとめて初期化する(TSFAPI)。
    global TSF_stacks,TSF_styles,TSF_callptrs,TSF_words,TSF_Initcalls,TSF_stackthat,TSF_stackthis,TSF_stackcount
    TSF_stacks,TSF_styles,TSF_callptrs,TSF_words=OrderedDict(),OrderedDict(),OrderedDict(),OrderedDict()
    TSF_stackthis,TSF_stackthat,TSF_stackcount=TSF_Forth_1ststack(),TSF_Forth_1ststack(),0
    TSF_stacks[TSF_stackthis]=["UTF-8","#TSF_encoding","0","#TSF_fin."]
    for TSF_argv in TSF_argvs:
        TSF_Forth_pushthis(TSF_argv)
    TSF_Forth_pushthis(str(len(TSF_argvs)))
    TSF_Initcalls=[TSF_Forth_Initwords]+TSF_addcalls
    for TSF_Initcall in TSF_Initcalls:
        TSF_words=TSF_Initcall(TSF_words)
    TSF_stacknext=None
    while True:
        while TSF_stackcount < len(TSF_stacks[TSF_stackthis]):
            print("TSF_stacks[TSF_stackthis][TSF_stackcount]",TSF_stacks[TSF_stackthis][TSF_stackcount])
            if TSF_stacks[TSF_stackthis][TSF_stackcount] in TSF_words:
                TSF_stacknext=TSF_words[TSF_stacks[TSF_stackthis][TSF_stackcount]]()
            else:
                TSF_Forth_pushthat(TSF_stacks[TSF_stackthis][TSF_stackcount])
            TSF_stackcount+=1
            print(TSF_stackcount,TSF_stacks[TSF_stackthis],len(TSF_stacks[TSF_stackthis]))
            if TSF_stacknext != None:
                print("TSF_stacknext",TSF_stacknext)
                if TSF_stacknext == "":
                    if len(TSF_callptrs) > 0:
                        TSF_stackthis,TSF_stackcount=TSF_callptrs.popitem(True)
                    else:
                        break
                elif TSF_stacknext in TSF_stacks:
                    if TSF_stacknext in TSF_callptrs:
                        while TSF_stacknext in TSF_callptrs:
                           TSF_callptrs.popitem(True)
                    TSF_callptrs[TSF_stackthis]=TSF_stackcount
                    TSF_stackthis=TSF_stacknext
                    TSF_stacknext=None
                    TSF_stackcount=0
                else:
                    break
        if len(TSF_callptrs) > 0:
            TSF_stackthis,TSF_stackcount=TSF_callptrs.popitem(True)
            TSF_stacknext=None
        else:
            break

def TSF_Forth_stackthat(TSF_that):    #TSF_doc:thatスタックの変更(TSFAPI)。
    global TSF_stackthat
    if TSF_that != None:
        TSF_stackthat=TSF_that
    return TSF_stackthat

def TSF_Forth_stackthis(TSF_this):    #TSF_doc:thisスタックの変更(TSFAPI)。
    global TSF_stackthis
    if TSF_this != None:
        TSF_stackthis=TSF_this
    return TSF_stackthis

def TSF_Forth_stackcount(TSF_count):    #TSF_doc:thisスタックの変更(TSFAPI)。
    global TSF_stackcount
    if TSF_count != None:
        TSF_stackcount=TSF_count
    return TSF_stackcount

def TSF_Forth_popthe(TSF_that):    #TSF_doc:スタックを積み下ろす(TSFAPI)。
    global TSF_stacks
    TSF_popdata=""
    if TSF_that in TSF_stacks and len(TSF_stacks[TSF_that]):
        TSF_popdata=TSF_stacks[TSF_that].pop()
    return TSF_popdata

def TSF_Forth_popthat():    #TSF_doc:thatにスタックを積み下ろす(TSFAPI)。
    TSF_popdata=TSF_Forth_popthe(TSF_stackthat)
    return TSF_popdata

def TSF_Forth_popthis():    #TSF_doc:thisにスタックを積み下ろす(TSFAPI)。
    TSF_popdata=TSF_Forth_popthe(TSF_stackthis)
    return TSF_popdata

def TSF_Forth_pushthe(TSF_that,TSF_pushdata):    #TSF_doc:スタックを積み上げる(TSFAPI)。
    global TSF_stacks
    if TSF_that in TSF_stacks:
        TSF_stacks[TSF_that].append(TSF_pushdata)
    else:
        TSF_stacks[TSF_that]=[TSF_pushdata]

def TSF_Forth_pushthat(TSF_pushdata):    #TSF_doc:thatにスタックを積み上げる(TSFAPI)。
   TSF_Forth_pushthe(TSF_stackthat,TSF_pushdata)

def TSF_Forth_pushthis(TSF_pushdata):    #TSF_doc:thisにスタックを積み上げる(TSFAPI)。
   TSF_Forth_pushthe(TSF_stackthis,TSF_pushdata)

def TSF_Forth_Initwords(TSF_words):    #TSF_doc:TSF_words(ワード)を初期化する(TSFAPI)。
    TSF_words["#TSF_fin."]=TSF_Forth_fin; TSF_words["#TSFを終了。"]=TSF_Forth_fin
    TSF_words["#TSF_over."]=TSF_Forth_over; TSF_words["#スタックを終了"]=TSF_Forth_over
    TSF_words["#TSF_encoding"]=TSF_Forth_encoding; TSF_words["#文字コード"]=TSF_Forth_encoding
    TSF_words["#TSF_this"]=TSF_Forth_this; TSF_words["#スタックに入る"]=TSF_Forth_this
    TSF_words["#TSF_that"]=TSF_Forth_that; TSF_words["#スタックに積み込む"]=TSF_Forth_that
    return TSF_words

TSF_exitcode="0"
def TSF_Forth_exitcode(TSF_fincode=None):
    global TSF_exitcode
    if TSF_fincode != None:
        TSF_exitcode=0 if TSF_exitcode in ["0","0|1","0.0"] else TSF_fincode
    return TSF_exitcode

def TSF_Forth_fin():    #TSF_doc:[errmsg]TSF終了時のオプションを指定する。1スタック積み下ろし。
    global TSF_callptrs
    TSF_Forth_exitcode(TSF_Forth_popthat())
    TSF_callptrs=OrderedDict()
    return ""

def TSF_Forth_over():    #TSF_doc:スタックを抜けてコールポインタを1つ減らす。コールポインタが0の時はTSF終了。スタック変化無し。
    return ""

TSF_encode="UTF-8"
def TSF_Forth_encoding():    #TSF_doc:[encode]TSFの文字コード宣言。極力冒頭に置くのが望ましい。1スタック積み下ろし。
    global TSF_encode
    TSF_encode=TSF_Forth_popthat()
    return None

def TSF_Forth_that():    #TSF_doc:thatスタックの変更。1スタック積み下ろし。
   TSF_Forth_stackthat(TSF_Forth_popthat())

def TSF_Forth_this():    #TSF_doc:thatスタックの変更。1スタック積み下ろし。
   TSF_Forth_stackthat(TSF_Forth_popthat())


def TSF_Forth_debug():    #TSF_doc:「TSF/TSF_Forth.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog("TSF_Tab-Separated-Forth:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_argvs:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argvs)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    TSF_Forth_run(TSF_argvs,[])
    TSF_timeQlist=OrderedDict([
        ("TSF_Initcalls:",TSF_Initcalls),
        ("TSF_words:",TSF_words),
        ("TSF_stacks:",TSF_stacks),
    ])
    for TSF_QlistK,TSF_QlistV in TSF_timeQlist.items():
        TSF_debug_log=TSF_io_printlog(TSF_QlistK,TSF_log=TSF_debug_log)
        for LTsv_timeQ in TSF_QlistV:
            TSF_debug_log=TSF_io_printlog("\t{0}⇔{1}".format(LTsv_timeQ,TSF_QlistV),TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/TSF_Forth_debug.txt"
    TSF_debug_log=TSF_Forth_debug()
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
