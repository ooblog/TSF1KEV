# プログラミング言語「TSF_Tab-Separated-Forth」開発予定。

目標は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」の「[LTsv/kanedit.vim](LTsv/kanedit.vim "LTsv/kanedit.vim")」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonで。  

    TSF_Tab-Separated-Forth:
    	UTF-8	#TSF_encoding	main1:	#TSF_this	0	#TSF_fin.
    
    main1:
    	aboutTSF:	#TSF_pushthe	aboutTSF:	#TSF_lenthe	#TSF_echoes	main2:	#TSF_this
    
    main2:
    	#分数電卓のテスト	#TSF_echo	16	#TSF_calcPR	calcQQtest:	#TSF_this	calcFXtest:	#TSF_this	calcDCtest:	#TSF_this	calcKNテスト:	#TSF_this	#	#TSF_echo	main3:	#TSF_this
    
    main3:
    	aboutCalc:	#TSF_pushthe	aboutCalc:	#TSF_lenthe	#TSF_echoes	main4:	#TSF_this
    
    main4:
    	aboutRPN:	#TSF_pushthe	aboutRPN:	#TSF_lenthe	#TSF_echoes	main5:	#TSF_this
    
    main5:
    	aboutCASE:	#TSF_pushthe	aboutCASE:	#TSF_lenthe	#TSF_echoes
    
    aboutTSF:
    	「TSF_Tab-Separated-Forth」の概要(暫定案)。
    	積んだスタックをワード(関数)などで消化していくForth風インタプリタ。スタック単位はtsv文字列。
    	文字から始まる行はスタック名、タブで始まる行はスタック内容。改行のみもしくは「#」で始まる行は読み飛ばし。
    	タブのみ行は1スタック計算。他にも二重タブや末尾タブが文字列長0のスタックとみなされるので注意。
    	起動時のスタック(thisスタックthatスタック両方とも)は「TSF_Tab-Separated-Forth:」なのでargvもそこに追加される。
    	TSFでは先頭からワードを実行するthisスタックと末尾に引数などを積み上げるthatスタックを別々に指定できる。
    	そもそもスタックが複数ある。他言語で言う変数の代わりにスタックがある。他言語で言う関数の引数や返り値もスタック経由。
    	存在しないthatスタックからの取得(存在するスタックのアンダーフロー含む)は0文字列を返却する。
    	存在しないthisスタックの呼び出し(存在するスタックのオーバーフロー含む)は呼び出し元に戻って続きから再開。
    	末尾再帰はループ。深い階層で祖先を「#TSF_this」すると子孫コールスタックはまとめて破棄される(未テスト)。
    	文字列連結は「#TSF_brackets」「#TSF_join」「#TSF_joinC」。文字列分解は「#TSF_split」「#TSF_chars」。
    	「#TSF_brackets」などの文字列連結と「#TSF_calcFX」などの分数電卓を組み合わせれば逆ポーランド記法への数式変換は強いられないはず。
    
    calcQQtest:
    	「1/3-m1|2」→	1/3-m1|2	#TSF_calcQQ	2	#TSF_join	#TSF_echo
    
    calcFXtest:
    	「1 3 m1|2」を数式風に「[2]/[1]-[0]」で連結→	1	3	m1|2	[2]/[1]-[0]	[]	#TSF_brackets	#TSF_calcFX	2	#TSF_join	#TSF_echo
    
    calcDCtest:
    	「1 / 3 - m1|2」まで分解して連結(ついでに小数デモ)→	1	/	3	-	m1|2	5	#TSF_join	#TSF_calcDC	2	#TSF_join	#TSF_echo
    
    calcKNテスト:
    	「一割る三引く(マイナス二分の一)」(ついでに単位付き計算デモ)は	一割る三引く(マイナス二分の一)	を単位付き計算する	2	個分連結	を表示する
    
    aboutCalc:
    	「calc」系ワード分数電卓の概要(暫定案)。
    	「#TSF_calcQQ」「#TSF_calcFX」「#TSF_calcDC」「#TSF_calcKN」と4種類の電卓用ワード(関数)があるが、基本的には分数計算。
    	「#TSF_calcDC」は小数表記。「#TSF_calcKN」億以上の単位を漢字表記。
    	「#TSF_calcQQ」は同じ数式は九九のように暗記(参照透過風)。「#TSF_calcFX」は逆に一度しかしないような計算は暗記しない用途。
    	「#TSF_calcPR」は有効桁数の調整。初期値は72桁(千無量大数)。「π」(円周率)「θ」(2*π)「ｅ」(ネイピア数)などは桁溢れ予防で68桁(一無量大数)。
    	「#TSF_calcRO」は端数処理の調整。初期値は「ROUND_DOWN」(0方向に丸める)。
    	有効桁数「#TSF_calcPR」や端数処理「#TSF_calcRO」など数式の計算結果に影響があると思われる場合は「#TSF_calcQQ」の九九を忘却。
    	「/」割り算と「|」分数は分けて表記。数値の「p」プラス「m」マイナスは演算子の「+」プラス「-」マイナスと分けて表記。
    	通常の割り算の他に1未満を切り捨てる「\」、余りを求める「#」演算子がある。掛け算は「*」演算子。
    	自然対数(logｅ)は「E」。常用対数(log10)は「L」。無理数は分数に丸められるので「E256/E2」や「L256/L2」が8にならない。
    	「81&3l」や「256の二進対数」という任意底対数の演算子は整数同士専用のアルゴリズムを使えるので「256&2l」が8になる。
    	「kM1~10」で1から10まで合計するような和数列(総和)が使える。同様に「kP1~10」で積数列(総乗)を用いて乗数や階乗の計算も可能。
    	(最大)公約数は「12&16G」。(最小)公倍数は「12&16g」。「&」のみを単独で使った場合は掛け算の同じ優先順位で加算する。
    	0で割るもしくは有効桁数溢れなど、何らかの事情で計算できない場合は便宜上「n|0」という事にする。「p」「m」は付かない。
    	「tan(θ*90|360)」なども何かしらの巨大な数ではなく0で割った「n|0」と表記したいがとりあえず未着手。
    	「2分の1を5乗」など日本語風表記で分数を扱う場合は「(2分の1)を5乗」と書かないと「2分の(1を5乗)」と解釈してしまう。
    	ゼロ比較演算子(条件演算子)は「Z」。「kZ1~0」の様な計算でkがゼロでない時は真なので1、ゼロの時は偽なので1。「n|0」の時は「n|0」。
    	条件演算子は0以上を調べる系「O」「o」、0以下を調べる系「U」「u」、0か調べる系「Z」「z」、「n|0」か調べる系「N」を用意。
    
    aboutRPN:
   	「RPN」系ワード逆ポーランド電卓の概要(暫定案)。
   	逆ポーランド記法の数式計算は強いられないとは言ったが、括弧も日本語訳も分数も排除した速度優先の電卓も別途準備(予定)。状況に合わせて使い分け(予定)。
   	「#TSF_calcFX」等に存在した演算優先順位(平方根常用対数など＞積商算公約公倍数任意底対数など＞加減算消費税など＞ゼロ比較演算子数列積和など)は存在しない。
   	分数やdecimal系を用いないので少数の制度が保証できない。
    
    aboutCASE:
    	条件分岐について(未定)。
    	数式と段取りの分離について(仮)。

    #分数電卓のテスト
    「1/3-m1|2」→p5|6
    「1 3 m1|2」を数式風に「[2]/[1]-[0]」で連結→p5|6
    「1 / 3 - m1|2」まで分解して連結(ついでに小数デモ)→0.8333333333333333
    「一割る三引くマイナス二分の一(ついでに単位付き計算デモ)」は6分の5
    #

TSFはまだ開発中なので、漢直をお探しの方は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」をお使いください。  


## 動作環境&#40;予定&#41;。

「Tahrpup6.0.5,Python2.7.6,vim.gtk7.4.52&#40;vim-gtk&#41;」および「Wine1.7.18,Python3.4.4,gvim8.0.134&#40;KaoriYa&#41;」で開発になると思います。  


## ライセンス・著作権など&#40;予定&#41;。

Copyright (c) 2017 ooblog  
License: MIT  
[https://github.com/ooblog/TSF1KEV/blob/master/LICENSE](LICENSE "https://github.com/ooblog/TSF1KEV/blob/master/LICENSE")  

