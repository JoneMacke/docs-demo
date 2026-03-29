---
sidebar: false
prev:
  text: '快速开始'
  link: '/guide/quickstart'
next:
  text: '获取令牌'
  link: '/guide/token'
---

# 📡 接口示例

本页展示 **枫叶AI** 常用接口的调用示例，帮助你快速上手接入服务。

::: tip 💡 前提条件
在开始之前，请确保你已经：
1. 注册并获取了 API Key（`sk-xxxxxx`）
2. 了解你需要调用的模型名称
:::

---

## 🔧 添加Provider

<a href="/guide/api-notes/provider" style="display:inline-block;margin-bottom:12px;padding:6px 14px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;font-size:14px;">📝 查看详细注释 →</a>

添加自定义模型服务提供商（Provider）：

::: warning ⚠️ 关键步骤
这是非常关键的配置步骤！请将以下 JSON 代码片段加入到 `models.providers` 块中，并替换为你自己的真实密钥。
:::

```json
{
  "models": {
    "providers": {
      "Claude": {
        "baseUrl": "https://api.katioai.com",
        "apiKey": "sk-xxxxxx你的真实秘钥",
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

| 参数 | 说明 |
| :--- | :--- |
| `baseUrl` | API 服务地址 |
| `apiKey` | 你的 API 密钥，请替换为真实值 |
| `api` | API 协议类型 |
| `contextWindow` | 上下文窗口大小（token 数量） |
| `maxTokens` | 最大输出 token 数 |

---

## 🌐 cURL 调用示例

<a href="/guide/api-notes/curl" style="display:inline-block;margin-bottom:12px;padding:6px 14px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;font-size:14px;">📝 查看详细注释 →</a>

通过 cURL 直接调用 **聊天补全接口**：

```bash
curl https://api.katioai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxxxxx你的真实秘钥" \
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

::: details 📋 请求参数说明
| 参数 | 类型 | 说明 |
| :--- | :--- | :--- |
| `model` | `string` | 要调用的模型名称 |
| `messages` | `array` | 消息列表，包含 `role` 和 `content` |
| `messages[].role` | `string` | 角色类型：`system`、`user`、`assistant` |
| `messages[].content` | `string` | 消息内容 |
:::

---

## 🐍 Python 调用示例

<a href="/guide/api-notes/python" style="display:inline-block;margin-bottom:12px;padding:6px 14px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;font-size:14px;">📝 查看详细注释 →</a>

使用 OpenAI 官方 SDK 调用枫叶AI 接口，只需修改 `base_url` 和 `api_key` 即可：

::: info 📦 安装依赖
```bash
pip install openai
```
:::

```python
from openai import OpenAI

# 初始化客户端，指向枫叶AI接口
client = OpenAI(
    api_key="sk-xxxxxxxx",          # 替换为你的真实密钥
    base_url="https://api.katioai.com/v1"  # 枫叶AI的API地址
)

# 发起聊天补全请求
response = client.chat.completions.create(
    model="gemini-3-pro-preview",   # 指定模型
    messages=[
        {"role": "user", "content": "Hi!"}
    ]
)

# 输出结果
print(response)
```

::: tip 🎯 小贴士
- 将 `sk-xxxxxxxx` 替换为你的真实 API Key
- `model` 参数可替换为其他支持的模型名称
- 接口兼容 OpenAI SDK，迁移成本极低
:::
