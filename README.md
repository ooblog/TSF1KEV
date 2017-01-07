# プログラミング言語「TSF_Tab-Separated-Forth」開発予定。目標は「LTsv10kanedit」の「kanedit.vim」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonで。

    TSF_Tab-Separated-Forth:
    	main:	:TSF_call	:TSF_fin.
    
    main:
   		about:	:TSF_push	about:	:TSF_diclen	:TSF_reverse	about:	:TSF_diclen	:TSF_prints
    
    about:
    	「TSF」の文法暫定案。
    	「TSF_Tab-Separated-Forth」を先頭に置くのが慣習。先頭辞書が初期スタックになるので「:TSF_fin.」も極力付ける。
    	文字列と辞書名とワード(関数)との文法上区別が無いので、便宜上辞書名に後方コロン、命令文に先頭コロンを用いてる。
    	特に命令文は文字データと被らないよう別の言葉に置換エスケープできるようにする予定。
    	辞書名は行頭にタブを含まない。辞書データ＝スタックは行頭にタブを設置。
        0文字列が有効なのでタブ文字の連続や末尾のタブでスタック数は増加するので注意。
    	末尾再帰はループ。深い階層から祖先を「:TSF_call」すると末裔スタックがまとめてpopされる。関数スタックは辞書とは別に存在。
    	関数の返り値は存在しない。スタックをに「:TSF_push」して「:TSF_pop」するだけ。スタックの単位はタブで区切られた文字列。

    corefunction:
    	構想中…
    	「:TSF_cal」「:TSF_push」「:TSF_pop」「:TSF_diclen」「:TSF_print」「:TSF_fin」などは暫定というか、
    	これらを文字データと被らないように置換する関数がまず必要。
