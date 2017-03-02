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
def TSF_Forth_init(TSF_argvs=[],TSF_addcalls=[]):    #TSF_doc:TSF_stacks,TSF_styles,TSF_callptrs,TSF_wordsなどをまとめて初期化する(TSFAPI)。
    global TSF_stacks,TSF_styles,TSF_callptrs,TSF_words,TSF_Initcalls,TSF_stackthat,TSF_stackthis,TSF_stackcount
    TSF_stacks,TSF_styles,TSF_callptrs,TSF_words=OrderedDict(),OrderedDict(),OrderedDict(),OrderedDict()
    TSF_stackthis,TSF_stackthat,TSF_stackcount=TSF_Forth_1ststack(),TSF_Forth_1ststack(),0
    TSF_stacks[TSF_stackthis]=["UTF-8","#TSF_encoding","0","#TSF_fin."]; TSF_Forth_pushargvs(TSF_argvs)
    TSF_Initcalls=[TSF_Forth_Initwords]+TSF_addcalls
    for TSF_Initcall in TSF_Initcalls:
        TSF_words=TSF_Initcall(TSF_words)

def TSF_Forth_run():    #TSF_doc:TSF_stacks,TSF_styles,TSF_callptrs,TSF_wordsなどをまとめて初期化する(TSFAPI)。
    global TSF_stacks,TSF_styles,TSF_callptrs,TSF_words,TSF_Initcalls,TSF_stackthat,TSF_stackthis,TSF_stackcount
    while True:
        while TSF_stackcount < len(TSF_stacks[TSF_stackthis]):
            TSF_stacknow,TSF_stacknext=TSF_stacks[TSF_stackthis][TSF_stackcount],None
            if TSF_stacknow in TSF_words:
                TSF_stacknext=TSF_words[TSF_stacknow]()
            else:
                TSF_Forth_pushthat(TSF_stacknow)
            TSF_stackcount+=1
            if TSF_stacknext != None:
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
                    TSF_stackcount=0
                else:
                    break
        if len(TSF_callptrs) > 0:
            TSF_stackthis,TSF_stackcount=TSF_callptrs.popitem(True)
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

def TSF_Forth_popthat():    #TSF_doc:thatからスタックを積み下ろす(TSFAPI)。
    TSF_popdata=TSF_Forth_popthe(TSF_stackthat)
    return TSF_popdata

def TSF_Forth_popthis():    #TSF_doc:thisからスタックを積み下ろす(TSFAPI)。
    TSF_popdata=TSF_Forth_popthe(TSF_stackthis)
    return TSF_popdata

def TSF_Forth_pintthe(TSF_that):    #TSF_doc:スタックを数値として積み下ろす(TSFAPI)。
    TSF_popdata=TSF_Forth_popthat()
    if '|' in TSF_popdata:
        TSF_calcN,TSF_calcD=TSF_calcQ.replace('m','-').replace('p','').split('|')
        TSF_popdata=TSF_io_intstr0x(TSF_calcN)//TSF_io_intstr0x(TSF_calcD)
    else:
        TSF_popdata=TSF_io_intstr0x(TSF_popdata)
    return TSF_popdata

def TSF_Forth_pintthat():    #TSF_doc:thatからスタックを数値として積み下ろす(TSFAPI)。
    TSF_popdata=TSF_Forth_pintthe(TSF_stackthat)
    return TSF_popdata

def TSF_Forth_pintthis():    #TSF_doc:thisからスタックを数値として積み下ろす(TSFAPI)。
    TSF_popdata=TSF_Forth_pintthe(TSF_stackthis)
    return TSF_popdata

def TSF_Forth_pushthe(TSF_that,TSF_pushdata):    #TSF_doc:スタックを積み上げる(TSFAPI)。
    global TSF_stacks
    if TSF_that in TSF_stacks:
        TSF_stacks[TSF_that].append(TSF_pushdata)
    else:
        TSF_stacks[TSF_that]=[TSF_pushdata]

def TSF_Forth_pushthat(TSF_pushdata):    #TSF_doc:thatにスタックを積み上げる(TSFAPI)。
   TSF_Forth_pushthe(TSF_stackthat,TSF_pushdata)

def TSF_Forth_pushargvs(TSF_argvs):    #TSF_doc:thisにスタックを積み上げる(TSFAPI)。
    for TSF_argv in TSF_argvs:
        TSF_Forth_pushthat(TSF_argv)

def TSF_Forth_pushthis(TSF_pushdata):    #TSF_doc:thisにスタックを積み上げる(TSFAPI)。
   TSF_Forth_pushthe(TSF_stackthis,TSF_pushdata)

def TSF_Forth_Initwords(TSF_words):    #TSF_doc:TSF_words(ワード)を初期化する(TSFAPI)。
    TSF_words["#TSF_fin."]=TSF_Forth_fin; TSF_words["#TSFを終了。"]=TSF_Forth_fin
    TSF_words["#TSF_over"]=TSF_Forth_over; TSF_words["#スタックを終了"]=TSF_Forth_over
    TSF_words["#TSF_encoding"]=TSF_Forth_encoding; TSF_words["#文字コード"]=TSF_Forth_encoding
    TSF_words["#TSF_this"]=TSF_Forth_this; TSF_words["#スタックに入る"]=TSF_Forth_this
    TSF_words["#TSF_that"]=TSF_Forth_that; TSF_words["#スタックに積込"]=TSF_Forth_that
    TSF_words["#TSF_echoes"]=TSF_Forth_echoes; TSF_words["#N行表示"]=TSF_Forth_echoes
    TSF_words["#TSF_viewthe"]=TSF_Forth_viewthe; TSF_words["#スタックを表示"]=TSF_Forth_viewthe
    TSF_words["#TSF_viewthis"]=TSF_Forth_viewthis; TSF_words["#実行中スタックを表示"]=TSF_Forth_viewthis
    TSF_words["#TSF_viewthat"]=TSF_Forth_viewthat; TSF_words["#積込先スタックを表示"]=TSF_Forth_viewthat
    TSF_words["#TSF_viewthey"]=TSF_Forth_viewthey; TSF_words["#スタック一覧を表示"]=TSF_Forth_viewthey
    TSF_words["#TSF_stylethe"]=TSF_Forth_stylethe; TSF_words["#スタックにスタイル指定"]=TSF_Forth_stylethe
    TSF_words["#TSF_stylethis"]=TSF_Forth_stylethis; TSF_words["#実行中スタックにスタイル指定"]=TSF_Forth_stylethis
    TSF_words["#TSF_stylethat"]=TSF_Forth_stylethat; TSF_words["#積込先スタックにスタイル指定"]=TSF_Forth_stylethat
    TSF_words["#TSF_readtext"]=TSF_Forth_readtext; TSF_words["#テキストファイルを読み込む"]=TSF_Forth_readtext
    TSF_words["#TSF_mergethe"]=TSF_Forth_mergethe; TSF_words["#TSFに合成する"]=TSF_Forth_mergethe
    TSF_words["#TSF_publishthe"]=TSF_Forth_publishthe; TSF_words["#スタックをテキスト化"]=TSF_Forth_publishthe
    TSF_words["#TSF_publishthis"]=TSF_Forth_publishthis; TSF_words["#実行中スタックをテキスト化"]=TSF_Forth_publishthis
    TSF_words["#TSF_publishthat"]=TSF_Forth_publishthat; TSF_words["#積込先スタックをテキスト化"]=TSF_Forth_publishthat
    TSF_words["#TSF_remove"]=TSF_Forth_remove; TSF_words["#ファイルを削除する"]=TSF_Forth_remove
    TSF_words["#TSF_savetext"]=TSF_Forth_savetext; TSF_words["#テキストファイルに上書きする"]=TSF_Forth_savetext
    TSF_words["#TSF_writetext"]=TSF_Forth_writetext; TSF_words["#テキストファイルに追記きする"]=TSF_Forth_writetext
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
    return None

def TSF_Forth_this():    #TSF_doc:thatスタックの変更。1スタック積み下ろし。
    return TSF_Forth_popthat()

def TSF_Forth_echoes():    #TSF_doc:[…valueB,valueA,count]スタック内容をstdout表示する。count自身とcount分スタック積み下ろし。
    TSF_loop=TSF_Forth_pintthat()
    for TSF_echocount in range(TSF_loop):
        TSF_io_printlog(TSF_Forth_popthat())
    return None

def TSF_Forth_view(TSF_the,TSF_view_io=True,TSF_view_log=""):    #TSF_doc:スタックの内容をテキスト表示(TSFAPI)。
    if TSF_the in TSF_stacks:
        TSF_stackV=[TSF_txt_ESCdecode(TSF_stk) for TSF_stk in TSF_stacks[TSF_the]]
        TSF_style=TSF_styles.get(TSF_the,"T")
        if TSF_style == "O":
            TSF_view_logline="{0}\t{1}\n".format(TSF_thename,"\t".join(TSF_stackV))
        elif TSF_style == "T":
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_the,"\t".join(TSF_stackV))
        else:  # TSF_style == "N":
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_the,"\n\t".join(TSF_stackV))
        if TSF_view_io == True:
            TSF_view_log=TSF_io_printlog(TSF_view_logline,TSF_log=TSF_view_log)
        else:
            TSF_view_log+=TSF_view_logline
    return TSF_view_log

def TSF_Forth_viewthe():    #TSF_doc:[stack]指定したスタックを表示する。1スタック積み下ろし。
    TSF_Forth_view(TSF_Forth_popthat())
    return None

def TSF_Forth_viewthis():    #TSF_doc:[]実行中スタックを表示する。0スタック積み下ろし。
    TSF_Forth_view(TSF_stackthis)
    return None

def TSF_Forth_viewthat():    #TSF_doc:[]積込先スタックを表示する。0スタック積み下ろし。
    TSF_Forth_view(TSF_stackthat)
    return None

def TSF_Forth_viewthey():    #TSF_doc:[]スタック一覧を表示する。0スタック積み下ろし。
    for TSF_thename in TSF_stacks.keys():
        TSF_Forth_view(TSF_thename)
    return None

def TSF_Forth_style(TSF_the,TSF_style=None):    #TSF_doc:スタックの表示スタイルを指定する(TSFAPI)。
    global TSF_styles
    if TSF_style != None:
        TSF_styles[TSF_the]=TSF_style
    return TSF_styles[TSF_the]

def TSF_Forth_stylethe():    #TSF_doc:[style,stack]スタックの表示スタイルを指定する。2スタック積み下ろし。
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_style(TSF_the,TSF_Forth_popthat())
    return None

def TSF_Forth_stylethis():    #TSF_doc:[stack]実行中スタックの表示スタイルを指定する。1スタック積み下ろし。
    TSF_Forth_style(TSF_stackthis,TSF_Forth_popthis())
    return None

def TSF_Forth_stylethat():    #TSF_doc:[stack]積込先スタックの表示スタイルを指定する。1スタック積み下ろし。
    TSF_Forth_style(TSF_stackthat,TSF_Forth_popthat())
    return None

def TSF_Forth_setTSF(TSF_the,TSF_text,TSF_style="T"):    #TSF_doc:スタックにTSFを読み込む(TSFAPI)。
    global TSF_stacks,TSF_styles
    TSF_stacks[TSF_the]=TSF_text.rstrip('\n').replace('\t','\n').split('\n')
    TSF_styles[TSF_the]=TSF_style

def TSF_Forth_loadtext(TSF_the,TSF_path):    #TSF_doc:テキストファイルを読み込んでTSF_stacksの一スタック扱いにする(TSFAPI)。
    TSF_text=TSF_io_loadtext(TSF_path)
    TSF_text=TSF_txt_ESCencode(TSF_text)
    TSF_Forth_setTSF(TSF_the,TSF_text)
    TSF_Forth_style(TSF_the,"N")
    return TSF_text

def TSF_Forth_readtext():   #TSF_doc:[filename]ファイルをスタックに積む。1スタック積み下ろし。
    TSF_path=TSF_Forth_popthat()
    TSF_Forth_loadtext(TSF_path,TSF_path)
    return None

def TSF_Forth_merge(TSF_stack,TSF_ESCstack=[]):    #TSF_doc:テキストをTSFとして読み込む(TSFAPI)。
    global TSF_stacks,TSF_styles
    TSF_that=TSF_Forth_1ststack()
    TSF_styles[TSF_that]="T"
    for TSF_stackV in TSF_stacks[TSF_stack]:
        if len(TSF_stackV) == 0: continue;
        if TSF_stackV.startswith("#"): continue;
        TSF_stackV=TSF_txt_ESCdecode(TSF_stackV)
        if not TSF_stackV.startswith('\t'):
            TSF_stackL=TSF_stackV.lstrip('\t').split('\t')
            if not TSF_stackL[0] in TSF_ESCstack:
                TSF_that=TSF_stackL[0]
                TSF_stacks[TSF_that]=[]
                TSF_styles[TSF_that]="O" if len(TSF_stackL) >= 2 else ""
        if not TSF_that in TSF_ESCstack:
            TSF_stackL=TSF_stackV.split('\t')[1:]
            TSF_stacks[TSF_that].extend(TSF_stackL)
            if TSF_styles[TSF_that] != "O":
                TSF_styles[TSF_that]="T" if len(TSF_stackL) >= 2 else "N"

def TSF_Forth_mergethe():   #TSF_doc:[stack]テキストをTSFとして読み込む。1スタック積み下ろし。
    TSF_Forth_merge(TSF_Forth_popthat(),TSF_ESCstack=[TSF_Forth_1ststack()])
    return None

def TSF_Forth_publishthe():   #TSF_doc:[filename,stack]スタックをテキスト化。2スタック積み下ろし。
    TSF_publish_log=TSF_Forth_view(TSF_Forth_popthat(),False,"")
    TSF_Forth_settext(TSF_Forth_popthat(),TSF_txt_ESCencode(TSF_publish_log),TSF_style="N")
    return None

def TSF_Forth_publishthis():   #TSF_doc:[filename]実行中スタックをテキスト化。1スタック積み下ろし。
    TSF_publish_log=TSF_Forth_view(TSF_stackthis,False,"")
    TSF_Forth_settext(TSF_Forth_popthat(),TSF_txt_ESCencode(TSF_publish_log),TSF_style="N")
    return None

def TSF_Forth_publishthat():   #TSF_doc:[filename]積込先スタックをテキスト化。1スタック積み下ろし。
    TSF_publish_log=TSF_Forth_view(TSF_stackthat,False,"")
    TSF_Forth_settext(TSF_Forth_popthat(),TSF_txt_ESCencode(TSF_publish_log),TSF_style="N")
    return None

def TSF_Forth_remove():   #TSF_doc:[filename]ファイルを削除する。1スタック積み下ろし。
    TSF_io_savetext(TSF_Forth_popthat(),TSF_text=None)
    return None

def TSF_Forth_savetext():   #TSF_doc:[filename,stack]スタック内容をテキストとみなしてファイルに保存する。2スタック積み下ろし。
    TSF_the=TSF_Forth_popthat()
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_stacks[TSF_the])) if TSF_the in TSF_stacks else ""
    TSF_io_savetext(TSF_Forth_popthat(),TSF_text=TSF_text)
    return None

def TSF_Forth_writetext():   #TSF_doc:[filename,stack]スタック内容をテキストとみなしてファイルに追記する。2スタック積み下ろし。
    TSF_the=TSF_Forth_popthat()
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_stacks[TSF_the])) if TSF_the in TSF_stacks else ""
    TSF_io_writetext(TSF_Forth_popthat(),TSF_text=TSF_text)
    return None

def TSF_Forth_debug(TSF_argvs):    #TSF_doc:「TSF/TSF_Forth.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_Forth_init(TSF_argvs,[])
    TSF_Forth_viewthey()
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argvs)),TSF_log=TSF_debug_log)
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","about:","#TSF_this","0","#TSF_fin."]))
    TSF_timeQlist=OrderedDict([
        ("TSF_Initcalls:",TSF_Initcalls),
        ("TSF_words:",TSF_words),
    ])
    for TSF_QlistK,TSF_QlistV in TSF_timeQlist.items():
        TSF_debug_log=TSF_io_printlog(TSF_QlistK,TSF_log=TSF_debug_log)
        for LTsv_timeQ in TSF_QlistV:
            TSF_debug_log=TSF_io_printlog("\t{0}⇔{1}".format(LTsv_timeQ,TSF_QlistV),TSF_debug_log)
    TSF_Forth_run()
    return TSF_debug_log

if __name__=="__main__":
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/TSF_Forth_debug.txt"
    TSF_debug_log=TSF_Forth_debug(TSF_argvs)
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
