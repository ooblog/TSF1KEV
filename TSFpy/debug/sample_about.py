#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import sys
import os
os.chdir(sys.path[0])
sys.path.append('/mnt/sda2/github/TSF1KEV/TSFpy')
from TSF_io import *
#from TSF_Forth import *
from TSF_shuffle import *
from TSF_match import *
from TSF_calc import *
from TSF_time import *

TSF_Forth_init(TSF_io_argvs(),[TSF_shuffle_Initwords,TSF_match_Initwords,TSF_calc_Initwords,TSF_time_Initwords])

TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
    "\t".join(["UTF-8","#TSF_encoding","30","#TSF_calcPR","main1:","#TSF_this","0","#TSF_fin."]),TSF_style="T")
TSF_Forth_setTSF("main1:",
    "\t".join(["aboutTSF:","#TSF_echothe","main2:","#TSF_this"]),TSF_style="T")
TSF_Forth_setTSF("main2:",
    "\t".join(["#-- 分岐の材料、電卓その他数値取得のテスト --"," ","2","#TSF_echoN","calcFXtest:","#TSF_this","calcDCtest:","#TSF_this","calcKNテスト:","#TSF_this","calenderテスト:","#TSF_this","matchテスト:","#TSF_this","shuffleテスト:","#TSF_this"," ","#-- (小数の桁数が異なる理由は分数電卓を用いない計算は有効桁数が短いため) --","2","#TSF_echoN","main3:","#TSF_this"]),TSF_style="T")
TSF_Forth_setTSF("main3:",
    "\t".join(["aboutCalc:","#TSF_echothe"]),TSF_style="T")
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
    "分岐は電卓(条件演算子など)で組む。「#TSF_this」の飛び先スタック名を「#TSF_peekthe」等で引っ張る際に「#TSF_calcFX」等の演算結果で選択する。"]),TSF_style="N")
TSF_Forth_setTSF("calcFXtest:",
    "\t".join(["「1 3 m1|2」を数式「[2]/[1]-[0]」で連結→","1","3","m1|2","[2]/[1]-[0]","#TSF_calcFX","2","#TSF_joinN","1","#TSF_echoN"]),TSF_style="T")
TSF_Forth_setTSF("calcDCtest:",
    "\t".join(["「1 / 3 - m1|2」を数式に連結(ついでに小数30桁デモ)→","1","/","3","-","m1|2","5","#TSF_joinN","#TSF_calcDC","2","#TSF_joinN","1","#TSF_echoN"]),TSF_style="T")
TSF_Forth_setTSF("calcKNテスト:",
    "\t".join(["「一割る三引く(マイナス二分の一)」(ついでに単位付き計算デモ)→","一割る三引く(マイナス二分の一)","#単位計算","2","#N個連結","1","#N行表示"]),TSF_style="T")
TSF_Forth_setTSF("calenderテスト:",
    "\t".join(["「@bt」SwatchBeat(スイスから時差8時間)→","-480","#TSF_diffminute","@bt","#TSF_calender","2","#TSF_joinN","1","#TSF_echoN"]),TSF_style="T")
TSF_Forth_setTSF("matchテスト:",
    "\t".join(["「いいまちがい」と「いいまつがい」の類似度→","いいまちがい","いいまつがい","#TSF_matcher","2","#TSF_joinN","1","#TSF_echoN"]),TSF_style="T")
TSF_Forth_setTSF("shuffleテスト:",
    "\t".join(["前半TSF概要の行数(スタック「aboutTSF:」の個数)→","aboutTSF:","#TSF_lenthe","2","#TSF_joinN","1","#TSF_echoN"]),TSF_style="T")
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
    "電卓以外の分岐「#TSF_casestacks」などはHTML版ドキュメント「TSF_doc(仮)」の方で解説予定。"]),TSF_style="N")

TSF_Forth_addfin(TSF_io_argvs())
TSF_Forth_argvsleftcut(TSF_io_argvs(),1)
TSF_Forth_run()