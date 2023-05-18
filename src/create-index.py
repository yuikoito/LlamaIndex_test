import csv
from llama_index import GPTVectorStoreIndex, SimpleWebPageReader, LLMPredictor
from langchain.chat_models import ChatOpenAI
# .envの読み込み
from dotenv import load_dotenv
load_dotenv()

article_urls = []
with open('tmp/article-urls.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        article_urls.append(row[0])

documents = SimpleWebPageReader().load_data(article_urls)
index =  GPTVectorStoreIndex.from_documents(documents=documents, llm_predictor=LLMPredictor(llm=ChatOpenAI(temperature=0)))
index.storage_context.persist('tmp')
