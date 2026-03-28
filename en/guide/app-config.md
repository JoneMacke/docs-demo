---
sidebar: false
---

# ⚙️ App Config

Application-level configuration for Maple AI.

## Model Selection

| Model | Use Case | Context |
|-------|----------|---------|
| maple-ai-v1 | Chat, text generation | 8K |
| maple-ai-pro | Complex reasoning, coding | 32K |
| maple-ai-vision | Image understanding | 16K |

## Parameters

```json
{
  "temperature": 0.7,
  "top_p": 0.9,
  "max_tokens": 2048,
  "frequency_penalty": 0,
  "presence_penalty": 0
}
```

## Rate Limits

| Plan | RPM | TPM |
|------|-----|-----|
| Free | 10 | 10K |
| Standard | 100 | 100K |
| Pro | 1000 | 1M |

## Error Handling

```javascript
try {
  const result = await client.chat(messages)
} catch (error) {
  if (error.status === 429) {
    console.log('Too many requests, please retry later')
  } else if (error.status === 401) {
    console.log('Invalid API Key')
  }
}
```
