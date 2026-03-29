---
sidebar: false
prev:
  text: '接口示例'
  link: '/guide/api-examples'
next: false
---

# 🌐 cURL 调用注释

> 本页为「cURL 调用示例」的详细注释说明，帮助你深入理解每个请求参数的含义与用法。

---

## 📌 基础调用示例

下面的示例展示了如何通过 cURL 调用 **聊天补全接口**：

```bash
curl https://api.katioai.com/v1/chat/completions \
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

::: tip 💡 说明
该请求会向聊天接口发送一条用户消息，并由指定模型生成回复。
:::

---

## 📋 请求说明

### 请求头（Headers）

| 字段 | 值 | 说明 |
| :--- | :--- | :--- |
| `Content-Type` | `application/json` | 请求体格式 |
| `Authorization` | `Bearer YOUR_API_KEY` | 鉴权令牌，替换为你的真实 API Key |

### 请求体参数（Body）

| 参数 | 类型 | 必填 | 说明 |
| :--- | :--- | :---: | :--- |
| `model` | `string` | ✅ | 要调用的模型名称 |
| `messages` | `array` | ✅ | 对话消息列表 |

---

### 💬 `messages` 格式

每条消息包含以下字段：

| 字段 | 类型 | 说明 |
| :--- | :--- | :--- |
| `role` | `string` | 消息角色，可选值：`system`、`user`、`assistant` |
| `content` | `string` | 消息内容 |

::: details 📄 messages 示例
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

## 🔄 多轮对话示例

通过在 `messages` 中添加多条消息，可以实现**多轮对话**的效果：

```bash
curl https://api.katioai.com/v1/chat/completions \
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
        "content": "请解释一下什么是 README。"
      }
    ]
  }'
```

::: info 🧩 角色说明
| 角色 | 用途 |
| :--- | :--- |
| `system` | 设定 AI 的行为和角色定位 |
| `user` | 用户发送的消息 |
| `assistant` | AI 的回复（用于上下文传递） |
:::

---

## ⚠️ 注意事项

::: warning 🔐 安全提醒
- 请将 `YOUR_API_KEY` 替换为你的 **真实 API Key**
- **切勿** 将 API Key 提交到 GitHub 等公开仓库
- 建议使用环境变量管理密钥，例如：`$API_KEY`
:::

::: tip 📝 其他提示
- 不同模型的参数和响应格式可能略有差异，请以实际接口文档为准
- 如遇到超时问题，可尝试添加 `--connect-timeout` 参数
- 返回结果默认为 JSON 格式，可配合 `jq` 工具进行格式化查看
:::

---

<a href="/guide/api-examples" style="display:inline-block;padding:8px 16px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;">← 返回接口示例</a>
