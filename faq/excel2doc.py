import os

import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

from common.constants import LOCAL_MODEl, MODEL_URL

FOLDER_PATH = "faq_db"

# 1. 读取 Excel
df = pd.read_excel("FAQ.xlsx")

# 2. 构造成文档格式
docs = []
for idx, row in df.iterrows():
    main_name = str(row["主板块名称"])
    function = str(row["分类"])
    answer = str(row["描述"])
    content = f"main_name: {main_name}\nfunction: {function}\nanswer: {answer}"
    docs.append(Document(page_content=content))

# 3. 文本切分（可选）
splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=5)
split_docs = splitter.split_documents(docs)

# 4. 向量化 + 建索引
embedding = OllamaEmbeddings(model=LOCAL_MODEl, base_url=MODEL_URL)
if not os.path.exists(FOLDER_PATH):
    vectorstore = FAISS.from_documents(split_docs, embedding)
    vectorstore.save_local(FOLDER_PATH)
else:
    vectorstore = FAISS.load_local(FOLDER_PATH, embedding,allow_dangerous_deserialization=True)
