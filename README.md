# プログラミング言語「TSF_Tab-Separated-Forth」開発予定。

目標は「LTsv10kanedit」の「kanedit.vim」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonで。  

    TSF_Tab-Separated-Forth:
    	main:	:TSF_call	:TSF_fin.
    
    main:
   		about:	:TSF_push	about:	:TSF_diclen	:TSF_reverse	about:	:TSF_diclen	:TSF_prints
    
    about:
    	「TSF」の文法暫定案。
    	「TSF_Tab-Separated-Forth:」を先頭に置くのが慣習。先頭辞書が初期スタックになるので「:TSF_fin.」も極力付ける。
    	文字列と辞書名とワード(関数)との文法上区別が無いので、便宜上辞書名に後方コロン、命令文に先頭コロンを用いてる。
    	特に命令文は文字データと被らないよう別の言葉に置換エスケープできるようにする予定。
    	辞書名は行頭にタブを含まない。辞書データ＝スタックは行頭にタブを設置。辞書名と辞書データのワンライナー&#40;一行&#41;化は可。
        0文字列が有効なのでタブ文字の連続や末尾のタブでスタック数は増加するので注意。
    	末尾再帰はループ。深い階層で祖先を「:TSF_call」すると関数スタックがまとめてpopされる。関数スタックは辞書とは別に存在。
    	関数の返り値は存在しない。スタックに「:TSF_push」して「:TSF_pop」するだけ。スタックの単位はタブで区切られた文字列。

    corefunction:
    	構想中…
    	「:TSF_cal」「:TSF_push」「:TSF_pop」「:TSF_diclen」「:TSF_print」「:TSF_fin」などは暫定というか、
    	これらを文字データと被らないように置換する関数がまず必要。

    oneliner:	ワンライナーは許可。「kanmap.tsv」や「kanchar.tsv」を直接読み書きできる程度の互換性を確保する。


## 動作環境&#40;予定&#41;。

「Tahrpup6.0.5,Python2.7.6,vim.gtk7.4.52」および「Wine1.7.18,Python3.4.4,gvim8.0.134」で開発になると思います。  


## ライセンス・著作権など&#40;予定&#41;。

Copyright (c) 2017 ooblog  
License: MIT  
[https://github.com/ooblog/TSF1KEV/blob/master/LICENSE](LICENSE "https://github.com/ooblog/TSF1KEV/blob/master/LICENSE")  

