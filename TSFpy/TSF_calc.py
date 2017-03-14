#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import math
import decimal
import fractions
import re
from collections import OrderedDict
from TSF_Forth import *

def TSF_calc_Initwords(TSF_words):    #TSF_doc:電卓関連のワードを追加する(TSFAPI)。
    TSF_words["#TSF_brackets"]=TSF_calc_brackets; TSF_words["#数式に連結"]=TSF_calc_brackets
    TSF_words["#TSF_calcFX"]=TSF_calc_calcFX; TSF_words["#分数計算"]=TSF_calc_calcFX
    TSF_words["#TSF_calcFXQQ"]=TSF_calc_calcFXQQ; TSF_words["#分数九九"]=TSF_calc_calcFXQQ
    TSF_words["#TSF_calcDC"]=TSF_calc_calcDC; TSF_words["#小数計算"]=TSF_calc_calcDC
    TSF_words["#TSF_calcDCQQ"]=TSF_calc_calcDCQQ; TSF_words["#小数九九"]=TSF_calc_calcDCQQ
    TSF_words["#TSF_calcKN"]=TSF_calc_calcKN; TSF_words["#単位計算"]=TSF_calc_calcKN
    TSF_words["#TSF_calcKNQQ"]=TSF_calc_calcKNQQ; TSF_words["#単位九九"]=TSF_calc_calcKNQQ
    TSF_words["#TSF_calcPR"]=TSF_calc_calcPR; TSF_words["#有効桁数"]=TSF_calc_calcPR
    TSF_words["#TSF_calcRO"]=TSF_calc_calcRO; TSF_words["#端数処理"]=TSF_calc_calcRO
    return TSF_words

def TSF_calc_calcbrackets(TSF_tsvBL,TSF_tsvBR):   #TSF_doc:括弧でスタックを連結する。
    TSF_tsvA=TSF_Forth_popthat()
    for TSF_stacksK,TSF_stacksV in TSF_Forth_stacksitems():
        TSF_calcK="".join([TSF_tsvBL,TSF_stacksK])
        if TSF_calcK in TSF_tsvA:
            for TSF_stackC,TSF_stackQ in enumerate(TSF_stacksV):
                TSF_calcK="".join([TSF_tsvBL,TSF_stacksK,str(TSF_stackC),TSF_tsvBR])
                if TSF_calcK in TSF_tsvA:
                    TSF_tsvA=TSF_tsvA.replace(TSF_calcK,TSF_stackQ)
    for TSF_stackC in range(TSF_Forth_stackslen()):
        TSF_calcK="".join([TSF_tsvBL,str(TSF_stackC),TSF_tsvBR])
        if TSF_calcK in TSF_tsvA:
            TSF_tsvA=TSF_tsvA.replace(TSF_calcK,TSF_Forth_popthat())
        else:
            break
    return TSF_tsvA

def TSF_calc_brackets():   #TSF_doc:[stackN…stackB,stackA,count,calc,brackets]これ自体は計算はせず、任意の括弧に囲まれたスタック番号をスタック内容に置換。bracketsとcalc自身とcalc内の該当括弧分スタック積み下ろし。
    TSF_tsvB=TSF_Forth_popthat()
    if len(TSF_tsvB) < 2: TSF_tsvB="[]"
    TSF_tsvBL,TSF_tsvBR=TSF_tsvB[0],TSF_tsvB[-1]
    TSF_Forth_pushthat(TSF_calc_calcbrackets(TSF_tsvBL,TSF_tsvBR))
    return None

def TSF_calc_calcFX():   #TSF_doc:[calc]分数電卓する。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_Forth_pushthat(TSF_calc(TSF_calc_calcbrackets("[","]"),None))
    return None

def TSF_calc_calcFXQQ():   #TSF_doc:[calc]分数電卓する(暗記もする)。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_Forth_pushthat(TSF_calc(TSF_calc_calcbrackets("[","]"),True))
    return None

def TSF_calc_calcDC():   #TSF_doc:[calc]分数電卓して結果を小数または整数で表示。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_Forth_pushthat(TSF_calc_decimalizeDC(TSF_calc(TSF_calc_calcbrackets("[","]"),None)))
    return None

def TSF_calc_calcDCQQ():   #TSF_doc:[calc]分数電卓して結果を小数または整数で表示(暗記もする)。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_Forth_pushthat(TSF_calc_decimalizeDC(TSF_calc(TSF_calc_calcbrackets("[","]"),True)))
    return None

def TSF_calc_calcKN():   #TSF_doc:[calc]分数電卓して結果を漢数字を混ぜてで表示。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_Forth_pushthat(TSF_calc_decimalizeKN(TSF_calc(TSF_calc_calcbrackets("[","]"),None)))
    return None

def TSF_calc_calcKNQQ():   #TSF_doc:[calc]分数電卓して結果を漢数字を混ぜてで表示(暗記もする)。calcと連結分スタック積み下ろし、1スタック積み上げ。
    TSF_Forth_pushthat(TSF_calc_decimalizeKN(TSF_calc(TSF_calc_calcbrackets("[","]"),True)))
    return None

def TSF_calc_calcPR():   #TSF_doc:[prec]有効桁数を変更する。桁数が変わると同じ式でも値が変わるので暗記(九九)も初期化する。
    TSF_calc_precision(TSF_Forth_popintthe(TSF_Forth_stackthat()))
    return None

def TSF_calc_calcRO():   #TSF_doc:[round]端数処理を変更する。端数が変わると同じ式でも値が変わるので暗記(九九)も初期化する。
    TSF_calc_rounding(TSF_Forth_popintthe(TSF_Forth_stackthat()))
    return None


TSF_calc_opewide="f1234567890.pm!|$ELRSsCcTtyYen+-*/\\#%(MPFZzOoUuN~k)&GglAa^><" \
                "銭十百千万億兆京垓𥝱穣溝澗正載極恒阿那思量" \
                "１２３４５６７８９０｜．" "絶負分点円圓" "一二三四五六七八九〇" "壱弐参肆伍陸漆捌玖零" \
                "＋－×÷／＼＃％" "加減乗除比税" "足引掛割" "和差積商" "陌阡萬仙秭" \
                "（）()｛｝{}［］[]「」｢｣『』Σ但※列Π囲～〜値とを約倍" \
                "乗常進対√根π周θｅ底∞無桁"
TSF_calc_opehalf="f1234567890.pm!|$ELRSsCcTtyYen+-*/\\#%(MPFZzOoUuN~k)&GglAa^><" \
                "銭十百千万億兆京垓𥝱穣溝澗正載極恒阿那思量" \
                "1234567890|." "!m$..." "1234567890" "1234567890" \
                "+-*//\\#%" "+-*/%%" "+-*/" "+-*/" "百千万銭𥝱" \
                "()()()()()()()()()MMMMP~~~k&&Gg" \
                "^LlERRyyYeennf"
TSF_calc_operator=OrderedDict(zip(list(TSF_calc_opewide),list(TSF_calc_opehalf)))
TSF_calc_opelong=["恒河沙","阿僧祇","那由他","不可思議","無量大数","無限","分の","円周率","2π","２π","ネイピア数","プラス","マイナス","氷点下","小数点", \
                "最大公約数","最小公倍数","公約数","公倍数","とんで","とばして","とぶことの","平方根","常用対数","進対数","自然対数","絶対値", \
                "sin","cos","tan"]
TSF_calc_opelshort=["恒","阿","那","思","量","∞","$","π","θ","θ","ｅ","p","m","点","点","絶", \
                "約","倍","約","倍","","","","根","常","進","対", \
                "S","C","T"]
TSF_calc_opeword=dict(zip(TSF_calc_opelong,TSF_calc_opelshort))
TSF_calc_opemarkC=["*+","*-","/+","/-","#+","#-","|+","|-","++","+-","-+","--",
                "0k", "1k", "2k", "3k", "4k", "5k", "6k", "7k", "8k", "9k", ".k",
                "0(", "1(", "2(", "3(", "4(", "5(", "6(", "7(", "8(", "9(", ".(",
                ")0", ")1", ")2", ")3", ")4", ")5", ")6", ")7", ")8", ")9", ").",
                ")(", "|(", "+$"]
TSF_calc_opemarkP=["*p","*m","/p","/m","#p","#m","|p","|m","+p","+m","-p","-m",
                "0*k","1*k","2*k","3*k","4*k","5*k","6*k","7*k","8*k","9*k",".*k",
                "0*(","1*(","2*(","3*(","4*(","5*(","6*(","7*(","8*(","9*(",".*(",
                ")*0",")*1",")*2",")*3",")4*",")*5",")*6",")*7",")*8",")*9",")*.",
                ")*(", "/(", "$"]
TSF_calc_opemark=dict(zip(TSF_calc_opemarkC,TSF_calc_opemarkP))
TSF_calc_okusenman="万億兆京垓𥝱穣溝澗正載極恒阿那思量"
TSF_calc_okusenzero=['1'+'0'*((o+1)*4) for o in range(len(TSF_calc_okusenman))]
TSF_calc_okusendic=dict(zip(list(TSF_calc_okusenman),TSF_calc_okusenzero))
TSF_calc_precisionMAX=72; decimal.getcontext().prec=TSF_calc_precisionMAX
TSF_calc_precisionPI=TSF_calc_precisionMAX-4;
TSF_calc_precisionROUND=decimal.ROUND_DOWN; decimal.getcontext().rounding=TSF_calc_precisionROUND
TSF_calc_PI="31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
TSF_calc_PI2="62831853071795864769252867665590057683943387987502116419498891846156328125724179972560696506842341359"
TSF_calc_E="27182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def TSF_calc_precision(TSF_prec):    #TSF_doc:電卓の有効桁数を変更する。初期値は72桁(千無量大数)。円周率とネイピア数も4桁控えて再計算する。
    global TSF_calc_precisionMAX,TSF_calc_precisionPI,TSF_calcQQmemory
    TSF_calc_precisionMAX=min(max(TSF_prec,5),1000); TSF_calc_precisionPI=TSF_calc_precisionMAX-4
    decimal.getcontext().prec=TSF_calc_precisionMAX*2
    TSF_PI_A,TSF_PI_B,TSF_PI_T,TSF_PI_C=decimal.Decimal(1),decimal.Decimal(1)/decimal.Decimal(2).sqrt(),decimal.Decimal(1)/decimal.Decimal(4),decimal.Decimal(1)
    for TSF_PI_X in range(int(math.ceil(math.log(TSF_calc_precisionPI,2)))):
       TSF_PI_AB=decimal.Decimal(TSF_PI_A+TSF_PI_B)/decimal.Decimal(2)
       TSF_PI_B=decimal.getcontext().sqrt(TSF_PI_A*TSF_PI_B)
       TSF_PI_T-=decimal.Decimal(TSF_PI_C)*decimal.getcontext().power(TSF_PI_A-TSF_PI_AB,2)
       TSF_PI_A=TSF_PI_AB; TSF_PI_C*=2
    TSF_PI_P2=decimal.getcontext().power(TSF_PI_A+TSF_PI_B,2)/TSF_PI_T/decimal.Decimal(2)
    TSF_calc_PI2=str(TSF_PI_P2).replace('.',''); TSF_calc_PI=str(TSF_PI_P2/decimal.Decimal(2)).replace('.','')
    TSF_PI_E,TSF_PI_K=decimal.Decimal(1),decimal.Decimal(1)
    for TSF_PI_X in range(TSF_calc_precisionPI):
        TSF_PI_K*=decimal.Decimal(TSF_PI_X+1)
        TSF_PI_E+=decimal.Decimal(1)/TSF_PI_K
    TSF_calc_E=str(TSF_PI_E).replace('.','')
    decimal.getcontext().prec=TSF_calc_precisionMAX
    TSF_calcQQmemory={}

TSF_calc_roundopt={
    "ROUND_DOWN":decimal.ROUND_DOWN,  "ゼロ方向に丸める":decimal.ROUND_DOWN,  "ゼロ方向に切り捨てる":decimal.ROUND_DOWN,
    "ROUND_UP":decimal.ROUND_UP,  "ゼロから遠ざかる方に丸める":decimal.ROUND_UP,   "ゼロから遠ざかる様に切り上げる":decimal.ROUND_UP,
    "ROUND_FLOOR":decimal.ROUND_FLOOR,  "マイナス無限方向に丸める":decimal.ROUND_FLOOR,  "マイナス無限方向に切り捨てる":decimal.ROUND_FLOOR,
    "ROUND_CEILING":decimal.ROUND_DOWN,  "プラス無限方向に丸める":decimal.ROUND_DOWN,  "プラス無限方向に切り上げる":decimal.ROUND_DOWN,
    "ROUND_HALF_UP":decimal.ROUND_HALF_UP,  "四捨五入する":decimal.ROUND_HALF_UP,
    "ROUND_HALF_DOWN":decimal.ROUND_HALF_DOWN,  "五捨五超入する":decimal.ROUND_HALF_DOWN,  "五捨六入する":decimal.ROUND_HALF_DOWN,
    "ROUND_HALF_EVEN":decimal.ROUND_HALF_EVEN,  "偶捨奇入する":decimal.ROUND_HALF_EVEN,  "銀行丸めする":decimal.ROUND_HALF_EVEN,  "ISO丸めする":decimal.ROUND_HALF_EVEN,
    "ROUND_05UP":decimal.ROUND_05UP,  "ゼロ方向に切り捨てた結果末尾桁が0か5になる場合はゼロから遠ざかる様に切り上げる":decimal.ROUND_05UP,
}
def TSF_calc_rounding(TSF_round):    #TSF_doc:電卓の端数処理を指定。初期値はROUND_DOWN(ゼロ方向に丸める)
    global TSF_calc_precisionROUND,TSF_calcQQmemory
    TSF_calc_precisionROUND=TSF_calc_roundopt.get(TSF_round,decimal.ROUND_DOWN)
    decimal.getcontext().prec=TSF_calc_precisionROUND
    TSF_calcQQmemory={}

def TSF_calc_bracketsbalance(TSF_calcQ):    #TSF_doc:括弧のバランスを整える。ついでに無効な演算子を除去したり円周率億千万など計算の下準備。
    TSF_calcA=""; TSF_calcbracketLR,TSF_calcbracketCAP=0,0
    for TSF_opewordK,TSF_opewordV in TSF_calc_opeword.items():
        TSF_calcQ=TSF_calcQ.replace(TSF_opewordK,TSF_opewordV)
    for TSF_calcbracketQ in TSF_calcQ:
        TSF_calcA+=TSF_calc_operator.get(TSF_calcbracketQ,'')
        if TSF_calcbracketQ == '(':
            TSF_calcbracketLR+=1
        if TSF_calcbracketQ == ')':
            TSF_calcbracketLR-=1
            if TSF_calcbracketLR<TSF_calcbracketCAP:
                TSF_calcbracketCAP=TSF_calcbracketLR
    if TSF_calcbracketLR > 0:
        TSF_calcA=TSF_calcA+')'*abs(TSF_calcbracketLR)
    if TSF_calcbracketLR < 0:
        TSF_calcA='('*abs(TSF_calcbracketLR)+TSF_calcA
    TSF_calcA='('*abs(TSF_calcbracketCAP)+TSF_calcA+')'*abs(TSF_calcbracketCAP)
    TSF_calcA=re.sub(re.compile("([0-9千百十]+?)銭"),"+(\\1)/100",TSF_calcA)
    for TSF_okusenK,TSF_okusenV in TSF_calc_okusendic.items():
        TSF_calcA=re.sub(re.compile("".join(["([0-9千百十]+?)",TSF_okusenK])),"".join(["(\\1)*",TSF_okusenV,"+"]),TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9]+?)千"),"(\\1*1000)+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9]+?)百"),"(\\1*100)+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9]+?)十"),"(\\1*10)+",TSF_calcA)
    TSF_calcA=TSF_calcA.replace('銭',"1|100+")
    TSF_calcA=TSF_calcA.replace('十',"10+")
    TSF_calcA=TSF_calcA.replace('百',"100+")
    TSF_calcA=TSF_calcA.replace('千',"1000+")
    for TSF_okusenK,TSF_okusenV in TSF_calc_okusendic.items():
        TSF_calcA=TSF_calcA.replace(TSF_okusenK,"".join([TSF_okusenV,"+"]))
    TSF_calcA=TSF_calcA.replace('y',"".join([TSF_calc_PI[:TSF_calc_precisionPI],"|1",'0'*(TSF_calc_precisionPI-1)]))
    TSF_calcA=TSF_calcA.replace('Y',"".join([TSF_calc_PI2[:TSF_calc_precisionPI],"|1",'0'*(TSF_calc_precisionPI-1)]))
    TSF_calcA=TSF_calcA.replace('e',"".join([TSF_calc_E[:TSF_calc_precisionPI],"|1",'0'*(TSF_calc_precisionPI-1)]))
    TSF_calcA=TSF_calcA.replace('f',str(TSF_calc_precisionMAX)).replace('n','(n|0)')
#    TSF_io_printlog("TSF_calc_bracketsbalance:{0}".format(TSF_calcA))
    for TSF_calc_opecase in TSF_calc_opemark:
        if TSF_calc_opecase in TSF_calcA:
            TSF_calcA=TSF_calcA.replace(TSF_calc_opecase,TSF_calc_opemark[TSF_calc_opecase])
    return TSF_calcA

def TSF_calc(TSF_calcQ,TSF_calcQQ=None):    #TSF_doc:分数電卓のmain。括弧の内側を検索(正規表現)。
    global TSF_calcQQmemory
    TSF_calcA="n|0"
    TSF_calcA=TSF_calc_bracketsbalance(TSF_calcQ);
    TSF_calc_bracketreg=re.compile("[(](?<=[(])[^()]*(?=[)])[)]")
    while "(" in TSF_calcA:
        for TSF_calcK in re.findall(TSF_calc_bracketreg,TSF_calcA):
            TSF_calcA=TSF_calcA.replace(TSF_calcK,TSF_calc_referential(TSF_calcK,TSF_calcQQ))
    TSF_calcA=TSF_calcA.replace(TSF_calcA,TSF_calc_referential(TSF_calcA,TSF_calcQQ))
    return TSF_calcA

TSF_calcQQmemory={}
def TSF_calc_referential(TSF_calcQ,TSF_calcQQ=None):    #TSF_doc:分数電卓の和集合積集合およびゼロ比較演算子系。
    global TSF_calcQQmemory
    TSF_calcQ=TSF_calcQ.lstrip("(").rstrip(")")
    if TSF_calcQQ != None:
        if TSF_calcQQ == True:
            TSF_calcA=TSF_calcQ.replace(TSF_calcQ,TSF_calcQQmemory.get(TSF_calcQ,TSF_calc_function(TSF_calcQ))); TSF_calcQQmemory[TSF_calcQ]=TSF_calcA
        else:
            TSF_calcA=TSF_calcQ.replace(TSF_calcQ,TSF_calc_function(TSF_calcQ))
    else:
        TSF_calcA=TSF_calcQ.replace(TSF_calcQ,TSF_calcQQmemory.get(TSF_calcQ,TSF_calc_function(TSF_calcQ)))
    return TSF_calcA

def TSF_calc_Fermatmodulo(TSF_calcSeq,TSF_pow,TSF_modulo):    #冪乗モジュロ。素数のフェルマーテストなどで使用。
    try:
        TSF_calcA="0"
        TSF_calcSeq=decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_calcSeq))).to_integral_value()
        TSF_pow=decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_pow))).to_integral_value()
        TSF_modulo=decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_modulo))).to_integral_value()
        TSF_calcA=str(decimal.getcontext().power(TSF_calcSeq,TSF_pow,TSF_modulo))
    except decimal.InvalidOperation:
        TSF_calcA="n|0"
    return TSF_calcA

TSF_calc_NOZUs=OrderedDict([
    ('N',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:TSF_LimFirst if TSF_calc_addition(TSF_calcSeq.replace('k',"0")) == "n|0" else TSF_LimRest)),
    ('Z',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:TSF_LimFirst if decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_calcSeq.replace('k',"0"))).replace("n|0","NaN")) == 0 else TSF_LimRest)),
    ('z',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:TSF_LimFirst if decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_calcSeq.replace('k',"0"))).replace("n|0","NaN")) != 0 else TSF_LimRest)),
    ('O',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:TSF_LimFirst if decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_calcSeq.replace('k',"0"))).replace("n|0","-Infinity")) >= 0 else TSF_LimRest)),
    ('o',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:TSF_LimFirst if decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_calcSeq.replace('k',"0"))).replace("n|0","-Infinity")) > 0 else TSF_LimRest)),
    ('U',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:TSF_LimFirst if decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_calcSeq.replace('k',"0"))).replace("n|0","+Infinity")) <= 0 else TSF_LimRest)),
    ('u',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:TSF_LimFirst if decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_calcSeq.replace('k',"0"))).replace("n|0","+Infinity")) < 0 else TSF_LimRest)),
    ('M',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:"+".join([TSF_calc_addition(TSF_calcSeq.replace('k',str(TSF_LimK))) for TSF_LimK in TSF_calc_function_limit(TSF_LimFirst,TSF_LimRest)]))),
    ('P',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:"*".join([TSF_calc_addition(TSF_calcSeq.replace('k',str(TSF_LimK))) for TSF_LimK in TSF_calc_function_limit(TSF_LimFirst,TSF_LimRest)]))),
    ('F',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:TSF_calc_Fermatmodulo(TSF_calcSeq,TSF_LimFirst,TSF_LimRest) )),
    ('$',(lambda TSF_calcSeq,TSF_LimFirst,TSF_LimRest:"/".join([str(TSF_calc_addition(TSF_LimFirst.replace('k',"0"))),str(TSF_calc_addition(TSF_calcSeq.replace('k',"0")))]))),
])

def TSF_calc_function_limit(TSF_LimFirst,TSF_LimRest):    #TSF_doc:和集合積集合のrange作成。
    try:
        TSF_LimStart,TSF_LimGoal=decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_LimFirst))).to_integral_value(),decimal.Decimal(TSF_calc_decimalizeDC(TSF_calc_addition(TSF_LimRest))).to_integral_value()
        if TSF_LimStart <= TSF_LimGoal:
            TSF_limstep=1; TSF_LimGoal+=1
        else:
            TSF_limstep=-1; TSF_LimGoal-=1
        return range(TSF_LimStart,TSF_LimGoal,TSF_limstep)
    except decimal.InvalidOperation:
        TSF_LimStart,TSF_LimGoal,TSF_limstep=None,None,None
        return range(0)

def TSF_calc_function(TSF_calcQ):    #TSF_doc:分数電卓の和集合積集合およびゼロ比較演算子系。
    TSF_calcOfind=-1; TSF_calc_NOZUin=""
    for TSF_calc_NOZU in TSF_calc_NOZUs.keys():
        if TSF_calc_NOZU in TSF_calcQ:
            TSF_calc_NOZUin+=TSF_calc_NOZU
            TSF_calcOfind=TSF_calcQ.find(TSF_calc_NOZUin)
    if TSF_calcOfind >= 0:
        TSF_calcQ='\t'.join([TSF_calcQ[:TSF_calcOfind],TSF_calcQ[TSF_calcOfind+1:]])
        for TSF_calc_NOZU in TSF_calc_NOZUin:
            TSF_calcQ=TSF_calcQ.replace(TSF_calc_NOZU,'')
        TSF_calcSeq,TSF_calcLim=TSF_calcQ.split('\t')
        if not '~' in TSF_calcLim:
            if TSF_calc_NOZUin in "MP":
                TSF_calcLim="~".join(["1",TSF_calcLim])
            elif TSF_calc_NOZUin in "$":
                TSF_calcLim=TSF_calcLim
            else:
                TSF_calcLim="~".join([TSF_calcLim,"0"])
        if '~' in TSF_calcLim:
            TSF_LimFirst,TSF_LimRest=TSF_calcLim.split('~')[0],TSF_calcLim.split('~')[-1]
        else:
            TSF_LimFirst,TSF_LimRest=TSF_calcLim,TSF_calcLim
        TSF_calcQ=TSF_calc_NOZUs[TSF_calc_NOZUin[-1]](TSF_calcSeq,TSF_LimFirst,TSF_LimRest)
    TSF_calcA=TSF_calc_addition(TSF_calcQ)
    return TSF_calcA
    
def TSF_calc_addition(TSF_calcQ):    #TSF_doc:分数電卓の足し算引き算・消費税計算等。
    TSF_calcLN,TSF_calcLD=decimal.Decimal(0),decimal.Decimal(1)
    TSF_calcQ=TSF_calcQ.replace('+','\t+').replace('-','\t-')
    TSF_calcQsplits=TSF_calcQ.strip('\t').split('\t')
    for TSF_calcQmulti in TSF_calcQsplits:
        TSF_calcO=TSF_calcQmulti[0] if len(TSF_calcQmulti)>0 else '+'
        TSF_calcO=TSF_calcO if not '%' in TSF_calcQmulti else '%'
        TSF_calcR=TSF_calc_multiplication(TSF_calcQmulti.replace('%',''))
        TSF_calcRN,TSF_calcRD=TSF_calcR.split('|')
        if float(TSF_calcRD) == 0.0:
            TSF_calcA="n|0"
            break
        if TSF_calcO == '%':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(100)+TSF_calcLN*decimal.Decimal(TSF_calcRN)*TSF_calcLD
            TSF_calcLD=TSF_calcLD*decimal.Decimal(100)
        else:  # TSF_calcO == '+' or TSF_calcO == '-':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRD)+decimal.Decimal(TSF_calcRN)*TSF_calcLD
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        try:
            TSF_GCD=fractions.gcd(TSF_calcLN,TSF_calcLD)
            TSF_calcLN=TSF_calcLN//TSF_GCD
            TSF_calcLD=TSF_calcLD//TSF_GCD
            if TSF_calcLD < 0: TSF_calcLN,TSF_calcLD=-TSF_calcLN,-TSF_calcLD
            TSF_calcA="|".join([str(TSF_calcLN),str(TSF_calcLD)])
        except decimal.InvalidOperation:
            TSF_calcA="n|0"
    if TSF_calcA != "0|1" and TSF_calcA != "n|0":
        TSF_calcA=TSF_calcA.replace('-','m') if TSF_calcA.startswith("-") else "".join(["p",str(TSF_calcA)])
    return TSF_calcA

def TSF_calc_multiplication(TSF_calcQ):    #TSF_doc:分数電卓の掛け算割り算等。公倍数公約数、最大値最小値も扱う。
    TSF_calcLN,TSF_calcLD=decimal.Decimal(1),decimal.Decimal(1)
    TSF_calcQ=TSF_calcQ.replace('*',"\t*").replace('/',"\t/").replace('\\',"\t\\").replace('#',"\t#").replace('&',"\t&")
    TSF_calcQ=TSF_calcQ.replace('G',"G\t").replace('g',"g\t").replace('^',"^\t").replace('l',"l\t").replace('A',"A\t").replace('a',"a\t").replace('>',">\t").replace('<',"<\t")
    TSF_calcQsplits=TSF_calcQ.replace("\t\t",'\t').strip('\t').split('\t')
    for TSF_calcQmulti in TSF_calcQsplits:
        TSF_calcO=TSF_calcQmulti[0] if len(TSF_calcQmulti)>0 else '*'
        TSF_calcO=TSF_calcO if not 'G' in TSF_calcQmulti else 'G'
        TSF_calcO=TSF_calcO if not 'g' in TSF_calcQmulti else 'g'
        TSF_calcO=TSF_calcO if not '^' in TSF_calcQmulti else '^'
        TSF_calcO=TSF_calcO if not 'l' in TSF_calcQmulti else 'l'
        TSF_calcO=TSF_calcO if not 'A' in TSF_calcQmulti else 'A'
        TSF_calcO=TSF_calcO if not 'a' in TSF_calcQmulti else 'a'
        TSF_calcO=TSF_calcO if not '>' in TSF_calcQmulti else '>'
        TSF_calcO=TSF_calcO if not '<' in TSF_calcQmulti else '<'
        TSF_calcR=TSF_calc_fractalize(TSF_calcQmulti.lstrip('*/\\#').rstrip('Gg^lAa><').replace('&',''))
        TSF_calcRN,TSF_calcRD=TSF_calcR.split('|')
        if decimal.Decimal(TSF_calcRD) == 0:
            TSF_calcA="n|0"
            break
        if TSF_calcO == '/':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRN)
            if TSF_calcLD < 0: TSF_calcLN,TSF_calcLD=-TSF_calcLN,-TSF_calcLD
        elif TSF_calcO == '\\':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRN)
            TSF_calcLN,TSF_calcLD=TSF_calcLN//TSF_calcLD,1
            if TSF_calcLD < 0: TSF_calcLN,TSF_calcLD=-TSF_calcLN,-TSF_calcLD
        elif TSF_calcO == '#':
            if decimal.Decimal(TSF_calcRN) == 0:
                TSF_calcLD=0
                break
#            TSF_calcLN=(TSF_calcLN*decimal.Decimal(TSF_calcRD))%(decimal.Decimal(TSF_calcRN)*TSF_calcLD)
            TSF_calcLND=decimal.Decimal(TSF_calcLN)*decimal.Decimal(TSF_calcRD)
            TSF_calcRND=decimal.Decimal(TSF_calcRN)*decimal.Decimal(TSF_calcLD)
            TSF_calcLN=decimal.getcontext().abs(TSF_calcLND%TSF_calcRND)
            if TSF_calcRND < 0:
                TSF_calcLN=decimal.getcontext().abs(TSF_calcRND)-TSF_calcLN
            TSF_calcLN=TSF_calcLN.copy_sign(TSF_calcLND)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
            if TSF_calcLD < 0: TSF_calcLN,TSF_calcLD=-TSF_calcLN,-TSF_calcLD
        elif TSF_calcO == 'G':
            TSF_calcLN=fractions.gcd(TSF_calcLN*decimal.Decimal(TSF_calcRD),decimal.Decimal(TSF_calcRN)*TSF_calcLD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        elif TSF_calcO == 'g':
            TSF_calcLN=TSF_calc_LCM(TSF_calcLN*decimal.Decimal(TSF_calcRD),decimal.Decimal(TSF_calcRN)*TSF_calcLD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        elif TSF_calcO == '^':
            try:
                TSF_calcRND=decimal.Decimal(TSF_calcRN)/decimal.Decimal(TSF_calcRD)
                TSF_calcRND="|".join([str(decimal.getcontext().power(TSF_calcLN,TSF_calcRND)),str(decimal.getcontext().power(TSF_calcLD,TSF_calcRND))])
                TSF_calcLND=TSF_calc_fractalize(TSF_calcRND)
                TSF_calcRN,TSF_calcRD=TSF_calcLND.replace('m','-').replace('p','').split('|')
                TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcRN),decimal.Decimal(TSF_calcRD)
            except decimal.InvalidOperation:
                TSF_calcA="n|0"
                break
        elif TSF_calcO == 'l':
            TSF_calcA=""
            if TSF_calcLD == 1 and decimal.Decimal(TSF_calcRD) == 1:
                TSF_calcLND=TSF_calcLN; TSF_calclogNL,TSF_calclogNR=0,decimal.Decimal(TSF_calcRN)
                if TSF_calclogNR > 0:
                    while decimal.getcontext().remainder(TSF_calcLND,TSF_calclogNR) == 0:
                        TSF_calcLND=decimal.Decimal(decimal.getcontext().divide(TSF_calcLND,TSF_calclogNR)); TSF_calclogNL+=1
                    if decimal.getcontext().power(TSF_calclogNR,TSF_calclogNL) == TSF_calcLN:
                        TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calclogNL),decimal.Decimal(1)
                        TSF_calcA="|".join([str(TSF_calcLN),str(TSF_calcLD)])
            if TSF_calcA == "":
                try:
                    TSF_calcLND=str(fractions.Fraction(decimal.getcontext().ln(TSF_calcLN/TSF_calcLD)/decimal.getcontext().ln(decimal.Decimal(TSF_calcRN)/decimal.Decimal(TSF_calcRD))))
                    if '/' in TSF_calcLND:
                        TSF_calcLN,TSF_calcLD=TSF_calcLND.split('/'); TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcLN),decimal.Decimal(TSF_calcLD)
                    else:
                        TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcLND),decimal.Decimal(1)
                except decimal.InvalidOperation:
                    TSF_calcA="n|0"
                    break
        elif TSF_calcO == 'A':
            try:
                TSF_calcLND=str(fractions.Fraction(math.atan2(TSF_calcLN/TSF_calcLD,decimal.Decimal(TSF_calcRN)/decimal.Decimal(TSF_calcRD))))
                if '/' in TSF_calcLND:
                    TSF_calcLN,TSF_calcLD=TSF_calcLND.split('/'); TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcLN),decimal.Decimal(TSF_calcLD)
                else:
                    TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcLND),decimal.Decimal(1)
            except decimal.InvalidOperation:
                TSF_calcA="n|0"
                break
        elif TSF_calcO == 'a':
            try:
                TSF_calcX,TSF_calcY=TSF_calcLN/TSF_calcLD,decimal.Decimal(TSF_calcRN)/decimal.Decimal(TSF_calcRD)
                TSF_calcLND=str(fractions.Fraction(decimal.getcontext().sqrt(decimal.getcontext().power(TSF_calcX,2)+decimal.getcontext().power(TSF_calcY,2))))
                if '/' in TSF_calcLND:
                    TSF_calcLN,TSF_calcLD=TSF_calcLND.split('/'); TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcLN),decimal.Decimal(TSF_calcLD)
                else:
                    TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcLND),decimal.Decimal(1)
            except decimal.InvalidOperation:
                TSF_calcA="n|0"
                break
        elif TSF_calcO == '>':
            TSF_calcLND=decimal.Decimal(TSF_calcLN/TSF_calcLD)
            TSF_calcRND=decimal.Decimal(TSF_calcRN)/decimal.Decimal(TSF_calcRD)
            if TSF_calcLND > TSF_calcRND:
                TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcRN),decimal.Decimal(TSF_calcRD)
        elif TSF_calcO == '<':
            TSF_calcLND=decimal.Decimal(TSF_calcLN/TSF_calcLD)
            TSF_calcRND=decimal.Decimal(TSF_calcRN)/decimal.Decimal(TSF_calcRD)
            if TSF_calcLND < TSF_calcRND:
                TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcRN),decimal.Decimal(TSF_calcRD)
        elif TSF_calcO == '&':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRD)+decimal.Decimal(TSF_calcRN)*TSF_calcLD
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        else:  # TSF_calcO == '`':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRN)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        try:
            if TSF_calcLD < 0: TSF_calcLN,TSF_calcLD=-TSF_calcLN,-TSF_calcLD
            TSF_GCD=fractions.gcd(TSF_calcLN,TSF_calcLD)
            TSF_calcLN=TSF_calcLN//TSF_GCD
            TSF_calcLD=TSF_calcLD//TSF_GCD
            TSF_calcA="|".join([str(TSF_calcLN),str(TSF_calcLD)])
        except decimal.InvalidOperation:
            TSF_calcA="n|0"
    return TSF_calcA

TSF_calc_SCTs=OrderedDict([
    ('R',(lambda TSF_calcN,TSF_calcD:str(decimal.Decimal(TSF_calcN/TSF_calcD).sqrt()))),
    ('E',(lambda TSF_calcN,TSF_calcD:str(decimal.Decimal(TSF_calcN/TSF_calcD).ln()))),
    ('L',(lambda TSF_calcN,TSF_calcD:str(decimal.Decimal(TSF_calcN/TSF_calcD).log10()))),
    ('S',(lambda TSF_calcN,TSF_calcD:str(decimal.Decimal(math.sin(decimal.Decimal(TSF_calcN/TSF_calcD)))))),
    ('C',(lambda TSF_calcN,TSF_calcD:str(decimal.Decimal(math.cos(decimal.Decimal(TSF_calcN/TSF_calcD)))))),
    ('T',(lambda TSF_calcN,TSF_calcD:str(decimal.Decimal(math.tan(decimal.Decimal(TSF_calcN/TSF_calcD)))))),
    ('s',(lambda TSF_calcN,TSF_calcD:str(decimal.Decimal(math.asin(decimal.Decimal(TSF_calcN/TSF_calcD)))))),
    ('c',(lambda TSF_calcN,TSF_calcD:str(decimal.Decimal(math.acos(decimal.Decimal(TSF_calcN/TSF_calcD)))))),
    ('t',(lambda TSF_calcN,TSF_calcD:str(decimal.Decimal(math.atan(decimal.Decimal(TSF_calcN/TSF_calcD)))))),
])
def TSF_calc_fractalize(TSF_calcQ):    #TSF_doc:分数電卓なので小数を分数に。ついでに平方根や三角関数も。0で割る、もしくは桁が限界越えたときなどは「n|0」を返す。
    TSF_calcQ=TSF_calcQ.replace('/','|').rstrip('.').rstrip('+')
    if not '|' in TSF_calcQ:
        TSF_calcQ="|".join([TSF_calcQ,"1"])
    TSF_calcM=TSF_calcQ.count('m')+TSF_calcQ.count('-') if not '!' in TSF_calcQ else 0
    TSF_calcQ=TSF_calcQ.replace('p','').replace('m','').replace('-','').replace('!','')
    TSF_calc_SCTin=""
    for TSF_calcSCT in TSF_calc_SCTs.keys():
        if TSF_calcSCT in TSF_calcQ:
            TSF_calc_SCTin+=TSF_calcSCT
            TSF_calcQ=TSF_calcQ.replace(TSF_calcSCT,'')
    TSF_calcR=TSF_calcQ.split('|'); TSF_calcNs,TSF_calcDs=TSF_calcR[0],TSF_calcR[1:]
    if len(TSF_calcNs) == 0: TSF_calcNs="0"
    if "n" in TSF_calcNs:
        TSF_calcA="n|0"
    else:
        try:
            TSF_calcN=decimal.Decimal(TSF_calcNs)
        except decimal.InvalidOperation:
            TSF_calcN=decimal.Decimal("0")
        TSF_calcD=decimal.Decimal("1")
        for TSF_calcDmulti in TSF_calcDs:
            if len(TSF_calcDmulti) == 0: TSF_calcDmulti="0"
            try:
                TSF_calcD=TSF_calcD*decimal.Decimal(TSF_calcDmulti)
            except decimal.InvalidOperation:
                TSF_calcD=decimal.Decimal("0")
        if TSF_calcD != decimal.Decimal("0"):
            try:
                TSF_GCD=fractions.gcd(TSF_calcN,TSF_calcD)
                TSF_calcN=TSF_calcN//TSF_GCD
                TSF_calcD=TSF_calcD//TSF_GCD
                if TSF_calcM%2 != 0:
                    TSF_calcN=-TSF_calcN
                TSF_calcA="|".join([str(TSF_calcN),str(TSF_calcD)])
            except decimal.InvalidOperation:
                TSF_calcA="n|0"
        else:
            TSF_calcA="n|0"
    if TSF_calcA != "n|0":
        if len(TSF_calc_SCTin) > 0:
            for TSF_calcSCT in TSF_calc_SCTin:
                try:
                    TSF_calcA=TSF_calc_SCTs[TSF_calcSCT](TSF_calcN,TSF_calcD)
                except ValueError:
                    TSF_calcA="n|0"
                except decimal.InvalidOperation:
                    TSF_calcA="n|0"
                TSF_calcA=TSF_calc_fractalize(TSF_calcA)
    return TSF_calcA

def TSF_calc_LCM(TSF_calcN,TSF_calcD):    #TSF_doc:最小公倍数の計算。
    return decimal.Decimal(TSF_calcN*TSF_calcD)//decimal.Decimal(fractions.gcd(TSF_calcN,TSF_calcD))

def TSF_calc_decimalizeDC(TSF_calcQ):    #TSF_doc:分数(が入力されてるものと信用して)を変換して小数を返す。ただし「n|0」の時は「n|0」を返す。
    TSF_calcRN,TSF_calcRD=TSF_calcQ.replace('m','-').replace('p','').split('|')
    if float(TSF_calcRD) != 0.0:
        TSF_calcA=str(decimal.Decimal(TSF_calcRN)/decimal.Decimal(TSF_calcRD))
    else:
        TSF_calcA="n|0"
    return TSF_calcA

def TSF_calc_decimalizeKN(TSF_calcQ):    #TSF_doc:分数(が入力されてるものと信用して)を変換して4桁毎に漢字で返す。ただし「n|0」の時は「n|0」を返す。
    TSF_calcF="マイナス" if TSF_calcQ.startswith('m') else ""
    TSF_calcRN,TSF_calcRD=TSF_calcQ.replace('m','').replace('p','').split('|')
    if float(TSF_calcRD) != 0.0:
        TSF_calcA="".join([TSF_calcF,TSF_calc_decimalizeKNcomma(TSF_calcRD),"分の",TSF_calc_decimalizeKNcomma(TSF_calcRN)])
        TSF_calcA=TSF_calcA.replace("1分の",'')
    else:
        TSF_calcA="n|0"
    TSF_calcA=TSF_calcA.replace('恒','恒河沙').replace('阿','阿僧祇').replace('那','那由他').replace('思','不可思議').replace('量','無量大数')
    return TSF_calcA

def TSF_calc_decimalizeKNcomma(TSF_calcQ):    #TSF_doc:整数を4桁で区切って漢数字を付ける。
    TSF_calcA=""
    TSF_calcO=decimal.Decimal(TSF_calcQ); TSF_calcK=TSF_calcO%decimal.Decimal(10000)
    if TSF_calcK:
        TSF_calcA="".join([TSF_calcA,str(TSF_calcK)])
    for TSF_okusenK in TSF_calc_okusenman:
        TSF_calcO=TSF_calcO//decimal.Decimal(10000); TSF_calcK=TSF_calcO%decimal.Decimal(10000)
        if TSF_calcK > decimal.Decimal(0):
            TSF_calcA="".join([str(TSF_calcK),TSF_okusenK,TSF_calcA])
    if TSF_calcO > decimal.Decimal(10000):
        TSF_calcO=TSF_calcO//decimal.Decimal(10000)
        TSF_calcA="".join([str(TSF_calcO),TSF_calcA])
    return TSF_calcA


def TSF_calc_debug():    #TSF_doc:「TSF/TSF_calc.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog("TSF_Tab-Separated-Forth:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_argvs:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argvs)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    TSF_calc_precision(10)
    LTsv_calcQlist=OrderedDict([
        ("TSF_calc漢数字:",["一割る三引く(マイナス二分の一)","2分の1を5乗","(2分の1)を5乗","2分の(1を5乗)","(100分の1)を5乗","(8万分の1)を5乗","(478万分の1)を5乗","億","二百万円","十億百二十円","十億と飛んで百二十円","百二十円","3.14","円周率","ネイピア数","∞","√２","√m2","２の平方根","256を二進対数","２を16乗","無量大数"]),
        ("TSF_calc小数分数パーセント:",["0.5|3.5","0.5/3.5","1|2/7|2","2|3|5|7","0/100","100/0","10000+%8", "10000-5%","7\\3","3.14\\1","9#6","3|2#1|3","-6","m6","-m6","-6!","m6!","-m6!"]),
        ("TSF_calcゼロ比較演算子(三項演算子):",["m1Z1|1~0|1","0Z1|1~0|1","p1Z1|1~0|1","m1z1|1~0|1","0z1|1~0|1","p1z1|1~0|1"]),
        ("TSF_calcゼロ以上演算子(三項演算子):",["m1O1|1~0|1","0O1|1~0|1","p1O1|1~0|1","m1o1|1~0|1","0o1|1~0|1","p1o1|1~0|1"]),
        ("TSF_calcゼロ以下演算子(三項演算子):",["m1U1|1~0|1","0U1|1~0|1","p1U1|1~0|1","m1u1|1~0|1","0u1|1~0|1","p1u1|1~0|1"]),
        ("TSF_calcゼロ除算演算子(三項演算子):",["n|0N1|1~0|1","0/1N1|1~0|1","1/0N1|1~0|1","1/0?1|1~0|1","n|0Z1|1~0|1","n|0z1|1~0|1","n|0O1|1~0|1","n|0o1|1~0|1","n|0U1|1~0|1","n|0u1|1~0|1"]),
        ("TSF_calc max,min:",["0&0<","0&1<","1&0<","1&1<","0&0>","0&1>","1&0>","1&1>"]),
        ("TSF_calc平方根atan2:",["√２","0&m9a","0&m9a","m9&m9A","m9&m9a","m9&0A","m9&0a","0&9A","0&9a","9&9A","9&9a","9&0A","9&0a","9&m9A","9&m9a","0&m9A","0&0A","0&0a"]),
        ("TSF_calc対数乗数:",["E1","E2","Ee","E0","L10000","L256","E256/E2","L256/L2","E256+L256","256&2l","254&2l","10000&10l","81&3l","E(256-2)","E(254)","2&16^","2&1|2^","2&0^","2&0|0^","0&0^","2&2^+3&2^"]),
        ("TSF_calc円周率:",["y","Y","π","θ","θ|2","θ*30|360","θ/360*30","30|360*θ","S(θ*30|360)","S(Y/360*30)"]),
        ("TSF_calc三角関数sincostan:",["sin(θ*0|360)","S(θ*30|360)","S(θ*60|360)","S(θ*90|360)","cos(θ*0|360)","C(θ*30|360)","C(θ*60|360)","C(θ*90|360)","tan(θ*0|360)","T(θ*30|360)","T(θ*60|360)","T(θ*90|360)"]),
        ("TSF_calc和数列積数列:",["kM7","kM5~10","kM10~0","kP7","kP5~10","kP10~0","kP10~2","kM100","kP1~10","2P16"]),
        ("TSF_calc公約数公倍数:",["12&16G","12と16の公約数","12と16の最大公約数","12&16g","12と16の公倍数","12と16の最小公倍数"]),
        ("TSF_calc冪乗モジュロ(素数フェルマーテスト):",["2F0~0","3F0~0","2F7~7","3F7~7","2F60~60","3F60~60","2F341~341","3F341~341","2F561~561","3F561~561"]),
    ])
    for TSF_QlistK,TSF_QlistV in iter(LTsv_calcQlist.items()):
        TSF_debug_log=TSF_io_printlog(TSF_QlistK,TSF_log=TSF_debug_log)
        for LTsv_calcQ in TSF_QlistV:
            TSF_debug_log=TSF_io_printlog("\t{0}⇔{1};{2};{3}".format(LTsv_calcQ,TSF_calc(LTsv_calcQ,True),TSF_calc_decimalizeDC(TSF_calc(LTsv_calcQ,True)),TSF_calc_decimalizeKN(TSF_calc(LTsv_calcQ,True))),TSF_debug_log)
#    print(TSF_calcQQmemory)
    return TSF_debug_log

if __name__=="__main__":
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/debug_calc.txt"
    TSF_debug_log=TSF_calc_debug()
    TSF_io_savetext(TSF_debug_savefilename,TSF_debug_log)
    print("")
    try:
        print("--- {0} ---\n{1}".format(TSF_debug_savefilename,TSF_debug_log))
    except:
        print("can't 'print(TSF_debug_savefilename,TSF_debug_log)'")
    finally:
        pass
    sys.exit()


