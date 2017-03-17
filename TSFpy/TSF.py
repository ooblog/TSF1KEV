#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import sys
import os
os.chdir(sys.path[0])
sys.path.append('.')
from TSF_io import *
#from TSF_Forth import *
from TSF_shuffle import *
from TSF_match import *
from TSF_uri import *
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
    TSF_Forth_argvsleftcut(TSF_argvs,2)
    TSF_Forth_run()

def TSF_sample_about():    #TSF_doc:TSFの概要サンプルプログラム。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","30","#TSF_calcPR","main1:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("main1:",
        "\t".join(["aboutTSF:","#TSF_echothe","main2:","#TSF_this"]),
        TSF_style="T")
    TSF_Forth_setTSF("main2:",
        "\t".join(["#-- 分岐の材料、電卓その他数値取得のテスト --"," ","2","#TSF_echoN","calcFXtest:","#TSF_this","calcDCtest:","#TSF_this","calcKNテスト:","#TSF_this","calenderテスト:","#TSF_this","matchテスト:","#TSF_this","shuffleテスト:","#TSF_this"," ","#-- (小数の桁数が異なる理由は分数電卓を用いない計算は有効桁数が短いため) --","2","#TSF_echoN","main3:","#TSF_this"]),
        TSF_style="T")
    TSF_Forth_setTSF("main3:",
        "\t".join(["aboutCalc:","#TSF_echothe"]),
        TSF_style="T")
    TSF_Forth_setTSF("aboutTSF:",
        "\t".join(["「TSF_Tab-Separated-Forth」の概要。",
        "スタックを積んでワード(関数)などで消化していくForth風インタプリタ。スタックの単位はtsv文字列。",
        "文字から始まる行はスタック名、タブで始まる行はスタック内容。改行のみもしくは「#」で始まる行は読み飛ばし。",
        "タブのみ行、項目の無い二重タブ、行末末尾タブ、は文字列長0のスタックが含まれるとみなされるので注意。",
        "起動時スタック「TSF_Tab-Separated-Forth:」にargvsが追加される。「#TSF_fin.」が無い場合はargvsより先に追加される。",
        "TSFでは先頭から順にワードを実行するthisスタックと末尾に引数などを積み上げ積み下げるthatスタックを別々に指定できる。",
        "そもそもスタックが複数あり、他言語で言う所の変数はスタックで代用する。関数の引数や返り値もargvs同様にスタック経由。",
        "存在しないthatスタックからの読込(存在するスタックのアンダーフロー含む)は文字列長0を返却する。",
        "存在しないthisスタックの呼び出し(存在するスタックのオーバーフロー含む)は呼び出し元に戻って続きから再開。",
        "ループは「#TSF_this」による再帰で組む。深い階層で祖先を「#TSF_this」すると子孫コールスタックはまとめて破棄される。",
        "分岐は電卓(条件演算子など)で組む。「#TSF_this」の飛び先スタック名を「#TSF_peekthe」等で引っ張る際に「#TSF_calcFX」等の演算結果で選択する。"]),
        TSF_style="N")
    TSF_Forth_setTSF("calcFXtest:",
        "\t".join(["「1 3 m1|2」を数式「[2]/[1]-[0]」で連結→","1","3","m1|2","[2]/[1]-[0]","#TSF_calcFX","2","#TSF_joinN","1","#TSF_echoN"]))
    TSF_Forth_setTSF("calcDCtest:",
        "\t".join(["「1 / 3 - m1|2」を数式に連結(ついでに小数30桁デモ)→","1","/","3","-","m1|2","5","#TSF_joinN","#TSF_calcDC","2","#TSF_joinN","1","#TSF_echoN"]))
    TSF_Forth_setTSF("calcKNテスト:",
        "\t".join(["「一割る三引く(マイナス二分の一)」(ついでに単位付き計算デモ)→","一割る三引く(マイナス二分の一)","#単位計算","2","#N個連結","1","#N行表示"]))
    TSF_Forth_setTSF("calenderテスト:",
        "\t".join(["「@bt」SwatchBeat(スイスから時差8時間)→","-480","#TSF_diffminute","@bt","#TSF_calender","2","#TSF_joinN","1","#TSF_echoN"]))
    TSF_Forth_setTSF("matchテスト:",
        "\t".join(["「いいまちがい」と「いいまつがい」の類似度→","いいまちがい","いいまつがい","#TSF_matcher","2","#TSF_joinN","1","#TSF_echoN"]))
    TSF_Forth_setTSF("shuffleテスト:",
        "\t".join(["前半TSF概要の行数(スタック「aboutTSF:」の個数)→","aboutTSF:","#TSF_lenthe","2","#TSF_joinN","1","#TSF_echoN"]))
    TSF_Forth_setTSF("aboutCalc:",
        "\t".join(["「calc」系分数電卓の概要(何らかの数値を取得したら何らかの計算して条件演算子に用いることもできる)。",
        "「#TSF_calcFX」は分数表記。「#TSF_calcDC」は小数表記。「#TSF_calcKN」億以上の単位を漢字表記。全部基本的には分数計算。",
        "「#TSF_calcPR」は有効桁数の調整。初期値は72桁(千無量大数)。「π」(円周率)「θ」(2*π)「ｅ」(ネイピア数)などは桁溢れ予防で68桁(一無量大数)。",
        "「#TSF_calcRO」は端数処理の調整。初期値は「ROUND_DOWN」(0方向に丸める)。",
        "「/」割り算と「|」分数は分けて表記。数値の正負も演算子の「+」プラス「-」マイナスと区別するため「p」プラス「m」マイナスと表記。",
        "通常の割り算の他に1未満を切り捨てる「\\」、余りを求める「#」、消費税計算用「%」演算子がある。掛け算は「*」演算子。",
        "自然対数(logｅ)は「E」。常用対数(log10)は「L」。無理数は分数に丸められるので「E256/E2」や「L256/L2」が8にならない。",
        "「81&3l」や「256の二進対数」という任意底対数の演算子は整数同士専用のアルゴリズムを使えるので「256&2l」が8になる。",
        "「kM1~10」で1から10まで合計するような和数列(総和)が使える。同様に「kP1~10」で積数列(総乗)を用いて乗数や階乗の計算も可能。",
        "(最大)公約数は「12&16G」。(最小)公倍数は「12&16g」。「&」のみを単独で使った場合は掛け算の同じ優先順位で加算する。",
        "0で割るもしくは有効桁数溢れなど、何らかの事情で計算できない場合は便宜上「n|0」という事にする。「p」「m」は付かない。",
        "「tan(θ*90|360)」なども何かしらの巨大な数ではなく0で割った「n|0」と表記したいがとりあえず未着手。",
        "マイナスによる剰余は「#TSF_peekcyclethe」の挙動に似せる。つまり「5#m4」は「4-(5#4)」と計算するので3になる。PDCAサイクルのイメージ。",
        "「2分の1を5乗」など日本語風表記で分数を扱う場合は「(2分の1)を5乗」と書かないと「2分の(1を5乗)」と解釈してしまう。",
        "ゼロ比較演算子(条件演算子)は「Z」。「kZ1~0」の様な計算でkがゼロの時は真なので1、ゼロでない時は偽なので0。「n|0」の時は「n|0」。",
        "条件演算子は0以上を調べる系「O」「o」、0以下を調べる系「U」「u」、0か調べる系「Z」「z」、「n|0」か調べる系「N」を用意。",
        "電卓以外の分岐「#TSF_casestacks」などはHTML版ドキュメント「TSF_doc(仮)」の方で解説予定。"]),
        TSF_style="N")
    TSF_sample_run("TSF_sample_about")

def TSF_sample_Helloworld():    #TSF_doc:Helloworldサンプル(「Hello world」を表示)。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["Hello world","1","#TSF_echoN"]),
        TSF_style="T")
    TSF_Forth_mainfile(".py")
    TSF_sample_run("TSF_sample_Helloworld")

def TSF_sample_Quine():    #TSF_doc:Quineサンプル(自身のTSFソースコードを表示)。
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","#TSF_popNthis","#TSF_viewthey","0","#TSF_fin."]))
    TSF_sample_run("TSF_sample_Quine")

def TSF_sample_99beer():    #TSF_doc:99Beerサンプル(「99 Bottles of Beer」を表示)。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","N-BottlesofBeer:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("N-BottlesofBeer:",
        "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[onthewallint:0]~[TSF_argvs:0]","#TSF_calcDC","onthewallint:","0","#TSF_pokethe","onthewallint:","#TSF_that","#TSF_carbonthat","#TSF_carbonthat","drinkbottles:","#TSF_this"]))
    TSF_Forth_setTSF("drinkbottles:",
        "\t".join(["#TSF_swapBAthat","1","#TSF_popNthat","[onthewallint:1]-1","#TSF_calcDC","countbottles:","#TSF_this"]))
    TSF_Forth_setTSF("countbottles:",
        "\t".join(["bottlesreplace:","bottlescall:","onthewallint:","1","#TSF_peekthe","#TSF_peeklimitthe","#TSF_clonethe","bottlesreplace:","onthewallstr:","onthewallint:","#TSF_replacestacks","bottlesreplace:","#TSF_echothe","lopbottles:","#TSF_this"]))
    TSF_Forth_setTSF("lopbottles:",
        "\t".join(["bottlesjump:","[onthewallint:2]O0~1","#TSF_calcDC","#TSF_peekthe","#TSF_this"]))
    TSF_Forth_setTSF("bottlesjump:",
        "\t".join(["drinkbottles:","#exit"]))
    TSF_Forth_setTSF("onthewallstr:",
        "\t".join(["{buybottles}","{drink}","{drinked}"]))
    TSF_Forth_setTSF("onthewallint:",
        "\t".join(["99"]),TSF_style="T")
    TSF_Forth_setTSF("bottlescall:",
        "\t".join(["nomorebottles:","1bottle:","2bottles:","3ormorebottles:"]))
    TSF_Forth_setTSF("3ormorebottles:",
        "\t".join(["{drink} bottles of beer on the wall, {drink} bottles of beer.",
        "Take one down and pass it around, {drinked} bottles of beer on the wall."]))
    TSF_Forth_setTSF("2bottles:",
        "\t".join(["{drink} bottles of beer on the wall, {drink} bottles of beer.",
        "Take one down and pass it around, 1 bottle of beer on the wall."]))
    TSF_Forth_setTSF("1bottle:",
        "\t".join(["{drink} bottle of beer on the wall, {drink} bottle of beer.",
    "Take one down and pass it around, no more bottles of beer on the wall."]))
    TSF_Forth_setTSF("nomorebottles:",
        "\t".join(["No more bottles of beer on the wall, no more bottles of beer.",
        "Go to the store and buy some more, {buybottles} bottles of beer on the wall."]))
    TSF_sample_run("TSF_sample_99beer")

def TSF_sample_FizzBuzz():    #TSF_doc:TSF_about.FizzBuzzサンプル(3の倍数の時Fizz5の倍数の時Buzzを表示)。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","N-FizzBuzz:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("N-FizzBuzz:",
        "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[FZcount:4]~[TSF_argvs:0]","#TSF_calcDC","FZcount:","4","#TSF_pokethe","FizzBuzz:","#TSF_this"]))
    TSF_Forth_setTSF("FizzBuzz:",
        "\t".join(["[FZcount:0]+1","#TSF_calcDC","FZcount:","0","#TSF_pokethe","FZcount:","([FZcount:0]#3Z1~0)+([FZcount:0]#5Z2~0)","#TSF_calcDC","#TSF_peekthe","1","#TSF_echoN","FZjump:","[FZcount:0]-[FZcount:4]O1~0","#TSF_calcDC","#TSF_peekthe","#TSF_this"]))
    TSF_Forth_setTSF("FZcount:",
        "\t".join(["0","Fizz","Buzz","Fizz&Buzz","20"]))
    TSF_Forth_setTSF("FZjump:",
        "\t".join(["FizzBuzz:","#exit"]))
    TSF_sample_run("TSF_sample_FizzBuzz")

def TSF_sample_ZunDoko():    #TSF_doc:TSF_about.ズンドコサンプル(ZunZunZunZunDokoの時VeronChoを表示)。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","N-ZunDoko:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("N-ZunDoko:",
        "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[Zcount:0]~[TSF_argvs:0]","#TSF_calcDC","Zcount:","0","#TSF_pokethe","Zreset:","#TSF_this"]))
    TSF_Forth_setTSF("Zreset:",
        "\t".join(["0","Zcount:","1","#TSF_pokethe","ZDdice:","#TSF_this"]))
    TSF_Forth_setTSF("ZDdice:",
        "\t".join(["ZDjump:","#TSF_shufflethe","ZDjump:","#TSF_carbonthe","#TSF_this"]))
    TSF_Forth_setTSF("ZDjump:",
        "\t".join(["Zun:","Doko:"]))
    TSF_Forth_setTSF("Zun:",
        "\t".join(["Zun","1","#TSF_echoN","[Zcount:1]+1","#TSF_calcDC","Zcount:","1","#TSF_pokethe","ZDdice:","#TSF_this"]))
    TSF_Forth_setTSF("Doko:",
        "\t".join(["Doko","1","#TSF_echoN","VCjump:","[Zcount:0]-[Zcount:1]Z1~0","#TSF_calcDC","#TSF_peekthe","#TSF_this"]))
    TSF_Forth_setTSF("VCjump:",
        "\t".join(["Zreset:","VeronCho:"]))
    TSF_Forth_setTSF("VeronCho:",
        "\t".join(["VeronCho","1","#TSF_echoN"]))
    TSF_Forth_setTSF("Zcount:",
        "\t".join(["4","0"]))
    TSF_sample_run("TSF_sample_ZunDoko")

def TSF_sample_Fibonacci(TSF_argvs):    #TSF_doc:TSF_about.フィボナッチ数列サンプル(「(4<<n*(3+n))//((4<<2*n)-(2<<n)-1)&((2<<n)-1)」を表示)。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","200","#TSF_calcPR","N-Fibonacci:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("N-Fibonacci:",
        "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[Fibcount:0]~[TSF_argvs:0]","#TSF_calcDC","Fibcount:","0","#TSF_pokethe","Fibonacci:","#TSF_this"]))
    TSF_Forth_setTSF("Fibonacci:",
        "\t".join(["[Fibcount:1]Z1~[Fibcount:1]","#TSF_calcDC","((2&(([0]+3)*[0]+2)^)/((2&(2*[0]+2)^)-(2&([0]+1)^)-1)\\1)#(2&([0]+1)^)","#TSF_calcDC","1","#TSF_echoN","[Fibcount:1]+1","#TSF_calcDC","Fibcount:","1","#TSF_pokethe","Fibjump:","[Fibcount:0]-([Fibcount:1]+1)o0~1","#TSF_calcDC","#TSF_peekthe","#TSF_this"]))
    TSF_Forth_setTSF("Fibcount:",
        "\t".join(["20","-1"]))
    TSF_Forth_setTSF("Fibjump:",
        "\t".join(["Fibonacci:","#exit"]))
    TSF_sample_run("TSF_sample_Fibonacci")

def TSF_sample_Prime(TSF_argvs):    #TSF_doc:TSF_about.素数列挙サンプル(約数が1とその数自身な数値を表示)。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","N-prime:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("N-prime:",
        "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[Pcount:0]~[TSF_argvs:0]","#TSF_calcDC","Pcount:","0","#TSF_pokethe","primeskip:","#TSF_this"]))
    TSF_Forth_setTSF("primeskip:",
        "\t".join(["Pstep:","[Pcount:1]","#TSF_calcDC","#TSF_peekcyclethe","Pcount:","#TSF_carbonthe","[0]+[1]","#TSF_calcDC","Pcount:","2","#TSF_pokethe","[Pcount:1]+1","#TSF_calcDC","Pcount:","1","#TSF_pokethe","primewhile:","#TSF_this"]))
    TSF_Forth_setTSF("primewhile:",
        "\t".join(["Pwhilejump:","[Pcount:0]-[Pcount:2]O0~1","#TSF_calcDC","#TSF_peekthe","#TSF_this"]))
    TSF_Forth_setTSF("Pwhilejump:",
        "\t".join(["prime2chk:","primeecho:"]))
    TSF_Forth_setTSF("prime2chk:",
        "\t".join(["P2chkjump:","Pcount:","#TSF_carbonthe","2F[0]~[0])-2Z0~1","#TSF_calcDC","#TSF_peekthe","#TSF_this"]))
    TSF_Forth_setTSF("P2chkjump:",
        "\t".join(["primeMchk:","primeskip:"]))
    TSF_Forth_setTSF("primeMchk:",
        "\t".join(["primeadd:","#TSF_this"]))
    TSF_Forth_setTSF("PMchkjump:",
        "\t".join(["primeadd:","primeskip:"]))
    TSF_Forth_setTSF("primeadd:",
        "\t".join(["Ppool:","Pcount:","#TSF_carbonthe","1","#TSF_addNthe","primeskip:","#TSF_this"]))
    TSF_Forth_setTSF("primeecho:",
        "\t".join(["[Pcount:0]-1U3~(6-[Pcount:0])/2","#TSF_calcDC","Ppool:","#TSF_popNthe","Ppool:","#TSF_echothe"]))
    TSF_Forth_setTSF("Pcount:",
        "\t".join(["100","0","1"]))
    TSF_Forth_setTSF("Ppool:",
        "\t".join(["2","3","5"]))
    TSF_Forth_setTSF("Pstep:",
        "\t".join(["6","4","2","4","2","4","6","2"]))
    TSF_sample_run("TSF_sample_Prime")

def TSF_sample_calcKN(TSF_argvs):    #TSF_doc:単位表示電卓サンプルプログラム。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","calcKN:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("calcKN:",
        "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[calcKNtest:0]~[TSF_argvs:0]","#TSF_calcKN","1","#TSF_echoN"]))
    TSF_Forth_setTSF("calcKNtest:",
        "\t".join(["1/3-m1|2"]))
    TSF_sample_run("TSF_sample_calcKN")

def TSF_sample_calcDC(TSF_argvs):    #TSF_doc:小数表示電卓サンプルプログラム。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","calcDC:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("calcDC:",
        "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[calcDCtest:0]~[TSF_argvs:0]","#TSF_calcDC","1","#TSF_echoN"]))
    TSF_Forth_setTSF("calcDCtest:",
        "\t".join(["1/3-m1|2"]))
    TSF_sample_run("TSF_sample_calcDC")

def TSF_sample_calcFX(TSF_argvs):    #TSF_doc:分数表示電卓サンプルプログラム。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","calcFX:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("calcFX:",
        "\t".join(["TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z[calcFXtest:0]~[TSF_argvs:0]","#TSF_calcFX","1","#TSF_echoN"]))
    TSF_Forth_setTSF("calcFXtest:",
        "\t".join(["1/3-m1|2"]))
    TSF_sample_run("TSF_sample_calcFX")

def TSF_sample_calender(TSF_argvs):    #TSF_doc:日時表示サンプルプログラム。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","calender:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("calender:",
        "\t".join(["testorargvs:","TSF_argvs:","#TSF_cloneargvs","TSF_argvs:","#TSF_lenthe","[0]Z1~0","#TSF_calcDC","#TSF_peekthe","#TSF_carbonthe","#TSF_calender","1","#TSF_echoN"]))
    TSF_Forth_setTSF("calendertest:",
        "\t".join(["@000y@0m@0dm@wdec@0h@0n@0s"]))
    TSF_Forth_setTSF("testorargvs:",
        "\t".join(["TSF_argvs:","calendertest:"]))
    TSF_sample_run("TSF_sample_calender")

def TSF_sample_help():    #TSF_doc:TSFコマンド一覧表示サンプルプログラム。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        "\t".join(["UTF-8","#TSF_encoding","replace:","#TSF_this","help:","#TSF_echothe","0","#TSF_fin."]))
    TSF_Forth_setTSF("help:",
        "\t".join(["usage: ./TSF.py [command|file.tsf] [argv] ...",
        "commands:",
        "  --help        this commands view",
        "  --about       about TSF UTF-8 text (Japanese) view\" ",
        "  --python      TSF.tsf to Python.py view or save\" ",
        "  --helloworld  \"Hello world  1  #TSF_echoN\" sample",
        "  --quine       TSF_Forth_viewthey() Quine (self source) sample",
        "  --99beer      99 Bottles of Beer sample",
        "  --fizzbuzz    ([0]#3Z1~0)+([0]#5Z2~0) Fizz Buzz Fizz&Buzz sample",
        "  --zundoko     Zun Zun Zun Zun Doko VeronCho sample",
        "  --fibonacci   Fibonacci number 0,1,1,2,3,5,8,13,21,55... sample",
        "  --prime       prime numbers 2,3,5,7,11,13,17,19,23,29... sample",
        "  --calcFX      fractions calculator \"1/3-m1|2\"-> p5|6 sample",
        "  --calcDC      fractions calculator \"1/3-m1|2\"-> 0.8333... sample",
        "  --calcKN      fractions calculator \"1/3-m1|2\"-> 6 bunno 5 sample",
        "  --calender    \"@000y@0m@0dm@wdec@0h@0n@0s\"-> TSF_time_getdaytime() sample"]),
        TSF_style="N")
    TSF_Forth_setTSF("replace:",
        "\t".join(["replaceN:","#TSF_carbonthe","#TSF_calender","replaceN:","0","#TSF_pokethe","help:","replaceO:","replaceN:","#TSF_replacestacks"]))
    TSF_Forth_setTSF("replaceO:",
        "\t".join(["TSF_time_getdaytime()"]))
    TSF_Forth_setTSF("replaceN:",
        "\t".join(["@000y@0m@0dm@wdec@0h@0n@0s"]))
    TSF_sample_run("TSF_sample_help")

TSF_argvs=TSF_io_argvs()
TSF_Forth_init(TSF_argvs,[TSF_shuffle_Initwords,TSF_match_Initwords,TSF_uri_Initwords,TSF_calc_Initwords,TSF_time_Initwords])
TSF_mergefile=''
if len(TSF_argvs) >= 2:
    TSF_mergefile=TSF_argvs[1]
if os.path.isfile(TSF_mergefile):
    if len(TSF_Forth_loadtext(TSF_mergefile,TSF_mergefile)):
        TSF_Forth_merge(TSF_mergefile,[],TSF_mergedel=True)
        TSF_Forth_mainfile(TSF_mergefile)
        TSF_sample_run()
elif TSF_mergefile in ["--about"]:
    TSF_sample_about()
elif TSF_mergefile in ["--py","--python","--Python"]:
    if len(TSF_argvs) >= 4:
        TSF_Forth_writesamplepy(TSF_argvs[2],TSF_argvs[3])
    elif len(TSF_argvs) >= 3:
        TSF_Forth_writesamplepy(TSF_argvs[2])
elif TSF_mergefile in ["--hello","--helloworld","--Helloworld"]:
    TSF_sample_Helloworld()
elif TSF_mergefile in ["--quine","--Quine"]:
    TSF_sample_Quine()
elif TSF_mergefile in ["--99beer","--beer99","--beer","--99"]:
    TSF_sample_99beer()
elif TSF_mergefile in ["--fizz","--buzz","--fizzbuzz","--FizzBuzz"]:
    TSF_sample_FizzBuzz()
elif TSF_mergefile in ["--zun","--doko","--veroncho","--zundoko","--ZunDoko","--ZunDokoVeronCho"]:
    TSF_sample_ZunDoko()
elif TSF_mergefile in ["--fib","--fibonacci","--Fibonacci"]:
    TSF_sample_Fibonacci(TSF_argvs)
elif TSF_mergefile in ["--prime","--Prime"]:
    TSF_sample_Prime(TSF_argvs)
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
