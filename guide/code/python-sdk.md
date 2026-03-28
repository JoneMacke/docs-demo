---
sidebar: false
---

# 🐍 Python SDK

枫叶AI Python SDK，方便 Python 开发者快速集成。

## 安装

```bash
pip install maple-ai-sdk
```

## 快速开始

```python
from maple_ai import MapleAI

client = MapleAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="maple-ai-v1",
    messages=[
        {"role": "user", "content": "你好"}
    ]
)

print(response.choices[0].message.content)
```

## 流式输出

```python
stream = client.chat.completions.create(
    model="maple-ai-v1",
    messages=[{"role": "user", "content": "写一首诗"}],
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
```
