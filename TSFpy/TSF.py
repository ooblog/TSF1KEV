#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Forth import *

def TSF_debug():    #TSF_doc:「TSF/TSF.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_stacks=TSF_Forth_stacks()
    TSF_stackK,TSF_stackV=TSF_Forth_1ststack(),TSF_stacks[TSF_Forth_1ststack()]
    TSF_debug_log=TSF_io_printlog(TSF_stackK,TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_stackV)),TSF_log=TSF_debug_log)
    for TSF_stackK,TSF_stackV in TSF_stacks.items():
        if TSF_stackK == TSF_Forth_1ststack(): continue;
        TSF_debug_log=TSF_io_printlog(TSF_stackK,TSF_log=TSF_debug_log)
        TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_stackV)),TSF_log=TSF_debug_log)
    TSF_Forth_stackview()

TSF_Forth_Init()
if len(sys.argv) < 2 or sys.argv[1] in "--":
    TSF_Forth_settext(TSF_Forth_1ststack(),"UTF-8\t:TSF_encoding\t0\nmain:\t:TSF_call\t:TSF_fin.")
    TSF_Forth_settext("main:","about:\t:TSF_push\tabout:\t:TSF_diclen\t:TSF_reverseS\tabout:\t:TSF_diclen\t:TSF_echoeS")
    TSF_Forth_settext("about:",
        "「TSF_Tab-Separated-Forth:」の概要(暫定案)。\n"
        "スタックはtsv単位。積んだスタックをワード(関数)で消化していくForth風構文。\n"
        "文字で始まる行はスタック名、タブで始まる行はスタック列内容。名と列のワンライナー記述可能。\n"
        "改行のみ行はスルーだが、二重タブや末尾タブは0文字列とみなされスタック数増加に繋がるので注意。\n"
        "末尾再帰はループ。深い階層で祖先を「:TSF_call」すると子孫コールスタックはまとめて破棄される。\n"
        "「:TSF_calc」という括弧が使える電卓を用意する予定なので逆ポーランド記法は強いられないはず。\n"
        )
    TSF_Forth_stackview(["about:"])
else:
    TSF_Forth_loadtext(sys.argv[1],sys.argv[1])
    TSF_Forth_stackview()

#TSF_debug()
sys.exit()
