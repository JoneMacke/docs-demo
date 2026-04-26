---
sidebar: false
prev:
  text: 'API Examples'
  link: '/en/guide/api-examples'
next: false
---

# 🔧 Provider Configuration Guide

> This project supports integrating model services compatible with the **Anthropic Messages API** through custom Providers.

---

## 🎯 Configuration Goals

By configuring a Provider, you can:

- 🌐 Specify the API service address
- 🔑 Configure access keys
- 📡 Declare the API protocol type
- 🤖 Register available models
- 📏 Set model context and output limits

---

## 📍 Configuration Location

Add the following content under the `models.providers` node in the configuration file:

```json
{
  "models": {
    "providers": {}
  }
}
```

::: info 💡 Tip
If other Providers already exist, simply add as a sibling object.
:::

---

## 📝 Configuration Examples

### Annotated Version

::: warning ⚠️ Note
The following example contains comments for explanation purposes only — **it cannot be used directly as a standard JSON file**.
:::

```js
{
  "models": {
    "providers": {
      "Claude": {
        // API service address
        "baseUrl": "https://ai.katioai.com",

        // API key
        "apiKey": "sk-xxxxxx-your-real-key",

        // API protocol type
        "api": "anthropic-messages",

        // Model list
        "models": [
          {
            "id": "claude-opus-4-6",       // Model call ID
            "name": "claude-opus-4-6",     // Model display name
            "reasoning": false,             // Whether it is a reasoning model
            "input": ["text"],              // Supported input types
            "cost": {                       // Cost information
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 200000,        // Context window size
            "maxTokens": 8192               // Maximum output tokens
          }
        ]
      }
    }
  }
}
```

---

### ✅ Ready-to-use JSON Configuration

::: details 📋 Click to expand full JSON configuration
```json
{
  "models": {
    "providers": {
      "Claude": {
        "baseUrl": "https://ai.katioai.com",
        "apiKey": "sk-xxxxxx-your-real-key",
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
:::

---

## 📖 Field Reference

### Provider-level Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `baseUrl` | `string` | API service address |
| `apiKey` | `string` | API access key |
| `api` | `string` | API protocol type, currently `anthropic-messages` |
| `models` | `array` | List of available models under this Provider |

### Model-level Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | Model call ID |
| `name` | `string` | Model display name |
| `reasoning` | `boolean` | Whether marked as a reasoning model |
| `input` | `array` | Supported input types, e.g. `["text"]` |
| `cost` | `object` | Cost configuration (see table below) |
| `contextWindow` | `number` | Maximum context window (token count) |
| `maxTokens` | `number` | Maximum output tokens per request |

### `cost` Sub-fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `input` | `number` | Input token cost |
| `output` | `number` | Output token cost |
| `cacheRead` | `number` | Cache read cost |
| `cacheWrite` | `number` | Cache write cost |

::: tip 💡 Tips
If the project does not currently rely on cost tracking, you can set all values to `0` for now.
:::

---

## ✏️ Required Changes Before Use

Before using the configuration, make sure to confirm the following **3 key settings**:

### 1️⃣ Update `apiKey`

Replace the placeholder with your real API Key:

```json
"apiKey": "sk-xxxxxx-your-real-key"
```

### 2️⃣ Confirm `baseUrl`

The current example address is:

```json
"baseUrl": "https://ai.katioai.com"
```

Please confirm this matches the service you are actually using.

### 3️⃣ Confirm Model `id`

The example uses:

```json
"id": "claude-opus-4-6"
```

::: warning ⚠️ Important
Make sure this model ID is a real model name supported by the server, otherwise the call may fail.
:::

---

## 🚀 Common Extended Usage

### Configure Multiple Models

If the same Provider supports multiple models, you can append them to the `models` array:

::: details 📋 Multi-model Configuration Example
```json
{
  "models": {
    "providers": {
      "Claude": {
        "baseUrl": "https://ai.katioai.com",
        "apiKey": "sk-xxxxxx-your-real-key",
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
          },
          {
            "id": "claude-sonnet-4",
            "name": "claude-sonnet-4",
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
:::

---

## ⚠️ Important Notes

::: danger 🔐 1. Never Commit Real Keys
Do not commit configurations containing real `apiKey` values to public repositories.

**Best Practices:**
- Only keep example values in README
- Add real configuration files to `.gitignore`
- Use environment variables or local private configuration files to store keys
:::

::: warning 📄 2. JSON Files Cannot Contain Comments
If your configuration file is standard JSON (`.json`), remove all `//` comments, otherwise parsing errors will occur.
:::

::: info 📡 3. API Protocol Must Match
The current configuration uses `"api": "anthropic-messages"`, so the server must be compatible with this protocol format, otherwise requests may fail.
:::

::: tip 💰 4. Cost Fields Are Placeholders Only
Values in `cost` are typically used as placeholders only and do not represent actual billing rates.
```json
"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 }
```
:::

---

## 🔍 Troubleshooting

If the configuration is complete but calls still fail, check the following:

| # | Check Item | Description |
| :---: | :--- | :--- |
| 1 | `baseUrl` | Is the service address correct? |
| 2 | `apiKey` | Is the key valid? |
| 3 | `api` | Does the protocol type match? |
| 4 | `id` | Does the model ID actually exist? |
| 5 | JSON format | Are there any syntax errors in the config file? |
| 6 | Permissions | Does the current key have access to the model? |

---

## 📁 Recommended Repository File Organization

We recommend distinguishing between the following files in your project:

| File | Purpose | Upload to Repo? |
| :--- | :--- | :---: |
| `README.md` | Configuration documentation | ✅ |
| `config.example.json` | Example configuration | ✅ |
| Local real config file | Store actual keys | ❌ |

::: details 📋 Example placeholder config — config.example.json
```json
{
  "models": {
    "providers": {
      "Claude": {
        "baseUrl": "https://ai.katioai.com",
        "apiKey": "YOUR_API_KEY",
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
:::

---

<a href="/en/guide/api-examples" style="display:inline-block;padding:8px 16px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;">← Back to API Examples</a>
