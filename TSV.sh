#!/bin/sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
cd $script_dir
cd TSFpy/
./TSF_Forth.py

