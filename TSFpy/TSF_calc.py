#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import math
import decimal
import fractions
import re
from collections import OrderedDict

from TSF_io import *

# Sin,Cos,Tan,Atan2
# max,min><,abs!
# ?~三項演算子
# 「o」ゼロ以上か「O」ゼロ越えるか＞≧
# 「Z」ゼロか・ゼロの時「z」ゼロでないか・ゼロでない時「N」ゼロ除算でないか・ゼロ除算の時 0|1 or 1|1 or n|0 #≠＝
# 「u」ゼロ以下か「U」ゼロ未満か＜≦
#「AND」z(z0|1*z1|1)
#「OR」z(z0|1+z1|1)
#「XOR」z(z0|1-z1|1)
#「NAND」Z(z0|1*z1|1)
#「NOR」Z(z0|1+z1|1)
#「NXOR」Z(z0|1-z1|1)
TSF_calc_opewide="f1234567890.|$pm!yen+-*/\\#%(MP?~k)&Ggl^ELRZzOoUuN><" \
                "銭十百千万億兆京垓𥝱穣溝澗正載極恒阿那思量" \
                "１２３４５６７８９０｜．" "絶負分点円圓" "一二三四五六七八九〇" "壱弐参肆伍陸漆捌玖零" \
                "＋－×÷／＼＃％" "加減乗除比税" "足引掛割" "和差積商" "陌阡萬仙秭" \
                "（）()｛｝{}［］[]「」｢｣『』Σ但※列Π囲～〜値とを約倍" \
                "乗常進対√根π周ｅ底∞無桁"
TSF_calc_opehalf="f1234567890.|$pm!yen+-*/\\#%(MP?~k)&Ggl^ELRZzOoUuN><" \
                "銭十百千万億兆京垓𥝱穣溝澗正載極恒阿那思量" \
                "1234567890|." "!m$..." "1234567890" "1234567890" \
                "+-*//\\#%" "+-*/%%" "+-*/" "+-*/" "百千万銭𥝱" \
                "()()()()()()()()()MMMMP~~~k&&Gg" \
                "^LlERRyyeennf"
TSF_calc_operator=OrderedDict(zip(list(TSF_calc_opewide),list(TSF_calc_opehalf)))
TSF_calc_opelong=["恒河沙","阿僧祇","那由他","不可思議","無量大数","無限","円周率","ネイピア数","プラス","マイナス","氷点下","小数点", \
                "最大公約数","最小公倍数","公約数","公倍数","とんで","とばして","とぶことの","平方根","常用対数","進対数","自然対数", \
                "絶対値"]
TSF_calc_opelshort=["恒","阿","那","思","量","∞","π","ｅ","p","m","点","点", \
                "約","倍","約","倍","","","","根","常","進","対", \
                "絶"]
TSF_calc_opeword=dict(zip(TSF_calc_opelong,TSF_calc_opelshort))
TSF_calc_opemarkC=["*+","*-","/+","/-","#+","#-","|+","|-","++","+-","-+","--",
                "0k", "1k", "2k", "3k", "4k", "5k", "6k", "7k", "8k", "9k", ".k",
                "0(", "1(", "2(", "3(", "4(", "5(", "6(", "7(", "8(", "9(", ".(",
                ")0", ")1", ")2", ")3", ")4", ")5", ")6", ")7", ")8", ")9", ").",
                ")(", "|("]
TSF_calc_opemarkP=["*p","*m","/p","/m","#p","#m","|p","|m","+p","+m","-p","-m",
                "0*k","1*k","2*k","3*k","4*k","5*k","6*k","7*k","8*k","9*k",".*k",
                "0*(","1*(","2*(","3*(","4*(","5*(","6*(","7*(","8*(","9*(",".*(",
                ")*0",")*1",")*2",")*3",")4*",")*5",")*6",")*7",")*8",")*9",")*.",
                ")*(", "/("]
TSF_calc_opemark=dict(zip(TSF_calc_opemarkC,TSF_calc_opemarkP))
TSF_calc_okusenman="万億兆京垓𥝱穣溝澗正載極恒阿那思量"
TSF_calc_okusenzero=['1'+'0'*((o+1)*4) for o in range(len(TSF_calc_okusenman))]
TSF_calc_okusendic=dict(zip(list(TSF_calc_okusenman),TSF_calc_okusenzero))
TSF_calc_precisionMAX=72; decimal.getcontext().prec=TSF_calc_precisionMAX
TSF_calc_precisionROUND=decimal.ROUND_DOWN; decimal.getcontext().rounding=TSF_calc_precisionROUND
TSF_calc_PI="31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
TSF_calc_E="27182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def TSF_calc_precision(TSF_prec):    #TSF_doc:電卓の有効桁数を変更する。初期値は72桁(千無量大数)
    global TSF_calc_precisionMAX
    TSF_calc_precisionMAX=min(max(TSF_prec,4),100)
    decimal.getcontext().prec=TSF_calc_precisionMAX

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
    global TSF_calc_precisionROUND
    TSF_calc_precisionROUND=TSF_calc_roundopt.get(TSF_round,decimal.ROUND_DOWN)
    decimal.getcontext().prec=TSF_calc_precisionROUND

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
        TSF_calcA=re.sub(re.compile("([0-9千百十]+?){0}".format(TSF_okusenK)),"(\\1)*{0}+".format(TSF_okusenV),TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9]+?)千"),"(\\1*1000)+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9]+?)百"),"(\\1*100)+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9]+?)十"),"(\\1*10)+",TSF_calcA)
    TSF_calcA=TSF_calcA.replace('銭',"1|100+")
    TSF_calcA=TSF_calcA.replace('十',"10+")
    TSF_calcA=TSF_calcA.replace('百',"100+")
    TSF_calcA=TSF_calcA.replace('千',"1000+")
    for TSF_okusenK,TSF_okusenV in TSF_calc_okusendic.items():
        TSF_calcA=TSF_calcA.replace(TSF_okusenK,"{0}+".format(TSF_okusenV))
    TSF_calcA=TSF_calcA.replace('y',("{0}|1".format(TSF_calc_PI[:TSF_calc_precisionMAX])+'0'*(TSF_calc_precisionMAX-1)))
    TSF_calcA=TSF_calcA.replace('e',("{0}|1".format(TSF_calc_E[:TSF_calc_precisionMAX])+'0'*(TSF_calc_precisionMAX-1)))
    TSF_calcA=TSF_calcA.replace('f',str(TSF_calc_precisionMAX)).replace('n','(n|0)')
#    TSF_io_printlog("TSF_calc_bracketsbalance:{0}".format(TSF_calcA))
    for TSF_calc_opecase in TSF_calc_opemark:
        if TSF_calc_opecase in TSF_calcA:
            TSF_calcA=TSF_calcA.replace(TSF_calc_opecase,TSF_calc_opemark[TSF_calc_opecase])
    return TSF_calcA

def TSF_calc(TSF_calcQ):    #TSF_doc:分数電卓のmain。括弧の内側を検索(正規表現)。
    TSF_calcA="n|0"
    TSF_calcA=TSF_calc_bracketsbalance(TSF_calcQ);
    TSF_calc_bracketreg=re.compile("[(](?<=[(])[^()]*(?=[)])[)]")
    while "(" in TSF_calcA:
        for TSF_func in re.findall(TSF_calc_bracketreg,TSF_calcA):
            TSF_calcA=TSF_calcA.replace(TSF_func,TSF_calc_function(TSF_func))
    TSF_calcA=TSF_calcA.replace(TSF_calcA,TSF_calc_function(TSF_calcA))
    TSF_calcA=TSF_calc_fractalize(TSF_calcA)
    if TSF_calcA != "0|1" and TSF_calcA != "n|0":
        TSF_calcA=TSF_calcA.replace('-','m') if TSF_calcA.startswith("-") else "p{0}".format(TSF_calcA)
    return TSF_calcA

def TSF_calc_function(TSF_calcQ):    #TSF_doc:分数電卓の和集合積集合およびSin,Cos,Tan,Atan2,sQrt,LOg予定地。
    TSF_calcQ=TSF_calcQ.lstrip("(").rstrip(")")
    TSF_calcO='?' if '?' in TSF_calcQ else ''
    TSF_calcO='P' if 'P' in TSF_calcQ else TSF_calcO
    TSF_calcO='M' if 'M' in TSF_calcQ else TSF_calcO
    if TSF_calcO != '':
        TSF_calcOfind=TSF_calcQ.find(TSF_calcO)
        TSF_calcQ=TSF_calcQ[:TSF_calcOfind]+'\t'+TSF_calcQ[TSF_calcOfind+1:]
        TSF_calcQ=TSF_calcQ.replace('M','').replace('P','').replace('?','')
        TSF_calcSeq,TSF_calcLim=TSF_calcQ.split('\t')
        TSF_calcsequences=""
        if not '~' in TSF_calcLim:
            TSF_calcLim="1~"+str(abs(decimal.Decimal(TSF_calc_decimalize(TSF_calcLim)).to_integral_value()))
        TSF_LimStart,TSF_LimGoal=TSF_calcLim.split('~')[0],TSF_calcLim.split('~')[-1]
        if TSF_calcO in "PM":
            TSF_calcO='+' if 'M'==TSF_calcO else '*'
            TSF_LimStart,TSF_LimGoal=decimal.Decimal(TSF_calc_decimalize(TSF_LimStart)).to_integral_value(),decimal.Decimal(TSF_calc_decimalize(TSF_LimGoal)).to_integral_value()
            if TSF_LimStart <= TSF_LimGoal:
                TSF_limstep=1; TSF_LimGoal+=1
            else:
                TSF_limstep=-1; TSF_LimGoal-=1
            for TSF_LimK in range(TSF_LimStart,TSF_LimGoal,TSF_limstep):
                TSF_calcsequences+=TSF_calc_addition(TSF_calcSeq.replace('k',str(TSF_LimK)))+TSF_calcO
            TSF_calcsequences=TSF_calcsequences.rstrip(TSF_calcO)
        elif TSF_calcO in "?":
            TSF_calcsequences=TSF_calc_addition(TSF_calcSeq.replace('k',"0"))
            if TSF_calcsequences == "n|0":
                TSF_calcsequences="n|0"
            else:
                TSF_calcsequences=TSF_LimStart if TSF_calcsequences != "0|1" else TSF_LimGoal
        TSF_calcQ=TSF_calc(TSF_calcsequences)
    else:
        TSF_calcQ=TSF_calcQ.replace('k','0')
    TSF_calcA=TSF_calc_addition(TSF_calcQ)
    return TSF_calcA
    
def TSF_calc_addition(TSF_calcQ):    #TSF_doc:分数電卓の足し算引き算・消費税計算等。
    TSF_calcLN,TSF_calcLD=decimal.Decimal(0),decimal.Decimal(1)
    TSF_calcQ=TSF_calcQ.replace("++","+").replace("+-","-").replace("--","+").replace("-+","-")
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
            TSF_calcA=str(TSF_calcLN)+"|"+str(TSF_calcLD)
        except decimal.InvalidOperation:
            TSF_calcA="n|0"
    return TSF_calcA

def TSF_calc_multiplication(TSF_calcQ):    #TSF_doc:分数電卓の掛け算割り算等。
    TSF_calcLN,TSF_calcLD=decimal.Decimal(1),decimal.Decimal(1)
    TSF_calcQ=TSF_calcQ.replace('*',"\t*").replace('/',"\t/").replace('\\',"\t\\").replace('#',"\t#").replace('&',"\t&")
    TSF_calcQ=TSF_calcQ.replace('G',"G\t").replace('g',"g\t").replace('^',"^\t").replace('l',"l\t")
    TSF_calcQ=TSF_calcQ.replace("+p","+").replace("+m","-").replace("-m","+").replace("-p","-")
    TSF_calcQ=TSF_calcQ.replace("p","+").replace("m","-")
    TSF_calcQsplits=TSF_calcQ.replace("\t\t",'\t').strip('\t').split('\t')
    for TSF_calcQmulti in TSF_calcQsplits:
#        print("TSF_calcQmulti",TSF_calcQmulti)
        TSF_calcO=TSF_calcQmulti[0] if len(TSF_calcQmulti)>0 else '*'
        TSF_calcO=TSF_calcO if not 'G' in TSF_calcQmulti else 'G'
        TSF_calcO=TSF_calcO if not 'g' in TSF_calcQmulti else 'g'
        TSF_calcO=TSF_calcO if not '^' in TSF_calcQmulti else '^'
        TSF_calcO=TSF_calcO if not 'l' in TSF_calcQmulti else 'l'
        TSF_calcR=TSF_calc_fractalize(TSF_calcQmulti.lstrip('*/\\#').replace('G','').replace('g','').replace('^','').replace('l','').replace('&',''))
        TSF_calcRN,TSF_calcRD=TSF_calcR.split('|')
        if decimal.Decimal(TSF_calcRD) == 0:
            TSF_calcA="n|0"
            break
        if TSF_calcO == '/':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRN)
        elif TSF_calcO == '\\':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRN)
            TSF_calcLN,TSF_calcLD=TSF_calcLN//TSF_calcLD,1
        elif TSF_calcO == '#':
            if decimal.Decimal(TSF_calcRN) == 0:
                TSF_calcLD=0
                break
            TSF_calcLN=(TSF_calcLN*decimal.Decimal(TSF_calcRD))%(decimal.Decimal(TSF_calcRN)*TSF_calcLD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        elif TSF_calcO == 'G':
            TSF_calcLN=fractions.gcd(TSF_calcLN*decimal.Decimal(TSF_calcRD),decimal.Decimal(TSF_calcRN)*TSF_calcLD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        elif TSF_calcO == 'g':
            TSF_calcLN=TSF_calc_LCM(TSF_calcLN*decimal.Decimal(TSF_calcRD),decimal.Decimal(TSF_calcRN)*TSF_calcLD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        elif TSF_calcO == '^':
            try:
                TSF_calcLND=str(fractions.Fraction(decimal.getcontext().power(TSF_calcLN/TSF_calcLD,decimal.Decimal(TSF_calcRN)/decimal.Decimal(TSF_calcRD))))
                if '/' in TSF_calcLND:
                    TSF_calcLN,TSF_calcLD=TSF_calcLND.split('/'); TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcLN),decimal.Decimal(TSF_calcLD)
                else:
                    TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcLND),decimal.Decimal(1)
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
                        TSF_calcA=str(TSF_calcLN)+"|"+str(TSF_calcLD)
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
        elif TSF_calcO == '&':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRD)+decimal.Decimal(TSF_calcRN)*TSF_calcLD
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        else:  # TSF_calcO == '`':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRN)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
        try:
            TSF_GCD=fractions.gcd(TSF_calcLN,TSF_calcLD)
            TSF_calcLN=TSF_calcLN//TSF_GCD
            TSF_calcLD=TSF_calcLD//TSF_GCD
            TSF_calcA=str(TSF_calcLN)+"|"+str(TSF_calcLD)
        except decimal.InvalidOperation:
            TSF_calcA="n|0"
    return TSF_calcA

def TSF_calc_fractalize(TSF_calcQ):    #TSF_doc:分数電卓なので小数を分数に。0で割る、もしくは桁が限界越えたときなどは「n|0」を返す。
    TSF_calc_root=False
    TSF_calc_ln,TSF_calc_log10=False,False
    TSF_calc_abs=False
    TSF_calcQ=TSF_calcQ.replace('/','|').rstrip('.').rstrip('+')
    if not '|' in TSF_calcQ:
        TSF_calcQ="{0}|1".format(TSF_calcQ)
    if '$' in TSF_calcQ:
        TSF_calcR=TSF_calcQ.split('$')
        TSF_calcQ="{1}|{0}".format(TSF_calcR[0],TSF_calcR[1])
    if 'R' in TSF_calcQ:
        TSF_calcQ=TSF_calcQ.replace('R','')
        TSF_calc_root=True
    if 'E' in TSF_calcQ:
        TSF_calcQ=TSF_calcQ.replace('E','')
        TSF_calc_ln=True
    if 'L' in TSF_calcQ:
        TSF_calcQ=TSF_calcQ.replace('L','')
        TSF_calc_log10=True
    if '!' in TSF_calcQ:
        TSF_calcQ=TSF_calcQ.replace('!','')
        TSF_calc_abs=True
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
                if TSF_calcD < decimal.Decimal("0"): TSF_calcN,TSF_calcD=-TSF_calcN,-TSF_calcD
                if TSF_calc_abs == True: TSF_calcN=TSF_calcN.copy_abs()
                TSF_calcA=str(TSF_calcN)+'|'+str(TSF_calcD)
            except decimal.InvalidOperation:
                TSF_calcA="n|0"
        else:
            TSF_calcA="n|0"
    if TSF_calcA != "n|0":
        if TSF_calc_root == True:
            try:
                TSF_calcA=str(decimal.Decimal(TSF_calcN/TSF_calcD).sqrt())
            except decimal.InvalidOperation:
                TSF_calcA="n|0"
            TSF_calcA=TSF_calc_fractalize(TSF_calcA)
        if TSF_calc_ln == True:
            try:
                TSF_calcA=str(decimal.Decimal(TSF_calcN/TSF_calcD).ln())
            except decimal.InvalidOperation:
                TSF_calcA="n|0"
            TSF_calcA=TSF_calc_fractalize(TSF_calcA)
        if TSF_calc_log10 == True:
            try:
                TSF_calcA=str(decimal.Decimal(TSF_calcN/TSF_calcD).log10())
            except decimal.InvalidOperation:
                TSF_calcA="n|0"
            TSF_calcA=TSF_calc_fractalize(TSF_calcA)
    return TSF_calcA

def TSF_calc_LCM(TSF_calcN,TSF_calcD):    #TSF_doc:最小公倍数の計算。
    return decimal.Decimal(TSF_calcN*TSF_calcD)//decimal.Decimal(fractions.gcd(TSF_calcN,TSF_calcD))

def TSF_calc_decimalize(TSF_calcQ):    #TSF_doc:分数電卓だけど分数ではなく小数を返す(再計算)。ただし「n|0」の時は「n|0」を返す。
    TSF_calcA=TSF_calc(TSF_calcQ); 
    return TSF_calc_decimalizeQQ(TSF_calcA)
    
def TSF_calc_decimalizeQQ(TSF_calcQ):    #TSF_doc:分数(が入力されてるものと信用して)を変換して小数を返す。ただし「n|0」の時は「n|0」を返す。
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
        TSF_calcA="{2}{1}分の{0}".format(TSF_calc_decimalizeKNcomma(TSF_calcRN),TSF_calc_decimalizeKNcomma(TSF_calcRD),TSF_calcF)
        TSF_calcA=TSF_calcA.replace("1分の",'')
    else:
        TSF_calcA="n|0"
    TSF_calcA=TSF_calcA.replace('恒','恒河沙').replace('阿','阿僧祇').replace('那','那由他').replace('思','不可思議').replace('量','無量大数')
    return TSF_calcA
    
def TSF_calc_decimalizeKNcomma(TSF_calcQ):    #TSF_doc:整数を4桁で区切って漢数字を付ける。
    TSF_calcA=""
    TSF_calcO=decimal.Decimal(TSF_calcQ); TSF_calcQ=TSF_calcO%decimal.Decimal(10000)
    if TSF_calcQ:
        TSF_calcA+=str(TSF_calcQ)
    for TSF_okusenK in TSF_calc_okusenman:
        TSF_calcO=TSF_calcO//decimal.Decimal(10000); TSF_calcQ=TSF_calcO%decimal.Decimal(10000)
        if TSF_calcQ > decimal.Decimal(0):
            TSF_calcA="{0}{1}{2}".format(TSF_calcQ,TSF_okusenK,TSF_calcA)
    if TSF_calcO > decimal.Decimal(10000):
        TSF_calcO=TSF_calcO//decimal.Decimal(10000)
        TSF_calcA=str(TSF_calcO)+TSF_calcA
    return TSF_calcA


def TSF_calc_debug(TSF_argv=[]):    #TSF_doc:「TSF/TSF_calc.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog("TSF_Tab-Separated-Forth:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_argv:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argv)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_calc漢数字:",TSF_log=TSF_debug_log)
    LTsv_calcQlist=["億","二百万円","十億百二十円","十億と飛んで百二十円","百二十円","3.14","円周率","ネイピア数","∞","√２","２の平方根","256を二進対数","２を16乗","無量大数"]
    for LTsv_calcQ in LTsv_calcQlist:
        TSF_debug_log=TSF_io_printlog("\t{0}⇔{1};{2};{3}".format(LTsv_calcQ,TSF_calc(LTsv_calcQ),TSF_calc_decimalize(LTsv_calcQ),TSF_calc_decimalizeKN(TSF_calc(LTsv_calcQ))),TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_calc小数分数パーセント:",TSF_log=TSF_debug_log)
    LTsv_calcQlist=["0.5|3.5","0.5/3.5","1|2/7|2","2|3|5|7","0/100","100/0","10000+%8", "10000-5%","7\\3","3.14\\1","9#6","3|2#1|3","-6","m6","-6!","m6!"]
    for LTsv_calcQ in LTsv_calcQlist:
        TSF_debug_log=TSF_io_printlog("\t{0}⇔{1};{2};{3}".format(LTsv_calcQ,TSF_calc(LTsv_calcQ),TSF_calc_decimalize(LTsv_calcQ),TSF_calc_decimalizeKN(TSF_calc(LTsv_calcQ))),TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_calc対数乗数:",TSF_log=TSF_debug_log)
    LTsv_calcQlist=["E1","E2","Ee","L10000","L256","E256/E2","L256/L2","E256+L256","256&2l","254&2l","10000&10l","81&3l","E(256-2)","E(254)","2&16^","2&1|2^","2&0^","2&0|0^","0&0^","2&2^+3&2^"]
    for LTsv_calcQ in LTsv_calcQlist:
        TSF_debug_log=TSF_io_printlog("\t{0}⇔{1};{2};{3}".format(LTsv_calcQ,TSF_calc(LTsv_calcQ),TSF_calc_decimalize(LTsv_calcQ),TSF_calc_decimalizeKN(TSF_calc(LTsv_calcQ))),TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_calc数列:",TSF_log=TSF_debug_log)
    LTsv_calcQlist=["kM7","kM5~10","kM10~0","kP7","kP5~10","kP10~0","kP10~2","kM100","kP1~10","2P16"]
    for LTsv_calcQ in LTsv_calcQlist:
        TSF_debug_log=TSF_io_printlog("\t{0}⇔{1};{2};{3}".format(LTsv_calcQ,TSF_calc(LTsv_calcQ),TSF_calc_decimalize(LTsv_calcQ),TSF_calc_decimalizeKN(TSF_calc(LTsv_calcQ))),TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_calc公約数公倍数:",TSF_log=TSF_debug_log)
    LTsv_calcQlist=["12&16G","12と16の公約数","12と16の最大公約数","12&16g","12と16の公倍数","12と16の最小公倍数"]
    for LTsv_calcQ in LTsv_calcQlist:
        TSF_debug_log=TSF_io_printlog("\t{0}⇔{1};{2};{3}".format(LTsv_calcQ,TSF_calc(LTsv_calcQ),TSF_calc_decimalize(LTsv_calcQ),TSF_calc_decimalizeKN(TSF_calc(LTsv_calcQ))),TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_calc条件演算子(三項演算子):",TSF_log=TSF_debug_log)
    LTsv_calcQlist=["1?111~222","0?111~222","n/0?111~222"]
    for LTsv_calcQ in LTsv_calcQlist:
        TSF_debug_log=TSF_io_printlog("\t{0}⇔{1};{2};{3}".format(LTsv_calcQ,TSF_calc(LTsv_calcQ),TSF_calc_decimalize(LTsv_calcQ),TSF_calc_decimalizeKN(TSF_calc(LTsv_calcQ))),TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    from TSF_io import *
    print("")
    print("--- {0} ---".format(sys.argv[0]))
    TSF_debug_savefilename="debug/TSF_calc_debug.txt"
    TSF_debug_log=TSF_calc_debug(sys.argv)
    TSF_io_savetext(TSF_debug_savefilename,TSF_debug_log)
    print("")
    try:
        print("--- {0} ---\n{1}".format(TSF_debug_savefilename,TSF_debug_log))
    except:
        print("can't 'print(TSF_debug_savefilename,TSF_debug_log)'")
    finally:
        pass
    sys.exit()


