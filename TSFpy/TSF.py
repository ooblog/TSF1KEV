#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Forth import *


def TSF_command_about(save_about_mergefile):    #TSF_doc:TSFの概要とサンプルプログラム。
    TSF_Forth_settext(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","main:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_settext("main:","\t".join(["about:","#TSF_pushthe","about:","#TSF_lenthe","#TSF_echoes", \
        "calcQQtest:","#TSF_this","calcFXtest:","#TSF_this","calcDCtest:","#TSF_this","calc日本語風:","#TSF_this"]))
    TSF_Forth_settext("about:",
        "「TSF_Tab-Separated-Forth」の概要(暫定案)。\n"
        "積んだスタックをワード(関数)などで消化していくForth風インタプリタ。スタック単位はtsv文字列。\n"
        "文字から始まる行はスタック名、タブで始まる行はスタック内容。改行のみもしくは「#」で始まる行は読み飛ばし。\n"
        "タブのみ行は1スタック計算。他にも二重タブや末尾タブが文字列長0のスタックとみなされるので注意。\n"
        "起動時のスタック(thisスタックthatスタック両方とも)は「TSF_Tab-Separated-Forth:」なのでargvもそこに追加される。\n"
        "TSFでは先頭からワードを実行するthisスタックと末尾に引数などを積み上げるthatスタックを別々に指定できる。\n"
        "そもそもスタックが複数ある。他言語で言う変数の代わりにスタックがある。他言語で言う関数の引数や返り値もスタック経由。\n"
        "存在しないthatスタックからの取得(存在するスタックのアンダーフロー含む)は0文字列を返却する。\n"
        "存在しないthisスタックの呼び出し(存在するスタックのオーバーフロー含む)は呼び出し元に戻って続きから再開。\n"
        "末尾再帰はループ。深い階層で祖先を「#TSF_this」すると子孫コールスタックはまとめて破棄される(未テスト)。\n"
        "「#TSF_calc[]」などの括弧と「#TSF_calcFX」などの分数電卓を用意したので逆ポーランド記法の数式計算は強いられないはず。\n"
        ,TSF_style="N")
    TSF_Forth_settext("calcQQtest:","\t".join(["QQ(1/3+1|2)→","1/3+1|2","#TSF_calcQQ","2","#TSF_join","#TSF_echo"]))
    TSF_Forth_settext("calcFXtest:","\t".join(["FX(1/3+1|2)→","1","3","1|2","[2]/[1]+[0]","#TSF_calc[]","#TSF_calcFX","2","#TSF_join","#TSF_echo"]))
    TSF_Forth_settext("calcDCtest:","\t".join(["DC(1/3+1|2)→","1","/","3","+","1|2","5","#TSF_join","#TSF_calcDC","2","#TSF_join","#TSF_echo"]))
    TSF_Forth_settext("calc日本語風:","\t".join(["日本語風(一割る三足す二分の一)→","一割る三足す二分の一","#TSF_calcFX","2","#TSF_join","#TSF_echo"]))
    print("-- TSF_Forth_stackview() --")
    TSF_debug_log=TSF_Forth_stackview()
    if save_about_mergefile:
        TSF_io_savetext(TSF_about_mergefile,TSF_debug_log)
    print("-- TSF_Forth_run() --")
    TSF_Forth_pushargv()
    TSF_Forth_run(TSF_Forth_1ststack())
    print("-- TSF_Forth_stackview() --")
    TSF_debug_log=TSF_Forth_stackview()

def TSF_command_helloworld():    #TSF_doc:TSFのより小さなサンプルプログラム。
    TSF_Forth_settext(TSF_Forth_1ststack(),"\t".join(["Hello world","#TSF_echo"]))
    TSF_Forth_stackview()

def TSF_command_help():    #TSF_doc:TSFのより小さなサンプルプログラム。
    TSF_Forth_settext(TSF_Forth_1ststack(),"\t".join(["about:","#TSF_pushthe","about:","#TSF_lenthe","#TSF_echoes","0","#TSF_fin."]))
    TSF_Forth_settext("about:",
        'usage: ./TSF.py [command|file.tsf] [argv] ...\n'
        'command:\n'
        '  --help        this commands view\n'
        '  --helloworld  "Hello world  #TSF_echo" view\n'
        '  --about       samplecode(UTF-8) view and saveto "' +TSF_about_mergefile+ '" \n'
        '  not exist     samplecode(UTF-8) view only (no save)\n'
        ,TSF_style="N")
    TSF_Forth_run(TSF_Forth_1ststack())


TSF_about_mergefile="TSF_about.tsf"
TSF_mergefile=""
TSF_Forth_Init(sys.argv)
if len(sys.argv) >= 2:
    TSF_mergefile=sys.argv[1]
if os.path.isfile(TSF_mergefile):
    if len(TSF_Forth_loadtext(TSF_mergefile,TSF_mergefile)):
        TSF_Forth_merge(TSF_mergefile,[])
        TSF_Forth_pushargv()
    TSF_Forth_run(TSF_Forth_1ststack())
elif TSF_mergefile == "--helloworld":
    TSF_command_helloworld()
elif TSF_mergefile == "--help":
    TSF_command_help()
elif TSF_mergefile == "--about":
    TSF_command_about(True)
else:
    TSF_command_about(False)
sys.exit()
