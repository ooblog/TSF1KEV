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
#TSF_meridian_Monthdays=TSF_monthleap(TSF_meridian_Year,TSF_meridian_Month)
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

TSF_time_diffminute,TSF_time_overhour=0,24
TSF_earlier_now,TSF_meridian_now,TSF_allnight_now=None,None,None
TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiac,TSF_meridian_YearDays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso=None,None,None,None,None,None,None
TSF_allnight_Year,TSF_allnight_Yearlower,TSF_allnight_YearZodiac,TSF_allnight_YearDays,TSF_allnight_YearIso,TSF_allnight_WeekNumberYearIso,TSF_allnight_WeekDayIso,TSF_allnight_carryYear=None,None,None,None,None,None,None,None
TSF_meridian_Month,TSF_meridian_Monthdays=None,None
TSF_allnight_Month,TSF_allnight_Monthdays,TSF_allnight_carryMonth=None,None,None
TSF_meridian_Daymonth,TSF_meridian_Dayyear=None,None
TSF_allnight_Daymonth,TSF_allnight_Dayyear,TSF_allnight_carryDay=None,None,None
TSF_meridian_Hour,TSF_meridian_HourAP=None,None
TSF_allnight_Hour,TSF_allnight_HourAP,TSF_allnight_carryHour=None,None,None
def TSF_time_setdaytime(TSF_diffminute=0,TSF_overhour=24):    #TSF_doc:時刻の初期化。実際の年月日等の取得は遅延処理で行う。
    global TSF_time_diffminute,TSF_time_overhour
    TSF_time_diffminute,TSF_time_overhour=TSF_diffminute,min(max(TSF_overhour,24),48)
    global TSF_earlier_now,TSF_meridian_now,TSF_allnight_now
    TSF_earlier_now,TSF_meridian_now,TSF_allnight_now=datetime.datetime.now(),None,None
    global TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiac,TSF_meridian_YearDays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso
    if TSF_meridian_Year != TSF_earlier_now.year:
        TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiac,TSF_meridian_YearDays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso=None,None,None,None,None,None,None
        global TSF_allnight_Year,TSF_allnight_Yearlower,TSF_allnight_YearZodiac,TSF_allnight_YearDays,TSF_allnight_YearIso,TSF_allnight_WeekNumberYearIso,TSF_allnight_WeekDayIso,TSF_allnight_carryYear
        TSF_allnight_Year,TSF_allnight_Yearlower,TSF_allnight_YearZodiac,TSF_allnight_YearDays,TSF_allnight_YearIso,TSF_allnight_WeekNumberYearIso,TSF_allnight_WeekDayIso,TSF_allnight_carryYear=None,None,None,None,None,None,None,None
    global TSF_meridian_Month,TSF_meridian_Monthdays
    if TSF_meridian_Month != TSF_earlier_now.month:
        TSF_meridian_Month,TSF_meridian_Monthdays=None,None
        global TSF_allnight_Month,TSF_allnight_Monthdays,TSF_allnight_carryMonth
        TSF_allnight_Month,TSF_allnight_Monthdays,TSF_allnight_carryMonth=None,None,None
    global TSF_meridian_Daymonth,TSF_meridian_Dayyear
    if TSF_meridian_Daymonth != TSF_earlier_now.day:
        TSF_meridian_Daymonth,TSF_meridian_Dayyear=None,None
        global TSF_allnight_Daymonth,TSF_allnight_Dayyear,TSF_allnight_carryDay
        TSF_allnight_Daymonth,TSF_allnight_Dayyear,TSF_allnight_carryDay=None,None,None
    global TSF_meridian_Hour,TSF_meridian_HourAP
    if TSF_meridian_Hour != TSF_earlier_now.day:
        TSF_meridian_Hour,TSF_meridian_HourAP=None,None
        global TSF_allnight_Hour,TSF_allnight_HourAP,TSF_allnight_carryHour
        TSF_allnight_Hour,TSF_allnight_HourAP,TSF_allnight_carryHour=None,None,None

def TSF_time_earlier_now():    #TSF_doc:現在時刻(時差を含まない)の遅延処理。
    global TSF_earlier_now
    TSF_earlier_now=TSF_earlier_now if TSF_earlier_now != None else datetime.datetime.now()
    return TSF_earlier_now
def TSF_time_meridian_now():    #TSF_doc:時差を加味した現在時刻の遅延処理。
    global TSF_meridian_now
    TSF_meridian_now=TSF_meridian_now if TSF_meridian_now != None else TSF_time_earlier_now()+datetime.timedelta(minutes=TSF_time_diffminute)
    return TSF_meridian_now
def TSF_time_allnight_now():    #TSF_doc:時差を加味した徹夜時刻の遅延処理。
    global TSF_allnight_now
    TSF_allnight_now=TSF_allnight_now if TSF_allnight_now != None else TSF_time_meridian_now()
    return TSF_allnight_now

def TSF_time_meridian_Year():    #TSF_doc:現在時刻年4桁の遅延処理。
    global TSF_meridian_Year
    TSF_meridian_Year=TSF_meridian_Year if TSF_meridian_Year != None else TSF_time_meridian_now().year
    return TSF_meridian_Year
def TSF_time_allnight_Year():    #TSF_doc:徹夜時刻年4桁の遅延処理。
    global TSF_allnight_Year
    TSF_allnight_Year=TSF_allnight_Year if TSF_allnight_Year != None else TSF_time_meridian_Year()+TSF_time_allnight_carryYear()
    return TSF_allnight_Year
def TSF_time_allnight_carryYear():    #TSF_doc:徹夜時刻年の位上がり処理。
    global TSF_allnight_carryYear
    TSF_allnight_carryYear=TSF_allnight_carryYear if TSF_allnight_carryYear != None else  -1 if TSF_time_meridian_Year()+TSF_time_allnight_carryMonth() < 1 else 0
    return TSF_allnight_carryYear

def TSF_time_meridian_Yearlower():    #TSF_doc:現在時刻年2桁の遅延処理。
    global TSF_meridian_Yearlower
    TSF_meridian_Yearlower=TSF_meridian_Yearlower if TSF_meridian_Yearlower != None else TSF_time_meridian_Year()%100
    return TSF_meridian_Yearlower
def TSF_time_allnight_Yearlower():    #TSF_doc:徹夜時刻年2桁の遅延処理。
    global TSF_allnight_Yearlower
    TSF_allnight_Yearlower=TSF_allnight_Yearlower if TSF_allnight_Yearlower != None else TSF_time_allnight_Year()%100
    return TSF_allnight_Yearlower

def TSF_time_meridian_Month():    #TSF_doc:現在時刻月2桁の遅延処理。
    global TSF_meridian_Month
    TSF_meridian_Month=TSF_meridian_Month if TSF_meridian_Month != None else TSF_time_meridian_now().month
    return TSF_meridian_Month
def TSF_time_allnight_Month():    #TSF_doc:徹夜時刻月2桁の遅延処理。
    global TSF_allnight_Month
    TSF_allnight_Month=TSF_allnight_Month if TSF_allnight_Month != None else TSF_time_meridian_Month()+TSF_time_allnight_carryDay()
    return TSF_allnight_Month
def TSF_time_allnight_carryMonth():    #TSF_doc:徹夜時刻年の位上がり処理。
    global TSF_allnight_carryMonth
    TSF_allnight_carryMonth=TSF_allnight_carryMonth if TSF_allnight_carryMonth != None else -1 if TSF_time_meridian_Month()+TSF_time_allnight_carryDay() < 1 else 0
    return TSF_allnight_carryMonth

def TSF_time_meridian_Daymonth():    #TSF_doc:現在時刻日2桁の遅延処理。
    global TSF_meridian_Daymonth
    TSF_meridian_Daymonth=TSF_meridian_Daymonth if TSF_meridian_Daymonth != None else TSF_time_meridian_now().day
    return TSF_meridian_Daymonth
def TSF_time_allnight_Daymonth():    #TSF_doc:徹夜時刻日2桁の遅延処理。
    global TSF_allnight_Daymonth
    TSF_allnight_Daymonth=TSF_allnight_Daymonth if TSF_allnight_Daymonth != None else TSF_time_meridian_Daymonth()+TSF_time_allnight_carryHour()
    return TSF_allnight_Daymonth
def TSF_time_allnight_carryDay():    #TSF_doc:徹夜時刻年の位上がり処理。
    global TSF_allnight_carryDay
    TSF_allnight_carryDay=TSF_allnight_carryDay if TSF_allnight_carryDay != None else -1 if TSF_time_meridian_Daymonth()+TSF_time_allnight_carryHour() < 1 else 0
    return TSF_allnight_carryDay

def TSF_time_meridian_Hour():    #TSF_doc:現在時刻時2桁の遅延処理。
    global TSF_meridian_Hour
    TSF_meridian_Hour=TSF_meridian_Hour if TSF_meridian_Hour != None else TSF_time_meridian_now().hour
    return TSF_meridian_Hour
def TSF_time_allnight_Hour():    #TSF_doc:徹夜時刻時2桁の遅延処理。
    global TSF_allnight_Hour
    TSF_allnight_Hour=TSF_allnight_Hour if TSF_allnight_Hour != None else 24+TSF_time_meridian_Hour() if TSF_time_allnight_carryHour() < 0 else TSF_time_meridian_Hour()
    return TSF_allnight_Hour
def TSF_time_allnight_carryHour():    #TSF_doc:徹夜時刻年の位上がり処理。
    global TSF_allnight_carryHour
    TSF_allnight_carryHour=TSF_allnight_carryHour if TSF_allnight_carryHour != None else -1 if 24+TSF_time_meridian_Hour() < TSF_time_overhour else 0
    return TSF_allnight_carryHour


def TSF_time_getdaytime(TSF_timeformat="@000y@0m@0dm@wdec@0h@0n@0s",TSF_diffminute=None):    #TSF_doc:「TSF/TSF_time.py」単体テスト風デバッグ関数。
    global TSF_earlier_now,TSF_meridian_now,TSF_allnight_now
    global TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiacTSF_meridian_YearDays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso
    if TSF_diffminute != None: TSF_time_setdaytime(TSF_diffminute)
    TSF_tfList=TSF_timeformat.split("@@")
    for TSF_tfcount,TSF_tf in enumerate(TSF_tfList):

        TSF_tf=TSF_tf if not "@000y" in TSF_tf else TSF_tf.replace("@000y","{0:0>4}".format(TSF_time_meridian_Year()))
        TSF_tf=TSF_tf if not "@___y" in TSF_tf else TSF_tf.replace("@___y","{0: >4}".format(TSF_time_meridian_Year()))
        TSF_tf=TSF_tf if not "@4y" in TSF_tf else TSF_tf.replace("@4y","{0:4}".format(TSF_time_meridian_Year()))
        TSF_tf=TSF_tf if not "@0y" in TSF_tf else TSF_tf.replace("@0y","{0:0>2}".format(TSF_time_meridian_Yearlower()))
        TSF_tf=TSF_tf if not "@_y" in TSF_tf else TSF_tf.replace("@_y","{0: >2}".format(TSF_time_meridian_Yearlower()))
        TSF_tf=TSF_tf if not "@2y" in TSF_tf else TSF_tf.replace("@2y","{0:2}".format(TSF_time_meridian_Yearlower()))
        TSF_tf=TSF_tf if not "@y" in TSF_tf else TSF_tf.replace("@Y","{0}".format(TSF_time_meridian_Year()))
        TSF_tf=TSF_tf if not "@000Y" in TSF_tf else TSF_tf.replace("@000Y" ,"{0:0>4}".format(TSF_time_allnight_Year()))
        TSF_tf=TSF_tf if not "@___Y" in TSF_tf else TSF_tf.replace("@___Y" ,"{0: >4}".format(TSF_time_allnight_Year()))
        TSF_tf=TSF_tf if not "@4Y" in TSF_tf else TSF_tf.replace("@4Y","{0:4}".format(TSF_time_allnight_Year()))
        TSF_tf=TSF_tf if not "@0Y" in TSF_tf else TSF_tf.replace("@0Y","{0:0>2}".format(TSF_time_allnight_Yearlower))
        TSF_tf=TSF_tf if not "@_Y" in TSF_tf else TSF_tf.replace("@_Y","{0: >2}".format(TSF_time_allnight_Yearlower))
        TSF_tf=TSF_tf if not "@2Y" in TSF_tf else TSF_tf.replace("@2Y","{0:2}".format(TSF_time_allnight_Yearlower))
        TSF_tf=TSF_tf if not "@Y" in TSF_tf else TSF_tf.replace("@Y","{0}".format(TSF_time_allnight_Year()))

        TSF_tf=TSF_tf if not "@0m" in TSF_tf else TSF_tf.replace("@0m","{0:0>2}".format(TSF_time_meridian_Month()))
        TSF_tf=TSF_tf if not "@_m" in TSF_tf else TSF_tf.replace("@_m","{0: >2}".format(TSF_time_meridian_Month()))
        TSF_tf=TSF_tf if not "@m" in TSF_tf else TSF_tf.replace("@m","{0:2}".format(TSF_time_meridian_Month()))
        TSF_tf=TSF_tf if not "@0M" in TSF_tf else TSF_tf.replace("@0M","{0:0>2}".format(TSF_time_allnight_Month()))
        TSF_tf=TSF_tf if not "@_M" in TSF_tf else TSF_tf.replace("@_M","{0: >2}".format(TSF_time_allnight_Month()))
        TSF_tf=TSF_tf if not "@M" in TSF_tf else TSF_tf.replace("@M","{0:2}".format(TSF_time_allnight_Month()))

        TSF_tf=TSF_tf if not "@0dm" in TSF_tf else TSF_tf.replace("@0dm","{0:2}".format(TSF_time_meridian_Daymonth()))
        TSF_tf=TSF_tf if not "@_dm" in TSF_tf else TSF_tf.replace("@_dm","{0: >2}".format(TSF_time_meridian_Month()))
        TSF_tf=TSF_tf if not "@dm" in TSF_tf else TSF_tf.replace("@dm","{0:2}".format(TSF_time_meridian_Month()))
        TSF_tf=TSF_tf if not "@0Dm" in TSF_tf else TSF_tf.replace("@0Dm","{0:2}".format(TSF_time_allnight_Daymonth()))
        TSF_tf=TSF_tf if not "@_Dm" in TSF_tf else TSF_tf.replace("@_Dm","{0: >2}".format(TSF_time_allnight_Daymonth()))
        TSF_tf=TSF_tf if not "@Dm" in TSF_tf else TSF_tf.replace("@Dm","{0:2}".format(TSF_time_allnight_Daymonth()))

        TSF_tf=TSF_tf if not "@0h" in TSF_tf else TSF_tf.replace("@0h","{0:2}".format(TSF_time_meridian_Hour()))
        TSF_tf=TSF_tf if not "@_h" in TSF_tf else TSF_tf.replace("@_h","{0: >2}".format(TSF_time_meridian_Hour()))
        TSF_tf=TSF_tf if not "@h" in TSF_tf else TSF_tf.replace("@h","{0:2}".format(TSF_time_meridian_Hour()))
        TSF_tf=TSF_tf if not "@0H" in TSF_tf else TSF_tf.replace("@0H","{0:2}".format(TSF_time_allnight_Hour()))
        TSF_tf=TSF_tf if not "@_H" in TSF_tf else TSF_tf.replace("@_H","{0: >2}".format(TSF_time_allnight_Hour()))
        TSF_tf=TSF_tf if not "@H" in TSF_tf else TSF_tf.replace("@H","{0:2}".format(TSF_time_allnight_Hour()))

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
        ("TSF_time:",["@000y@0m@0dm@wdec@0h@0n@0s","@000Y@0M@0Dm@Wdec@0H@0N@0S"]),
        ("TSF_time-09:00:",["@000y-@0m-@0dmT@0h:@0n:@0s-09:00","@000Y-@0M-@0DmT@0H:@0N:@0S-09:00"]),
    ])
    for TSF_QlistK,TSF_QlistV in LTsv_timeQlist.items():
        TSF_debug_log=TSF_io_printlog(TSF_QlistK,TSF_log=TSF_debug_log)
        TSF_time_setdaytime(0,47)
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
