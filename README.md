# Glithcer
多分使える。ベースの画像も用意する。ベースの画像以外で、作成すると、バイナリのオフセットとかが違うから使用できないはずだよ。とりあえず使い方は、PY内の、MOVEVALUEが移動する値。0x10以上にすると、多分FAILDが増える。256byte以上の書き込みがあった場合、そこは0x00で置き換えられるよ。で、ベース画像を読み込むだけ。必ず、アニメの画像でも何でもいいから、＊全部同じ色のファイルははじかれる。バイナリ分かる人ならわかる。
