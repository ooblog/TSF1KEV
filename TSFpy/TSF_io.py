#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import locale
import codecs
import os
import subprocess
import ctypes
import zipfile
import base64
import datetime
import math
from collections import OrderedDict
from collections import deque


TSF_io_name2codepoint,TSF_io_urlliburlretrieve=None,None
if sys.version_info.major == 2:
    import htmlentitydefs
    TSF_io_name2codepoint=htmlentitydefs.name2codepoint
    import HTMLParser
    TSF_io_htmlparser=HTMLParser
    import urllib
    TSF_io_urlliburlretrieve=urllib.urlretrieve
if sys.version_info.major == 3:
    import html.entities
    TSF_io_name2codepoint=html.entities.name2codepoint
    import html.parser
    TSF_io_htmlparser=html.parser
    import urllib.request
    TSF_io_urlliburlretrieve=rllib.request.urlretrieve

TSF_libc=None
if sys.platform.startswith("win"):
    TSF_libc=ctypes.cdll.msvcrt
if sys.platform.startswith("linux"):
    TSF_libc=ctypes.CDLL("libc.so.6")

def TSF_io_loadtext(TSF_path,TSF_encoding="UTF-8"):    #TSF_doc:TSF_pathからTSF_textを読み込む。初期文字コードは「UTF-8」なのでいわゆるシフトJISを読み込む場合は「cp932」を指定する。
    TSF_text=""
    if os.path.isfile(TSF_path):
        if sys.version_info.major == 2:
            with open(TSF_path,"r") as TSF_io_fileobj:
                TSF_byte=TSF_io_fileobj.read()
            TSF_text=unicode(TSF_byte,TSF_encoding,errors="xmlcharrefreplace")
        if sys.version_info.major == 3:
            with open(TSF_path,mode="r",encoding=TSF_encoding,errors="xmlcharrefreplace") as TSF_io_fileobj:
                TSF_text=TSF_io_fileobj.read()
    return TSF_text

TSF_io_stdout=sys.stdout.encoding if sys.stdout.encoding != None else locale.getpreferredencoding()
def TSF_io_printlog(TSF_text,TSF_log=None):    #TSF_doc:TSF_textをターミナル(stdout)に表示する。TSF_logに追記もできる。
    TSF_io_printf=TSF_text.encode(TSF_io_stdout,"xmlcharrefreplace")
    if TSF_text.endswith('\n'):
        TSF_libc.printf(b"%s",TSF_io_printf)
        TSF_log="".join([TSF_log,TSF_text]) if TSF_log != None else ""
    else:
        TSF_libc.printf(b"%s\n",TSF_io_printf)
        TSF_log="".join([TSF_log,TSF_text,'\n']) if TSF_log != None else ""
    return TSF_log

def TSF_io_argvs():
    TSF_argvs=[]
    for TSF_argv in sys.argv:
        TSF_argvs.append(TSF_argv.decode(TSF_io_stdout))
    return TSF_argvs

def TSF_io_intstr0x(TSF_io_codestr):    #TSF_doc:テキストを整数に変換する(整数10進か16進数)。
    TSF_io_codestr="{0}".format(TSF_io_codestr)
    TSF_io_codeint=0
    try:
        TSF_io_codeint=int(float(TSF_io_codestr))
    except ValueError:
        pass
    for TSF_io_hexstr in ["0x","U+","$"]:
        if TSF_io_hexstr in TSF_io_codestr:
            try:
                TSF_io_codeint=int(TSF_io_codestr.replace(TSF_io_hexstr,""),16)
            except ValueError:
                pass
            break
    return TSF_io_codeint

def TSF_io_floatstr(TSF_io_codestr):    #TSF_doc:テキストを小数に変換する。
    TSF_io_codestr="{0}".format(TSF_io_codestr)
    TSF_io_codefloat=0.0
    try:
        TSF_io_codefloat=float(TSF_io_codestr)
    except ValueError:
        pass
    return TSF_io_codefloat

def TSF_txt_ESCencode(TSF_text):
    TSF_text=TSF_text.replace('&',"&amp;").replace('\t',"&tab;")
    return TSF_text

def TSF_txt_ESCdecode(TSF_text):
    TSF_text=TSF_text.replace("&tab;",'\t').replace("&amp;",'&')
    return TSF_text

def TSF_io_readlinedeno(TSF_text):    #TSF_doc:TSF_textの行数を取得。
    if len(TSF_text) > 0:
        TSF_linedeno=TSF_text.count('\n') if TSF_text.endswith('\n') else TSF_text.count('\n')+1
    else:
        TSF_linedeno=0
    return TSF_linedeno

def TSF_io_readlinenum(TSF_text,TSF_linenum):    #TSF_doc:TSF_textから1行取得。
    TSF_line=""
    TSF_splits=TSF_text.rstrip('\n').split('\n')
    if 0 <= LTsv_linenum < len(TSF_splits):
        TSF_line=TSF_splits[LTsv_linenum]
    return TSF_line

def TSF_io_overlinenum(TSF_text,TSF_linenum,TSF_line=None):    #TSF_doc:TSF_textの1行上書。LTsv_line=Noneの時は1行削除。
    TSF_splits=TSF_text.rstrip('\n').split('\n')
    if LTsv_linenum < 0:
        if TSF_line != None:
            TSF_text = '\n'.join(TSF_line.rstrip('\n').split('\n')+TSF_splits)
    elif len(TSF_splits) <= LTsv_linenum:
        if TSF_line != None:
            TSF_text = '\n'.join(TSF_splits+TSF_line.rstrip('\n').split('\n'))
    else:
        if TSF_line != None:
            if TSF_linenum == int(TSF_linenum):
                LTsv_text = '\n'.join(TSF_splits[:TSF_linenum]+LTsv_line.rstrip('\n').split('\n')+TSF_splits[TSF_linenum+1:])
            else:
                LTsv_text = '\n'.join(TSF_splits[:math.floor(TSF_linenum)]+LTsv_line.rstrip('\n').split('\n')+TSF_splits[math.ceil(TSF_linenum):])
        else:
            if type(LTsv_linenum) in (int, long):
                TSF_splits.pop(LTsv_linenum); TSF_text = '\n'.join(TSF_splits)
    return LTsv_text

def TSF_io_savedir(TSF_path):    #TSF_doc:「TSF_io_savetext()」でファイル保存する時、1階層分のフォルダ1個を作成する。
    TSF_io_workdir=os.path.dirname(os.path.normpath(TSF_path))
    if not os.path.exists(TSF_io_workdir) and not os.path.isdir(TSF_io_workdir) and len(TSF_io_workdir): os.mkdir(TSF_io_workdir)

def TSF_io_savedirs(TSF_path):    #TSF_doc:「TSF_io_savetext()」でファイル保存する時、一気に深い階層のフォルダを複数作れてしまうので取扱い注意(扱わない)。
    TSF_io_workdir=os.path.dirname(os.path.normpath(TSF_path))
    if not os.path.exists(TSF_io_workdir) and not os.path.isdir(TSF_io_workdir) and len(TSF_io_workdir): os.makedirs(TSF_io_workdir)

def TSF_io_savetext(TSF_path,TSF_text=None):    #TSF_doc:TSF_pathにTSF_textを保存する。TSF_textを省略した場合ファイルを削除する。空のファイルを作る場合はTSF_textに文字列長さ0の文字列変数を用意する。
    if TSF_text != None:
        TSF_io_savedir(TSF_path)
        if not TSF_text.endswith('\n'):
            TSF_text+='\n'
        if sys.version_info.major == 2:
            with open(TSF_path,'wb') as TSF_io_fileobj:
                TSF_io_fileobj.write(TSF_text.encode("UTF-8"))
        if sys.version_info.major == 3:
            with open(TSF_path,mode="w",encoding="UTF-8",errors="xmlcharrefreplace",newline='\n') as TSF_io_fileobj:
                TSF_io_fileobj.write(TSF_text)
    else:
        os.remove(TSF_text)

def TSF_io_writetext(TSF_path,TSF_text):    #TSF_doc:TSF_pathにTSF_textを追記する。
    if TSF_text != None:
        TSF_io_savedir(TSF_path)
        if not TSF_text.endswith('\n'):
            TSF_text+='\n'
        if sys.version_info.major == 2:
            with open(TSF_path,'ab') as TSF_io_fileobj:
                TSF_io_fileobj.write(TSF_text.encode("UTF-8"))
        if sys.version_info.major == 3:
            with open(TSF_path,mode="a",encoding="UTF-8",errors="xmlcharrefreplace",newline='\n') as TSF_io_fileobj:
                TSF_io_fileobj.write(TSF_text)


def TSF_io_debug():    #TSF_doc:「TSF/TSF_io.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog("TSF_Tab-Separated-Forth:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_argvs:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argvs)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    print("")
    TSF_argvs=TSF_io_argvs()
    print("--- {0} ---".format(TSF_argvs[0]))
    TSF_debug_savefilename="debug/debug_io.log"
    TSF_debug_log=TSF_io_debug()
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
