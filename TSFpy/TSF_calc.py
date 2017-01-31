#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import math
import re


TSF_calc_stackwide="｛｝{}［］「」『』"
TSF_calc_stackhalf="{}{}{}{}{}"
TSF_calc_stackbracket=dict(zip(list(TSF_calc_stackwide),list(TSF_calc_stackhalf)))
TSF_calc_opewide="ＰｐPpＭｍMm１２３４５６７８９０｜．" "正負分小円" "一二三四五六七八九〇" "壱弐参肆伍陸漆捌玖零" \
               "＋－％×／＼÷＃" "加減乗除余比" "足引掛割" "和差積商" "陌阡萬仙" \
               "（）(){}{}ΣＳｓSsＣｃCc～！ＬｌllＧｇgg" "列但※囲〜値約倍" \
               "周底無∞"
TSF_calc_opehalf="ppppmmmm1234567890|." "pm|.." "1234567890" "1234567890" \
               "+-%*/\\/#" "+-*/#" "+-*/%" "+-*/" "百千万銭" \
               "()()()()SSSSScccc~LLLLGGGG!" "SSSS~cLG" \
               "yenn"
TSF_calc_operator=dict(zip(list(TSF_calc_opewide),list(TSF_calc_opehalf)))
TSF_calc_opemarkC=["*+","*-","/+","/-","#+","#-","|+","|-","++","+-","-+","--",
              "0c", "1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", ".c",
              "0(", "1(", "2(", "3(", "4(", "5(", "6(", "7(", "8(", "9(", ".(",
              ")0", ")1", ")2", ")3", ")4", ")5", ")6", ")7", ")8", ")9", ").",
              ")(", "|("]
TSF_calc_opemarkP=["*p","*m","/p","/m","#p","#m","|p","|m","+p","+m","-p","-m",
              "0*c","1*c","2*c","3*c","4*c","5*c","6*c","7*c","8*c","9*c",".*c",
              "0*(","1*(","2*(","3*(","4*(","5*(","6*(","7*(","8*(","9*(",".*(",
              ")*0",")*1",")*2",")*3",")4*",")*5",")*6",")*7",")*8",")*9",")*.",
              ")*(", "/("]
TSF_calc_opemark=dict(zip(TSF_calc_opemarkC,TSF_calc_opemarkP))
TSF_calc_usemark="1234567890.|pmyecn+-*/\\#%(S!LG~)" "銭十百千万億兆京垓"

def TSF_calc_GCM(TSF_calcL,TSF_calcR):
    TSF_GCMm,TSF_GCMn=abs(int(TSF_calcL)),abs(int(TSF_calcR))
    if TSF_GCMm < TSF_GCMn:
        TSF_GCMm,TSF_GCMn=TSF_GCMn,TSF_GCMm
    while TSF_GCMn > 0:
        TSF_GCMm,TSF_GCMn=TSF_GCMn,TSF_GCMm%TSF_GCMn
    return TSF_GCMm

def TSF_calc_LCM(TSF_calcL,TSF_calcR):
    return abs(int(TSF_calcL))*abs(int(TSF_calcR))//TSF_calc_GCM(TSF_calcL,TSF_calcR)

def TSF_calc_stackmarge(TSF_calcQ):
    TSF_calcK,TSF_calcA="",""
    TSF_calc_stackreg=re.compile("[{](?<=[{])[^{}]*(?=[}])[}]")
    for TSF_calcbracketQ in TSF_calcQ:
        TSF_calcK+=TSF_calc_stackbracket.get(TSF_calcbracketQ,TSF_calcbracketQ)
    for TSF_func in re.findall(TSF_calc_stackreg,TSF_calcA):
        TSF_calcK=TSF_calcA.replace(TSF_func,"({0})".format(TSF_func))
    for TSF_calcbracketK in TSF_calcK:
        TSF_calcA+=TSF_calc_operator.get(TSF_calcbracketK,TSF_calcbracketK)
    return TSF_calcA

def TSF_calc_bracketsbalance(TSF_calcQ):
    TSF_calcQ=TSF_calc_stackmarge(TSF_calcQ)
    TSF_calcA=""; TSF_calcbracketLR,TSF_calcbracketCAP=0,0
    for TSF_calcbracketQ in TSF_calcQ:
        TSF_calcA+=TSF_calcbracketQ if TSF_calcbracketQ in TSF_calc_usemark else ''
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
    TSF_calcA=re.sub(re.compile("([0-9千百十]+?)銭"),"+(\\1/100)",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9千百十]+?)万"),"(\\1)*1"+'0'*4+"+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9千百十]+?)億"),"(\\1)*1"+'0'*8+"+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9千百十]+?)兆"),"(\\1)*1"+'0'*12+"+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9千百十]+?)京"),"(\\1)*1"+'0'*16+"+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9千百十]+?)垓"),"(\\1)*1"+'0'*20+"+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9]+?)千"),"(\\1*1000)+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9]+?)百"),"(\\1*100)+",TSF_calcA)
    TSF_calcA=re.sub(re.compile("([0-9]+?)十"),"(\\1*10)+",TSF_calcA)
    TSF_calcA=TSF_calcA.replace('千','1000')
    TSF_calcA=TSF_calcA.replace('百','100')
    TSF_calcA=TSF_calcA.replace('十','10')
    return TSF_calcA

def TSF_calc(TSF_calcQ):
    TSF_calcQ=TSF_calcQ.replace('\n','\t').replace('\t',''); TSF_calcA="n|0"
    TSF_calcA=TSF_calc_bracketsbalance(TSF_calcQ);
    return TSF_calcA


def TSF_calc_debug(TSF_argv=[]):    #TSF_doc:「TSF/TSF_calc.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog("TSF_Tab-Separated-Forth:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_argv:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argv)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_calc:",TSF_log=TSF_debug_log)
    LTsv_calcQlist=[ "1/3)｛｝","(1/3*3","(1|3*3)","1|3","{1}+{2}","二百万円","十億円"]
    for LTsv_calcQ in LTsv_calcQlist:
        TSF_debug_log=TSF_io_printlog("\t{0}⇔{1}".format(LTsv_calcQ,TSF_calc(LTsv_calcQ)),TSF_debug_log)
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


