# アプリケーション名

kyuzyoushoutwitter.py

# アプリケーション概要

APIを利用してtwitterにyoutubeの急上昇動画を載せるコードを作成しました。
ターミナルのcronを使ってbot化しました。
曜日を利用して月曜日には急上昇１位の動画情報を取得し曜日ごとに違う順位の動画を取得します。
・月~日・・・1~7位

# URL

https://github.com/TAKAi3y0/twitterbot

# 各種API

・TwitterAPI
CK = "APIkey"
CS = "APIkeysecret"
AT = "Accesstoken"
AS = "Accesstokensecret"

・YouTubeDataAPIv3
DEVELOPER_KEY = "youtubeAPI"
YOUTUBE_API_SERVICE_NAME = "youtube"

# 利用方法

投稿したいtwitterのアカウントとGoogleのアカウントを作成してください。
作成したアカウントから各種APIを取得し、環境変数を使用し変数に代入してください。
PYTHON3で実行するためパスを通します。(MacOSのデフォルトがPYTHON2のため)
ターミナルで"echo $PATH"コマンドを実行し、"PATH=/~~~~"と表示されるのでコピー。
ターミナルにて"crontab -e"コマンドを実行し、crontabを開き先程コピーしたPATHを貼り付けます。
改行して
X Y * * * python /ファイルの絶対パス/kyuzyoushoutwitter.py > /Users/ユーザー名/Desktop/exec-error.log 2>&1
を貼り付けます。
Xには何分に投稿したいかを入力します。(0~59の整数)
Yには何時に投稿したいかを入力します。(0~23の整数)
*の部分は全てを意味しますので上記の記述だと毎日何時何分に投稿する設定になります。
絶対パスの後の記述を記載しておくとデスクトップにエラーログを表示します。

# 目的

情報を検索し、SNSで拡散するという時間をなくすために作成した。
Twitterを自動で運用し、ニーズのある情報を拡散する。(今回はYouTubeのAPIを使用しているがインターネットニュースの記事などでも良い)

# これからの課題

・Bot化をローカル環境(cron)ではなく、クラウド上で行う
・フレームワークの実装

# ローカルでの動作方法

・macのバージョン
macOS Catalina 10.15.7
・Pythonのバージョン
3.7.3