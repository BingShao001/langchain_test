from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from common.constants import LOCAL_MODEl, MODEL_URL
from faq.excel2doc import vectorstore

llm = ChatOllama(model=LOCAL_MODEl, base_url=MODEL_URL, temperature=0.3)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_type="similarity", k=2),
    return_source_documents=True,
)
