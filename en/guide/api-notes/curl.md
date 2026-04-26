---
sidebar: false
prev:
  text: 'API Examples'
  link: '/en/guide/api-examples'
next: false
---

# 🌐 cURL Call Notes

> This page provides detailed annotations for the cURL call example, helping you deeply understand the meaning and usage of each request parameter.

---

## 📌 Basic Call Example

The following example shows how to call the **Chat Completions API** via cURL:

```bash
curl https://ai.katioai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
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

::: tip 💡 Note
This request sends a user message to the chat API, and the specified model generates a reply.
:::

---

## 📋 Request Details

### Headers

| Field | Value | Description |
| :--- | :--- | :--- |
| `Content-Type` | `application/json` | Request body format |
| `Authorization` | `Bearer YOUR_API_KEY` | Authentication token, replace with your real API Key |

### Body Parameters

| Parameter | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `model` | `string` | ✅ | Name of the model to call |
| `messages` | `array` | ✅ | List of conversation messages |

---

### 💬 `messages` Format

Each message contains the following fields:

| Field | Type | Description |
| :--- | :--- | :--- |
| `role` | `string` | Message role, options: `system`, `user`, `assistant` |
| `content` | `string` | Message content |

::: details 📄 messages Example
```json
[
  {
    "role": "user",
    "content": "Hi!"
  }
]
```
:::

---

## 🔄 Multi-turn Conversation Example

By adding multiple messages to `messages`, you can achieve **multi-turn conversation**:

```bash
curl https://ai.katioai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "gemini-3-pro-preview",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Please explain what a README is."
      }
    ]
  }'
```

::: info 🧩 Role Description
| Role | Purpose |
| :--- | :--- |
| `system` | Sets the AI's behavior and role |
| `user` | Messages sent by the user |
| `assistant` | AI's replies (used for context passing) |
:::

---

## ⚠️ Notes

::: warning 🔐 Security Warning
- Replace `YOUR_API_KEY` with your **real API Key**
- **Never** commit API Keys to public repositories like GitHub
- Use environment variables to manage keys, e.g.: `$API_KEY`
:::

::: tip 📝 Other Tips
- Parameters and response formats may vary slightly between models; refer to the actual API documentation
- If you encounter timeout issues, try adding the `--connect-timeout` parameter
- Responses are in JSON format by default; use the `jq` tool to format the output
:::

---

<a href="/en/guide/api-examples" style="display:inline-block;padding:8px 16px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;">← Back to API Examples</a>
