#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import random
import copy
from TSF_io import *

def TSF_Forth_1ststack():    #TSF_doc:TSF_初期化に使う最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSF_doc:TSF_初期化に使うバージョン(ブランチ)名(TSFAPI)。
    return "20170301W224954"

def TSF_Forth_Initwords(TSF_words):    #TSF_doc:ワードを初期化する(TSFAPI)。
    TSF_words["#TSF_fin."]=TSF_Forth_fin; TSF_words["#TSFを終了。"]=TSF_Forth_fin
    TSF_words["#TSF_over"]=TSF_Forth_over; TSF_words["#スタックを終了"]=TSF_Forth_over
    TSF_words["#TSF_encoding"]=TSF_Forth_encoding; TSF_words["#文字コード"]=TSF_Forth_encoding
    TSF_words["#TSF_this"]=TSF_Forth_this; TSF_words["#スタックに入る"]=TSF_Forth_this
    TSF_words["#TSF_that"]=TSF_Forth_that; TSF_words["#スタックに積込"]=TSF_Forth_that
    TSF_words["#TSF_input"]=TSF_Forth_input; TSF_words["#文字列入力"]=TSF_Forth_input
    TSF_words["#TSF_echoN"]=TSF_Forth_echoN; TSF_words["#N行表示"]=TSF_Forth_echoN
    TSF_words["#TSF_echothe"]=TSF_Forth_echothe; TSF_words["#スタック行表示"]=TSF_Forth_echothe
    TSF_words["#TSF_echothis"]=TSF_Forth_echothis; TSF_words["#実行中スタック行表示"]=TSF_Forth_echothis
    TSF_words["#TSF_echothat"]=TSF_Forth_echothat; TSF_words["#積込先スタック行表示"]=TSF_Forth_echothat
    TSF_words["#TSF_viewthe"]=TSF_Forth_viewthe; TSF_words["#スタック表示"]=TSF_Forth_viewthe
    TSF_words["#TSF_viewthis"]=TSF_Forth_viewthis; TSF_words["#実行中スタックを表示"]=TSF_Forth_viewthis
    TSF_words["#TSF_viewthat"]=TSF_Forth_viewthat; TSF_words["#積込先スタックを表示"]=TSF_Forth_viewthat
    TSF_words["#TSF_viewthey"]=TSF_Forth_viewthey; TSF_words["#スタック一覧を表示"]=TSF_Forth_viewthey
    TSF_words["#TSF_viewargvs"]=TSF_Forth_viewargvs; TSF_words["#argvs(1stスタック)を表示"]=TSF_Forth_viewargvs
    TSF_words["#TSF_stylethe"]=TSF_Forth_stylethe; TSF_words["#スタックにスタイル指定"]=TSF_Forth_stylethe
    TSF_words["#TSF_stylethis"]=TSF_Forth_stylethis; TSF_words["#実行中スタックにスタイル指定"]=TSF_Forth_stylethis
    TSF_words["#TSF_stylethat"]=TSF_Forth_stylethat; TSF_words["#積込先スタックにスタイル指定"]=TSF_Forth_stylethat
    TSF_words["#TSF_readtext"]=TSF_Forth_readtext; TSF_words["#テキストファイルを読込"]=TSF_Forth_readtext
    TSF_words["#TSF_mergethe"]=TSF_Forth_mergethe; TSF_words["#TSFに合成"]=TSF_Forth_mergethe
    TSF_words["#TSF_publishthe"]=TSF_Forth_publishthe; TSF_words["#スタックをテキスト化"]=TSF_Forth_publishthe
    TSF_words["#TSF_publishthis"]=TSF_Forth_publishthis; TSF_words["#実行中スタックをテキスト化"]=TSF_Forth_publishthis
    TSF_words["#TSF_publishthat"]=TSF_Forth_publishthat; TSF_words["#積込先スタックをテキスト化"]=TSF_Forth_publishthat
    TSF_words["#TSF_remove"]=TSF_Forth_remove; TSF_words["#ファイルを削除する"]=TSF_Forth_remove
    TSF_words["#TSF_savetext"]=TSF_Forth_savetext; TSF_words["#テキストファイルに上書"]=TSF_Forth_savetext
    TSF_words["#TSF_writetext"]=TSF_Forth_writetext; TSF_words["#テキストファイルに追記"]=TSF_Forth_writetext
    return TSF_words

TSF_exitcode="0"
def TSF_Forth_exitcode(TSF_fincode=None):
    global TSF_exitcode
    if TSF_fincode != None:
        TSF_exitcode=TSF_fincode
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

def TSF_Forth_input():   #TSF_doc:[]文字列を入力させる。1スタック積み込み。
    TSF_tsvA=raw_input()
    TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_Forth_echoN():    #TSF_doc:[…valueB,valueA,count]N個のスタックをstdout表示する。count自身とcount分スタック積み下ろし。
    TSF_countlen=TSF_Forth_popintthe(TSF_stackthat)
    for TSF_count in range(TSF_countlen):
        TSF_io_printlog(TSF_Forth_popthat())
    return None

def TSF_Forth_echothe():    #TSF_doc:[stack]
    TSF_io_printlog("\n".join(TSF_stacks[TSF_Forth_popthat()]))
    return None

def TSF_Forth_echothis():    #TSF_doc:[]
    TSF_io_printlog("\n".join(TSF_stacks[TSF_stackthis]))
    return None

def TSF_Forth_echothat():    #TSF_doc:[]
    TSF_io_printlog("\n".join(TSF_stacks[TSF_stackthat]))
    return None

def TSF_Forth_view(TSF_the,TSF_view_io=True,TSF_view_log=""):    #TSF_doc:スタックの内容をテキスト表示(TSFAPI)。
    if TSF_the in TSF_stacks:
        TSF_stackV=[TSF_txt_ESCdecode(TSF_stk) for TSF_stk in TSF_stacks[TSF_the]]
        TSF_style=TSF_styles.get(TSF_the,"T")
        if TSF_style == "O":
            TSF_view_logline="{0}\t{1}\n".format(TSF_the,"\t".join(TSF_stackV))
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

def TSF_Forth_viewargvs():    #TSF_doc:[]1stスタックを表示する。0スタック積み下ろし。
    TSF_Forth_view(TSF_Forth_1ststack())
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
    TSF_Forth_style(TSF_stackthis,TSF_Forth_popthat())
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

def TSF_Forth_merge(TSF_the,TSF_ESCstack=[],TSF_mergedel=None):    #TSF_doc:テキストをTSFとして読み込む(TSFAPI)。
    global TSF_stacks,TSF_styles
    if TSF_the in TSF_stacks:
        TSF_that=TSF_Forth_1ststack()
        for TSF_stackV in TSF_stacks[TSF_the]:
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
        if TSF_mergedel:
            del TSF_stacks[TSF_the]

def TSF_Forth_mergethe():   #TSF_doc:[stack]テキストをTSFとして読み込む。1スタック積み下ろし。
    TSF_Forth_merge(TSF_Forth_popthat(),TSF_ESCstack=[TSF_Forth_1ststack()])
    return None

def TSF_Forth_publishthe():   #TSF_doc:[filename,stack]スタックをテキスト化。2スタック積み下ろし。
    TSF_publish_log=TSF_Forth_view(TSF_Forth_popthat(),False,"")
    TSF_Forth_setTSF(TSF_Forth_popthat(),TSF_txt_ESCencode(TSF_publish_log),TSF_style="N")
    return None

def TSF_Forth_publishthis():   #TSF_doc:[filename]実行中スタックをテキスト化。1スタック積み下ろし。
    TSF_publish_log=TSF_Forth_view(TSF_stackthis,False,"")
    TSF_Forth_setTSF(TSF_Forth_popthat(),TSF_txt_ESCencode(TSF_publish_log),TSF_style="N")
    return None

def TSF_Forth_publishthat():   #TSF_doc:[filename]積込先スタックをテキスト化。1スタック積み下ろし。
    TSF_publish_log=TSF_Forth_view(TSF_stackthat,False,"")
    TSF_Forth_setTSF(TSF_Forth_popthat(),TSF_txt_ESCencode(TSF_publish_log),TSF_style="N")
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


TSF_Initcalls=[]
TSF_stacks,TSF_styles,TSF_callptrs,TSF_words=OrderedDict(),OrderedDict(),OrderedDict(),OrderedDict()
TSF_stackthis,TSF_stackthat,TSF_stackcount=TSF_Forth_1ststack(),TSF_Forth_1ststack(),0
def TSF_Forth_init(TSF_argvs=[],TSF_addcalls=[]):    #TSF_doc:TSF_stacks,TSF_styles,TSF_callptrs,TSF_wordsなどをまとめて初期化する(TSFAPI)。
    global TSF_stacks,TSF_styles,TSF_callptrs,TSF_words,TSF_Initcalls,TSF_stackthat,TSF_stackthis,TSF_stackcount
    TSF_stacks,TSF_styles,TSF_callptrs,TSF_words=OrderedDict(),OrderedDict(),OrderedDict(),OrderedDict()
    TSF_stackthis,TSF_stackthat,TSF_stackcount=TSF_Forth_1ststack(),TSF_Forth_1ststack(),0
    TSF_stacks[TSF_stackthis]=["UTF-8","#TSF_encoding","0","#TSF_fin."]; TSF_Forth_addfin(TSF_argvs)
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

def TSF_Forth_stackthis(TSF_this=None):    #TSF_doc:thisスタックの変更(TSFAPI)。
    global TSF_stackthis
    if TSF_this != None:
        TSF_stackthis=TSF_this
    return TSF_stackthis

def TSF_Forth_stackcount(TSF_count=None):    #TSF_doc:thisカウントの変更(TSFAPI)。
    global TSF_stackcount
    if TSF_count != None:
        TSF_stackcount=TSF_count
    return TSF_stackcount

def TSF_Forth_stackthat(TSF_that=None):    #TSF_doc:thatスタックの変更(TSFAPI)。
    global TSF_stackthat
    if TSF_that != None:
        TSF_stackthat=TSF_that
    return TSF_stackthat

def TSF_Forth_stacklen(TSF_the):    #TSF_doc:thisスタックの個数(TSFAPI)。
    return len(TSF_stacks.get(TSF_the,[]))

def TSF_Forth_stackvalue(TSF_the):    #TSF_doc:スタックのデータ(TSFAPI)。
    return TSF_stacks.get(TSF_the,[])

def TSF_Forth_stackslen():    #TSF_doc:スタック一覧の個数(TSFAPI)。
    return len(TSF_stacks)

def TSF_Forth_stackskeys():    #TSF_doc:スタック一覧の鍵のイテレータ(TSFAPI)。
    return TSF_stacks.keys()

def TSF_Forth_stacksvalues():    #TSF_doc:スタック一覧の値のイテレータ(TSFAPI)。
    return TSF_stacks.values()

def TSF_Forth_stacksitems():    #TSF_doc:スタック一覧の鍵値タプルのイテレータ(TSFAPI)。
    return TSF_stacks.items()

def TSF_Forth_popthe(TSF_that):    #TSF_doc:スタックから積み下ろす(TSFAPI)。
    global TSF_stacks
    TSF_popdata=""
    if TSF_that in TSF_stacks and len(TSF_stacks[TSF_that]):
        TSF_popdata=TSF_stacks[TSF_that].pop()
    return TSF_popdata

def TSF_Forth_popthat():    #TSF_doc:thatからスタックから積み下ろす(TSFAPI)。
    TSF_popdata=TSF_Forth_popthe(TSF_stackthat)
    return TSF_popdata

def TSF_Forth_popthis():    #TSF_doc:thisからスタックから積み下ろす(TSFAPI)。
    TSF_popdata=TSF_Forth_popthe(TSF_stackthis)
    return TSF_popdata

def TSF_Forth_popintthe(TSF_that):    #TSF_doc:スタックから数値として積み下ろす(TSFAPI)。
    TSF_calcQ=TSF_Forth_popthat()
    if '|' in TSF_calcQ:
        TSF_calcN,TSF_calcD=TSF_calcQ.replace('m','-').replace('p','').split('|')
        TSF_popdata=TSF_io_intstr0x(TSF_calcN)//TSF_io_intstr0x(TSF_calcD)
    else:
        TSF_calcN=TSF_calcQ.replace('m','-').replace('p','')
        TSF_popdata=TSF_io_intstr0x(TSF_calcN)
    return TSF_popdata

def TSF_Forth_pushthe(TSF_the,TSF_pushdata):    #TSF_doc:スタックに積み上げる(TSFAPI)。
    global TSF_stacks
    if TSF_the in TSF_stacks:
        TSF_stacks[TSF_the].append(TSF_pushdata)
    else:
        TSF_stacks[TSF_the]=[TSF_pushdata]

def TSF_Forth_pushthis(TSF_pushdata):    #TSF_doc:実行中スタックに積み上げる(TSFAPI)。
   TSF_Forth_pushthe(TSF_stackthis,TSF_pushdata)

def TSF_Forth_pushthat(TSF_pushdata):    #TSF_doc:積込先スタックに積み上げる(TSFAPI)。
   TSF_Forth_pushthe(TSF_stackthat,TSF_pushdata)

def TSF_Forth_addargvs(TSF_the,TSF_argvs):    #TSF_doc:積込先スタックにargvsを積み上げる(TSFAPI)。
    for TSF_argv in TSF_argvs:
        TSF_Forth_pushthe(TSF_the,TSF_argv)

def TSF_Forth_addargvslen(TSF_argvs):    #TSF_doc:積込先スタックにargvsの数を積み上げる(TSFAPI)。
    TSF_Forth_pushthat(str(len(TSF_argvs)))

def TSF_Forth_addfin(TSF_argvs):    #TSF_doc:「#TSF_fin.」が含まれてない場合追加してからargvsとargvslenを追加(TSFAPI)。
    if not "#TSF_fin." in TSF_stacks[TSF_Forth_1ststack()]:
        TSF_stacks[TSF_Forth_1ststack()].extend(["0","#TSF_fin."])
    TSF_Forth_addargvs(TSF_Forth_1ststack(),TSF_argvs)
    TSF_Forth_addargvslen(TSF_argvs)

def TSF_Forth_peekthe(TSF_the,TSF_count):    #TSF_doc:スタックの読込(TSFAPI)。
    TSF_peekdata=""
    if TSF_the in TSF_stacks:
        if 0 <= TSF_count < len(TSF_stacks[TSF_the]):
            TSF_peekdata=TSF_stacks[TSF_the][TSF_count]
        elif -len(TSF_stacks[TSF_the]) <= TSF_count < 0:
            TSF_peekdata=TSF_stacks[TSF_the][TSF_count]
    return TSF_peekdata

def TSF_Forth_peekcyclethe(TSF_the,TSF_count):    #TSF_doc:周択でスタックの読込(TSFAPI)。
    TSF_peekdata=""
    if TSF_the in TSF_stacks:
        TSF_countmod=TSF_count%len(TSF_stacks[TSF_the]) if TSF_count >=0 else len(TSF_stacks[TSF_the])-(abs(TSF_count)%len(TSF_stacks[TSF_the]))
        TSF_peekdata=TSF_stacks[TSF_the][TSF_countmod] if len(TSF_stacks[TSF_the]) > 0 else TSF_peekdata
    return TSF_peekdata

def TSF_Forth_peeklimitthe(TSF_the,TSF_count):    #TSF_doc:囲択でスタックの読込(TSFAPI)。
    TSF_peekdata=""
    if TSF_the in TSF_stacks:
        TSF_countlimit=max(min(TSF_count,len(TSF_stacks[TSF_the])-1),0)
        TSF_peekdata=TSF_stacks[TSF_the][TSF_countlimit] if len(TSF_stacks[TSF_the]) > 0 else TSF_peekdata
    return TSF_peekdata

def TSF_Forth_reversethe(TSF_the):    #TSF_doc:スタックのシャッフル(TSFAPI)。
    if TSF_the in TSF_stacks:
        TSF_stacks[TSF_the]=list(reversed(TSF_stacks[TSF_the]))

def TSF_Forth_shufflethe(TSF_the):    #TSF_doc:スタックのシャッフル(TSFAPI)。
    if TSF_the in TSF_stacks:
        random.shuffle(TSF_stacks[TSF_the])

def TSF_Forth_pokethe(TSF_the,TSF_count,TSF_poke):    #TSF_doc:スタックへの書込(TSFAPI)。
    TSF_pokeerr=0
    if TSF_the in TSF_stacks:
        if 0 <= TSF_count < len(TSF_stacks[TSF_the]):
            TSF_stacks[TSF_the][TSF_count]=TSF_poke
        elif -len(TSF_stacks[TSF_the]) <= TSF_count < 0:
            TSF_stacks[TSF_the][TSF_count]=TSF_poke
        else:
            TSF_pokeerr=1
    else:
        TSF_pokeerr=2
    return TSF_pokeerr

def TSF_Forth_pokecyclethe(TSF_the,TSF_count):    #TSF_doc:周択でスタックの書込(TSFAPI)。
    TSF_peekdata=""
    if TSF_the in TSF_stacks:
        TSF_countmod=TSF_count%len(TSF_stacks[TSF_the]) if TSF_count >=0 else len(TSF_stacks[TSF_the])-(abs(TSF_count)%len(TSF_stacks[TSF_the]))
        if len(TSF_stacks[TSF_the]) > 0:
            TSF_stacks[TSF_the][TSF_countmod]=TSF_poke
        else:
            TSF_pokeerr=1
    else:
        TSF_pokeerr=2

def TSF_Forth_pokelimitthe(TSF_the,TSF_count):    #TSF_doc:囲択でスタックの書込(TSFAPI)。
    TSF_peekdata=""
    if TSF_the in TSF_stacks:
        TSF_countlimit=max(min(TSF_count,len(TSF_stacks[TSF_the])),0)
        if len(TSF_stacks[TSF_the]) > 0:
            TSF_stacks[TSF_the][TSF_countmod]=TSF_poke
        else:
            TSF_pokeerr=1
    else:
        TSF_pokeerr=2

def TSF_Forth_delthe(TSF_the):   #TSF_doc:スタックを削除(TSFAPI)。
    if TSF_the in TSF_stacks:
        del TSF_stacks[TSF_the]
    return None if TSF_stackthis != TSF_the else ""

def TSF_Forth_clonethe(TSF_clone,TSF_the):   #TSF_doc:スタックを複製する(TSFAPI)
    TSF_stacks[TSF_clone]=list(tuple(TSF_stacks[TSF_the] if TSF_the in TSF_stacks else []))

def TSF_Forth_clonethey(TSF_clone):   #TSF_doc:(TSFAPI)
    TSF_stacks[TSF_clone]=list(tuple(TSF_stacks.keys()))


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
    TSF_debug_savefilename="debug/debug_Forth.txt"
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
