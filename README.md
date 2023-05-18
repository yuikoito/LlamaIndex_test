# このリポジトリについて

LlamaIndex を試してみます

## 環境構築

pip3 install llama_index html2text python-dotenv
touch .env OPENAI_API_KEY=xxx
mkdir tmp
touch tmp/article-urls.csv xxxxx

## 起動コマンド

python3 src/create-index.py
python3 src/query.py
