from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama

from common.constants import LOCAL_MODEl, MODEL_URL
from msg_pool.msg_pool_excel2doc import vectorstore
from msg_pool.parse_json import extract_msg_list_from_dict
from msg_pool.prompt import msg_prompt

# 初始化语言模型
llm = ChatOllama(model=LOCAL_MODEl, base_url=MODEL_URL, temperature=0.0)


# 定义自定义 Prompt
# RetrievalQA 会自动帮你检索到文档并把结果放到 {context}
# 用户的问题 query 会放到 {question}
# 最终拼接出完整的 Prompt 给大模型调用
qa_prompt = PromptTemplate(
    input_variables=["question","context"],
    template=msg_prompt
)

# 创建 RetrievalQA 链（传入自定义 Prompt）
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_type="similarity", k=2),
    return_source_documents=False,
    chain_type_kwargs={"prompt": qa_prompt}  # 关键参数
)

query = "请提供3条暧昧类型的消息。分别用汉语和英语来输出"
response = qa_chain.invoke(query)
print(extract_msg_list_from_dict(response))
