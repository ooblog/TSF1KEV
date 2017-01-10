# プログラミング言語「TSF_Tab-Separated-Forth」開発予定。

目標は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」の「[LTsv/kanedit.vim](LTsv/kanedit.vim "LTsv/kanedit.vim")」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonで。  

    TSF_Tab-Separated-Forth:
    	main:	:TSF_call	:TSF_fin.
    
    main:
   		about:	:TSF_push	about:	:TSF_diclen	:TSF_reverseS	about:	:TSF_diclen	:TSF_echoeS
    
    about:
    	「TSF」の文法暫定案。
    	「TSF_Tab-Separated-Forth:」を先頭に置くのが慣習。先頭辞書が初期スタックになるので「:TSF_fin.」も極力付ける。
    	文字列と辞書名とワード(関数)との文法上区別が無いので、便宜上辞書名に後方コロン、命令文に先頭コロンを用いてる。
    	特に命令文は文字データと被らないよう別の言葉に置換エスケープできるようにする予定。
    	辞書名は行頭にタブを含まない。辞書データ＝スタックは行頭にタブを設置。辞書名と辞書データのワンライナー(一行)化は可。
        0文字列が有効なのでタブ文字の連続や末尾のタブでスタック数は増加するので注意。
    	末尾再帰はループ。深い階層で祖先を「:TSF_call」すると関数スタックがまとめてpopされる。関数スタックは辞書とは別に存在。
    	関数の返り値は存在しない。スタックに「:TSF_push」して「:TSF_pop」するだけ。スタックの単位はタブで区切られた文字列。

    corefunction:
    	構想中…
    	ワード(関数)は単数形複数形を用意して、複数形の直前にスタックを読み込む個数を指定する。単数形の個数は関数毎に異なる。
    	上記「main:」文の関数は暫定というか、これらを文字データと被らないように置換する関数がまず必要。
    	スタック操作の関数構想中…。ファイル読書日時電卓などは「LTsv10kanedit」モジュールがベースになると思う。

    oneliner:	ワンライナーは許可。「kanmap.tsv」や「kanchar.tsv」を直接読み書きできる程度の互換性を確保する。

TSFはまだ開発中なので、漢直をお探しの方は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」をお使いください。  


## 動作環境&#40;予定&#41;。

「Tahrpup6.0.5,Python2.7.6,vim.gtk7.4.52」および「Wine1.7.18,Python3.4.4,gvim8.0.134」で開発になると思います。  


## ライセンス・著作権など&#40;予定&#41;。

Copyright (c) 2017 ooblog  
License: MIT  
[https://github.com/ooblog/TSF1KEV/blob/master/LICENSE](LICENSE "https://github.com/ooblog/TSF1KEV/blob/master/LICENSE")  
