#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_io import *
from TSF_calc import *
from TSF_time import *


def TSF_Forth_1ststack():    #TSF_doc:TSF_初期化に使う1ststack名
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSF_doc:TSF_初期化に使うバージョン(ブランチ)名
    return "20170108U045559"

TSF_words={}
def TSF_Forth_Initwords():    #TSF_doc:TSF_words(ワード)を初期化する
    global TSF_words
    TSF_words={
        "#TSF_fin.":TSF_Forth_fin,  "コードと共にTSFを終了。":TSF_Forth_fin,
        "#TSF_over":TSF_Forth_over,  "スタックを出る":TSF_Forth_over,  "スタックを出る(TSFも終了)":TSF_Forth_over,
# "TSF_GUI" "をGUI処理"
# "TSF_newword" "という言葉を作る"
# "TSF_noword" "という言葉を忘れる"
        "#TSF_encoding":TSF_Forth_encoding,  "でエンコード":TSF_Forth_encoding,
        "#TSF_this":TSF_Forth_this,  "のスタックに入る":TSF_Forth_this,  "スタックを実行":TSF_Forth_this,
        "#TSF_that":TSF_Forth_that,  "スタックを積込先にする":TSF_Forth_that,
        "#TSF_viewthe":TSF_Forth_viewthe,  "を表示する":TSF_Forth_viewthe,
        "#TSF_viewthis":TSF_Forth_viewthis,  "実行中スタックを表示する":TSF_Forth_viewthis,
        "#TSF_viewthat":TSF_Forth_viewthat,  "積込先スタックを表示する":TSF_Forth_viewthat,
        "#TSF_viewthey":TSF_Forth_viewthey,  "スタック一覧を表示する":TSF_Forth_viewthey,
        "#TSF_stylethe":TSF_Forth_stylethe,  "スタイルをスタックに設定する":TSF_Forth_stylethe,
        "#TSF_stylethis":TSF_Forth_stylethis,  "スタイルを実行中スタックに設定する":TSF_Forth_stylethis,
        "#TSF_stylethat":TSF_Forth_stylethat,  "スタイルを積込先スタックに設定する":TSF_Forth_stylethat,
        "#TSF_echoes":TSF_Forth_echoes,  "行表示する":TSF_Forth_echoes,
        "#TSF_lenthe":TSF_Forth_lenthe,  "のスタック個数":TSF_Forth_lenthe,
        "#TSF_lenthis":TSF_Forth_lenthis,  "実行中スタックの個数":TSF_Forth_lenthis,
        "#TSF_lenthat":TSF_Forth_lenthat,  "積込先スタックの個数":TSF_Forth_lenthat,
        "#TSF_lenthey":TSF_Forth_lenthey,  "スタック名一覧の個数":TSF_Forth_lenthey,
        "#TSF_pushthe":TSF_Forth_pushthe,  "のスタックを積む":TSF_Forth_pushthe,
        "#TSF_pushthis":TSF_Forth_pushthis,  "実行中スタックを自身に積む":TSF_Forth_pushthis,
        "#TSF_pushthat":TSF_Forth_pushthat,  "積込先スタックから積む":TSF_Forth_pushthat,
        "#TSF_pushthey":TSF_Forth_pushthey,  "スタック名一覧を積む":TSF_Forth_pushthey,
        "#TSF_carbonthe":TSF_Forth_carbonthe,  "スタックの一番上を複製する":TSF_Forth_carbonthe,
        "#TSF_carbonthis":TSF_Forth_carbonthis,  "実行中スタックの一番上を複製する":TSF_Forth_carbonthis,
        "#TSF_carbonthat":TSF_Forth_carbonthat,  "積込先スタックの一番上を複製する":TSF_Forth_carbonthat,
# "TSF_findthe" "正規表現でスタックから探す"
# "TSF_findthat" "正規表現で積み込み先スタックを探す"
# "TSF_replacethe" "正規表現でスタックを置換する"
# "TSF_replacethat" "正規表現で積み込み先スタックにて置換する"
        "#TSF_popthe":TSF_Forth_popthe,  "スタックから拾う":TSF_Forth_popthe,
        "#TSF_popthis":TSF_Forth_popthis,  "実行中スタックから拾う":TSF_Forth_popthis,
        "#TSF_popthat":TSF_Forth_popthat,  "積込先スタックから除く":TSF_Forth_popthat,
        "#TSF_peekthe":TSF_Forth_peekthe,  "番目のスタックから読み込む":TSF_Forth_peekthe,
        "#TSF_pokethe":TSF_Forth_pokethe,  "番目のスタックに上書き":TSF_Forth_pokethe,
        "#TSF_delthe":TSF_Forth_delthe,  "のスタック削除":TSF_Forth_delthe,
        "#TSF_delthis":TSF_Forth_delthat,  "実行中スタックを削除":TSF_Forth_delthis,
        "#TSF_delthat":TSF_Forth_delthat,  "積込先スタックを削除":TSF_Forth_delthat,
        "#TSF_calcFX":TSF_Forth_calcFX,  "を分数する":TSF_Forth_calcFX,
        "#TSF_calcFXQQ":TSF_Forth_calcFXQQ,  "を分数九九する":TSF_Forth_calcFXQQ,
        "#TSF_calcDC":TSF_Forth_calcDC,  "を小数する":TSF_Forth_calcDC,
        "#TSF_calcDCQQ":TSF_Forth_calcDCQQ,  "を小数九九する":TSF_Forth_calcDCQQ,
        "#TSF_calcKN":TSF_Forth_calcKN,  "を単位付き計算する":TSF_Forth_calcKN,
        "#TSF_calcKNQQ":TSF_Forth_calcKNQQ,  "を単位付き九九する":TSF_Forth_calcKNQQ,
        "#TSF_calcPR":TSF_Forth_calcPR,  "を有効桁数":TSF_Forth_calcPR,
        "#TSF_calcRO":TSF_Forth_calcRO,  "で端数処理":TSF_Forth_calcRO,
# "TSF_RPN" "逆ポーランド電卓で計算する"
# "TSF_RPNQQ" "逆ポーランド電卓で九九する"
# "TSF_LISP" "ポーランド電卓で計算する"
# "TSF_LISPQQ" "ポーランド電卓で九九する"
# "TSF_CALENDER" "日時を取得する"
# "TSF_TIMER" "時間をを測定する"
        "#TSF_brackets":TSF_Forth_brackets,  "括弧で数式に連結":TSF_Forth_brackets,
        "#TSF_join":TSF_Forth_join,  "個分連結":TSF_Forth_join,
        "#TSF_joinC":TSF_Forth_joinC,  "で回数分挟んで連結":TSF_Forth_joinC,
        "#TSF_split":TSF_Forth_split,  "の文字で分離":TSF_Forth_split,
        "#TSF_chars":TSF_Forth_chars,  "一文字ずつに分離":TSF_Forth_chars,
        "#TSF_read":TSF_Forth_read,  "ファイルを読み込む":TSF_Forth_read,
        "#TSF_mergethe":TSF_Forth_mergethe,  "スタック上のTSFテキストを混ぜる":TSF_Forth_mergethe,
        "#TSF_publishthe":TSF_Forth_publishthe,  "スタックをテキスト化して別スタックに読み込む":TSF_Forth_publishthe,
        "#TSF_publishthis":TSF_Forth_publishthis,  "実行中スタックをテキスト化して別スタックに読み込む":TSF_Forth_publishthis,
        "#TSF_publishthat":TSF_Forth_publishthat,  "積込先スタックをテキスト化して別スタックに読み込む":TSF_Forth_publishthat,
        "#TSF_remove":TSF_Forth_remove,  "テキストファイルを削除する":TSF_Forth_remove,
        "#TSF_savethe":TSF_Forth_savethe,  "スタックをテキストファイルに上書きする":TSF_Forth_savethe,
        "#TSF_writethe":TSF_Forth_writethe,  "スタックをテキストファイルに追記する":TSF_Forth_writethe,
    }
    return TSF_words

def TSF_Forth_words(TSF_word=None):    #TSF_doc:TSF_words(ワード)を取得する
    global TSF_words
    return TSF_words

def TSF_Forth_pushargv():    #TSF_doc:sys.argv(コマンドライン引数)を「TSF_Tab-Separated-Forth:」に追加。
    for TSF_argvcount in range(len(sys.argv)):
        TSF_Forth_push(TSF_Forth_1ststack(),sys.argv[-TSF_argvcount-1])
    TSF_Forth_push(TSF_Forth_1ststack(),str(len(sys.argv)))

TSF_stacks=OrderedDict()
def TSF_Forth_Initstacks(TSF_argv):    #TSF_doc:TSF_stacks(スタック)を初期化する
    global TSF_stacks
    TSF_stacks=OrderedDict()
    TSF_stacks[TSF_Forth_1ststack()]=["UTF-8",":TSF_encoding","0",":TSF_fin."]+TSF_argv+[str(len(TSF_argv))]
    TSF_Forth_pushargv()
    return TSF_stacks

def TSF_Forth_stacks():    #TSF_doc:TSF_stacks(スタック)を取得する
    global TSF_stacks
    return TSF_stacks

TSF_callptrs=OrderedDict()
def TSF_Forth_Initcallptrs():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を初期化する
    global TSF_callptrs
    TSF_callptrs=OrderedDict();
    return TSF_callptrs

def TSF_Forth_callptrs():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を取得する
    global TSF_callptrs
    return TSF_callptrs

TSF_styles=OrderedDict()
def TSF_Forth_Initstyles():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を初期化する
    global TSF_styles
    TSF_styles=OrderedDict()
    TSF_styles[TSF_Forth_1ststack()]="T"
    return TSF_styles

def TSF_Forth_styles():    #TSF_doc:TSF_callwords,TSF_callcounts(コールスタック)を取得する
    global TSF_styles
    return TSF_styles

TSF_thisstack_name,TSF_thisstack_count=TSF_Forth_1ststack(),0
def TSF_Forth_thisstack():    #TSF_doc:スタック実行元、TSF_thisstack_name,TSF_thisstack_countを取得する
    return TSF_thisstack_name,TSF_thisstack_count

TSF_thatstack_name=TSF_thisstack_name
def TSF_Forth_thatstack():    #TSF_doc:スタック積み上げ先、TSF_thatstack_nameを取得する
    return TSF_thatstack_name

def TSF_Forth_Init(TSF_argv):    #TSF_doc:TSF_words,TSF_stacks,TSF_callptrsの3つをまとめて初期化する。thisthatも初期化。
    TSF_Forth_Initstacks(TSF_argv); TSF_Forth_Initwords(); TSF_Forth_Initcallptrs(); TSF_Forth_Initstyles()
    TSF_thisstack_name,TSF_thisstack_count=TSF_Forth_1ststack(),0
    TSF_thatstack_name=TSF_thisstack_name
    return TSF_words,TSF_stacks,TSF_callptrs

def TSF_Forth_settext(TSF_stack,TSF_text,TSF_style="T"):    #TSF_doc:テキストを読み込んでTSF_stacksの一スタック扱いにする。
    global TSF_stacks,TSF_styles
    TSF_stacks[TSF_stack]=TSF_text.rstrip('\n').replace('\t','\n').split('\n')
    TSF_styles[TSF_stack]=TSF_style

def TSF_Forth_pop(TSF_that):    #TSF_doc:スタックを積み下ろす。
    TSF_popdata=""
    if TSF_that in TSF_stacks and len(TSF_stacks[TSF_that]):
        TSF_popdata=TSF_stacks[TSF_that].pop()
    return TSF_popdata

def TSF_Forth_popdecimalize(TSF_that):    #TSF_doc:複数形のワードで最初のcountを数値として取得。
    TSF_decimalT=TSF_Forth_pop(TSF_that); 
    TSF_decimalT=TSF_calc_decimalizeDC(TSF_calc(TSF_decimalT,True))
    TSF_decimalI=abs(int(float(TSF_decimalT if TSF_decimalT != "n|0" else "0")))
    return TSF_decimalI

def TSF_Forth_push(TSF_that,TSF_pushdata):    #TSF_doc:スタックを積み上げる。
    if TSF_that in TSF_stacks:
        TSF_stacks[TSF_that].append(TSF_pushdata)
    else:
        TSF_stacks[TSF_that]=[TSF_pushdata]

def TSF_Forth_peek(TSF_that,TSF_count):    #TSF_doc:スタックから読み取る。
    TSF_peekdata=""
    if TSF_that in TSF_stacks:
        if 0 <= TSF_count < len(TSF_stacks[TSF_that]):
            TSF_peekdata=TSF_stacks[TSF_that][TSF_count]
        elif len(TSF_stacks[TSF_that]) <= -TSF_count < 0:
            TSF_peekdata=TSF_stacks[TSF_that][TSF_count]
    return TSF_peekdata

def TSF_Forth_poke(TSF_that,TSF_count,TSF_poke):    #TSF_doc:スタックに書き込む。正常なら0。TSF_countの値がはみ出した場合1。スタック自体が無かったら2。
    TSF_pokeerr=0
    if TSF_that in TSF_stacks:
        if 0 <= TSF_count < len(TSF_stacks[TSF_that]):
            TSF_stacks[TSF_that][TSF_count]=TSF_poke
        elif len(TSF_stacks[TSF_that]) <= -TSF_count < 0:
            TSF_stacks[TSF_that][TSF_count]=TSF_poke
        else:
            TSF_pokeerr=1
    else:
        TSF_pokeerr=2
    return TSF_pokeerr


TSF_exitcode="0"
def TSF_Forth_exitcode(TSF_fincode=None):
    global TSF_exitcode
    if TSF_fincode != None:
        TSF_exitcode=TSF_fincode
    return TSF_exitcode

def TSF_Forth_fin():    #TSF_doc:[errmsg]TSF終了時のオプションを指定する。1スタック積み下ろし。
    global TSF_callptrs
    TSF_callptrs={}
    TSF_Forth_exitcode(TSF_Forth_pop(TSF_thatstack_name))
    return ""

def TSF_Forth_over():    #TSF_doc:スタックを抜けてコールポインタを1つ減らす。コールポインタが0の時はTSF終了。スタック変化無し。
    return ""

TSF_encode="UTF-8"
def TSF_Forth_encoding():    #TSF_doc:[encode]TSFの文字コード宣言。極力冒頭に置くのが望ましい。1スタック積み下ろし。
    global TSF_encode
    TSF_encode=TSF_Forth_pop(TSF_thatstack_name)
    return None

def TSF_Forth_this():    #TSF_doc:[stack]thisスタックを変更(スタックをワード(関数)として呼ぶ)。通常はオーバーフローで呼び出し元に戻るが、再帰呼び出し等はループ扱いになる。ワード自体は1スタック積み下ろしだがスタック変化は未知数。
    TSF_thisnext=TSF_Forth_pop(TSF_thatstack_name)
    return TSF_thisnext

def TSF_Forth_that():    #TSF_doc:[stack]thatスタック(積み込み先スタック)を変更。1スタック積み下ろし。
    global TSF_thatstack_name
    TSF_thatstack_name=TSF_Forth_pop(TSF_thatstack_name)
    return None

def TSF_Forth_view(TSF_thename,TSF_view_io=True,TSF_view_log=""):    #TSF_doc:スタックの内容をテキスト表示する。
    if TSF_thename in TSF_stacks:
        TSF_stackV=[TSF_txt_ESCdecode(TSF_stk) for TSF_stk in TSF_stacks[TSF_thename]]
        TSF_style=TSF_styles.get(TSF_thename,"T")
        if TSF_style == "O":
            TSF_view_logline="{0}\t{1}\n".format(TSF_thename,"\t".join(TSF_stackV))
        elif TSF_style == "T":
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_thename,"\t".join(TSF_stackV))
        else:  # TSF_style == "N":
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_thename,"\n\t".join(TSF_stackV))
        if TSF_view_io == True:
            TSF_view_log=TSF_io_printlog(TSF_view_logline,TSF_log=TSF_view_log)
        else:
            TSF_view_log+=TSF_view_logline
    return TSF_view_log

def TSF_Forth_viewprintlog(TSF_view_log=""):    #TSF_doc:printlog用途でスタック一覧を表示する"。
    for TSF_thename in TSF_stacks.keys():
        TSF_view_log=TSF_Forth_view(TSF_thename,True,TSF_view_log)
    return TSF_view_log

def TSF_Forth_viewthe():    #TSF_doc:[stack]指定したスタックの内容をテキスト取得する。1スタック積み下ろし。
    TSF_Forth_view(TSF_Forth_pop(TSF_thatstack_name))
    return None

def TSF_Forth_viewthis():    #TSF_doc:[stack]実行中スタックを表示する"。1スタック積み下ろし。
    TSF_Forth_view(TSF_thisstack_name)
    return None

def TSF_Forth_viewthat():    #TSF_doc:[stack]積込先スタックを表示する"。1スタック積み下ろし。
    TSF_Forth_view(TSF_thatstack_name)
    return None

def TSF_Forth_viewthey():    #TSF_doc:[stack]スタック一覧を表示する"。1スタック積み下ろし。
    for TSF_thename in TSF_stacks.keys():
        TSF_Forth_view(TSF_thename)
    return None

def TSF_Forth_style(TSF_thename,TSF_style=None):    #TSF_doc:スタックの表示スタイルを指定する。
    global TSF_styles
    if TSF_style != None:
        TSF_styles[TSF_thename]=TSF_style
    elif TSF_thename in TSF_stacks:
        del TSF_stacks[TSF_thename]

def TSF_Forth_stylethe():    #TSF_doc:[stack]指定したスタックの表示スタイルを指定する。1スタック積み下ろし。
    TSF_style=TSF_Forth_pop(TSF_thatstack_name)
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    TSF_Forth_style(TSF_thename,TSF_style)
    return None

def TSF_Forth_stylethis():    #TSF_doc:[stack]指定したスタックの表示スタイルを指定する。1スタック積み下ろし。
    TSF_Forth_style(TSF_thisstack_name,TSF_Forth_pop(TSF_thatstack_name))
    return None

def TSF_Forth_stylethat():    #TSF_doc:[stack]指定したスタックの表示スタイルを指定する。1スタック積み下ろし。
    TSF_Forth_style(TSF_thatstack_name,TSF_Forth_pop(TSF_thatstack_name))
    return None

def TSF_Forth_echoes():    #TSF_doc:[…valueB,valueA,count]指定した個数スタック内容を端末で表示する。count分スタック積み下ろし。
    TSF_echoloopI=TSF_Forth_popdecimalize(TSF_thatstack_name)
    for TSF_echocount in range(TSF_echoloopI):
        TSF_io_printlog(TSF_Forth_pop(TSF_thatstack_name))
    return None

def TSF_Forth_lenthe():   #TSF_doc:[stack]指定したスタックの数を数える。1スタック積み上げ。
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    TSF_Forth_push(TSF_thatstack_name,str(len(TSF_stacks.get(TSF_thename,[]))))
    return None

def TSF_Forth_lenthis():   #TSF_doc:[]thisスタック(実行中スタック)の数を数える。1スタック積み上げ。
    TSF_Forth_push(TSF_thatstack_name,str(len(TSF_stacks.get(TSF_thisstack_name,[]))))
    return None

def TSF_Forth_lenthat():   #TSF_doc:[]thatスタック(積み込み先スタック)の数を数える。1スタック積み上げ。
    TSF_Forth_push(TSF_thatstack_name,str(len(TSF_stacks.get(TSF_thatstack_name,[]))))
    return None

def TSF_Forth_lenthey():   #TSF_doc:[]スタック名一覧の数を数える。1スタック積み上げ。
    TSF_Forth_push(TSF_thatstack_name,str(len(TSF_stacks)))
    return None

def TSF_Forth_pushthe():   #TSF_doc:[stack]指定したスタックを丸ごとthatスタック(積み込み先スタック)に積み上げ。
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    if TSF_thename in TSF_stacks:
        for TSF_tsv in reversed(TSF_stacks.get(TSF_thename,[])):
            TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return None

def TSF_Forth_pushthis():   #TSF_doc:[]実行中スタックを丸ごとthatスタック(積み込み先スタック)に積み上げ。
    if TSF_thisstack_name in TSF_stacks:
        for TSF_tsv in reversed(TSF_stacks.get(TSF_thisstack_name,[])):
            TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return None

def TSF_Forth_pushthat():   #TSF_doc:[]thatスタック(積み込み先スタック)を丸ごとthatスタック(積み込み先スタック)に積み上げ。
    if TSF_thatstack_name in TSF_stacks:
        for TSF_tsv in reversed(TSF_stacks.get(TSF_thatstack_name,[])):
            TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return None

def TSF_Forth_pushthey():   #TSF_doc:[]スタック名一覧を丸ごとthatスタック(積み込み先スタック)に積み上げ。
    for TSF_tsv in reversed(TSF_stacks):
        TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return None

def TSF_Forth_carbonthe():   #TSF_doc:[stack]スタックの一番上のスタックを複製する。
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    TSF_carbon=TSF_stacks[TSF_thename][-1] if len(TSF_stacks[TSF_thename]) > 0 else ""
    TSF_Forth_push(TSF_thatstack_name,TSF_carbon)
    return None

def TSF_Forth_carbonthis():   #TSF_doc:[]実行中スタックの一番上のスタックを複製する。
    TSF_carbon=TSF_stacks[TSF_thisstack_name][-1] if len(TSF_stacks[TSF_thisstack_name]) > 0 else ""
    TSF_Forth_push(TSF_thatstack_name,TSF_carbon)
    return None

def TSF_Forth_carbonthat():   #TSF_doc:[]積込先スタックの一番上のスタックを複製する。
    TSF_carbon=TSF_stacks[TSF_thatstack_name][-1] if len(TSF_stacks[TSF_thatstack_name]) > 0 else ""
    TSF_Forth_push(TSF_thatstack_name,TSF_carbon)
    return None

def TSF_Forth_popthe():   #TSF_doc:[stack]スタックから積込先スタックに1スタック積み下ろす。
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    TSF_tsv=TSF_Forth_pop(TSF_thename)
    TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return None

def TSF_Forth_popthis():   #TSF_doc:[]実行中スタックから積込先スタックに1スタック積み下ろす。
    TSF_tsv=TSF_Forth_pop(TSF_thisstack_name)
    TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return None

def TSF_Forth_popthat():   #TSF_doc:[]積込先スタックから1スタック積み下ろす(削除)。
    TSF_Forth_pop(TSF_thisstack_name)
    return ""

def TSF_Forth_delthe():   #TSF_doc:[stack]スタックを削除。
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    del TSF_stacks[TSF_thename]
    return None

def TSF_Forth_peekthe():   #TSF_doc:[stack,pointer]スタックから読み込む。2スタック積み下ろして、1スタック積み上げ。
    TSF_peekcount=TSF_Forth_popdecimalize(TSF_thatstack_name)
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    TSF_tsv=TSF_Forth_peek(TSF_thename,TSF_peekcount)
    TSF_Forth_push(TSF_thatstack_name,TSF_tsv)
    return None

def TSF_Forth_pokethe():   #TSF_doc:[data,stack,pointer]スタックに上書き。3スタック積み下ろす。
    TSF_pokecount=TSF_Forth_popdecimalize(TSF_thatstack_name)
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    TSF_tsv=TSF_Forth_pop(TSF_thatstack_name)
    TSF_Forth_poke(TSF_thename,TSF_pokecount,TSF_tsv)
    return None

def TSF_Forth_delthis():   #TSF_doc:[]実行中スタックを削除。スタックも抜けてコールポインタを1つ減らす。
    del TSF_stacks[TSF_thisstack_name]
    return ""

def TSF_Forth_delthat():   #TSF_doc:[]積込先スタックを削除。
    del TSF_stacks[TSF_thatstack_name]
    return None

def TSF_Forth_calcbrackets(TSF_tsvBL,TSF_tsvBR):   #TSF_doc:括弧でスタックを連結する。
    TSF_tsvA=TSF_Forth_pop(TSF_thatstack_name)
    for TSF_stacksK,TSF_stacksV in TSF_stacks.items():
        TSF_calcK="".join([TSF_tsvBL,TSF_stacksK])
        if TSF_calcK in TSF_tsvA:
            for TSF_stackC,TSF_stackQ in enumerate(TSF_stacksV):
                TSF_calcK="".join([TSF_tsvBL,TSF_stacksK,str(TSF_stackC),TSF_tsvBR])
                if TSF_calcK in TSF_tsvA:
                    TSF_tsvA=TSF_tsvA.replace(TSF_calcK,TSF_stackQ)
    for TSF_stackC,TSF_stackQ in enumerate(TSF_stacks[TSF_thatstack_name]):
        TSF_calcK="".join([TSF_tsvBL,str(TSF_stackC),TSF_tsvBR])
        if TSF_calcK in TSF_tsvA:
            TSF_tsvA=TSF_tsvA.replace(TSF_calcK,TSF_Forth_pop(TSF_thatstack_name))
        else:
            break
    return TSF_tsvA

def TSF_Forth_calcFX():   #TSF_doc:[calc]スタック内容で分数電卓する。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_tsvQ=TSF_Forth_calcbrackets("[","]")
    TSF_tsvA=TSF_calc(TSF_tsvQ,None)
    TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return None

def TSF_Forth_calcFXQQ():   #TSF_doc:[calc]スタック内容で分数電卓する(暗記もする)。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_tsvQ=TSF_Forth_calcbrackets("[","]")
    TSF_tsvA=TSF_calc(TSF_tsvQ,True)
    TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return None

def TSF_Forth_calcDC():   #TSF_doc:[calc]スタック内容で分数電卓して結果を小数または整数で表示。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_tsvQ=TSF_Forth_calcbrackets("[","]")
    TSF_tsvA=TSF_calc_decimalizeDC(TSF_calc(TSF_tsvQ,None))
    TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return None

def TSF_Forth_calcDCQQ():   #TSF_doc:[calc]スタック内容で分数電卓して結果を小数または整数で表示(暗記もする)。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_tsvQ=TSF_Forth_calcbrackets("[","]")
    TSF_tsvA=TSF_calc_decimalizeDC(TSF_calc(TSF_tsvQ,True))
    TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return None

def TSF_Forth_calcKN():   #TSF_doc:[calc]スタック内容で分数電卓して結果を漢数字を混ぜてで表示。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_tsvQ=TSF_Forth_calcbrackets("[","]")
    TSF_tsvA=TSF_calc_decimalizeKN(TSF_calc(TSF_tsvQ,None))
    TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return None

def TSF_Forth_calcKNQQ():   #TSF_doc:[calc]スタック内容で分数電卓して結果を漢数字を混ぜてで表示(暗記もする)。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_tsvQ=TSF_Forth_calcbrackets("[","]")
    TSF_tsvA=TSF_calc_decimalizeKN(TSF_calc(TSF_tsvQ,True))
    TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return None

def TSF_Forth_calcPR():   #TSF_doc:[prec]有効桁数を変更する。桁数が変わると同じ式でも値が変わるので暗記(九九)も初期化する。
    TSF_calc_precision(TSF_Forth_popdecimalize(TSF_thatstack_name))
    return None

def TSF_Forth_calcRO():   #TSF_doc:[round]端数処理を変更する。端数が変わると同じ式でも値が変わるので暗記(九九)も初期化する。
    TSF_calc_rounding(TSF_Forth_popdecimalize(TSF_thatstack_name))
    return None

def TSF_Forth_brackets():   #TSF_doc:[…stackB,stackA,calc,brackets]これ自体は計算はせず、任意の括弧に囲まれたスタック番号をスタック内容に置換。bracketsとcalc自身とcalc内の該当括弧分スタック積み下ろし。
    TSF_tsvB=TSF_Forth_pop(TSF_thatstack_name)
    if len(TSF_tsvB) < 2: TSF_tsvB="[]"
    TSF_tsvBL,TSF_tsvBR=TSF_tsvB[0],TSF_tsvB[-1]
    TSF_tsvA=TSF_Forth_calcbrackets(TSF_tsvBL,TSF_tsvBR)
    TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return None

def TSF_Forth_join():   #TSF_doc:[…stackB,stackA,count]文字列に連結する。count自身とcount数値分スタック積み下ろし、連結した文字列を積み込み。
    TSF_joinloopI=TSF_Forth_popdecimalize(TSF_thatstack_name)
    TSF_joinlist=[]
    for TSF_joincount in range(TSF_joinloopI):
        TSF_joinlist.append(TSF_Forth_pop(TSF_thatstack_name))
    TSF_Forth_push(TSF_thatstack_name,"".join(reversed(TSF_joinlist)))
    return None

def TSF_Forth_joinC():   #TSF_doc:[…stackB,stackA,count,joint]文字列に連結する。jointとcount自身の2つ+count数値分スタック積み下ろし、連結した文字列を積み込み。
    TSF_joinloopC=TSF_Forth_pop(TSF_thatstack_name)
    TSF_joinloopI=TSF_Forth_popdecimalize(TSF_thatstack_name)
    TSF_joinlist=[]
    for TSF_joincount in range(TSF_joinloopI):
        TSF_joinlist.append(TSF_Forth_pop(TSF_thatstack_name))
    TSF_Forth_push(TSF_thatstack_name,TSF_joinloopC.join(reversed(TSF_joinlist)))
    return None

def TSF_Forth_split():   #TSF_doc:[…stackB,stackA,string,spliter]文字列を分割する。stringとspliter分スタック積み下ろし、分割された文字列分スタック積み込み。
    TSF_tsvP=TSF_Forth_pop(TSF_thatstack_name)
    TSF_tsvQ=TSF_Forth_pop(TSF_thatstack_name)
    TSF_tsvK=TSF_tsvQ.split(TSF_tsvP)
    for TSF_tsvA in TSF_tsvK:
        TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return None

def TSF_Forth_chars():   #TSF_doc:[…stackB,stackA,string]文字列を一文字ずつに分割する。stringスタック積み下ろし、分割された文字分スタック積み込み。
    TSF_tsvQ=TSF_Forth_pop(TSF_thatstack_name)
    for TSF_tsvA in TSF_tsvQ:
        TSF_Forth_push(TSF_thatstack_name,TSF_tsvA)
    return None

def TSF_Forth_loadtext(TSF_stack,TSF_path):    #TSF_doc:テキストファイルを読み込んでTSF_stacksの一スタック扱いにする。
    global TSF_stacks,TSF_styles
    TSF_text=TSF_io_loadtext(TSF_path)
    TSF_text=TSF_txt_ESCencode(TSF_text)
    TSF_Forth_settext(TSF_stack,TSF_text)
    TSF_styles[TSF_stack]="N"
    return TSF_text

def TSF_Forth_read():   #TSF_doc:[filename]ファイルをスタックに積む。1スタック積み下ろし。
    TSF_path=TSF_Forth_pop(TSF_thatstack_name)
    TSF_Forth_loadtext(TSF_path,TSF_path)
    return None

def TSF_Forth_merge(TSF_stack,TSF_ESCstack=[]):    #TSF_doc:「TSF_Forth_settext()」で読み込んだテキストをスタックに変換する。
    global TSF_stacks,TSF_styles
    TSF_stackthat=TSF_Forth_1ststack()
    TSF_styles[TSF_stackthat]="T"
    for TSF_stackV in TSF_stacks[TSF_stack]:
        if len(TSF_stackV) == 0: continue;
        if TSF_stackV.startswith("#"): continue;
        TSF_stackV=TSF_txt_ESCdecode(TSF_stackV)
        if not TSF_stackV.startswith('\t'):
            TSF_stackL=TSF_stackV.lstrip('\t').split('\t')
            if not TSF_stackL[0] in TSF_ESCstack:
                TSF_stackthat=TSF_stackL[0]
                TSF_stacks[TSF_stackthat]=[]
                TSF_styles[TSF_stackthat]="O" if len(TSF_stackL) >= 2 else ""
        if not TSF_stackthat in TSF_ESCstack:
            TSF_stackL=TSF_stackV.split('\t')[1:]
            TSF_stacks[TSF_stackthat].extend(TSF_stackL)
            if TSF_styles[TSF_stackthat] != "O":
                TSF_styles[TSF_stackthat]="T" if len(TSF_stackL) >= 2 else "N"

def TSF_Forth_mergethe():   #TSF_doc:[stack,filename]ファイルをスタックに積む。1スタック積み下ろし。
    TSF_Forth_merge(TSF_Forth_pop(TSF_thatstack_name),TSF_ESCstack=[TSF_Forth_1ststack()])
    return None

def TSF_Forth_publishthe():   #TSF_doc:[stack,filename]スタックをテキスト化してスタックに読み込む。2スタック積み下ろし。
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    TSF_publish_log=TSF_Forth_view(TSF_thename,False,"")
    TSF_publish_log=TSF_txt_ESCencode(TSF_publish_log)
    TSF_Forth_settext(TSF_Forth_pop(TSF_thatstack_name),TSF_publish_log,TSF_style="N")
    return None

def TSF_Forth_publishthis():   #TSF_doc:[stack]実行中スタックをテキスト化してスタックに読み込む。1スタック積み下ろし。
    TSF_publish_log=TSF_Forth_view(TSF_thisstack_name,False,"")
    TSF_publish_log=TSF_txt_ESCencode(TSF_publish_log)
    TSF_Forth_settext(TSF_Forth_pop(TSF_thatstack_name),TSF_publish_log,TSF_style="N")
    return None

def TSF_Forth_publishthat():   #TSF_doc:[stack]積込先スタックをテキスト化してスタックに読み込む。1スタック積み下ろし。
    TSF_publish_log=TSF_Forth_view(TSF_thatstack_name,False,"")
    TSF_publish_log=TSF_txt_ESCencode(TSF_publish_log)
    TSF_Forth_settext(TSF_Forth_pop(TSF_thatstack_name),TSF_publish_log,TSF_style="N")
    return None

def TSF_Forth_remove():
    return None

def TSF_Forth_savethe():
    TSF_thename=TSF_Forth_pop(TSF_thatstack_name)
    TSF_path=TSF_Forth_pop(TSF_thatstack_name)
    TSF_text=TSF_txt_ESCdecode("\n".join(TSF_stacks[TSF_thename])) if TSF_thename in TSF_stacks else ""
    TSF_io_savetext(TSF_path,TSF_text=TSF_text)
    return None

def TSF_Forth_writethe():
    return None


def TSF_Forth_run(TSF_this=None,TSF_that=None):    #TSF_doc:TSFを実行していく。
    global TSF_thisstack_name,TSF_thatstack_name,TSF_thisstack_count
    TSF_thisstack_name=TSF_this if TSF_this != None else TSF_Forth_1ststack()
    TSF_thatstack_name=TSF_that if TSF_that != None else TSF_Forth_1ststack()
    TSF_thisstack_count=0
    TSF_nextstack=None
    while True:
        while TSF_thisstack_count < len(TSF_stacks[TSF_thisstack_name]):
            if TSF_stacks[TSF_thisstack_name][TSF_thisstack_count] in TSF_words:
                TSF_nextstack=TSF_words[TSF_stacks[TSF_thisstack_name][TSF_thisstack_count]]()
            else:
                TSF_Forth_push(TSF_thatstack_name,TSF_stacks[TSF_thisstack_name][TSF_thisstack_count])
            TSF_thisstack_count += 1
            if TSF_nextstack != None:
                if TSF_nextstack == "":
                    if len(TSF_callptrs) > 0:
                        TSF_thisstack_name,TSF_thisstack_count=TSF_callptrs.popitem(True)
                    else:
                        break
                elif TSF_nextstack in TSF_stacks:
                    if TSF_nextstack in TSF_callptrs:
                        while TSF_nextstack in TSF_callptrs:
                           TSF_callptrs.popitem(True)
                    TSF_callptrs[TSF_thisstack_name]=TSF_thisstack_count
                    TSF_thisstack_name=TSF_nextstack; TSF_nextstack=None
                    TSF_thisstack_count=0
                else:
                    break
        if len(TSF_callptrs) > 0:
            TSF_thisstack_name,TSF_thisstack_count=TSF_callptrs.popitem(True); TSF_nextstack=None
        else:
            break


def TSF_Forth_debug():    #TSF_doc:「TSF/TSF_Forth.py」単体テスト風デバッグ関数。
    TSF_Forth_Init(TSF_argvs)
    TSF_debug_log=""
    TSF_debug_readmeL="../README.md"
    TSF_debug_readmeS="/debug/README.txt"
    TSF_Forth_loadtext(TSF_debug_readmeL,TSF_debug_readmeL)
    TSF_debug_log=TSF_Forth_viewprintlog(TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/TSF_Forth_debug.txt"
    TSF_debug_log=TSF_Forth_debug()
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
