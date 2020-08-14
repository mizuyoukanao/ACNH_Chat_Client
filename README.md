# ACNH_Chat_Clientとは
「あつまれ どうぶつの森」の非公開APIにアクセスし、特定のフレンドやフレンド全員にメッセージを送れるpythonのGUIプログラムです。
勢いで書いたので雑なのは許して...
[acnh_info_edited.py](acnh_info_edited.py)はxSke氏の[この](https://gist.github.com/xSke/8a4f06f9499a17b3e28cedfc094f57ca)スクリプトを現在のバージョンでも動作するように少しだけ書き換えたものです(でもぶっちゃけほぼコピペです、勝手に使って申し訳ない...)
# つかいかた
1. pythonのライブラリをインストールします

```
pip install requests
```

2. [acnh_info_edited.py](acnh_info_edited.py)を実行します
3. 任天堂のログインページがブラウザで開かれるのでログインしてください（すでにログインしている方は次へ）
4. 「この人にする」ボタンを右クリックして「リンクのアドレスをコピー」してください(画像を参照)

![ログイン画面](https://cdn.discordapp.com/attachments/593485514301243413/743762114824503356/auth_nintendo.png)

5. [acnh_info_edited.py](acnh_info_edited.py)を実行しているウィンドウにペーストし、Enterを押すとTOKENの生成、あつ森のAPIへのログインが始まります。
6. ACNH TOKEN~まで表示されたらログイン完了です。(後で使うので残っているログをメモ帳などに保存しておきましょう)
7. 最後に[acnh_chat_gui.py](acnh_chat_gui.py)を実行します
8. 先ほど抽出したACNH TOKENとフレンドのUser ID等の情報を入力してメッセージを送信できれば成功です!
# すぺしゃるさんくす
[dqn's blog](https://dqnn.hatenablog.com/entry/2020/05/02/005843)、およびに[githubリポジトリ](https://github.com/dqn/acnh)、
[こちらのissuesも参考になりました。](https://github.com/ZekeSnider/NintendoSwitchRESTAPI/issues/13)改めて感謝します!
