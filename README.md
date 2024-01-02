# usage
1. ngrokでローカルサーバーを外部に公開
```bash
ngrok http 192.168.3.9:8080
```
2. 表示されたURLを使い、linedevelopersページのmessageing API設定を開きWebhook設定のWebhook URL欄に"URL/callback"と書く。
3. 日本語生成モデルのための環境構築 docker起動
```bash
docker run -it --rm --name line_bot -p 8080:3000 -v $(pwd):/home/work/ --gpus all line_bot:latest
```
4. アプリ起動
```bash
python3 app.py
```
