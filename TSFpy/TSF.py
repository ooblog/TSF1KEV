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
    TSF_Forth_settext("main2:","\t".join(["#分数電卓のテスト","1","#TSF_echoes","16","#TSF_calcPR","calcFXtest:","#TSF_this","calcDCtest:","#TSF_this","calcKNテスト:","#TSF_this","#","1","#TSF_echoes","main3:","#TSF_this"]))
    TSF_Forth_settext("main3:","\t".join(["aboutCalc:","#TSF_pushthe","aboutCalc:","#TSF_lenthe","#TSF_echoes","main4:","#TSF_this"]))
    TSF_Forth_settext("main4:","\t".join(["aboutRPN+LISP:","#TSF_pushthe","aboutRPN+LISP:","#TSF_lenthe","#TSF_echoes"]))
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
        "ループは再帰で組む。深い階層で祖先を「#TSF_this」すると子孫コールスタックはまとめて破棄される。\n"
        "分岐は配列で組む。電卓の比較演算子の結果と「#TSF_peekthe」を組み合わせて飛び先スタック名を変更。「fizzbuzz.tsf」も参考。\n"
        "文字列連結は「#TSF_brackets」「#TSF_join」「#TSF_joinC」。文字列分解は「#TSF_split」「#TSF_chars」。\n"
        "「#TSF_brackets」などの文字列連結と「#TSF_calcDC」などの電卓を組み合わせれば逆ポーランド記法への数式変換は強いられないはず。\n"
        ,TSF_style="N")
    TSF_Forth_settext("calcFXtest:","\t".join(["「1 3 m1|2」を数式「[2]/[1]-[0]」で連結→","1","3","m1|2","[2]/[1]-[0]","#TSF_calcFX","2","#TSF_join","1","#TSF_echoes"]))
    TSF_Forth_settext("calcDCtest:","\t".join(["「1 / 3 - m1|2」を数式に連結(ついでに小数デモ)→","1","/","3","-","m1|2","5","#TSF_join","#TSF_calcDC","2","#TSF_join","1","#TSF_echoes"]))
    TSF_Forth_settext("calcKNテスト:","\t".join(["「一割る三引く(マイナス二分の一)」(ついでに単位付き計算デモ)は","一割る三引く(マイナス二分の一)","を単位付き計算する","2","個分連結","1","行表示する"]))
    TSF_Forth_settext("aboutCalc:",
        "「calc」系ワード分数電卓の概要(暫定案)。\n"
        "「#TSF_calcFX」は分数表記。「#TSF_calcDC」は小数表記。「#TSF_calcKN」億以上の単位を漢字表記。全部基本的には分数計算。\n"
        "「#TSF_calcFXQQ」「#TSF_calcDCQQ」「#TSF_calcKNQQ」という演算結果をハッシュに追加する九九のような機能がある。\n"
        "「#TSF_calcPR」は有効桁数の調整。初期値は72桁(千無量大数)。「π」(円周率)「θ」(2*π)「ｅ」(ネイピア数)などは桁溢れ予防で68桁(一無量大数)。\n"
        "「#TSF_calcRO」は端数処理の調整。初期値は「ROUND_DOWN」(0方向に丸める)。\n"
        "有効桁数「#TSF_calcPR」や端数処理「#TSF_calcRO」など数式の計算結果に影響するので九九は忘却。\n"
        "「/」割り算と「|」分数は分けて表記。数値の「p」プラス「m」マイナスも演算子の「+」プラス「-」マイナスと分けて表記。\n"
        "通常の割り算の他に1未満を切り捨てる「\\」、余りを求める「#」、消費税計算用「%」演算子がある。掛け算は「*」演算子。\n"
        "自然対数(logｅ)は「E」。常用対数(log10)は「L」。無理数は分数に丸められるので「E256/E2」や「L256/L2」が8にならない。\n"
        "「81&3l」や「256の二進対数」という任意底対数の演算子は整数同士専用のアルゴリズムを使えるので「256&2l」が8になる。\n"
        "「kM1~10」で1から10まで合計するような和数列(総和)が使える。同様に「kP1~10」で積数列(総乗)を用いて乗数や階乗の計算も可能。\n"
        "(最大)公約数は「12&16G」。(最小)公倍数は「12&16g」。「&」のみを単独で使った場合は掛け算の同じ優先順位で加算する。\n"
        "0で割るもしくは有効桁数溢れなど、何らかの事情で計算できない場合は便宜上「n|0」という事にする。「p」「m」は付かない。\n"
        "「tan(θ*90|360)」なども何かしらの巨大な数ではなく0で割った「n|0」と表記したいがとりあえず未着手。\n"
        "「2分の1を5乗」など日本語風表記で分数を扱う場合は「(2分の1)を5乗」と書かないと「2分の(1を5乗)」と解釈してしまう。\n"
        "ゼロ比較演算子(条件演算子)は「Z」。「kZ1~0」の様な計算でkがゼロの時は真なので1、ゼロでない時は偽なので0。「n|0」の時は「n|0」。\n"
        "条件演算子は0以上を調べる系「O」「o」、0以下を調べる系「U」「u」、0か調べる系「Z」「z」、「n|0」か調べる系「N」を用意。\n"
        ,TSF_style="N")
    TSF_Forth_settext("aboutRPN+LISP:",
        "「RPN」系ワード逆ポーランド電卓の概要(暫定案)。\n"
        "逆ポーランド記法の数式計算は強いられないとは言ったが、括弧も日本語訳も分数も排除した速度優先の電卓も別途準備(予定)。状況に合わせて使い分け(予定)。\n"
        "「#TSF_calcFX」等に存在した演算優先順位(平方根常用対数など＞積商算公約公倍数任意底対数など＞加減算消費税など＞ゼロ比較演算子数列積和など)は存在しない。\n"
        "分数やdecimal系を用いないので少数の制度が保証できない。\n"
        "「LISP」系ワードポーランド電卓の概要(暫定案)。\n"
        "RPNと大体同じだがこっちは括弧を必要。「(+ p1 p2 m3)」の様に引数の自由度が優先される(予定)。\n"
        ,TSF_style="N")
    print("-- TSF_Forth_viewprintlog() --")
    TSF_debug_log=TSF_Forth_viewprintlog("")
    if save_about_mergefile:
        TSF_io_savetext(TSF_about_mergefile,TSF_debug_log)
    print("-- TSF_Forth_run() --")
    TSF_Forth_pushargv()
    TSF_Forth_run(TSF_Forth_1ststack())
    print("-- TSF_Forth_viewprintlog() --")
    TSF_Forth_viewprintlog()

def TSF_command_Helloworld():    #TSF_doc:TSF_about.tsfより小さなサンプルHelloworldプログラム。
    TSF_Forth_settext(TSF_Forth_1ststack(),"\t".join(["Hello world","1","#TSF_echoes"]))
    TSF_Forth_viewprintlog()

def TSF_command_FizzBuzz():    #TSF_doc:TSF_about.tsfより小さなサンプルFizzBuzzプログラム。
    TSF_Forth_settext(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","FizzBuzz:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_settext("FizzBuzz:","\t".join([ \
    "[FZcount:0]+1","#TSF_calcDC","FZcount:","0","#TSF_pokethe",
    "FZcount:","([FZcount:0]#3Z1~0)+([FZcount:0]#5Z2~0)","#TSF_calcDC","#TSF_peekthe","1","#TSF_echoes",
    "FZjump:","[FZcount:0]-20O1~0","#TSF_calcDC","#TSF_peekthe","#TSF_this",
    ]))
    TSF_Forth_settext("FZcount:","\t".join(["0","Fizz","Buzz","Fizz&Buzz"]))
    TSF_Forth_settext("FZjump:","\t".join(["FizzBuzz:","#exit"]))
    TSF_Forth_viewprintlog()

def TSF_command_calc(TSF_calctype=None):    #TSF_doc:TSFのより小さなサンプルプログラム。
    TSF_calcQ=TSF_argvs[2] if len(TSF_argvs) > 2 else "n|0"
    if TSF_calctype == "--calcDC":
        TSF_calcA=TSF_calc_decimalize(TSF_calcQ,False)
    elif TSF_calctype == "--calcKN":
        TSF_calcA=TSF_calc_decimalizeKN(TSF_calc(TSF_calcQ,False))
    else:
        TSF_calcA=TSF_calc(TSF_calcQ,False)
    TSF_io_printlog(TSF_calcA)

def TSF_command_help():    #TSF_doc:TSFのより小さなサンプルプログラム。
    TSF_Forth_settext(TSF_Forth_1ststack(),"\t".join(["about:","#TSF_pushthe","about:","#TSF_lenthe","#TSF_echoes","0","#TSF_fin."]))
    TSF_Forth_settext("about:",
        'usage: ./TSF.py [command|file.tsf] [argv] ...\n'
        'command:\n'
        '  --help        this commands view\n'
        '  --about       samplecode(UTF-8) view and saveto "' +TSF_about_mergefile+ '" \n'
        '  --helloworld  "Hello world  1  #TSF_echoes" view\n'
        '  --fizzbuzz    ([0]#3Z1~0)+([0]#5Z2~0) Fizz Buzz Fizz&Buzz view\n'
        '  --calc        fractions calculator --calc "1/3-m1|2"-> p5|6 \n'
        '  --calcDC      fractions calculator --calc "1/3-m1|2"-> 0.8333... \n'
        '  --calcKN      fractions calculator --calc "1/3-m1|2"-> 6分の5 \n'
#        '  not exist     samplecode(UTF-8) view only (no save)\n'
        ,TSF_style="N")
    TSF_Forth_run(TSF_Forth_1ststack())


TSF_about_mergefile="TSF_about.tsf"
TSF_mergefile=""
TSF_argvs=TSF_io_argvs()
TSF_Forth_Init(TSF_argvs)
if len(TSF_argvs) >= 2:
    TSF_mergefile=TSF_argvs[1]
if os.path.isfile(TSF_mergefile):
    if len(TSF_Forth_loadtext(TSF_mergefile,TSF_mergefile)):
        TSF_Forth_merge(TSF_mergefile,[])
        TSF_Forth_pushargv()
    TSF_Forth_run(TSF_Forth_1ststack())
elif TSF_mergefile == "--about":
    TSF_command_about(True)
elif TSF_mergefile == "--helloworld":
    TSF_command_Helloworld()
elif TSF_mergefile == "--fizzbuzz":
    TSF_command_FizzBuzz()
elif TSF_mergefile in ["--calc","--calcDC","--calcKN"]:
    TSF_command_calc(TSF_mergefile)
elif TSF_mergefile == "--help":
    TSF_command_help()
else:
#    TSF_command_about(False)
    TSF_command_help()
sys.exit(0 if TSF_Forth_exitcode() == "0" or TSF_Forth_exitcode() == "0|1" else TSF_Forth_exitcode())


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
