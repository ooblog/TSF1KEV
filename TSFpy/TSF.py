#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_io import *
from TSF_calc import *
from TSF_time import *
from TSF_Forth import *


def TSF_command_about(save_about_mergefile):    #TSF_doc:TSFの概要とサンプルプログラム。
    TSF_Forth_settext(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","main1:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_settext("main1:","\t".join(["aboutTSF:","#TSF_pushthe","aboutTSF:","#TSF_lenthe","#TSF_echoes","main2:","#TSF_this"]))
    TSF_Forth_settext("main2:","\t".join(["#分数電卓のテスト","#TSF_echo","16","#TSF_calcPR","calcQQtest:","#TSF_this","calcFXtest:","#TSF_this","calcDCtest:","#TSF_this","calcKNテスト:","#TSF_this","#","#TSF_echo","main3:","#TSF_this"]))
    TSF_Forth_settext("main3:","\t".join(["aboutCalc:","#TSF_pushthe","aboutCalc:","#TSF_lenthe","#TSF_echoes"]))
    TSF_Forth_settext("aboutTSF:",
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
    TSF_Forth_settext("calcQQtest:","\t".join(["「1/3-m1|2」→","1/3-m1|2","#TSF_calcQQ","2","#TSF_join","#TSF_echo"]))
    TSF_Forth_settext("calcFXtest:","\t".join(["「1 3 m1|2」を数式風に「[2]/[1]-[0]」で連結→","1","3","1|2","[2]/[1]-[0]","#TSF_calc[]","#TSF_calcFX","2","#TSF_join","#TSF_echo"]))
    TSF_Forth_settext("calcDCtest:","\t".join(["「1 / 3 - m1|2」まで分解して連結(ついでに小数デモ)→","1","/","3","-","m1|2","5","#TSF_join","#TSF_calcDC","2","#TSF_join","#TSF_echo"]))
    TSF_Forth_settext("calcKNテスト:","\t".join(["「一割る三引くマイナス二分の一(ついでに単位付き計算デモ)」は","一割る三引くマイナス二分の一","を単位付き計算する","2","個分連結","を表示する"]))
    TSF_Forth_settext("aboutCalc:",
        "「calc」系ワード分数電卓の概要(暫定案)。\n"
        "「#TSF_calcQQ」「#TSF_calcFX」「#TSF_calcDC」と３つも電卓用ワード(関数)があるが、基本的には同じ分数計算。\n"
        "「#TSF_calcDC」は小数表示用途。「#TSF_calcQQ」は数式を九九のように暗記(参照透過風)。\n"
        "「#TSF_calcPR」は有効桁数の調整。初期値は72桁(千無量大数)。「π」(円周率)「ｅ」(ネイピア数)の都合で4桁から100桁の範囲。\n"
        "「#TSF_calcRO」は端数処理の調整。初期値は「ROUND_DOWN」(0方向に丸める)。\n"
        "有効桁数「#TSF_calcPR」や端数処理「#TSF_calcRO」など数式の計算結果に影響があると思われる場合は「#TSF_calcQQ」の九九を忘却。\n"
        "「#TSF_calc{}」「#TSF_calc[]」「#TSF_calc｢｣」ワードもあるが、計算ではなく「#TSF_join」など文字列連結操作扱い。\n"
        "「/」割り算と「|」分数は分けて表記。数値の「p」プラス「m」マイナスは演算子の「+」プラス「-」マイナスと分けて表記。\n"
        "通常の割り算の他に1未満を切り捨てる「\\」、余りを求める「#」、消費税計算用「%」演算子がある。掛け算は「*」演算子。\n"
        "アラビア数字の他に漢数字〇一二三四五六七八九十百千万億兆京なども使用可能。「#TSF_calcKN」で計算結果も一部漢数字使用可。\n"
        "自然対数(logｅ)は「E」。常用対数(log10)は「L」。無理数は分数に丸められるので「E256/E2」や「L256/L2」が8にならない。\n"
        "「81&3l」や「256の二進対数」という任意底対数の演算子で整数同士専用のアルゴリズムを経由できた場合は「256&2l」が8になる。\n"
        "「kM1~10」で1から10まで合計するような和数列(総和)が使える。同様に「kP1~10」で積数列(総乗)を用いて乗数や階乗の計算も可能。\n"
        "(最大)公約数は「12&16G」。(最小)公倍数は「12&16g」。「&」のみを単独で使った場合は掛け算の同じ優先順位で加算する。\n"
        "0で割るもしくは有効桁数溢れなど、何らかの事情で計算できない場合は便宜上「n|0」という事にする。「p」「m」は付かない。\n"
        ,TSF_style="N")
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
sys.exit(0 if TSF_exitcode == "0" or TSF_exitcode == "0|1" else TSF_exitcode)


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
