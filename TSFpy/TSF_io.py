#! /usr/bin/env python
# -*- coding: utf-8 -*-
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

TSF_io_name2codepoint=None
if sys.version_info.major == 2:
    import htmlentitydefs
    TSF_io_name2codepoint=htmlentitydefs.name2codepoint
if sys.version_info.major == 3:
    import html.entities
    TSF_io_name2codepoint=html.entities.name2codepoint

TSF_libc=None
if sys.platform.startswith("win"):
    TSF_libc=ctypes.cdll.msvcrt
if sys.platform.startswith("linux"):
    TSF_libc=ctypes.CDLL("libc.so.6")

TSF_io_stdout=sys.stdout.encoding if sys.stdout.encoding != None else locale.getpreferredencoding()
def TSF_printlog(TSF_text,TSF_log=None):    #TSF_doc:TSF_textをターミナル(stdout)に表示する。TSF_logに追記もできる。
    TSF_io_printf=TSF_text.encode(TSF_io_stdout,"xmlcharrefreplace")
    if TSF_libc != None:
        TSF_libc.printf(b"%s\n",TSF_io_printf)
    else:
        print(TSF_text)
    TSF_log=TSF_log+"{0}\n".format(TSF_io_printf) if TSF_log != None else ""
    return TSF_log


def TSF_io_savedir(TSF_path):
    TSF_io_workdir=os.path.dirname(os.path.normpath(LTsv_path))
    if not os.path.exists(TSF_io_workdir) and not os.path.isdir(TSF_io_workdir) and len(TSF_io_workdir): os.mkdir(TSF_io_workdir)

def TSF_io_savedirs(TSF_path):
    TSF_io_workdir=os.path.dirname(os.path.normpath(LTsv_path))
    if not os.path.exists(TSF_io_workdir) and not os.path.isdir(TSF_io_workdir) and len(TSF_io_workdir): os.makedirs(TSF_io_workdir)

def TSF_io_savetext(TSF_path,TSF_text):    #TSF_doc:TSF_pathにTSF_textを保存する。TSF_textを省略した場合ファイルを削除する。空のファイルを作る場合はTSF_textに文字列長さ0の文字列変数を用意する。
    if TSF_text != None:
#        LTsv_savedir(LTsv_path)
        if sys.version_info.major == 2:
            with open(TSF_path,'wb') as TSF_io_fileobj:
                TSF_io_fileobj.write(TSF_text.encode("utf-8"))
        if sys.version_info.major == 3:
            with open(TSF_path,mode="w",encoding="utf-8",errors="xmlcharrefreplace",newline='\n') as TSF_io_fileobj:
                TSF_io_fileobj.write(TSF_text)
    else:
        os.remove(TSF_text)

def TSF_io_debug(TSF_argv=[]):    #TSF_doc:「TSF/TSF_io.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    print("Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print(TSF_argv)
    TSF_debug_log=TSF_printlog("TSF_Tab-Separated-Forth",TSF_log=TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    TSF_debug_log=TSF_io_debug(sys.argv)
    TSF_debug_savefilename="TSF_debug_io.txt"
    print(TSF_debug_log)
    sys.exit()
