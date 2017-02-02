#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_io import *
from TSF_time import *
from TSF_calc import *


def TSF_Forth_1ststack():    #TSF_doc:TSF_初期化に使う1ststack名
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSF_doc:TSF_初期化に使うバージョン(ブランチ)名
    return "20170108U045559"

TSF_words={}
def TSF_Forth_Initwords():    #TSF_doc:TSF_words(ワード)を初期化する
    global TSF_words
    TSF_words={}
    TSF_words={
        "#TSF_fin.":TSF_Forth_fin,
        "#TSF_encoding":TSF_Forth_encoding,
        "#TSF_this":TSF_Forth_this, "#TSF_that":TSF_Forth_that,
        "#TSF_echo":TSF_Forth_echo, "#TSF_echoes":TSF_Forth_echoes,
        "#TSF_lenthe":TSF_Forth_lenthe, "#TSF_lenthis":TSF_Forth_lenthis, "#TSF_lenthat":TSF_Forth_lenthat,
        "#TSF_pushthe":TSF_Forth_pushthe, "#TSF_pushthis":TSF_Forth_pushthis, "#TSF_pushthat":TSF_Forth_pushthat,
        "#TSF_calcQQ":TSF_Forth_calcQQ,"#TSF_calcFX":TSF_Forth_calcFX,
    }
    return TSF_words

def TSF_Forth_words():    #TSF_doc:TSF_words(ワード)を取得する
    global TSF_words
    return TSF_words

def TSF_Forth_pushargv():    #TSF_doc:sys.argv(コマンドライン引数)を「TSF_Tab-Separated-Forth:」に追加。
    for TSF_argvcount in range(len(sys.argv)):
        TSF_Forth_push(TSF_Forth_1ststack(),sys.argv[-TSF_argvcount-1])
    TSF_Forth_push(TSF_Forth_1ststack(),str(len(sys.argv)))

TSF_stacks=OrderedDict()
def TSF_Forth_Initstacks(TSF_argv):    #TSF_doc:TSF_stacks(スタック)を初期化する
    global TSF_stacks
    TSF_stacks=OrderedDict()
    TSF_stacks[TSF_Forth_1ststack()]=["UTF-8",":TSF_encoding","0",":TSF_fin."]+TSF_argv+[str(len(TSF_argv))]
    TSF_Forth_pushargv()
    return TSF_stacks

def TSF_Forth_stacks():    #TSF_doc:TSF_stacks(スタック)を取得する
    global TSF_stacks
    return TSF_stacks

TSF_callptrs=OrderedDict()
def TSF_Forth_Initcallptrs():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を初期化する
    global TSF_callptrs
    TSF_callptrs=OrderedDict();
    return TSF_callptrs

def TSF_Forth_callptrs():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を取得する
    global TSF_callptrs
    return TSF_callptrs

TSF_styles=OrderedDict()
def TSF_Forth_Initstyles():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を初期化する
    global TSF_styles
    TSF_styles=OrderedDict()
    TSF_styles[TSF_Forth_1ststack()]="T"
    return TSF_styles

def TSF_Forth_styles():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を取得する
    global TSF_styles
    return TSF_styles

TSF_thisstack_name,TSF_thisstack_count=TSF_Forth_1ststack(),0
def TSF_Forth_thisstack():    #TSF_doc:スタック実行元、TSF_thisstack_name,TSF_thisstack_countを取得する
    return TSF_thisstack_name,TSF_thisstack_count

TSF_thatstack_name=TSF_thisstack_name
def TSF_Forth_thatstack():    #TSF_doc:スタック積み上げ先、TSF_thatstack_nameを取得する
    return TSF_thatstack_name

def TSF_Forth_Init(TSF_argv):    #TSF_doc:TSF_words,TSF_stacks,TSF_callptrsの3つをまとめて初期化する。thisthatも初期化。
    TSF_Forth_Initstacks(TSF_argv); TSF_Forth_Initwords(); TSF_Forth_Initcallptrs(); TSF_Forth_Initstyles()
    TSF_thisstack_name,TSF_thisstack_count=TSF_Forth_1ststack(),0
    TSF_thatstack_name=TSF_thisstack_name
    return TSF_words,TSF_stacks,TSF_callptrs

def TSF_Forth_settext(TSF_stack,TSF_text,TSF_style="T"):    #TSF_doc:テキストを読み込んでTSF_stacksの一スタック扱いにする。
    global TSF_stacks
    TSF_stacks[TSF_stack]=TSF_text.rstrip('\n').replace('\t','\n').split('\n')
    TSF_styles[TSF_stack]=TSF_style

def TSF_Forth_loadtext(TSF_stack,TSF_path):    #TSF_doc:テキストファイルを読み込んでTSF_stacksの一スタック扱いにする。
    TSF_text=TSF_io_loadtext(TSF_path)
    TSF_text=TSF_txt_ESCencode(TSF_text)
    TSF_Forth_settext(TSF_stack,TSF_text)
    TSF_styles[TSF_stack]="N"
    return TSF_text

def TSF_Forth_merge(TSF_stack,TSF_ESCstack=[]):    #TSF_doc:「TSF_Forth_settext()」で読み込んだテキストをスタックに変換する。
    TSF_stackthat=TSF_Forth_1ststack()
    TSF_styles[TSF_stackthat]="T"
    for TSF_stackV in TSF_stacks[TSF_stack]:
        if len(TSF_stackV) == 0: continue;
        if TSF_stackV.startswith("#"): continue;
        TSF_stackV=TSF_txt_ESCdecode(TSF_stackV)
        if not TSF_stackV.startswith('\t'):
            TSF_stackL=TSF_stackV.lstrip('\t').split('\t')
            if not TSF_stackL[0] in TSF_ESCstack:
                TSF_stackthat=TSF_stackL[0]
                TSF_stacks[TSF_stackthat]=[]
                TSF_styles[TSF_stackthat]="O" if len(TSF_stackL) >= 2 else ""
        if not TSF_stackthat in TSF_ESCstack:
            TSF_stackL=TSF_stackV.split('\t')[1:]
            TSF_stacks[TSF_stackthat].extend(TSF_stackL)
            if TSF_styles[TSF_stackthat] != "O":
                TSF_styles[TSF_stackthat]="T" if len(TSF_stackL) >= 2 else "N"
#    del TSF_stacks[TSF_stack]

def TSF_Forth_stackview():    #TSF_doc:TSF_stacksの内容をテキスト取得する。
    TSF_view_log=""
    TSF_stacks=TSF_Forth_stacks()
    TSF_stackK,TSF_stackV=TSF_Forth_1ststack(),TSF_stacks[TSF_Forth_1ststack()]
    for TSF_stackK,TSF_stackV in TSF_stacks.items():
        TSF_stackV=[TSF_txt_ESCdecode(TSF_stk) for TSF_stk in TSF_stackV]
        if TSF_styles[TSF_stackK] == "O":
            TSF_view_log=TSF_io_printlog("{0}\t{1}\n".format(TSF_stackK,"\t".join(TSF_stackV)),TSF_log=TSF_view_log)
        elif TSF_styles[TSF_stackK] == "T":
            TSF_view_log=TSF_io_printlog("{0}\n\t{1}\n".format(TSF_stackK,"\t".join(TSF_stackV)),TSF_log=TSF_view_log)
        else:  # TSF_styles[TSF_stackK] == "N":
            TSF_view_log=TSF_io_printlog("{0}\n\t{1}\n".format(TSF_stackK,"\n\t".join(TSF_stackV)),TSF_log=TSF_view_log)
    return TSF_view_log

def TSF_Forth_pop(TSF_that):    #TSF_doc:スタックを積み下ろす。
    TSF_popdata=""
    if TSF_that in TSF_stacks and len(TSF_stacks[TSF_that]):
        TSF_popdata=TSF_stacks[TSF_that].pop()
    return TSF_popdata

def TSF_Forth_push(TSF_that,TSF_pushdata):    #TSF_doc:スタックを積み上げる。
    if TSF_that in TSF_stacks:
        TSF_stacks[TSF_that].append(TSF_pushdata)
    else:
        TSF_stacks[TSF_that]=[TSF_pushdata]

def TSF_Forth_peek(TSF_that,TSF_count):    #TSF_doc:スタックから読み取る。
    TSF_peekdata=""
    if TSF_that in TSF_stacks:
        if 0 <= TSF_count < len(TSF_stacks[TSF_that]):
            TSF_peekdata=TSF_stacks[TSF_that][TSF_count]
        elif len(TSF_stacks[TSF_that]) <= -TSF_count < 0:
            TSF_peekdata=TSF_stacks[TSF_that][TSF_count]
    return TSF_peekdata

def TSF_Forth_poke(TSF_that,TSF_poke,TSF_count):    #TSF_doc:スタックに書き込む。正常なら0。TSF_countの値がはみ出した場合1。スタック自体が無かったら2。
    TSF_pokeerr=0
    if TSF_that in TSF_stacks:
        if 0 <= TSF_count < len(TSF_stacks[TSF_that]):
            TSF_stacks[TSF_that][TSF_count]=TSF_poke
        elif len(TSF_stacks[TSF_that]) <= -TSF_count < 0:
            TSF_stacks[TSF_that][TSF_count]=TSF_poke
        else:
            TSF_pokeerr=1
    else:
        TSF_pokeerr=2
    return TSF_pokeerr

TSF_exitcode="0"
def TSF_Forth_fin():    #TSF_doc:TSFファイルのエンコードを指定する。
    global TSF_exitcode
    TSF_exitcode=TSF_Forth_pop(TSF_thatstack_name)
    return ""

TSF_encode="UTF-8"
def TSF_Forth_encoding():    #TSF_doc:[encode]TSFの文字コード宣言。極力冒頭に置くのが望ましい。1スタック積み下ろし。
    global TSF_encode
    TSF_encode=TSF_Forth_pop(TSF_thatstack_name)
    return TSF_thisstack_name

def TSF_Forth_this():    #TSF_doc:[stack]thisスタックを変更(スタックをワード(関数)として呼ぶ)。通常はオーバーフローで呼び出し元に戻るが、再帰呼び出し等はループ扱いになる。ワード自体は1スタック積み下ろしだがスタック変化は未知数。
    TSF_callptrs[TSF_thisstack_name]=TSF_thisstack_count+1
    TSF_thisnext=TSF_Forth_pop(TSF_thatstack_name)
    return TSF_thisnext

def TSF_Forth_that():    #TSF_doc:[stack]thatスタック(積み込み先スタック)を変更。1スタック積み下ろし。
    global TSF_thatstack_name
    TSF_thatstack_name=TSF_Forth_pop(TSF_thatstack_name)
    return TSF_thisstack_name

def TSF_Forth_echo():    #TSF_doc:[value]直近1つのスタック内容を端末で表示する。1スタック消費。
    TSF_echotext=TSF_Forth_pop(TSF_thatstack_name)
    TSF_io_printlog(TSF_echotext)
    return TSF_thisstack_name

def TSF_Forth_echoes():    #TSF_doc:[…valueB,valueA,count]指定した個数スタック内容を端末で表示する。count分スタック消費。
    TSF_echoloopT=TSF_Forth_pop(TSF_thatstack_name); TSF_echoloopI=abs(TSF_io_intstr0x(TSF_echoloopT))
    for TSF_echocount in range(TSF_echoloopI):
        TSF_Forth_echo()
    return TSF_thisstack_name

def TSF_Forth_lenthe():   #TSF_doc:[stack]指定したスタックの数を数える。1スタック積み上げ。
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    TSF_Forth_push(TSF_thatstack_name,str(len(TSF_stacks[TSF_thename])))
    return TSF_thisstack_name

def TSF_Forth_lenthis():   #TSF_doc:thisスタック(実行中スタック)の数を数える。1スタック積み上げ。
    TSF_Forth_push(TSF_thatstack_name,str(len(TSF_stacks[TSF_thisstack_name])))
    return TSF_thisstack_name

def TSF_Forth_lenthat():   #TSF_doc:thatスタック(積み込み先スタック)の数を数える。1スタック積み上げ。
    TSF_Forth_push(TSF_thatstack_name,str(len(TSF_stacks[TSF_thatstack_name])))
    return TSF_thisstack_name

def TSF_Forth_pushthe():   #TSF_doc:[stack]指定したスタックを丸ごとthatスタック(積み込み先スタック)に積み上げ。
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    if TSF_thename in TSF_stacks:
        for TSF_tsv in reversed(TSF_stacks[TSF_thename]):
            TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return TSF_thisstack_name

def TSF_Forth_pushthis():   #TSF_doc:thisスタック(実行中スタック)を丸ごとthatスタック(積み込み先スタック)に積み上げ。
    if TSF_thisstack_name in TSF_stacks:
        for TSF_tsv in reversed(TSF_stacks[TSF_thisstack_name]):
            TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return TSF_thisstack_name

def TSF_Forth_pushthat():   #TSF_doc:thatスタック(積み込み先スタック)を丸ごとthatスタック(積み込み先スタック)に積み上げ。
    if TSF_thatstack_name in TSF_stacks:
        for TSF_tsv in reversed(TSF_stacks[TSF_thatstack_name]):
            TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return TSF_thisstack_name

TSF_calcs={}
def TSF_Forth_calcQQ():   #TSF_doc:[calc]スタック内容で分数電卓する。一度計算した値を暗記(九九)。1スタック積み下ろし1スタック積み上げ(スタック内容の変化)。
    global TSF_calcs
    TSF_tsvQ=TSF_Forth_pop(TSF_thatstack_name)
    if TSF_tsvQ in TSF_calcs:
        TSF_tsvA=TSF_calcs[TSF_tsvQ]
    else:
        TSF_tsvA=TSF_calc(TSF_tsvQ); TSF_calcs[TSF_tsvQ]=TSF_tsvA
    TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return TSF_thisstack_name

def TSF_Forth_calcFX():   #TSF_doc:[…stackB,stackA,calc,count]複数のスタック内容で毎回再計算(分数電卓)する。count+1(calc)分スタック積み下ろし。
    TSF_calcloopT=TSF_Forth_pop(TSF_thatstack_name); TSF_calcloopI=abs(TSF_io_intstr0x(TSF_calcloopT))
    TSF_tsvQ=TSF_Forth_pop(TSF_thatstack_name)
    TSF_stacksQ=[]
    for TSF_calccount in range(TSF_calcloopI):
        TSF_stacksQ.append(TSF_Forth_pop(TSF_thatstack_name))
    TSF_tsvQ=TSF_calc_stackmarge(TSF_tsvQ,*tuple(TSF_stacksQ))
    TSF_tsvA=TSF_calc(TSF_tsvQ)
    TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return TSF_thisstack_name


def TSF_Forth_run(TSF_this=None,TSF_that=None):    #TSF_doc:TSFを実行していく。
    global TSF_thisstack_name,TSF_thatstack_name,TSF_thisstack_count
    TSF_thisstack_name=TSF_this if TSF_this != None else TSF_Forth_1ststack()
    TSF_thatstack_name=TSF_that if TSF_that != None else TSF_Forth_1ststack()
    TSF_thisstack_count=0
    TSF_nextstack=TSF_thisstack_name
    while True:
        while TSF_thisstack_count < len(TSF_stacks[TSF_thisstack_name]) < 19:
            if TSF_stacks[TSF_thisstack_name][TSF_thisstack_count] in TSF_words:
                TSF_nextstack=TSF_words[TSF_stacks[TSF_thisstack_name][TSF_thisstack_count]]()
            else:
                TSF_Forth_push(TSF_thatstack_name,TSF_stacks[TSF_thisstack_name][TSF_thisstack_count])
            TSF_thisstack_count += 1
            if TSF_thisstack_name != TSF_nextstack:
                if TSF_nextstack in TSF_stacks:
                    TSF_thisstack_name = TSF_nextstack
                    TSF_thisstack_count = 0
                else:
                    break
        if len(TSF_callptrs) > 0:
            TSF_thisstack_name,TSF_thisstack_count=TSF_callptrs.popitem(True); TSF_nextstack=TSF_thisstack_name
        else:
            break

#    TSF_wordsdef=[
##        ":TSF_encoding":TSF_encoding,    # [encode]TSFの文字コード宣言。極力冒頭に置くのが望ましい。1スタック積み下ろし。
##        ":TSF_this",                   # [stack]thisスタックを変更(スタックをワード(関数)として呼ぶ)。通常はオーバーフローで呼び出し元に戻るが、再帰呼び出し等はループ扱いになる。ワード自体は1スタック積み下ろしだがスタック変化は未知数。
##        ":TSF_that",                  # [stack]thatスタック(積み込み先スタック)を変更。1スタック積み下ろし。
##        ":TSF_lenthis",               # [stack]thisスタック(実行中スタック)の数を数える。1スタック積み上げ。
##        ":TSF_lenthat",               # [stack]thatスタック(積み込み先スタック)の数を数える。1スタック積み上げ。
##        ":TSF_pushthis",             # [stack]指定したスタックを丸ごとthisスタック(実行中スタック)に積み上げ。
##       ":TSF_pushthat",             # [stack]指定したスタックを丸ごとthatスタック(積み込み先スタック)に積み上げ。
#        ":TSF_over.",                  # [errorcode]スタックを終了する。他言語のreturn返り値的なモノを用意する場合、単純ににスタックに積むだけ。
##        ":TSF_fin.",                    # [errorcode]TSFを終了する。終了時に返却する数値が指定できる。1スタック消費。
##       ":TSF_echo",                  # [value]直近1つのスタック内容を端末で表示する。1スタック消費。
##       ":TSF_echoes",               # […valueB,valueA,count]指定した個数スタック内容を端末で表示する。count分スタック消費。
#        ":TSF_alias",                  # [after,before]TSFワード(関数)を置き換える。2スタック積み下ろし。
#        ":TSF_ifthis",                 # [stack,value]valueが0以外ならthisスタックを変更(スタックをワード(関数)として呼ぶ)。通常はオーバーフローで呼び出し元に戻るが、再帰呼び出し等はループ扱いになる。ワード自体は2スタック積み下ろしだがスタック変化は未知数。
#        ":TSF_ifthat",                 # [stack,value]valueが0以外ならthatスタック(積み込み先スタック)を変更。2スタック積み下ろし。
#        ":TSF_casethis",              # […stackB,valueB,stackA,valueA,count]valueが0以外ならthisスタックを変更(スタックをワード(関数)として呼ぶ)。通常はオーバーフローで呼び出し元に戻るが、再帰呼び出し等はループ扱いになる。ワード自体はcount*2+1分スタック積み下ろしだがスタック変化は未知数。
#        ":TSF_casethat",              # […stackB,valueB,stackA,valueA,count]valueが0以外ならthatスタック(積み込み先スタック)を変更。count*2+1分スタック積み下ろし。
#        ":TSF_slicethis",             # [first,lest,stack]指定したスタックの一部をthisスタック(実行中スタック)に積み上げ。
#        ":TSF_slicethat",             # [first,lest,stack]指定したスタックの一部をthatスタック(積み込み先スタック)に積み上げ。
#        ":TSF_calc",                  # [calc]スタックの内容で電卓する。スタック積み下ろし量はcalcの内容に左右されるので注意。
#        ":TSF_style",                 # ['&tab;',styleNTO,stack]テキスト出力する時の表示方法を指定する。
#        ":TSF_view",                  # []スタック全体像を表示。
#        ":TSF_viewsave",              # [path]指定したスタックをテキストファイルに保存。1スタック消費。
#        ":TSF_save",                  # [stack,path]指定したスタックをテキストファイルに保存。2スタック消費。
#        ":TSF_load",                  # [stack,path]指定したスタックにテキストファイルを読み込む。TSF構文解析は「:TSF_merge」を使う。2スタック消費。
#        ":TSF_merge",                # [stack]指定したスタックをTSFプログラムとみなして取り込む。
#        ":TSF_swap"  ,               # [stackB,stackA]積み込み先スタックの直近2つの順番を入れ替える。
#        ":TSF_reverse",               # […stackB,stackA,count]積み込み先スタックの順番を指定した個数順番を入れ替える。
#        ":TSF_postpone",            # […stackB,stackA,count]積み込み先スタックの直近1つを指定した個数奥に突っ込む。
#        ":TSF_‎Interrupt",             # […stackB,stackA,count]積み込み先スタックの指定した個数奥から1つを引っ張り出し一番手前に積む。
#    ]


def TSF_Forth_debug(TSF_argv=[]):    #TSF_doc:「TSF/TSF_Forth.py」単体テスト風デバッグ関数。
    TSF_Forth_Init(sys.argv)
    TSF_debug_log=""
    TSF_debug_readme="debug/README.md"
    TSF_Forth_loadtext(TSF_debug_readme,TSF_debug_readme)
    TSF_debug_log+=TSF_Forth_stackview()
    return TSF_debug_log

if __name__=="__main__":
    print("")
    print("--- {0} ---".format(sys.argv[0]))
    TSF_debug_savefilename="debug/TSF_Forth_debug.txt"
    TSF_debug_log=TSF_Forth_debug(sys.argv)
    TSF_io_savetext(TSF_debug_savefilename,TSF_debug_log)
    print("")
    try:
        print("--- {0} ---\n{1}".format(TSF_debug_savefilename,TSF_debug_log))
    except:
        print("can't 'print(TSF_debug_savefilename,TSF_debug_log)'")
    finally:
        pass
    sys.exit()
