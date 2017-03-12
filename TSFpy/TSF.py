#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_io import *
#from TSF_Forth import *
from TSF_shuffle import *
from TSF_match import *
from TSF_calc import *
from TSF_time import *


def TSF_sample_run(TSF_sample_sepalete=None):    #TSF_doc:TSFサンプルプログラム実行。
    if TSF_sample_sepalete != None:
        TSF_io_printlog("-- {0} source --".format(TSF_sample_sepalete))
        TSF_Forth_viewthey()
        TSF_Forth_addfin(TSF_argvs)
        TSF_io_printlog("-- {0} advgs --".format(TSF_sample_sepalete))
        TSF_Forth_viewargvs()
        TSF_io_printlog("-- {0} run --".format(TSF_sample_sepalete))
    else:
        TSF_Forth_addfin(TSF_argvs)
    TSF_Forth_run()

def TSF_sample_about():    #TSF_doc:TSFの概要サンプルプログラム。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","main1:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("main1:","\t".join(["aboutTSF:","#TSF_echothe","main2:","#TSF_this"]))
    TSF_Forth_setTSF("main2:","\t".join(["#分数電卓のテスト","1","#TSF_echoN","16","#TSF_calcPR","calcFXtest:","#TSF_this","calcDCtest:","#TSF_this","calcKNテスト:","#TSF_this","#","1","#TSF_echoN","main3:","#TSF_this"]))
    TSF_Forth_setTSF("main3:","\t".join(["aboutCalc:","#TSF_echothe","main4:","#TSF_this"]))
    TSF_Forth_setTSF("main4:","\t".join(["aboutMatch:","#TSF_echothe"]))
    TSF_Forth_setTSF("aboutTSF:",
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
        "分岐の別解として「#TSF_matchcasethe」準備中。条件に一致する文字列がスタックに含まれてたらその位置を返すワードにする予定。\n"
        "「#TSF_brackets」などの文字列処理と「#TSF_calcDC」などの電卓を組み合わせれば逆ポーランド記法への数式変換は強いられないはず。\n"
        ,TSF_style="N")
    TSF_Forth_setTSF("calcFXtest:","\t".join(["「1 3 m1|2」を数式「[2]/[1]-[0]」で連結→","1","3","m1|2","[2]/[1]-[0]","#TSF_calcFX","2","#TSF_joinN","1","#TSF_echoN"]))
    TSF_Forth_setTSF("calcDCtest:","\t".join(["「1 / 3 - m1|2」を数式に連結(ついでに小数デモ)→","1","/","3","-","m1|2","5","#TSF_joinN","#TSF_calcDC","2","#TSF_joinN","1","#TSF_echoN"]))
    TSF_Forth_setTSF("calcKNテスト:","\t".join(["「一割る三引く(マイナス二分の一)」(ついでに単位付き計算デモ)→","一割る三引く(マイナス二分の一)","#単位計算","2","#N個連結","1","#N行表示"]))
    TSF_Forth_setTSF("aboutCalc:",
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
        "マイナスによる剰余は「#TSF_peekcyclethe」の挙動に似せる。つまり「5#m4」は「4-(5#4)」と計算するので3になる。PDCAサイクルのイメージ。\n"
        "「2分の1を5乗」など日本語風表記で分数を扱う場合は「(2分の1)を5乗」と書かないと「2分の(1を5乗)」と解釈してしまう。\n"
        "ゼロ比較演算子(条件演算子)は「Z」。「kZ1~0」の様な計算でkがゼロの時は真なので1、ゼロでない時は偽なので0。「n|0」の時は「n|0」。\n"
        "条件演算子は0以上を調べる系「O」「o」、0以下を調べる系「U」「u」、0か調べる系「Z」「z」、「n|0」か調べる系「N」を用意。\n"
        ,TSF_style="N")
    TSF_Forth_setTSF("aboutMatch:",
        "「match」系ワード解説は準備中…。\n"
        ,TSF_style="N")
    TSF_sample_run("TSF_sample_about")

def TSF_sample_Helloworld():    #TSF_doc:Helloworldサンプル(「Hello world」を表示)。
#    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["Hello world","1","#TSF_echoN","0","#TSF_fin."]))
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["Hello world","1","#TSF_echoN"]))
    TSF_sample_run("TSF_sample_Helloworld")

def TSF_sample_Quine():    #TSF_doc:Quineサンプル(自身のソースコードを表示)。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","#TSF_popNthis","#TSF_viewthey","0","#TSF_fin."]))
    TSF_sample_run("TSF_sample_Quine")

def TSF_sample_99beer():    #TSF_doc:99Beerサンプル(「99 Bottles of Beer」を表示)。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","N-BottlesofBeer:","#TSF_this","","0","#TSF_fin."]))
    TSF_Forth_setTSF("N-BottlesofBeer:","\t".join(["99","#TSF_swapBAthat","m1","#TSF_peekthat","m[0]","#TSF_calcDC","#TSF_peekthat",
        "#TSF_carbonthat","buybottles:","0","#TSF_pokethe",
        "#TSF_carbonthat","onthewall:","1","#TSF_pokethe",
        "onthewall:","#TSF_that","drinkbottles:","#TSF_this"]))
    TSF_Forth_setTSF("drinkbottles:","\t".join(["#TSF_swapCBthat","2","#TSF_popNthat","#TSF_carbonthat","[0]-1","#TSF_calcDC","buybottles:",
        "#TSF_carbonthe","countbottles:","#TSF_this"]))
    TSF_Forth_setTSF("countbottles:","\t".join(["bottlesreplace:","bottlescall:","onthewall:","0","#TSF_peekthe","#TSF_peeklimitthe","#TSF_clonethe",
        "bottlesreplace:","onthewallstr:","onthewall:","#TSF_replacestacks",
        "bottlesreplace:","#TSF_echothe","lopbottles:","#TSF_this"]))
    TSF_Forth_setTSF("lopbottles:","\t".join(["Beerjump:","[onthewall:1]O0~1","#TSF_calcDC","#TSF_peekthe","#TSF_this"]))
    TSF_Forth_setTSF("buybottles:","\t".join(["99"]))
    TSF_Forth_setTSF("onthewallstr:","\t".join(["{drink}","{drinked}","{buybottles}"]))
    TSF_Forth_setTSF("onthewall:","\t".join(["98","99","99"]))
    TSF_Forth_setTSF("Beerjump:","\t".join(["drinkbottles:","#exit"]))
    TSF_Forth_setTSF("bottlescall:","\t".join(["nomorebottles:","1bottle:","2bottles:","3ormorebottles:"]))
    TSF_Forth_setTSF("3ormorebottles:","\t".join(["{drink} bottles of beer on the wall, {drink} bottles of beer.\n"
        "Take one down and pass it around, {drinked} bottles of beer on the wall."]),TSF_style="N")
    TSF_Forth_setTSF("2bottles:","\t".join(["{drink} bottles of beer on the wall, {drink} bottles of beer.\n"
        "Take one down and pass it around, 1 bottle of beer on the wall."]),TSF_style="N")
    TSF_Forth_setTSF("1bottle:","\t".join(["{drink} bottle of beer on the wall, {drink} bottle of beer.\n"
        "Take one down and pass it around, no more bottles of beer on the wall."]),TSF_style="N")
    TSF_Forth_setTSF("nomorebottles:","\t".join(["No more bottles of beer on the wall, no more bottles of beer.\n"
        "Go to the store and buy some more, {buybottles} bottles of beer on the wall."]),TSF_style="N")
    TSF_sample_run("TSF_sample_99beer")

def TSF_sample_FizzBuzz():    #TSF_doc:TSF_about.FizzBuzzサンプル(3の倍数の時Fizz5の倍数の時Buzzを表示)。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","N-FizzBuzz:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("N-FizzBuzz:","\t".join(["FZcount:","4","#TSF_peekthe","#TSF_swapBAthat","m1","#TSF_peekthat","m[0]","#TSF_calcDC","#TSF_peekthat",
        "FZcount:","4","#TSF_pokethe","FizzBuzz:","#TSF_this"]))
    TSF_Forth_setTSF("FizzBuzz:","\t".join([ \
        "[FZcount:0]+1","#TSF_calcDC","FZcount:","0","#TSF_pokethe",
        "FZcount:","([FZcount:0]#3Z1~0)+([FZcount:0]#5Z2~0)","#TSF_calcDC","#TSF_peekthe","1","#TSF_echoN",
        "FZjump:","[FZcount:0]-[FZcount:4]O1~0","#TSF_calcDC","#TSF_peekthe","#TSF_this",
    ]))
    TSF_Forth_setTSF("FZcount:","\t".join(["0","Fizz","Buzz","Fizz&Buzz","20"]))
    TSF_Forth_setTSF("FZjump:","\t".join(["FizzBuzz:","#exit"]))
    TSF_sample_run("TSF_sample_FizzBuzz")

def TSF_sample_Fibonacci(TSF_argvs):    #TSF_doc:TSF_about.フィボナッチ数列サンプル(「(4<<n*(3+n))//((4<<2*n)-(2<<n)-1)&((2<<n)-1)」を表示)。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","200","#TSF_calcPR","N-Fibonacci:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("N-Fibonacci:","\t".join(["Fibcount:","1","#TSF_peekthe","#TSF_swapBAthat","m1","#TSF_peekthat","m[0]","#TSF_calcDC","#TSF_peekthat",
        "Fibcount:","1","#TSF_pokethe","Fibonacci:","#TSF_this"]))
    TSF_Forth_setTSF("Fibonacci:","\t".join(["Fibcount:","0","#TSF_peekthe","[0]Z1~[0]","#TSF_calcDC","((2&(([0]+3)*[0]+2)^)/((2&(2*[0]+2)^)-(2&([0]+1)^)-1)\\1)#(2&([0]+1)^)",
        "#TSF_calcDC","1","#TSF_echoN","[Fibcount:0]+1","#TSF_calcDC","Fibcount:","0","#TSF_pokethe",
        "Fibjump:","[Fibcount:0]-[Fibcount:1]+1O1~0","#TSF_calcDC","#TSF_peekthe","#TSF_this"]))
    TSF_Forth_setTSF("Fibcount:","\t".join(["-1","20"]))
    TSF_Forth_setTSF("Fibjump:","\t".join(["Fibonacci:","#exit"]))
    TSF_sample_run("TSF_sample_Fibonacci")

def TSF_sample_calcKN(TSF_argvs):    #TSF_doc:単位表示電卓サンプルプログラム。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","calcKN:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("calcKN:","\t".join([
        "1/3-m1|2","#TSF_swapBAthat","m1","#TSF_peekthat","m[0]","#TSF_calcDC","#TSF_peekthat",
        "#TSF_calcKN","1","#TSF_echoN"
    ]),TSF_style="T")
    TSF_sample_run("TSF_sample_calcKN")

def TSF_sample_calcDC(TSF_argvs):    #TSF_doc:小数表示電卓サンプルプログラム。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","calcDC:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("calcDC:","\t".join([
        "1/3-m1|2","#TSF_swapBAthat","m1","#TSF_peekthat","m[0]","#TSF_calcDC","#TSF_peekthat",
        "#TSF_calcDC","1","#TSF_echoN"
    ]),TSF_style="T")
    TSF_sample_run("TSF_sample_calcDC")

def TSF_sample_calcFX(TSF_argvs):    #TSF_doc:分数表示電卓サンプルプログラム。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","calcFX:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("calcFX:","\t".join([
        "1/3-m1|2","#TSF_swapBAthat","m1","#TSF_peekthat","m[0]","#TSF_calcDC","#TSF_peekthat",
        "#TSF_calcFX","1","#TSF_echoN"
    ]),TSF_style="T")
    TSF_sample_run("TSF_sample_calcFX")

def TSF_sample_calender(TSF_argvs):    #TSF_doc:日時表示サンプルプログラム。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","calender:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("calender:","\t".join([
        "@000y@0m@0dm@wdec@0h@0n@0s","#TSF_swapBAthat","m1","#TSF_peekthat","m[0]","#TSF_calcDC","#TSF_peekthat",
        "#TSF_calender","1","#TSF_echoN"
    ]),TSF_style="T")
    TSF_sample_run("TSF_sample_calender")

def TSF_sample_help():    #TSF_doc:TSFコマンド一覧表示サンプルプログラム。
#    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","replace:","#TSF_this","help:","#TSF_pushthe","help:","#TSF_lenthe","#TSF_reverseN","help:","#TSF_lenthe","#TSF_echoN","0","#TSF_fin."]))
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","replace:","#TSF_this","help:","#TSF_echothe","0","#TSF_fin."]))
    TSF_Forth_setTSF("help:",
        'usage: ./TSF.py [command|file.tsf] [argv] ...\n'
        'commands:\n'
        '  --help        this commands view\n'
        '  --about       about TSF UTF-8 text (Japanese) view" \n'
        '  --helloworld  "Hello world  1  #TSF_echoN" view\n'
        '  --quine       TSF_Forth_viewthey() Quine (self source) view\n'
        '  --99beer      99 Bottles of Beer view\n'
        '  --fizzbuzz    ([0]#3Z1~0)+([0]#5Z2~0) Fizz Buzz Fizz&Buzz view\n'
#        zundoko VeronCho
        '  --fibonacci   Fibonacci number 0,1,1,2,3,5,8,13,21,55... view\n'
#        prime
        '  --calcFX      fractions calculator "1/3-m1|2"-> p5|6 view\n'
        '  --calcDC      fractions calculator "1/3-m1|2"-> 0.8333... view\n'
        '  --calcKN      fractions calculator "1/3-m1|2"-> 6 bunno 5 view\n'
        '  --calender    "@000y@0m@0dm@wdec@0h@0n@0s"-> TSF_time_getdaytime()\n'
        ,TSF_style="N")
    TSF_Forth_setTSF("replace:","\t".join(["replaceN:","#TSF_carbonthe","#TSF_calender","replaceN:","0","#TSF_pokethe","help:","replaceO:","replaceN:","#TSF_replacestacks"]))
    TSF_Forth_setTSF("replaceO:","\t".join(["TSF_time_getdaytime()"]))
    TSF_Forth_setTSF("replaceN:","\t".join(["@000y@0m@0dm@wdec@0h@0n@0s"]))
    TSF_sample_run("TSF_sample_help")

TSF_mergefile=""
TSF_argvs=TSF_io_argvs()
TSF_Forth_init(TSF_argvs,[TSF_shuffle_Initwords,TSF_match_Initwords,TSF_calc_Initwords,TSF_time_Initwords])
if len(TSF_argvs) >= 2:
    TSF_mergefile=TSF_argvs[1]
if os.path.isfile(TSF_mergefile):
    if len(TSF_Forth_loadtext(TSF_mergefile,TSF_mergefile)):
        TSF_Forth_merge(TSF_mergefile,[],TSF_mergedel=True)
        TSF_sample_run()
elif TSF_mergefile in ["--about"]:
    TSF_sample_about()
elif TSF_mergefile in ["--hello","--helloworld","--Helloworld"]:
    TSF_sample_Helloworld()
elif TSF_mergefile in ["--quine","--Quine"]:
    TSF_sample_Quine()
elif TSF_mergefile in ["--99beer","--beer99","--beer","--99"]:
    TSF_sample_99beer()
elif TSF_mergefile in ["--fizz","--buzz","--fizzbuzz","--FizzBuzz"]:
    TSF_sample_FizzBuzz()
elif TSF_mergefile in ["--fib","--fibonacci","--Fibonacci"]:
    TSF_sample_Fibonacci(TSF_argvs)
elif TSF_mergefile in ["--calcKN"]:
    TSF_sample_calcKN(TSF_argvs)
elif TSF_mergefile in ["--calcDC"]:
    TSF_sample_calcDC(TSF_argvs)
elif TSF_mergefile in ["--calc","--calcFX"]:
    TSF_sample_calcFX(TSF_argvs)
elif TSF_mergefile in ["--time","--calender"]:
    TSF_sample_calender(TSF_argvs)
else:  #TSF_mergefile in ["--help"]:
    TSF_sample_help()
sys.exit(0 if TSF_Forth_exitcode() in ["0","0|1","0.0"] else TSF_Forth_exitcode())


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
