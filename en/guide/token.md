---
sidebar: false
---

# 🔑 Get Token

Learn how to obtain and manage your API tokens.

## Get API Key

1. Log in to the [Maple AI Console](https://example.com)
2. Navigate to "API Management"
3. Click "Create New Key"
4. Copy and safely store your API Key

::: warning Security Notice
Never expose your API Key in frontend code. Use a backend proxy to forward requests.
:::

## Pricing

| Model | Input Price | Output Price |
|-------|-----------|-------------|
| maple-ai-v1 | $0.001/1K tokens | $0.002/1K tokens |
| maple-ai-pro | $0.003/1K tokens | $0.006/1K tokens |

## Check Usage

```bash
curl https://api.example.com/v1/usage \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Key Management

- Up to 5 API Keys per account
- Independent rate limits per key
- Disable or delete keys anytime
