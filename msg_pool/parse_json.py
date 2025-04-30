import json
import re

def extract_msg_list_from_dict(response_dict):
    # 如果你拿到的是完整结构的数据，直接抽 msg 数组
    msg_list = response_dict.get("result") or response_dict.get("messages") or response_dict  # 根据结构适配
    if isinstance(msg_list, str):
        return extract_msg_list(msg_list)  # 调用之前写的字符串版解析器
    elif isinstance(msg_list, list):
        # 结构正确，直接过滤
        return [
            {"msg_type": item["msg_type"], "msg": item["msg"]}
            for item in msg_list
            if isinstance(item, dict) and "msg_type" in item and "msg" in item
        ]
    else:
        raise ValueError("未知数据格式")

def extract_msg_list(response_text):
    # 尝试提取一个 JSON 数组块（匹配 [ {...}, {...} ] 结构）
    match = re.search(r'\[\s*{.*?}\s*\]', response_text, re.DOTALL)
    if not match:
        raise ValueError("未找到合法的 JSON 数组")

    json_str = match.group(0)

    try:
        msg_list = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError("解析 JSON 失败") from e

    # 可选：确保只保留 msg_type 和 msg 字段
    clean_list = [
        {"msg_type": item["msg_type"], "msg": item["msg"]}
        for item in msg_list
        if isinstance(item, dict) and "msg" in item and "msg_type" in item
    ]

    return clean_list

