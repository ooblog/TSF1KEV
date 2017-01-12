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
from collections import OrderedDict


TSF_io_name2codepoint,TSF_io_urlliburlretrieve=None,None
if sys.version_info.major == 2:
    import htmlentitydefs
    TSF_io_name2codepoint=htmlentitydefs.name2codepoint
    import urllib
    TSF_io_urlliburlretrieve=urllib.urlretrieve
if sys.version_info.major == 3:
    import html.entities
    TSF_io_name2codepoint=html.entities.name2codepoint
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
    TSF_libc.printf(b"%s\n",TSF_io_printf)
    TSF_log=TSF_log+"{0}\n".format(TSF_text) if TSF_log != None else ""
    return TSF_log

def TSF_io_savedir(TSF_path):    #TSF_doc:「TSF_io_savetext()」でファイル保存する時、1階層分のフォルダ1個を作成する。
    TSF_io_workdir=os.path.dirname(os.path.normpath(TSF_path))
    if not os.path.exists(TSF_io_workdir) and not os.path.isdir(TSF_io_workdir) and len(TSF_io_workdir): os.mkdir(TSF_io_workdir)

def TSF_io_savedirs(TSF_path):    #TSF_doc:「TSF_io_savetext()」でファイル保存する時、一気に深い階層のフォルダを複数作れてしまうので取扱い注意(扱わない)。
    TSF_io_workdir=os.path.dirname(os.path.normpath(TSF_path))
    if not os.path.exists(TSF_io_workdir) and not os.path.isdir(TSF_io_workdir) and len(TSF_io_workdir): os.makedirs(TSF_io_workdir)

def TSF_io_savetext(TSF_path,TSF_text):    #TSF_doc:TSF_pathにTSF_textを保存する。TSF_textを省略した場合ファイルを削除する。空のファイルを作る場合はTSF_textに文字列長さ0の文字列変数を用意する。
    if TSF_text != None:
        TSF_io_savedir(TSF_path)
        if sys.version_info.major == 2:
            with open(TSF_path,'wb') as TSF_io_fileobj:
                TSF_io_fileobj.write(TSF_text.encode("UTF-8"))
        if sys.version_info.major == 3:
            with open(TSF_path,mode="w",encoding="UTF-8",errors="xmlcharrefreplace",newline='\n') as TSF_io_fileobj:
                TSF_io_fileobj.write(TSF_text)
    else:
        os.remove(TSF_text)


def TSF_io_debug(TSF_argv=[]):    #TSF_doc:「TSF/TSF_io.py」単体テスト風デバッグ関数。
    TSF_debug_log=""
    TSF_debug_log=TSF_io_printlog("TSF_Tab-Separated-Forth:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["UTF-8",":TSF_encoding","0",":TSF_fin."])),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_argv:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(TSF_argv)),TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("TSF_py:",TSF_log=TSF_debug_log)
    TSF_debug_log=TSF_io_printlog("\t{0}".format("\t".join(["Python{0.major}.{0.minor}.{0.micro}".format(sys.version_info),sys.platform,TSF_io_stdout])),TSF_log=TSF_debug_log)
    return TSF_debug_log

if __name__=="__main__":
    print("")
    print("--- {0} ---".format(sys.argv[0]))
    TSF_debug_savefilename="debug/TSF_io_debug.txt"
    TSF_debug_log=TSF_io_debug(sys.argv)
    TSF_io_savetext(TSF_debug_savefilename,TSF_debug_log)
    print("")
    try:
        print("--- {0} ---\n{1}".format(TSF_debug_savefilename,TSF_debug_log))
    except:
        print("can't 'print(TSF_debug_savefilename,TSF_debug_log)'")
    finally:
        pass
    sys.exit()
