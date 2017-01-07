# プログラミング言語「TSF_Tab-Separated-Forth」開発予定。目標は「LTsv10kanedit」の「kanedit.vim」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonで。

    TSF_Tab-Separated-Forth:
    	main:	:TSF_call	:TSF_fin.
    
    main:
   		about:	:TSF_push	about:	:TSF_diclen	:TSF_reverse	about:	:TSF_diclen	:TSF_prints
    
    about:
    	「TSF」の文法暫定案。
    	「TSF_Tab-Separated-Forth」を先頭に置くのが慣習。先頭辞書が初期スタックになるので「:TSF_fin.」も極力付ける。
    	文字列と辞書名と関数との文法上の区別は無いので、便宜上辞書名に後方コロン、命令文に先頭コロンを用いてる。特に命令文は別の言葉に置換エスケープできるようにする予定。
    	辞書名は行頭にタブを含まない。辞書データ＝スタックは行頭にタブを設置。0文字列有効なのでタブ文字の連続や末尾のタブでスタック増加するので注意。
    	末尾再帰はループ。祖先を「:TSF_call」すると末裔が無かった事になる(関数呼び出しスタックがまとめてpopされる)。スタックや辞書の書き替えは残る。
    	関数の返り値は存在しないし変数も存在しない。スタックをに「:TSF_push」して「:TSF_pop」するだけ。スタックの単位はタブで区切られた文字列。

    corefunction:
    	構想中…
    	「:TSF_cal」「:TSF_push」「:TSF_pop」「:TSF_diclen」「:TSF_print」「:TSF_fin」などは暫定というか、これらを置換する関数がまず必要。
