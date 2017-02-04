# プログラミング言語「TSF_Tab-Separated-Forth」開発予定。

目標は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」の「[LTsv/kanedit.vim](LTsv/kanedit.vim "LTsv/kanedit.vim")」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonで。  

    TSF_Tab-Separated-Forth:
    	UTF-8	#TSF_encoding	main:	#TSF_this	0	#TSF_fin.
    
    main:
    	about:	#TSF_pushthe	about:	#TSF_lenthe	#TSF_echoes	calcQQtest:	#TSF_this	calcFXtest:	#TSF_this
    
    about:
    	「TSF_Tab-Separated-Forth」の概要(暫定案)。
    	積んだスタックをワード(関数)などで消化していくForth風インタプリタ。スタック単位はtsv文字列。
    	文字から始まる行はスタック名、タブで始まる行はスタック内容。改行のみもしくは「#」で始まる行は読み飛ばし。
    	タブのみ行は1スタック計算。他にも二重タブや末尾タブが文字列長0のスタックとみなされるので注意。
    	起動時のスタック(thisスタックthatスタック両方とも)は「TSF_Tab-Separated-Forth:」なのでargvもそこに追加される。
    	TSFでは先頭からワードを実行するthisスタックと末尾に引数などを積み上げるthatスタックを別々に指定できる。
    	そもそもスタックが複数ある。他言語で言う変数の代わりにスタックがある。他言語で言う関数の引数や返り値もスタック経由。
    	存在しないthatスタックからの取得(存在するスタックのアンダーフロー含む)は0文字列を返却する。
    	存在しないthisスタックの呼び出し(存在するスタックのオーバーフロー含む)は呼び出し元に戻って続きから再開。
    	末尾再帰はループ。深い階層で祖先を「#TSF_this」すると子孫コールスタックはまとめて破棄される(未実装)。
    	「#TSF_calc[]」などの括弧と「#TSF_calcFX」などの分数電卓を用意したので逆ポーランド記法の数式計算は強いられないはず。
    
    calcQQtest:
    	QQ(1/3+1|2)=	#TSF_echo	1/3+1|2	#TSF_calcQQ	#TSF_echo
    
    calcFXtest:
    	FX(1/3+1|2)=	#TSF_echo	1/3	1|2	[1]+[0]	#TSF_calc[]	#TSF_calcFX	#TSF_echo
    
    calcDCtest:
    	DC(1/3+1|2)=	#TSF_echo	1/3	1|2	[1]+[0]	#TSF_calc[]	#TSF_calcDC	#TSF_echo

TSFはまだ開発中なので、漢直をお探しの方は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」をお使いください。  


## 動作環境&#40;予定&#41;。

「Tahrpup6.0.5,Python2.7.6,vim.gtk7.4.52&#40;vim-gtk&#41;」および「Wine1.7.18,Python3.4.4,gvim8.0.134&#40;KaoriYa&#41;」で開発になると思います。  


## ライセンス・著作権など&#40;予定&#41;。

Copyright (c) 2017 ooblog  
License: MIT  
[https://github.com/ooblog/TSF1KEV/blob/master/LICENSE](LICENSE "https://github.com/ooblog/TSF1KEV/blob/master/LICENSE")  

