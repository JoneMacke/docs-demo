---
sidebar: false
---

# 📡 API Examples

This page shows common API call examples for Maple AI.

## Chat API

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
      { role: 'system', content: 'You are a helpful assistant' },
      { role: 'user', content: 'Introduce yourself' }
    ]
  })
})

const data = await response.json()
console.log(data.choices[0].message.content)
```

## Image Generation

```python
import requests

response = requests.post(
    'https://api.example.com/v1/images',
    headers={'Authorization': 'Bearer YOUR_API_KEY'},
    json={'prompt': 'A cute maple leaf cat', 'size': '1024x1024'}
)
print(response.json()['data'][0]['url'])
```

## Streaming

```javascript
const response = await fetch('https://api.example.com/v1/chat', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    model: 'maple-ai-v1',
    messages: [{ role: 'user', content: 'Write a poem' }],
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
