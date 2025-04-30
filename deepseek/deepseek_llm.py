from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key="sk-d138256fe3774a9287e149152c902dd3",
    openai_api_base="https://api.deepseek.com/v1",  # 注意 URL 路径
    model_name="deepseek-chat",  # 模型名，如 deepseek-chat
    temperature=0.7
)

response = llm.predict("介绍一下LangChain框架")
print(response)
