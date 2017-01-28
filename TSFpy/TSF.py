#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Forth import *


TSF_mergefile=""
TSF_Forth_Init(sys.argv)
if len(sys.argv) >= 2:
    TSF_mergefile=sys.argv[1]
if os.path.isfile(TSF_mergefile):
    if len(TSF_Forth_loadtext(TSF_mergefile,TSF_mergefile)):
        TSF_Forth_merge(TSF_mergefile,[])
        for TSF_argvcount in range(len(sys.argv)):
            TSF_push(TSF_Forth_1ststack(),sys.argv[-TSF_argvcount-1])
        TSF_push(TSF_Forth_1ststack(),str(len(sys.argv)))
    TSF_debug_log=TSF_Forth_stackview()
    TSF_Forth_run(TSF_Forth_1ststack())
else:
    TSF_Forth_settext(TSF_Forth_1ststack(),"\t".join(["UTF-8",":TSF_encoding","main:",":TSF_this","0",":TSF_fin."]))
    TSF_Forth_settext("main:","\t".join(["about:",":TSF_pushthat","about:",":TSF_lenthat",":TSF_echoes"]))
    TSF_Forth_settext("about:",
        "「TSF_Tab-Separated-Forth:」の概要(暫定案)。\n"
        "積んだスタックをワード(関数)などで消化していくForth風インタプリタ。スタック単位はtsv文字列。\n"
        "文字から始まる行はスタック名、タブで始まる行はスタック内容。改行のみもしくは「#」で始まる行は読み飛ばし。\n"
        "タブのみ行は1スタック計算。他にも二重タブや末尾タブが文字列長0のスタックとみなされるので注意。\n"
        "TSFでは先頭からワードを実行するthisスタックと末尾に引数などを積み上げるthatスタックを別々に指定できる。\n"
        "thatスタックのアンダーフローは0文字列を返却する。\n"
        "起動時のthatスタック(thisスタックも)は「TSF_Tab-Separated-Forth:」なのでargvもそこに追加される。\n"
        "thisスタックのオーバーフローはコールスタックを消費して呼び出し元に戻って続きから再開。\n"
        "末尾再帰はループ。深い階層で祖先を「:TSF_this」すると子孫コールスタックはまとめて破棄される。\n"
        "「:TSF_calc」という括弧が使える電卓を用意する予定なので逆ポーランド記法の数式計算は強いられないはず。\n"
        ,TSF_style="N")
    TSF_debug_mergefile="debug/TSF.tsf"
    TSF_debug_log=TSF_Forth_stackview()
    TSF_io_savetext(TSF_debug_mergefile,TSF_debug_log)
    for TSF_argvcount in range(len(sys.argv)):
        TSF_push(TSF_Forth_1ststack(),sys.argv[-TSF_argvcount-1])
    TSF_Forth_run(TSF_Forth_1ststack())
sys.exit()
