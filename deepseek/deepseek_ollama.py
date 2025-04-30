from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:1.5b",  # 或者 deepseek-chat
    base_url="http://localhost:11434",
    temperature=0.7,
)

response = llm.invoke("介绍一下 LangChain 怎么结合社交类产品")
print(response.content)
