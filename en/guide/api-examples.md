---
sidebar: false
prev:
  text: 'Quick Start'
  link: '/en/guide/quickstart'
next:
  text: 'Get Token'
  link: '/en/guide/token'
---

# 📡 API Examples

This page shows common **MapleAI** API call examples to help you get started quickly.

::: tip 💡 Prerequisites
Before you begin, make sure you have:
1. Registered and obtained an API Key (`sk-xxxxxx`)
2. Know the name of the model you want to call
:::

---

## 🔧 Add Provider

<a href="/en/guide/api-notes/provider" style="display:inline-block;margin-bottom:12px;padding:6px 14px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;font-size:14px;">📝 View Detailed Notes →</a>

Add a custom model service provider (Provider):

::: warning ⚠️ Key Step
This is a critical configuration step! Add the following JSON code snippet to the `models.providers` block, and replace with your own real API key.
:::

```json
{
  "models": {
    "providers": {
      "Claude": {
        "baseUrl": "https://ai.katioai.com",
        "apiKey": "sk-xxxxxx-your-real-key",
        "api": "anthropic-messages",
        "models": [
          {
            "id": "claude-opus-4-6",
            "name": "claude-opus-4-6",
            "reasoning": false,
            "input": ["text"],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 200000,
            "maxTokens": 8192
          }
        ]
      }
    }
  }
}
```

| Parameter | Description |
| :--- | :--- |
| `baseUrl` | API service address |
| `apiKey` | Your API key, replace with your real value |
| `api` | API protocol type |
| `contextWindow` | Context window size (token count) |
| `maxTokens` | Maximum output tokens |

---

## 🌐 cURL Call Example

<a href="/en/guide/api-notes/curl" style="display:inline-block;margin-bottom:12px;padding:6px 14px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;font-size:14px;">📝 View Detailed Notes →</a>

Directly call the **Chat Completions API** via cURL:

```bash
curl https://ai.katioai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxxxxx-your-real-key" \
  -d '{
    "model": "gemini-3-pro-preview",
    "messages": [
      {
        "role": "user",
        "content": "Hi!"
      }
    ]
  }'
```

::: details 📋 Request Parameter Description
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `model` | `string` | Name of the model to call |
| `messages` | `array` | Message list, containing `role` and `content` |
| `messages[].role` | `string` | Role type: `system`, `user`, `assistant` |
| `messages[].content` | `string` | Message content |
:::

---

## 🐍 Python Call Example

<a href="/en/guide/api-notes/python" style="display:inline-block;margin-bottom:12px;padding:6px 14px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;font-size:14px;">📝 View Detailed Notes →</a>

Use the official OpenAI SDK to call the MapleAI API — just modify `base_url` and `api_key`:

::: info 📦 Install Dependencies
```bash
pip install openai
```
:::

```python
from openai import OpenAI

# Initialize client, pointing to MapleAI API
client = OpenAI(
    api_key="sk-xxxxxxxx",          # Replace with your real API key
    base_url="https://ai.katioai.com/v1"  # MapleAI API address
)

# Make a chat completion request
response = client.chat.completions.create(
    model="gemini-3-pro-preview",   # Specify model
    messages=[
        {"role": "user", "content": "Hi!"}
    ]
)

# Print result
print(response)
```

::: tip 🎯 Tips
- Replace `sk-xxxxxxxx` with your real API Key
- The `model` parameter can be replaced with other supported model names
- The API is compatible with OpenAI SDK, migration cost is very low
:::
