# プログラミング言語「TSF_Tab-Separated-Forth」開発予定。

目標は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」の「[LTsv/kanedit.vim](LTsv/kanedit.vim "LTsv/kanedit.vim")」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonで。  

    TSF_Tab-Separated-Forth:
    	main:	:TSF_call	:TSF_fin.
    
    main:
    	about:	:TSF_push	about:	:TSF_len	:TSF_echoes
    
    about:
    	「TSF_Tab-Separated-Forth:」の概要(暫定案)。
    	スタックはtsv単位。積んだスタックをワード(関数)で消化していくForth風構文。
    	文字で始まる行はスタック名、タブで始まる行はスタック列内容。名と列のワンライナー記述可能。
    	改行のみ行はスルーだが、二重タブや末尾タブは0文字列とみなされスタック数増加に繋がるので注意。
    	末尾再帰はループ。深い階層で祖先を「:TSF_call」すると子孫コールスタックはまとめて破棄される。
    	「:TSF_calc」という括弧が使える電卓を用意する予定なので逆ポーランド記法は強いられないはず。

TSFはまだ開発中なので、漢直をお探しの方は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」をお使いください。  


## 動作環境&#40;予定&#41;。

「Tahrpup6.0.5,Python2.7.6,vim.gtk7.4.52」および「Wine1.7.18,Python3.4.4,gvim8.0.134」で開発になると思います。  


## ライセンス・著作権など&#40;予定&#41;。

Copyright (c) 2017 ooblog  
License: MIT  
[https://github.com/ooblog/TSF1KEV/blob/master/LICENSE](LICENSE "https://github.com/ooblog/TSF1KEV/blob/master/LICENSE")  

