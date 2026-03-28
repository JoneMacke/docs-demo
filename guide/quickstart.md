---
sidebar: false
---

# 🚀 快速开始

欢迎使用枫叶AI，本页将帮助你快速上手。

## 环境要求

- Node.js 18+
- 支持的浏览器：Chrome、Firefox、Edge

## 安装步骤

1. 注册账号并获取 API Key
2. 安装 SDK
3. 配置环境变量
4. 发起第一个请求

## 第一个请求

```bash
curl https://api.example.com/v1/chat \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "maple-ai-v1", "messages": [{"role": "user", "content": "你好"}]}'
```

## 下一步

- [接口示例](/guide/api-examples) - 查看更多 API 调用示例
- [获取令牌](/guide/token) - 了解如何获取和管理令牌
