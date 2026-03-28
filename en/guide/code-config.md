---
sidebar: false
---

# 💻 Code Config

Configure and use the Maple AI SDK in your project.

## Install SDK

::: code-group
```bash [npm]
npm install maple-ai-sdk
```

```bash [pnpm]
pnpm add maple-ai-sdk
```

```bash [yarn]
yarn add maple-ai-sdk
```
:::

## Initialize

```javascript
import { MapleAI } from 'maple-ai-sdk'

const client = new MapleAI({
  apiKey: process.env.MAPLE_AI_KEY,
  baseURL: 'https://api.example.com/v1',
  timeout: 30000
})
```

## Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| apiKey | string | - | API key (required) |
| baseURL | string | default | API base URL |
| timeout | number | 30000 | Request timeout (ms) |
| maxRetries | number | 2 | Max retry count |

## Environment Variables

Use a `.env` file to manage secrets:

```env
MAPLE_AI_KEY=your-api-key-here
MAPLE_AI_BASE_URL=https://api.example.com/v1
```
