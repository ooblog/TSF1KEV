#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import datetime
import os
import random
from TSF_Forth import *


def TSF_shuffle_Initwords(TSF_words):    #TSF_doc:スタック並び替え関連のワードを追加する(TSFAPI)。
    TSF_words["#TSF_swapBAthat"]=TSF_shuffle_swapBAthat; TSF_words["#スタックBA交換"]=TSF_shuffle_swapBAthat
    TSF_words["#TSF_swapCAthat"]=TSF_shuffle_swapCAthat; TSF_words["#スタックCA交換"]=TSF_shuffle_swapCAthat
    TSF_words["#TSF_swapCBthat"]=TSF_shuffle_swapCBthat; TSF_words["#スタックCB交換"]=TSF_shuffle_swapCBthat
    TSF_words["#TSF_reverseN"]=TSF_shuffle_reverseN; TSF_words["#スタックN個逆順"]=TSF_shuffle_reverseN
    TSF_words["#TSF_lenthe"]=TSF_shuffle_lenthe; TSF_words["#スタック個数"]=TSF_shuffle_lenthe
    TSF_words["#TSF_lenthis"]=TSF_shuffle_lenthis; TSF_words["#実行中スタック個数"]=TSF_shuffle_lenthis
    TSF_words["#TSF_lenthat"]=TSF_shuffle_lenthat; TSF_words["#積込先スタック個数"]=TSF_shuffle_lenthat
    TSF_words["#TSF_lenthey"]=TSF_shuffle_lenthey; TSF_words["#スタック一覧個数"]=TSF_shuffle_lenthey
    TSF_words["#TSF_peekthe"]=TSF_shuffle_peekthe; TSF_words["#スタック読込"]=TSF_shuffle_peekthe
    TSF_words["#TSF_peekthis"]=TSF_shuffle_peekthis; TSF_words["#実行中スタック読込"]=TSF_shuffle_peekthis
    TSF_words["#TSF_peekthat"]=TSF_shuffle_peekthat; TSF_words["#積込先スタック読込"]=TSF_shuffle_peekthat
    TSF_words["#TSF_peekrndthe"]=TSF_shuffle_peekrndthe; TSF_words["#スタック乱択"]=TSF_shuffle_peekrndthe
    TSF_words["#TSF_peekrndthis"]=TSF_shuffle_peekrndthis; TSF_words["#実行中スタック乱択"]=TSF_shuffle_peekrndthis
    TSF_words["#TSF_peekrndthat"]=TSF_shuffle_peekrndthat; TSF_words["#積込先スタック乱択"]=TSF_shuffle_peekrndthat
    TSF_words["#TSF_peekcyclethe"]=TSF_shuffle_peekcyclethe; TSF_words["#スタック周択"]=TSF_shuffle_peekcyclethe
    TSF_words["#TSF_peekcyclethis"]=TSF_shuffle_peekcyclethis; TSF_words["#実行中スタック周択"]=TSF_shuffle_peekcyclethis
    TSF_words["#TSF_peekcyclethat"]=TSF_shuffle_peekcyclethat; TSF_words["#積込先スタック周択"]=TSF_shuffle_peekcyclethat
    TSF_words["#TSF_peeklimitthe"]=TSF_shuffle_peeklimitthe; TSF_words["#スタック囲択"]=TSF_shuffle_peeklimitthe
    TSF_words["#TSF_peeklimitthis"]=TSF_shuffle_peeklimitthis; TSF_words["#実行中スタック囲択"]=TSF_shuffle_peeklimitthis
    TSF_words["#TSF_peeklimitthat"]=TSF_shuffle_peeklimitthat; TSF_words["#積込先スタック囲択"]=TSF_shuffle_peeklimitthat
    TSF_words["#TSF_carbonthe"]=TSF_shuffle_carbonthe; TSF_words["#スタックの表面を複製"]=TSF_shuffle_carbonthe
    TSF_words["#TSF_carbonthis"]=TSF_shuffle_carbonthis; TSF_words["#実行中スタックの表面を複製"]=TSF_shuffle_carbonthis
    TSF_words["#TSF_carbonthat"]=TSF_shuffle_carbonthat; TSF_words["#積込先スタックの表面を複製"]=TSF_shuffle_carbonthat
    TSF_words["#TSF_pokethe"]=TSF_shuffle_pokethe; TSF_words["#スタックに上書き"]=TSF_shuffle_pokethe
    TSF_words["#TSF_pokethis"]=TSF_shuffle_pokethis; TSF_words["#実行中スタックに上書"]=TSF_shuffle_pokethis
    TSF_words["#TSF_pokethat"]=TSF_shuffle_pokethat; TSF_words["#積込先スタックに上書"]=TSF_shuffle_pokethat
    TSF_words["#TSF_pokerndthe"]=TSF_shuffle_pokerndthe; TSF_words["#スタックに乱択上書"]=TSF_shuffle_pokerndthe
    TSF_words["#TSF_pokerndthis"]=TSF_shuffle_pokerndthis; TSF_words["#実行中スタックに乱択上書"]=TSF_shuffle_pokerndthis
    TSF_words["#TSF_pokerndthat"]=TSF_shuffle_pokerndthat; TSF_words["#積込先スタックに乱択上書"]=TSF_shuffle_pokerndthat
    TSF_words["#TSF_pokecyclethe"]=TSF_shuffle_pokecyclethe; TSF_words["#スタックに周択上書"]=TSF_shuffle_pokecyclethe
    TSF_words["#TSF_pokecyclethis"]=TSF_shuffle_pokecyclethis; TSF_words["#実行中スタックに周択上書"]=TSF_shuffle_pokecyclethis
    TSF_words["#TSF_pokecyclethat"]=TSF_shuffle_pokecyclethat; TSF_words["#積込先スタックに周択上書"]=TSF_shuffle_pokecyclethat
    TSF_words["#TSF_pokelimitthe"]=TSF_shuffle_pokelimitthe; TSF_words["#スタックに囲択上書"]=TSF_shuffle_pokelimitthe
    TSF_words["#TSF_pokelimitthis"]=TSF_shuffle_pokelimitthis; TSF_words["#実行中スタックに囲択上書"]=TSF_shuffle_pokelimitthis
    TSF_words["#TSF_pokelimitthat"]=TSF_shuffle_pokelimitthat; TSF_words["#積込先スタックに囲択上書"]=TSF_shuffle_pokelimitthat
    TSF_words["#TSF_delthe"]=TSF_shuffle_delthe; TSF_words["#スタックを削除"]=TSF_shuffle_delthe
    TSF_words["#TSF_delthis"]=TSF_shuffle_delthis; TSF_words["#実行中スタックを削除"]=TSF_shuffle_delthis
    TSF_words["#TSF_delthat"]=TSF_shuffle_delthat; TSF_words["#積込先スタックを削除"]=TSF_shuffle_delthat
    TSF_words["#TSF_clonethe"]=TSF_shuffle_clonethe; TSF_words["#スタックの複製"]=TSF_shuffle_clonethe
    TSF_words["#TSF_clonethis"]=TSF_shuffle_clonethis; TSF_words["#実行中スタックの複製"]=TSF_shuffle_clonethis
    TSF_words["#TSF_clonethat"]=TSF_shuffle_clonethat; TSF_words["#積込先スタックの複製"]=TSF_shuffle_clonethat
    TSF_words["#TSF_clonethey"]=TSF_shuffle_clonethey; TSF_words["#スタック名一覧の複製"]=TSF_shuffle_clonethey
    TSF_words["#TSF_cloneargvs"]=TSF_shuffle_cloneargvs; TSF_words["#コマンドライン引数の複製"]=TSF_shuffle_cloneargvs
    TSF_words["#TSF_pushthe"]=TSF_shuffle_pushthe; TSF_words["#スタックを積む"]=TSF_shuffle_pushthe
    TSF_words["#TSF_pushthis"]=TSF_shuffle_pushthis; TSF_words["#実行中スタックを積む"]=TSF_shuffle_pushthis
    TSF_words["#TSF_pushthat"]=TSF_shuffle_pushthat; TSF_words["#積込先スタックを積む"]=TSF_shuffle_pushthat
    TSF_words["#TSF_pushthey"]=TSF_shuffle_pushthey; TSF_words["#スタック名一覧を積む"]=TSF_shuffle_pushthey
    TSF_words["#TSF_addNthe"]=TSF_shuffle_addNthe; TSF_words["#N個スタックを別のスタックに追加"]=TSF_shuffle_addNthe
    TSF_words["#TSF_addNthis"]=TSF_shuffle_addNthis; TSF_words["#N個スタックを実行中スタックに追加"]=TSF_shuffle_addNthis
    TSF_words["#TSF_popNthe"]=TSF_shuffle_popNthe; TSF_words["#N個スタックを削除"]=TSF_shuffle_popNthe
    TSF_words["#TSF_popNthis"]=TSF_shuffle_popNthis; TSF_words["#N個実行中スタックを削除"]=TSF_shuffle_popNthis
    TSF_words["#TSF_popNthat"]=TSF_shuffle_popNthat; TSF_words["#N個積込先スタックを削除"]=TSF_shuffle_popNthat
    TSF_words["#TSF_reversethe"]=TSF_shuffle_reversethe; TSF_words["#スタックを逆順"]=TSF_shuffle_reversethe
    TSF_words["#TSF_reversethat"]=TSF_shuffle_reversethat; TSF_words["#積込先スタックを逆順"]=TSF_shuffle_reversethat
    TSF_words["#TSF_shufflethe"]=TSF_shuffle_shufflethe; TSF_words["#スタックシャッフル"]=TSF_shuffle_shufflethe
    TSF_words["#TSF_shufflethat"]=TSF_shuffle_shufflethat; TSF_words["#積込先スタックシャッフル"]=TSF_shuffle_shufflethat
    return TSF_words

def TSF_shuffle_swapBAthat():   #TSF_doc:[stackB,stackA]スタックAとスタックBを交換する。
    TSF_tsvA=TSF_Forth_popthat()
    TSF_tsvB=TSF_Forth_popthat()
    TSF_Forth_pushthat(TSF_tsvA)
    TSF_Forth_pushthat(TSF_tsvB)
    return None

def TSF_shuffle_swapCAthat():   #TSF_doc:[stackC,stackB,stackA]スタックAとスタックCを交換する。
    TSF_tsvA=TSF_Forth_popthat()
    TSF_tsvB=TSF_Forth_popthat()
    TSF_tsvC=TSF_Forth_popthat()
    TSF_Forth_pushthat(TSF_tsvA)
    TSF_Forth_pushthat(TSF_tsvB)
    TSF_Forth_pushthat(TSF_tsvC)
    return None

def TSF_shuffle_swapCBthat():   #TSF_doc:[stackC,stackB,stackA]スタックBとスタックCを交換する。
    TSF_tsvA=TSF_Forth_popthat()
    TSF_tsvB=TSF_Forth_popthat()
    TSF_tsvC=TSF_Forth_popthat()
    TSF_Forth_pushthat(TSF_tsvB)
    TSF_Forth_pushthat(TSF_tsvC)
    TSF_Forth_pushthat(TSF_tsvA)
    return None

def TSF_shuffle_reverseN():   #TSF_doc:[stackN…stackB,stackA,count]スタックを逆順にする。count自身とcountの回数分スタック積み下ろし。
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthat()); TSF_reverse=[""]*TSF_countlen
    for TSF_count in range(TSF_countlen):
        TSF_reverse[TSF_count]=TSF_Forth_popthat()
    for TSF_count in range(TSF_countlen):
        TSF_Forth_pushthat(TSF_reverse[TSF_count])
    return None

def TSF_shuffle_lenthe():   #TSF_doc:[stack]指定したスタックの数を数える。1スタック積み上げ。
    TSF_Forth_pushthat(str(TSF_Forth_stacklen(TSF_Forth_popthat())))
    return None

def TSF_shuffle_lenthis():   #TSF_doc:[]thisスタック(実行中スタック)の数を数える。1スタック積み上げ。
    TSF_Forth_pushthat(str(TSF_Forth_stacklen(TSF_Forth_stackthis())))
    return None

def TSF_shuffle_lenthat():   #TSF_doc:[]thatスタック(積込先スタック)の数を数える。1スタック積み上げ。
    TSF_Forth_pushthat(str(TSF_Forth_stacklen(TSF_Forth_stackthat())))
    return None

def TSF_shuffle_lenthey():   #TSF_doc:[]スタック名一覧の数を数える。1スタック積み上げ。
    TSF_Forth_pushthat(str(TSF_Forth_stackslen()))
    return None

def TSF_shuffle_peekthe():   #TSF_doc:[stack,counter]スタックから読み込む。2スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_Forth_popthat(),TSF_count))
    return None

def TSF_shuffle_peekthis():   #TSF_doc:[counter]実行中スタックから読み込む。1スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_Forth_stackthis(),TSF_count))
    return None

def TSF_shuffle_peekthat():   #TSF_doc:[counter]積込先スタックから読み込む。1スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_Forth_stackthat(),TSF_count))
    return None

def TSF_shuffle_peekrndthe():   #TSF_doc:[stack]スタックから読み込む(乱択)。1スタック積み下ろして、1スタック積み上げ。
    TSF_the=TSF_Forth_popthat()
    TSF_count=random.randint(1,TSF_Forth_stacklen(TSF_the))-1
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_the,TSF_count))
    return None

def TSF_shuffle_peekrndthis():   #TSF_doc:[]実行中スタックから読み込む(乱択)。1スタック積み上げ。
    TSF_the=TSF_Forth_stackthis()
    TSF_count=random.randint(1,TSF_Forth_stacklen(TSF_the))-1
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_the,TSF_count))
    return None

def TSF_shuffle_peekrndthat():   #TSF_doc:[]積込先スタックから読み込む(乱択)。1スタック積み上げ。
    TSF_the=TSF_Forth_stackthat()
    TSF_count=random.randint(1,TSF_Forth_stacklen(TSF_the))-1
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_the,TSF_count))
    return None

def TSF_shuffle_peekcyclethe():   #TSF_doc:[stack,counter]スタックから読み込む(周択)。2スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_Forth_pushthat(TSF_Forth_peekcyclethe(TSF_Forth_popthat(),TSF_count))
    return None

def TSF_shuffle_peekcyclethis():   #TSF_doc:[counter]実行中スタックから読み込む(周択)。1スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_Forth_pushthat(TSF_Forth_peekcyclethe(TSF_Forth_stackthis(),TSF_count))
    return None

def TSF_shuffle_peekcyclethat():   #TSF_doc:[counter]積込先スタックから読み込む(周択)。1スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_Forth_pushthat(TSF_Forth_peekcyclethe(TSF_Forth_stackthat(),TSF_count))
    return None

def TSF_shuffle_peeklimitthe():   #TSF_doc:[stack,counter]スタックから読み込む(囲択)。2スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_Forth_pushthat(TSF_Forth_peeklimitthe(TSF_Forth_popthat(),TSF_count))
    return None

def TSF_shuffle_peeklimitthis():   #TSF_doc:[stack,counter]実行中スタックから読み込む(囲択)。2スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_Forth_pushthat(TSF_Forth_peeklimitthe(TSF_Forth_stackthis(),TSF_count))
    return None

def TSF_shuffle_peeklimitthat():   #TSF_doc:[stack,counter]積込先スタックから読み込む(囲択)。2スタック積み下ろして、1スタック積み上げ。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_Forth_pushthat(TSF_Forth_peeklimitthe(TSF_Forth_stackthat(),TSF_count))
    return None

def TSF_shuffle_carbonthe():   #TSF_doc:[stack]スタックの一番上のスタックを複製する。0スタック積み下ろし。
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_Forth_popthat(),-1))
    return None

def TSF_shuffle_carbonthis():   #TSF_doc:[]実行中スタックの一番上のスタックを複製する。0スタック積み下ろし。
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_Forth_stackthis(),-1))
    return None

def TSF_shuffle_carbonthat():   #TSF_doc:[]積込先スタックの一番上のスタックを複製する。0スタック積み下ろし。
    TSF_Forth_pushthat(TSF_Forth_peekthe(TSF_Forth_stackthat(),-1))
    return None

def TSF_shuffle_pokethe():   #TSF_doc:[poke,stack,counter]積込先スタックに上書き。3スタック積み下ろし。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_pokethe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokethis():   #TSF_doc:[stack,counter]実行中スタックに上書き。2スタック積み下ろし。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_the=TSF_Forth_stackthis()
    TSF_Forth_pokethe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokethat():   #TSF_doc:[stack,counter]積込先スタックに上書き。2スタック積み下ろし。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_the=TSF_Forth_stackthat()
    TSF_Forth_pokethe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokerndthe():   #TSF_doc:[poke,stack]積込先スタックに上書き(乱択)。2スタック積み下ろし。
    TSF_the=TSF_Forth_popthat()
    TSF_count=random.randint(1,TSF_Forth_stacklen(TSF_the))-1
    TSF_Forth_pokethe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokerndthis():   #TSF_doc:[poke]実行中スタックに上書き(乱択)。1スタック積み下ろし。
    TSF_the=TSF_Forth_stackthis()
    TSF_count=random.randint(1,TSF_Forth_stacklen(TSF_the))-1
    TSF_Forth_pokethe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokerndthat():   #TSF_doc:[poke]積込先スタックに上書き(乱択)。1スタック積み下ろし。
    TSF_the=TSF_Forth_stackthat()
    TSF_count=random.randint(1,TSF_Forth_stacklen(TSF_the))-1
    TSF_Forth_pokethe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokecyclethe():   #TSF_doc:[poke,stack,counter]積込先スタックに上書き(周択)。3スタック積み下ろし。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_pokecyclethe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokecyclethis():   #TSF_doc:[stack,counter]実行中スタックに上書き(周択)。2スタック積み下ろし。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_the=TSF_Forth_stackthis()
    TSF_Forth_pokecyclethe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokecyclethat():   #TSF_doc:[stack,counter]積込先スタックに上書き(周択)。2スタック積み下ろし。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_the=TSF_Forth_stackthat()
    TSF_Forth_pokecyclethe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokelimitthe():   #TSF_doc:[poke,stack,counter]積込先スタックに上書き(囲択)。3スタック積み下ろし。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_pokelimitthe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokelimitthis():   #TSF_doc:[stack,counter]実行中スタックに上書き(囲択)。2スタック積み下ろし。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_the=TSF_Forth_stackthis()
    TSF_Forth_pokelimitthe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_pokelimitthat():   #TSF_doc:[stack,counter]積込先スタックに上書き(囲択)。2スタック積み下ろし。
    TSF_count=TSF_Forth_popintthe(TSF_Forth_stackthat())
    TSF_the=TSF_Forth_stackthat()
    TSF_Forth_pokelimitthe(TSF_the,TSF_count,TSF_Forth_popthat())
    return None

def TSF_shuffle_delthe():   #TSF_doc:[stack]スタックを削除。1スタック積み下ろし。
    TSF_the=TSF_Forth_popthat()
    return TSF_Forth_delthe(TSF_the)

def TSF_shuffle_delthis():   #TSF_doc:[]実行中スタックを削除。スタックも抜けてコールポインタを1つ減らす。1スタック積み下ろし。
    TSF_the=TSF_Forth_stackthis()
    return TSF_Forth_delthe(TSF_the)

def TSF_shuffle_delthat():   #TSF_doc:[]積込先スタックを削除。実行中スタックも抜けてコールポインタを1つ減らす。全スタック積み下ろし。
    TSF_the=TSF_Forth_popthat()
    return TSF_Forth_delthe(TSF_the)

def TSF_shuffle_clonethe():   #TSF_doc:[stackC,stack]スタックを複製する。2スタック積み下ろし。
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_clonethe(TSF_Forth_popthat(),TSF_the)
    return None

def TSF_shuffle_clonethis():   #TSF_doc:[stackC]実行中スタックを複製する。1スタック積み下ろし。
    TSF_the=TSF_Forth_stackthis()
    TSF_Forth_clonethe(TSF_Forth_popthat(),TSF_the)
    return None

def TSF_shuffle_clonethat():   #TSF_doc:[stackC]積込先スタック複製する。1スタック積み下ろし。
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_clonethe(TSF_Forth_popthat(),TSF_the)
    return None

def TSF_shuffle_clonethey():   #TSF_doc:[stackC]スタック名一覧をスタックとして複製する。1スタック積み下ろし。
    TSF_Forth_clonethey(TSF_Forth_popthat())
    return None

def TSF_shuffle_cloneargvs():   #TSF_doc:[stackC]コマンドライン引数を複製する。自身の実行ファイル名は除外。1スタック積み下ろし。
    TSF_Forth_cloneargvs(TSF_Forth_popthat())
    return None

def TSF_shuffle_pushthe():   #TSF_doc:[stack]指定したスタックを積込先スタックに積み上げ。1スタック積み下ろしてからスタック積み上げ。
    TSF_Forth_addargvs(TSF_Forth_stackthat(),TSF_Forth_stackvalue(TSF_Forth_popthat()))
    return None

def TSF_shuffle_pushthis():   #TSF_doc:[]実行中スタックを丸ごと積込先スタックに積み上げ。
    TSF_Forth_addargvs(TSF_Forth_stackthat(),TSF_Forth_stackvalue(TSF_Forth_stackthis()))
    return None

def TSF_shuffle_pushthat():   #TSF_doc:[]積込先スタックを丸ごと積込先スタックに積み上げ。
    TSF_Forth_addargvs(TSF_Forth_stackthat(),tuple(TSF_Forth_stackvalue(TSF_Forth_stackthat())))
    return None

def TSF_shuffle_pushthey():   #TSF_doc:[]スタック名一覧を丸ごと積込先スタックに積み上げ。
    TSF_Forth_addargvs(TSF_Forth_stackthat(),deque(TSF_Forth_stackskeys()))
    return None

def TSF_shuffle_addNthe():   #TSF_doc:[stack,…valueB,valueA,count]スタックを別のスタックに積み上げ。count自身とcountの回数分と指定スタック名分、スタック積み下ろし。
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthat()); TSF_addN=[""]*TSF_countlen
    for TSF_count in range(max(TSF_countlen,0)):
        TSF_addN[TSF_count]=TSF_Forth_popthat()
    TSF_the=TSF_Forth_popthat()
    TSF_Forth_addargvs(TSF_the,reversed(TSF_addN))
    return None

def TSF_shuffle_addNthis():   #TSF_doc:[…valueB,valueA,count]スタックを実行中スタックに積み上げ。count自身とcountの回数分スタック積み下ろし。
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthat()); TSF_addN=[""]*TSF_countlen
    for TSF_count in range(max(TSF_countlen,0)):
        TSF_addN[TSF_count]=TSF_Forth_popthat()
    TSF_the=TSF_Forth_stackthis()
    TSF_Forth_addargvs(TSF_the,reversed(TSF_addN))
    return None

def TSF_shuffle_popNthe():   #TSF_doc:[count,stack]count自身とcountの回数分スタック積み下ろし。
    TSF_the=TSF_Forth_popthat()
    TSF_countlen=TSF_Forth_popintthe(TSF_the)
    for TSF_count in range(max(TSF_countlen,0)):
        TSF_Forth_popthe(TSF_the)
    return None

def TSF_shuffle_popNthis():   #TSF_doc:[count]実行中スタックのcount自身とcountの回数分スタック積み下ろし。
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthis())
    for TSF_count in range(max(TSF_countlen,0)):
        TSF_Forth_popthis()
    return None

def TSF_shuffle_popNthat():   #TSF_doc:[count]積込先スタックのcount自身とcountの回数分スタック積み下ろし。
    TSF_countlen=TSF_Forth_popintthe(TSF_Forth_stackthat())
    for TSF_count in range(max(TSF_countlen,0)):
        TSF_Forth_popthat()
    return None

def TSF_shuffle_reversethe():   #TSF_doc:[stack]スタックを逆順化。1スタック積み下ろし。
    TSF_Forth_reversethe(TSF_Forth_popthat())
    return None

def TSF_shuffle_reversethat():   #TSF_doc:[]積込先スタックを逆順化。0スタック積み下ろし。
    TSF_Forth_reversethe(TSF_Forth_stackthat())
    return None

def TSF_shuffle_shufflethe():   #TSF_doc:[stack]スタックをシャッフル。1スタック積み下ろし。
    TSF_Forth_shufflethe(TSF_Forth_popthat())
    return None

def TSF_shuffle_shufflethat():   #TSF_doc:[]積込先スタックをシャッフル。0スタック積み下ろし。
    TSF_Forth_shufflethe(TSF_Forth_stackthat())
    return None


def TSF_shuffle_debug(TSF_argvs):    #TSF_doc:「TSF/TSF_shuffle.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_Forth_init(TSF_argvs,[TSF_shuffle_Initwords])
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"\t".join(["UTF-8","#TSF_encoding","TSF_argvs:","#TSF_cloneargvs","TSF_shuffletest:","#TSF_this","0","#TSF_fin."]))
    TSF_Forth_setTSF("TSF_shuffle.py:","\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout]))
    TSF_Forth_setTSF("TSF_shuffletest:","\t".join(["TSF_shuffleAF:","TSF_shuffleBF:","#TSF_clonethe","TSF_shuffleAF:","#TSF_shufflethe"]))
    TSF_Forth_setTSF("TSF_shuffleBF:","\t".join(["P","D","C","A"]))
    TSF_Forth_addfin(TSF_argvs)
    TSF_Forth_argvsleftcut(TSF_argvs,1)
    TSF_Forth_run()
    for TSF_thename in TSF_Forth_stackskeys():
        TSF_debug_log=TSF_Forth_view(TSF_thename,True,TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    from collections import OrderedDict
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/debug_shuffle.log"
    TSF_debug_log=TSF_shuffle_debug(TSF_argvs)
    TSF_io_savetext(TSF_debug_savefilename,TSF_debug_log)
    print("")
    try:
        print("--- {0} ---\n{1}".format(TSF_debug_savefilename,TSF_debug_log))
    except:
        print("can't 'print(TSF_debug_savefilename,TSF_debug_log)'")
    finally:
        pass
    sys.exit()

# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
