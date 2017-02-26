#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import datetime
import os
from collections import OrderedDict

from TSF_io import *

#TSF_earlier_now=datetime.datetime.now()
#TSF_meridian_now=TSF_earlier_now
#TSF_meridian_Year=TSF_meridian_now.year
#TSF_meridian_Yearlower=TSF_meridian_Year%100
#TSF_meridian_YearZodiac=(TSF_meridian_Year+8)%12
#TSF_meridian_YearDays=365 if not TSF_yearleap(TSF_meridian_Year) else 366
#TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso=TSF_meridian_now.isocalendar()
#TSF_meridian_YearWeeksIso=TSF_yearweeks(TSF_meridian_Year)
#TSF_meridian_Month=TSF_meridian_now.month
#TSF_meridian_MonthDays=TSF_monthleap(TSF_meridian_Year,TSF_meridian_Month)
#TSF_meridian_WeekDay=TSF_meridian_now.weekday()
#TSF_meridian_WeekNumberMonth=TSF_meridian_WeekDay//7+1
#TSF_meridian_DayMonth=TSF_meridian_now.day
#TSF_meridian_DayYear=TSF_meridian_now.toordinal()-datetime.date(TSF_meridian_Year,1,1).toordinal()+1
#TSF_meridian_Hour=TSF_meridian_now.hour
#TSF_meridian_HourAP=TSF_meridian_Hour%12
#TSF_meridian_AP=TSF_meridian_Hour//12
#TSF_meridian_APO=TSF_meridian_Hour//12
#TSF_meridian_miNute=TSF_meridian_now.minute
#TSF_meridian_Second=TSF_meridian_now.second
#TSF_meridian_micRoSecond=TSF_meridian_now.microsecond
#TSF_meridian_miLliSecond=TSF_meridian_micRoSecond//1000
#TSF_meridian_Beat,TSF_meridian_BeatInteger,TSF_meridian_BeatPoint=TSF_beat864(TSF_meridian_Hour,TSF_meridian_miNute,TSF_meridian_Second)

TSF_earlier_now,TSF_meridian_now,TSF_allnight_now=None,None,None
def TSF_time_setdaytime(TSF_diffminute=0):    #TSF_doc:時刻の初期化。実際の年月日等の取得は遅延処理で行う。
    global TSF_earlier_now,TSF_meridian_now,TSF_allnight_now
    TSF_earlier_now=datetime.datetime.now()
    TSF_meridian_now=TSF_earlier_now+datetime.timedelta(minutes=TSF_diffminute)
    TSF_allnight_now=TSF_meridian_now
    global TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiac,TSF_meridian_YearDays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso
    TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiac,TSF_meridian_YearDays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso=None,None,None,None,None,None,None

def TSF_time_TSF_meridian_Year():    #TSF_doc:年4桁の遅延処理。
    global TSF_meridian_Year
    TSF_meridian_Year=TSF_meridian_Year if TSF_meridian_Year != None else TSF_meridian_now.year
    return TSF_meridian_Year

def TSF_time_meridian_Yearlower():    #TSF_doc:年2桁の遅延処理。
    global TSF_meridian_Yearlower
    TSF_meridian_Yearlower=TSF_meridian_Yearlower if TSF_meridian_Yearlower != None else TSF_time_TSF_meridian_Year()%100
    return TSF_meridian_Yearlower

def TSF_time_getdaytime(TSF_timeformat="@000y@0m@0dm@wdec@0h@0n@0s",TSF_diffminute=None):    #TSF_doc:「TSF/TSF_time.py」単体テスト風デバッグ関数。
    global TSF_earlier_now,TSF_meridian_now,TSF_allnight_now
    global TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiacTSF_meridian_YearDays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso
    if TSF_diffminute != None: TSF_time_setdaytime(TSF_diffminute)
    TSF_tfList=TSF_timeformat.split("@@")
    for TSF_tfcount,TSF_tf in enumerate(TSF_tfList):

        TSF_tf=TSF_tf if not "@000y" in TSF_tf else TSF_tf.replace("@000y" ,"{0:0>4}".format(TSF_time_TSF_meridian_Year()))
        TSF_tf=TSF_tf if not "@___y" in TSF_tf else TSF_tf.replace("@___y" ,"{0: >4}".format(TSF_time_TSF_meridian_Year()))
        TSF_tf=TSF_tf if not "@4y" in TSF_tf else TSF_tf.replace("@4y" ,"{0:4}".format(TSF_time_TSF_meridian_Year()))
        TSF_tf=TSF_tf if not "@0y" in TSF_tf else TSF_tf.replace("@0y" ,"{0:0>2}".format(TSF_time_meridian_Yearlower()))
        TSF_tf=TSF_tf if not "@_y" in TSF_tf else TSF_tf.replace("@_y" ,"{0: >2}".format(TSF_time_meridian_Yearlower()))
        TSF_tf=TSF_tf if not "@2y" in TSF_tf else TSF_tf.replace("@2y" ,"{0:2}".format(TSF_time_meridian_Yearlower()))

        TSF_tf=TSF_tf if not "@T" in TSF_tf else TSF_tf.replace("@T"  ,"\t")
        TSF_tf=TSF_tf if not "@E" in TSF_tf else TSF_tf.replace("@E"  ,"\n")
        TSF_tf=TSF_tf if not "@Z" in TSF_tf else TSF_tf.replace("@Z"  ,"")
        TSF_tfList[TSF_tfcount]=TSF_tf

    TSF_timeformat="@".join(TSF_tfList)
    return TSF_timeformat

def TSF_time_debug():    #TSF_doc:「TSF/TSF_time.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog("TSF_Tab-Separated-Forth:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_argvs:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argvs)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    LTsv_timeQlist=OrderedDict([
        ("TSF_time:",["@000y@0m@0dm@wdec@0h@0n@0s"]),
    ])
    for TSF_QlistK,TSF_QlistV in LTsv_timeQlist.items():
        TSF_debug_log=TSF_io_printlog(TSF_QlistK,TSF_log=TSF_debug_log)
        TSF_time_setdaytime(0)
        for LTsv_timeQ in TSF_QlistV:
            TSF_debug_log=TSF_io_printlog("\t{0}⇔{1}".format(LTsv_timeQ,TSF_time_getdaytime(LTsv_timeQ)),TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/TSF_time_debug.txt"
    TSF_debug_log=TSF_time_debug()
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
