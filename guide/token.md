---
sidebar: false
---

# 🔑 获取令牌

本页介绍如何获取和管理 API 令牌（Token）。

## 获取 API Key

1. 登录 [枫叶AI控制台](https://example.com)
2. 进入「API 管理」页面
3. 点击「创建新密钥」
4. 复制并妥善保存你的 API Key

::: warning 安全提示
请勿在前端代码中暴露你的 API Key，建议通过后端代理转发请求。
:::

## Token 计费规则

| 模型 | 输入价格 | 输出价格 |
|------|---------|---------|
| maple-ai-v1 | ¥0.01/1K tokens | ¥0.02/1K tokens |
| maple-ai-pro | ¥0.03/1K tokens | ¥0.06/1K tokens |

## 查看用量

```bash
curl https://api.example.com/v1/usage \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## 令牌管理

- 每个账号最多创建 5 个 API Key
- 可以为每个 Key 设置独立的速率限制
- 支持随时禁用或删除 Key
