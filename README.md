# 方法1: 開発環境での直接実行

1. 必要なファイルを準備
requirements.txt を作成
echo "Flask==2.3.3" > requirements.txt
echo "gunicorn==21.2.0" >> requirements.txt

2. 依存関係をインストール
pip install -r requirements.txt

3. 開発サーバーで実行
ファイル名がmain.pyの場合
flask --app main run

# 方法2: Dockerで実行

1. Dockerfileと一緒にビルド
docker build -t my-flask-app .

2. コンテナを実行
PORTを5000に設定して実行
docker run -p 5000:5000 -e PORT=5000 my-flask-app

# 方法3: Gunicornで本番環境風に実行

直接gunicornコマンドで実行
gunicorn main:app --bind 0.0.0.0:5000 --workers 2 --threads 4

# アクセス方法
どの方法で実行しても、ブラウザで以下のURLにアクセスできます：
http://localhost:5000