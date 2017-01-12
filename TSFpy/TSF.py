#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Forth import *

def TSF_debug():    #TSF_doc:「TSF/TSF.py」単体テスト風デバッグ関数。
    TSF_mergefile="debug/TSF_Forth_debug.txt"
    if len(TSF_Forth_loadtext(TSF_mergefile,TSF_mergefile)):
        TSF_Forth_merge(TSF_mergefile)
    TSF_Forth_stackview()

TSF_Forth_Init()
#TSF_debug()
#sys.exit()

if len(sys.argv) < 2 or sys.argv[1] in "--":
    TSF_Forth_settext(TSF_Forth_1ststack(),"\t".join(["UTF-8",":TSF_encoding","tab(foobarhogehogeblabla)",":TSF_Tab","main:",":TSF_this","0",":TSF_fin."]))
    TSF_Forth_settext("main:","\t".join(["about:",":TSF_pushthat","about:",":TSF_lenthat",":TSF_echoes"]))
    TSF_Forth_settext("about:",
        "「TSF_Tab-Separated-Forth:」の概要(暫定案)。\n"
        "積んだスタックをワード(関数)などで消化していくForth風構文。スタックはtsVテキスト。\n"
        "TSFテキスト上の文字から始まる行はスタック名、タブで始まる行はスタック列内容。名と列のワンライナー記述可能。\n"
        "改行のみ行はスルーだが、二重タブや末尾タブは0文字列とみなされスタック数増加に繋がるので注意。\n"
        "TSFでは先頭から関数などを実行するthisスタックと末尾に引数などを積み上げるthatスタックを別々に指定できる。\n"
        "thisスタックのオーバーフローはコールスタックを消費して呼び出し元に戻って続きから再開。\n"
        "thatスタックのアンダーフローは0文字列を返却する。\n"
        "末尾再帰はループ。深い階層で祖先を「:TSF_this」すると子孫コールスタックはまとめて破棄される。\n"
        "「:TSF_calc」という括弧が使える電卓を用意する予定なので逆ポーランド記法は強いられないはず。\n"
        ,TSF_style="N")
    TSF_Forth_stackview()
else:
    TSF_mergefile=sys.argv[1]
    if len(TSF_Forth_loadtext(TSF_mergefile,TSF_mergefile)):
        TSF_Forth_merge(TSF_mergefile)
    TSF_Forth_stackview()

#TSF_debug()
sys.exit()
