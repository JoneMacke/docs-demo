---
sidebar: false
prev:
  text: 'API Examples'
  link: '/en/guide/api-examples'
next: false
---

# 🐍 Python Call Notes

> This page provides detailed annotations for the Python call example, helping you quickly understand and integrate with KatioAI services.

---

## ✨ Overview

This example demonstrates how to use the official `openai` Python SDK to access **KatioAI** services through an OpenAI-compatible API.

Suitable for the following scenarios:

- 🧪 Quick verification that the API works
- 📄 Minimal example for project integration
- 📖 For README, development docs, or integration guides

---

## 🚀 Features

| Feature | Description |
| :--- | :--- |
| ✅ OpenAI SDK Compatible | No extra learning needed, directly reuse existing code |
| ✅ Custom `base_url` | Easily switch to KatioAI service |
| ✅ Chat Completions API | Supports single and multi-turn conversations |
| ✅ Environment Variable Config | Secure API Key management |
| ✅ Minimal Runnable Example | Ready to use out of the box |

---

## 📦 Install Dependencies

::: info 📦 Prerequisites
Please install the official Python SDK first (requires Python 3.7+):
```bash
pip install openai
```
:::

---

## ⚡ Quick Start

Here is the simplest runnable example:

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxxxxxxxxx",                   # Replace with your real key
    base_url="https://ai.katioai.com/v1"       # KatioAI API address
)

response = client.chat.completions.create(
    model="gemini-3-pro-preview",               # Specify model
    messages=[
        {"role": "user", "content": "Hi!"}
    ]
)

print(response.choices[0].message.content)
```

::: tip 💡 Tips
Make sure to replace `api_key` with your real API Key before running.
:::

---

## 🛠 Configuration Guide

Before using, please confirm the following **3 key settings**:

### 1️⃣ API Key

Replace the example API Key with your real key:

```python
api_key="sk-xxxxxxxxxx"
```

### 2️⃣ Base URL

Use the following API address:

```python
base_url="https://ai.katioai.com/v1"
```

### 3️⃣ Model

The example model is:

```python
model="gemini-3-pro-preview"
```

::: warning ⚠️ Note
If the platform supports different model names, please replace accordingly.
:::

---

## 🧩 Complete Examples

### Basic Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxxxxxxxxx",
    base_url="https://ai.katioai.com/v1"
)

response = client.chat.completions.create(
    model="gemini-3-pro-preview",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

### Multi-turn Conversation Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxxxxxxxxx",
    base_url="https://ai.katioai.com/v1"
)

response = client.chat.completions.create(
    model="gemini-3-pro-preview",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain in one sentence how to integrate KatioAI."}
    ]
)

print(response.choices[0].message.content)
```

::: info 🧩 Role Description
| Role | Purpose |
| :--- | :--- |
| `system` | Sets the AI's behavior and role |
| `user` | Messages sent by the user |
| `assistant` | AI's replies (used for context passing) |
:::

---

## 🔐 Using Environment Variables

::: danger 🔐 Security Warning
For security reasons, it is **strongly recommended** not to hardcode API Keys in your source code. Use environment variables to manage keys instead.
:::

### Linux / macOS

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxx"
```

### Windows PowerShell

```powershell
setx OPENAI_API_KEY "sk-xxxxxxxxxx"
```

### Reading Environment Variables in Python

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),        # Read from environment variable
    base_url="https://ai.katioai.com/v1"
)

response = client.chat.completions.create(
    model="gemini-3-pro-preview",
    messages=[
        {"role": "user", "content": "Hi!"}
    ]
)

print(response.choices[0].message.content)
```

---

## 📘 Parameter Reference

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `api_key` | `string` | API key, used for authentication |
| `base_url` | `string` | API base address: `https://ai.katioai.com/v1` |
| `model` | `string` | Name of the model to call |
| `messages` | `list` | Chat message list |

::: details 📄 messages Format Example
```python
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hi!"}
]
```
:::

---

## 📤 Response Handling

View the **full response object**:

```python
print(response)
```

Get only the **model's response text**:

```python
print(response.choices[0].message.content)
```

::: tip 💡 Recommendation
In production environments, it is recommended to add exception handling and null checks for `response` to prevent crashes.
:::

---

## ❓ FAQ

::: details 🤔 Why must I set `base_url`?
Because this integrates with a **custom service address** compatible with the OpenAI API, not the SDK's default official OpenAI address.

Please make sure to set it to:
```
https://ai.katioai.com/v1
```
:::

::: details 🔑 What if authentication fails?
Please check the following:

| Check Item | Description |
| :--- | :--- |
| API Key | Is it correct and enabled? |
| `base_url` | Is it filled in correctly? |
| Model name | Is it a valid model supported by the platform? |
:::

::: details 🤖 What if the model doesn't exist?
Replace the following field with a currently available model on the platform:
```python
model="gemini-3-pro-preview"
```
You can check the supported model list in the platform console.
:::

::: details 🔄 Can I use this with existing OpenAI SDK projects?
**Yes!** If your project already uses the OpenAI Python SDK, you only need to change 3 parameters:

| Parameter | Replace With |
| :--- | :--- |
| `api_key` | Your KatioAI key |
| `base_url` | `https://ai.katioai.com/v1` |
| `model` | A model name supported by the platform |
:::

---

## 🧪 Minimal Example

A minimal code snippet suitable for displaying on a homepage or in documentation:

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxxxxxxxxx",
    base_url="https://ai.katioai.com/v1"
)

response = client.chat.completions.create(
    model="gemini-3-pro-preview",
    messages=[{"role": "user", "content": "Hi!"}]
)

print(response.choices[0].message.content)
```

---

## 📁 Recommended Directory Structure

If you plan to put this example into a small project, you can reference the following structure:

```
.
├── README.md            # Project description
├── requirements.txt     # Dependencies
└── example.py           # Example code
```

::: details 📋 requirements.txt
```txt
openai>=1.0.0
```
:::

::: details 📋 example.py
```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxxxxxxxxx",
    base_url="https://ai.katioai.com/v1"
)

response = client.chat.completions.create(
    model="gemini-3-pro-preview",
    messages=[
        {"role": "user", "content": "Hi!"}
    ]
)

print(response.choices[0].message.content)
```
:::

---

## 📝 Important Notes

::: danger 🔐 Key Security
- Never commit real API Keys to public repositories
- Use environment variables to manage keys whenever possible
:::

::: tip 🎯 Usage Recommendations
- Model names should match the platform's actual supported list
- To integrate more APIs, extend from this example
- Add error handling and retry logic in production environments
:::

---

<a href="/en/guide/api-examples" style="display:inline-block;padding:8px 16px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;">← Back to API Examples</a>
