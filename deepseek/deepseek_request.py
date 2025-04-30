import requests

headers = {
    "Authorization": "Bearer sk-cd5abdb0e736483e8a630b86cb709b07",
    "Content-Type": "application/json"
}
json_data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "介绍一下 LangChain"}],
    "temperature": 0.7
}

r = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=json_data)

print("状态码:", r.status_code)
print("响应内容:", r.text)
