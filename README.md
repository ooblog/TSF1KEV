# プログラミング言語「TSF_Tab-Separated-Forth」開発予定。

目標は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」の「[LTsv/kanedit.vim](LTsv/kanedit.vim "LTsv/kanedit.vim")」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonで。  

    TSF_Tab-Separated-Forth:
    	UTF-8	#TSF_encoding	main1:	#TSF_this	0	#TSF_fin.
    
    main1:
    	aboutTSF:	#TSF_pushthe	aboutTSF:	#TSF_lenthe	#TSF_echoes	main2:	#TSF_this
    
    main2:
    	#分数電卓のテスト	#TSF_echo	16	#TSF_calcPR	calcQQtest:	#TSF_this	calcFXtest:	#TSF_this	calcDCtest:	#TSF_this	calc日本語風:	#TSF_this	#	#TSF_echo	main3:	#TSF_this
    
    main3:
    	aboutCalc:	#TSF_pushthe	aboutCalc:	#TSF_lenthe	#TSF_echoes
    
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
    	「1/3-m1|2」→	1/3-m1|2	#TSF_calcQQ	2	#TSF_join	#TSF_echo
    
    calcFXtest:
    	「1 3 m1|2」を数式風に「[2]/[1]-[0]」で連結→	1	3	1|2	[2]/[1]-[0]	#TSF_calc[]	#TSF_calcFX	2	#TSF_join	#TSF_echo
    
    calcDCtest:
    	「1 / 3 - m1|2」まで分解して連結(ついでに小数デモ)→	1	/	3	-	m1|2	5	#TSF_join	#TSF_calcDC	2	#TSF_join	#TSF_echo
    
    calc日本語風:
    	日本語風に「一割る三引くマイナス二分の一」→	一割る三引くマイナス二分の一	#TSF_calcKN	2	#TSF_join	#TSF_echo
    
    aboutCalc:
    	「calc」系ワード分数電卓の概要(暫定案)。
    	「#TSF_calcQQ」「#TSF_calcFX」「#TSF_calcDC」と３つも電卓用ワード(関数)があるが、基本的には同じ分数計算。
    	「#TSF_calcDC」は小数表示用途。「#TSF_calcQQ」は数式を九九のように暗記(参照透過風)。
    	「#TSF_calc{}」「#TSF_calc[]」「#TSF_calc｢｣」ワードもあるが、計算ではなく「#TSF_join」など文字列連結操作扱い。
    	「/」割り算と「|」分数は分けて表記。数値の「p」プラス「m」マイナスは演算子の「+」プラス「-」マイナスと分けて表記。
    	アラビア数字の他に漢数字〇一二三四五六七八九十百千万億兆京なども使用可能。「#TSF_calcKN」で計算結果も一部漢数字使用可。
    	「#TSF_calcPR」で有効桁数の調整。初期値は72桁(千無量大数)。「π」(円周率)「ｅ」(ネイピア数)の都合で4桁から100桁の範囲。
    	自然対数(logｅ)は「E」。常用対数(log10)は「L」。無理数は分数に丸められるので「E256/E2」や「L256/L2」が8にならない問題中。
    	「kM1~10」で1から10まで合計するような和数列(総和)が使える。同様に「kP1~10」で積数列(総乗)を用いた階乗の計算も可能。
    	0で割るもしくは有効桁数溢れなど、何らかの事情で計算できない場合は便宜上「n|0」という事にする。「p」「m」は付かない。

    #分数電卓のテスト
    「1/3-m1|2」→p5|6
    「1 3 m1|2」を数式風に「[2]/[1]-[0]」で連結→m1|6
    「1 / 3 - m1|2」まで分解して連結(ついでに小数デモ)→0.8333333333333333
    日本語風に「一割る三引くマイナス二分の一」→6分の5
    #

TSFはまだ開発中なので、漢直をお探しの方は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」をお使いください。  


## 動作環境&#40;予定&#41;。

「Tahrpup6.0.5,Python2.7.6,vim.gtk7.4.52&#40;vim-gtk&#41;」および「Wine1.7.18,Python3.4.4,gvim8.0.134&#40;KaoriYa&#41;」で開発になると思います。  


## ライセンス・著作権など&#40;予定&#41;。

Copyright (c) 2017 ooblog  
License: MIT  
[https://github.com/ooblog/TSF1KEV/blob/master/LICENSE](LICENSE "https://github.com/ooblog/TSF1KEV/blob/master/LICENSE")  

