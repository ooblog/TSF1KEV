#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_io import *
from TSF_txt import *
#from TSF_calc import *


def TSF_Forth_1ststack():    #TSF_doc:TSF_初期化に使う1ststack名
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSF_doc:TSF_初期化に使うバージョン(ブランチ)名
    return "20170108U045559"

TSF_words={}
def TSF_Forth_Initwords():    #TSF_doc:TSF_words(ワード)を初期化する
    global TSF_words
    TSF_words={}
    TSF_wordsdef=[
        ":TSF_encoding",              # [encode]TSFの文字コード宣言。極力冒頭に置くのが望ましい。1スタック積み下ろし。
        ":TSF_alias",                  # [after,before]TSFワード(関数)を置き換える。2スタック積み下ろし。
        ":TSF_this",                   # [stack]thisスタックを変更(スタックをワード(関数)として呼ぶ)。通常はオーバーフローで呼び出し元に戻るが、再帰呼び出し等はループ扱いになる。ワード自体は1スタック積み下ろしだがスタック変化は未知数。
        ":TSF_that",                  # [stack]thatスタック(積み込み先スタック)を変更。1スタック積み下ろし。
        ":TSF_ifthis",                 # [stack,value]valueが0以外ならthisスタックを変更(スタックをワード(関数)として呼ぶ)。通常はオーバーフローで呼び出し元に戻るが、再帰呼び出し等はループ扱いになる。ワード自体は2スタック積み下ろしだがスタック変化は未知数。
        ":TSF_ifthat",                 # [stack,value]valueが0以外ならthatスタック(積み込み先スタック)を変更。2スタック積み下ろし。
        ":TSF_casethis",              # […stackB,valueB,stackA,valueA,count]valueが0以外ならthisスタックを変更(スタックをワード(関数)として呼ぶ)。通常はオーバーフローで呼び出し元に戻るが、再帰呼び出し等はループ扱いになる。ワード自体はcount*2+1分スタック積み下ろしだがスタック変化は未知数。
        ":TSF_casethat",              # […stackB,valueB,stackA,valueA,count]valueが0以外ならthatスタック(積み込み先スタック)を変更。count*2+1分スタック積み下ろし。
        ":TSF_NOT",                  # [value]thisスタック直近が0以外なら0に、0だったら1に上書き。文字列は数値変換できない場合は0。1スタック積み下ろして1スタック積み上げ。
        ":TSF_NOTs",                 # […valueB,valueA,count]「:TSF_NOT」の複数形。countの回数分、thisスタック直近が0以外なら0に、0だったら1に上書き。文字列は数値変換できない場合は0。count+1分スタック積み下ろしてcount分スタック積み上げ。
        ":TSF_AND",                  # [stackB,stackA]stackAが0以外ならAを、stackAが0ならBをスタックに残す。2スタック積み下ろして1スタック積み上げ。
        ":TSF_ANDs",                  # […valueB,valueA,count]「:TSF_AND」の複数形。countの回数範囲内で全部のスタックが0以外の時直近のスタックを残す。全滅の時は0をスタックに残す。count+1分スタック積み下ろして1スタック積み上げ。
        ":TSF_OR",                  # [stackB,stackA]stackAが0ならAを、stackAが0以外ならBをスタックに残す。2スタック積み下ろして1スタック積み上げ。
        ":TSF_ORs",                  # […valueB,valueA,count]「:TSF_AND」の複数形。countの回数範囲内で先に見つけた0以外スタックを残す。全滅の時は0をスタックに残す。count+1分スタック積み下ろして1スタック積み上げ。
        ":TSF_lenthis",               # [stack]thisスタック(実行中スタック)の数を数える。1スタック積み上げ。
        ":TSF_lenthat",               # [stack]thatスタック(積み込み先スタック)の数を数える。1スタック積み上げ。
        ":TSF_pushthis",             # [stack]指定したスタックを丸ごとthisスタック(実行中スタック)に積み上げ。
        ":TSF_pushthat",             # [stack]指定したスタックを丸ごとthatスタック(積み込み先スタック)に積み上げ。
        ":TSF_slicethis",             # [first,lest,stack]指定したスタックの一部をthisスタック(実行中スタック)に積み上げ。
        ":TSF_slicethat",             # [first,lest,stack]指定したスタックの一部をthatスタック(積み込み先スタック)に積み上げ。
        ":TSF_calc",                  # [calc]スタックの内容で電卓する。1スタック積み下ろして1スタック積み上げ。
        ":TSF_style",                 # ['&tab;',styleNTO,stack]テキスト出力する時の表示方法を指定する。
        ":TSF_echo",                  # [value]直近1つのスタック内容を端末で表示する。1スタック消費。
        ":TSF_echoes",               # […valueB,valueA,count]指定した個数スタック内容を端末で表示する。count分スタック消費。
        ":TSF_view",                  # []スタック全体像を表示。
        ":TSF_fin.",                    # [errorcode]TSFを終了する。終了時に返却する数値が指定できる。1スタック消費。
        ":TSF_swap"  ,               # [stackB,stackA]積み込み先スタックの直近2つの順番を入れ替える。
        ":TSF_reverse",               # […stackB,stackA,count]積み込み先スタックの順番を指定した個数順番を入れ替える。
        ":TSF_postpone",            # […stackB,stackA,count]積み込み先スタックの直近1つを指定した個数奥に突っ込む。
        ":TSF_‎Interrupt",             # […stackB,stackA,count]積み込み先スタックの指定した個数奥から1つを引っ張り出し一番手前に積む。
        ":TSF_retart",                # [stack]指定したスタックをTSFプログラムとみなして最初から実行。
        ":TSF_merge",                # [stack]指定したスタックをTSFプログラムとみなして取り込む。
    ]
    for TSF_word in TSF_wordsdef:
        TSF_words[TSF_word]=TSF_word
    return TSF_words

def TSF_Forth_words():    #TSF_doc:TSF_words(ワード)を取得する
    global TSF_words
    return TSF_words

TSF_stacks=OrderedDict()
def TSF_Forth_Initstacks(TSF_argv):    #TSF_doc:TSF_stacks(スタック)を初期化する
    global TSF_stacks
    TSF_stacks=OrderedDict()
    TSF_stacks[TSF_Forth_1ststack()]=["UTF-8",":TSF_encoding","0",":TSF_fin."]+TSF_argv
    return TSF_stacks

def TSF_Forth_stacks():    #TSF_doc:TSF_stacks(スタック)を取得する
    global TSF_stacks
    return TSF_stacks

TSF_callptrs=OrderedDict()
def TSF_Forth_Initcallptrs():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を初期化する
    global TSF_callptrs
    TSF_callptrs=OrderedDict(); TSF_callptrs[TSF_Forth_1ststack()]=0
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

def TSF_Forth_Init(TSF_argv):    #TSF_doc:TSF_words,TSF_stacks,TSF_callptrsの3つをまとめて初期化する
    TSF_Forth_Initstacks(TSF_argv); TSF_Forth_Initwords(); TSF_Forth_Initcallptrs(); TSF_Forth_Initstyles()
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
    del TSF_stacks[TSF_stack]

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
