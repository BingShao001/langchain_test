from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key="sk-49647c02e4d74b3e8f71b96fb4a63080",
    openai_api_base="https://api.deepseek.com/v1",  # 替换为 DeepSeek 地址
    model_name="deepseek-chat",                     # 支持的模型如 deepseek-chat、deepseek-coder
    temperature=0.7
)

response = llm.predict("用一句话介绍LangChain")
print(response)
