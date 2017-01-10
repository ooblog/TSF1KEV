#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_io import *
from TSF_txt import *

def TSF_Forth_1ststack():    #TSF_doc:TSF_初期化に使う1ststack名
    return "TSF_Tab-Separated-Forth"

def TSF_Forth_version():    #TSF_doc:TSF_初期化に使うバージョン(ブランチ)名
    return "20170108U045559"

TSF_words={}
def TSF_Forth_Initwords():    #TSF_doc:TSF_words(ワード)を初期化する
    global TSF_words
    TSF_words={}
    TSF_wordsdef=[
        ":TSF_encoding",              # [encode]TSFの文字コード宣言。極力冒頭に置くのが望ましい。1スタック消費。
        ":TSF_word",                  # [after,before]TSFワードを置き換える。2スタック消費。
        ":TSF_fin.",                    # [errorcode]TSFを終了する。とりあえず0を返しておく。1スタック消費。
    ]
    for TSF_word in TSF_wordsdef:
        TSF_words[TSF_word]=TSF_word
    return TSF_words

def TSF_Forth_words():    #TSF_doc:TSF_words(ワード)を取得する
    return TSF_words

TSF_stacks={}
def TSF_Forth_Initstacks():    #TSF_doc:TSF_stacks(スタック)を初期化する
    global TSF_stacks
    TSF_stacks={}
    TSF_stacks[TSF_Forth_1ststack()]=["UTF-8",":TSF_encoding","0",":TSF_fin."]
    return TSF_stacks

def TSF_Forth_stacks():    #TSF_doc:TSF_stacks(スタック)を取得する
    return TSF_stacks

TSF_callwords,TSF_callcounts=[],[]
def TSF_Forth_Initcallptrs():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を初期化する
    global TSF_callwords,TSF_callcounts
    TSF_callwords,TSF_callcounts=[TSF_Forth_1ststack()],[0]
    return TSF_callwords,TSF_callcounts

def TSF_Forth_stacks():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を取得する
    return TSF_callwords,TSF_callcounts

def TSF_Forth_Init():    #TSF_doc:TSF_words,TSF_stacks,TSF_callptrsの3つをまとめて初期化する
    TSF_Forth_Initstacks(); TSF_Forth_Initwords(); TSF_Forth_Initcallptrs()
    return TSF_words,TSF_stacks,TSF_callwords,TSF_callcounts

def TSF_Forth_settext(TSF_stack,TSF_text):    #TSF_doc:テキストを読み込んでTSF_stacksの一スタック扱いにする。
    global TSF_stacks
    TSF_splits=TSF_text.rstrip('\n').split('\n')
    TSF_stacks[TSF_stack]=[""]*len(TSF_splits)
    for TSF_stackno in range(len(TSF_splits)):
        TSF_split=TSF_readlinenum(TSF_text,TSF_stackno)
        TSF_stacks[TSF_stack][TSF_stackno]="test"
        if sys.version_info.major == 2:
            TSF_stacks[TSF_stack][TSF_stackno]=base64.b64encode("test")
    return TSF_stacks[TSF_stack]

def TSF_Forth_loadtext(TSF_stack,TSF_path):    #TSF_doc:テキストファイルを読み込んでTSF_stacksの一スタック扱いにする。
    TSF_text=TSF_io_loadtext(TSF_path)
    TSF_Forth_settext(TSF_stack,TSF_text)
    return TSF_text


def TSF_Forth_debug(TSF_argv=[]):    #TSF_doc:「TSF/TSF_Forth.py」単体テスト風デバッグ関数。
    TSF_Forth_Init()
    TSF_debug_log=""
    TSF_debug_readme="debug/README.md"
    TSF_debug_log=TSF_io_printlog(TSF_Forth_1ststack(),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_stacks[TSF_Forth_1ststack()])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_argv:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argv)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_Forth_loadtext({0},{1})".format(TSF_debug_readme,TSF_debug_readme),TSF_log=TSF_debug_log)
    TSF_debug_readmeT=TSF_Forth_loadtext(TSF_debug_readme,TSF_debug_readme)
    TSF_debug_log=TSF_io_printlog("{0}:".format(TSF_debug_readme),TSF_log=TSF_debug_log)
    for TSF_stack in TSF_stacks[TSF_debug_readme]:
        if sys.version_info.major == 2:
            TSF_stack=base64.b64decode(TSF_stack)
        TSF_debug_log=TSF_io_printlog("\t{0}".format(TSF_stack),TSF_log=TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    print("")
    print("--- {0} ---".format(sys.argv[0]))
    TSF_debug_savefilename="debug/TSF_Forth_debug.txt"
    TSF_debug_log=TSF_Forth_debug(sys.argv)
    TSF_io_savetext(TSF_debug_savefilename,TSF_debug_log)
    TSF_debug_log=TSF_io_loadtext(TSF_debug_savefilename)
    print("")
    print("--- {0} ---".format(TSF_debug_savefilename))
    print(TSF_debug_log)
    sys.exit()
