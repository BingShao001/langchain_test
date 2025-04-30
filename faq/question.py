from faq.faq_rag import qa_chain

query = "我怎么样能获得pop积分？"
result = qa_chain.invoke({"query": query})
print("\n📌 回答：", result["result"])
print("\n📄 来源：")
for doc in result["source_documents"]:
    print("-", doc.page_content)