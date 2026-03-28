---
sidebar: false
---

# 📡 接口示例

本页展示枫叶AI常用接口的调用示例。

## 对话接口

```javascript
const response = await fetch('https://api.example.com/v1/chat', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    model: 'maple-ai-v1',
    messages: [
      { role: 'system', content: '你是一个有帮助的助手' },
      { role: 'user', content: '请介绍一下自己' }
    ]
  })
})

const data = await response.json()
console.log(data.choices[0].message.content)
```

## 图像生成接口

```python
import requests

response = requests.post(
    'https://api.example.com/v1/images',
    headers={'Authorization': 'Bearer YOUR_API_KEY'},
    json={
        'prompt': '一只可爱的枫叶猫',
        'size': '1024x1024'
    }
)
print(response.json()['data'][0]['url'])
```

## 流式输出

```javascript
const response = await fetch('https://api.example.com/v1/chat', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    model: 'maple-ai-v1',
    messages: [{ role: 'user', content: '写一首诗' }],
    stream: true
  })
})

const reader = response.body.getReader()
const decoder = new TextDecoder()

while (true) {
  const { done, value } = await reader.read()
  if (done) break
  console.log(decoder.decode(value))
}
```
