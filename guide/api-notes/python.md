---
sidebar: false
prev:
  text: '接口示例'
  link: '/guide/api-examples'
next: false
---

# 🐍 Python 调用注释

> 本页为「Python 调用示例」的详细注释说明，帮助你快速理解并接入 KatioAI 服务。

---

## ✨ 项目简介

本示例演示如何使用官方 `openai` Python SDK，通过兼容 OpenAI API 的方式访问 **KatioAI** 服务。

适用于以下场景：

- 🧪 快速验证 API 是否可用
- 📄 作为项目接入时的最小示例
- 📖 用于 README、开发文档或接入说明

---

## 🚀 功能特性

| 特性 | 说明 |
| :--- | :--- |
| ✅ 兼容 OpenAI SDK | 无需额外学习，直接复用现有代码 |
| ✅ 自定义 `base_url` | 轻松切换到 KatioAI 服务 |
| ✅ 聊天补全接口 | 支持单轮 / 多轮对话 |
| ✅ 环境变量配置 | API Key 安全管理 |
| ✅ 最小可运行示例 | 开箱即用，快速上手 |

---

## 📦 安装依赖

::: info 📦 前置要求
请先安装官方 Python SDK（需要 Python 3.7+）：
```bash
pip install openai
```
:::

---

## ⚡ 快速开始

下面是最简单的可运行示例：

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxxxxxxxxx",                   # 替换为你的真实密钥
    base_url="https://ai.katioai.com/v1"       # KatioAI 接口地址
)

response = client.chat.completions.create(
    model="gemini-3-pro-preview",               # 指定模型
    messages=[
        {"role": "user", "content": "Hi!"}
    ]
)

print(response.choices[0].message.content)
```

::: tip 💡 小贴士
运行前请确保已替换 `api_key` 为你的真实 API Key。
:::

---

## 🛠 配置说明

在正式使用前，请确认以下 **3 项关键配置**：

### 1️⃣ API Key

将示例中的 API Key 替换为你的真实密钥：

```python
api_key="sk-xxxxxxxxxx"
```

### 2️⃣ Base URL

请使用以下接口地址：

```python
base_url="https://ai.katioai.com/v1"
```

### 3️⃣ Model

示例模型如下：

```python
model="gemini-3-pro-preview"
```

::: warning ⚠️ 注意
如平台支持的模型名称不同，请按实际情况替换。
:::

---

## 🧩 完整示例

### 基础示例

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

### 多轮消息示例

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
        {"role": "user", "content": "请用一句话介绍如何接入 KatioAI。"}
    ]
)

print(response.choices[0].message.content)
```

::: info 🧩 角色说明
| 角色 | 用途 |
| :--- | :--- |
| `system` | 设定 AI 的行为和角色定位 |
| `user` | 用户发送的消息 |
| `assistant` | AI 的回复（用于上下文传递） |
:::

---

## 🔐 使用环境变量

::: danger 🔐 安全提醒
为了安全起见，**强烈推荐** 不要把 API Key 直接写在代码里，请使用环境变量管理密钥。
:::

### Linux / macOS

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxx"
```

### Windows PowerShell

```powershell
setx OPENAI_API_KEY "sk-xxxxxxxxxx"
```

### Python 中读取环境变量

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),        # 从环境变量读取
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

## 📘 参数说明

| 参数 | 类型 | 说明 |
| :--- | :--- | :--- |
| `api_key` | `string` | API 密钥，用于身份认证 |
| `base_url` | `string` | 接口基础地址：`https://ai.katioai.com/v1` |
| `model` | `string` | 要调用的模型名称 |
| `messages` | `list` | 聊天消息列表 |

::: details 📄 messages 格式示例
```python
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hi!"}
]
```
:::

---

## 📤 响应处理

查看**完整响应对象**：

```python
print(response)
```

只获取**模型返回文本**：

```python
print(response.choices[0].message.content)
```

::: tip 💡 建议
在生产环境中，建议对 `response` 做异常处理和空值判断，避免程序崩溃。
:::

---

## ❓ 常见问题

::: details 🤔 为什么必须设置 `base_url`？
因为这里接入的是兼容 OpenAI API 的 **自定义服务地址**，而不是 SDK 默认的 OpenAI 官方地址。

请确保设置为：
```
https://ai.katioai.com/v1
```
:::

::: details 🔑 认证失败怎么办？
请检查以下内容：

| 检查项 | 说明 |
| :--- | :--- |
| API Key | 是否正确、是否已启用 |
| `base_url` | 是否填写正确 |
| 模型名称 | 是否为平台支持的有效模型 |
:::

::: details 🤖 提示模型不存在怎么办？
请将以下字段替换为平台当前可用模型：
```python
model="gemini-3-pro-preview"
```
可在平台控制台查看支持的模型列表。
:::

::: details 🔄 是否可以直接用于现有 OpenAI SDK 项目？
**可以！** 如果你的项目已经基于 OpenAI Python SDK，只需替换 3 个参数即可：

| 参数 | 替换为 |
| :--- | :--- |
| `api_key` | 你的 KatioAI 密钥 |
| `base_url` | `https://ai.katioai.com/v1` |
| `model` | 平台支持的模型名称 |
:::

---

## 🧪 最小示例

适合直接展示在首页或开发文档中的极简代码：

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

## 📁 推荐目录结构

如果你准备把这个示例放进一个小项目中，可以参考下面的结构：

```
.
├── README.md            # 项目说明
├── requirements.txt     # 依赖清单
└── example.py           # 示例代码
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

## 📝 注意事项

::: danger 🔐 密钥安全
- 不要在公开仓库中提交真实 API Key
- 推荐优先使用环境变量管理密钥
:::

::: tip 🎯 使用建议
- 模型名称请以平台实际支持列表为准
- 如需接入更多接口，可在当前示例基础上扩展
- 建议在生产环境中添加错误处理和重试逻辑
:::

---

<a href="/guide/api-examples" style="display:inline-block;padding:8px 16px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;">← 返回接口示例</a>
