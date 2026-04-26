---
sidebar: false
prev:
  text: '接口示例'
  link: '/guide/api-examples'
next: false
---

# 🔧 Provider 配置说明

> 本项目支持通过自定义 Provider 的方式接入兼容 **Anthropic Messages API** 的模型服务。

---

## 🎯 配置目标

通过配置 Provider，你可以：

- 🌐 指定 API 服务地址
- 🔑 配置访问密钥
- 📡 声明接口协议类型
- 🤖 注册可用模型
- 📏 设置模型上下文与输出限制

---

## 📍 配置位置

请将以下内容添加到配置文件中的 `models.providers` 节点下：

```json
{
  "models": {
    "providers": {}
  }
}
```

::: info 💡 提示
如果已经存在其他 Provider，请作为同级对象继续追加即可。
:::

---

## 📝 配置示例

### 带注释的说明版本

::: warning ⚠️ 注意
以下示例包含注释，仅用于说明，**不能直接作为标准 JSON 文件使用**。
:::

```js
{
  "models": {
    "providers": {
      "Claude": {
        // API 服务地址
        "baseUrl": "https://ai.katioai.com",

        // API 密钥
        "apiKey": "sk-xxxxxx你的真实秘钥",

        // 接口协议类型
        "api": "anthropic-messages",

        // 模型列表
        "models": [
          {
            "id": "claude-opus-4-6",       // 模型调用 ID
            "name": "claude-opus-4-6",     // 模型显示名称
            "reasoning": false,             // 是否为推理模型
            "input": ["text"],              // 支持的输入类型
            "cost": {                       // 成本信息
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 200000,        // 上下文窗口大小
            "maxTokens": 8192               // 最大输出 token 数
          }
        ]
      }
    }
  }
}
```

---

### ✅ 可直接使用的 JSON 配置

::: details 📋 点击展开完整 JSON 配置
```json
{
  "models": {
    "providers": {
      "Claude": {
        "baseUrl": "https://ai.katioai.com",
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
:::

---

## 📖 字段说明

### Provider 级别字段

| 字段 | 类型 | 说明 |
| :--- | :--- | :--- |
| `baseUrl` | `string` | API 服务地址 |
| `apiKey` | `string` | API 访问密钥 |
| `api` | `string` | 接口协议类型，当前为 `anthropic-messages` |
| `models` | `array` | 当前 Provider 下可用模型列表 |

### 模型级别字段

| 字段 | 类型 | 说明 |
| :--- | :--- | :--- |
| `id` | `string` | 模型实际调用名称 |
| `name` | `string` | 模型显示名称 |
| `reasoning` | `boolean` | 是否标记为推理模型 |
| `input` | `array` | 模型支持的输入类型，如 `["text"]` |
| `cost` | `object` | 成本信息配置（见下表） |
| `contextWindow` | `number` | 最大上下文窗口（token 数量） |
| `maxTokens` | `number` | 单次最大输出 token 数 |

### `cost` 子字段

| 字段 | 类型 | 说明 |
| :--- | :--- | :--- |
| `input` | `number` | 输入 token 成本 |
| `output` | `number` | 输出 token 成本 |
| `cacheRead` | `number` | 缓存读取成本 |
| `cacheWrite` | `number` | 缓存写入成本 |

::: tip 💡 小贴士
如果项目当前不依赖成本统计功能，可暂时统一填写为 `0`。
:::

---

## ✏️ 使用前必须修改

在正式使用前，请务必确认以下 **3 项关键配置**：

### 1️⃣ 修改 `apiKey`

将占位值替换为你的真实 API Key：

```json
"apiKey": "sk-xxxxxx你的真实秘钥"
```

### 2️⃣ 确认 `baseUrl`

当前示例地址为：

```json
"baseUrl": "https://ai.katioai.com"
```

请确认该地址与你实际使用的服务一致。

### 3️⃣ 确认模型 `id`

示例中使用的是：

```json
"id": "claude-opus-4-6"
```

::: warning ⚠️ 重要
请确保该模型 ID 为服务端真实支持的模型名称，否则可能调用失败。
:::

---

## 🚀 常见扩展用法

### 配置多个模型

如果同一个 Provider 支持多个模型，可以继续在 `models` 数组中追加：

::: details 📋 多模型配置示例
```json
{
  "models": {
    "providers": {
      "Claude": {
        "baseUrl": "https://ai.katioai.com",
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

## ⚠️ 注意事项

::: danger 🔐 1. 不要提交真实密钥
请勿将包含真实 `apiKey` 的配置提交到公开仓库。

**建议做法：**
- README 中只保留示例值
- 将真实配置文件加入 `.gitignore`
- 优先使用环境变量或本地私有配置文件保存密钥
:::

::: warning 📄 2. JSON 文件不能写注释
如果你的配置文件是标准 JSON（`.json`），请移除所有 `//` 注释内容，否则会解析报错。
:::

::: info 📡 3. 接口协议必须匹配
当前配置使用 `"api": "anthropic-messages"`，因此服务端必须兼容该协议格式，否则请求可能报错。
:::

::: tip 💰 4. 示例成本字段仅作占位
`cost` 中的值通常仅用于占位或展示，不代表真实计费标准。
```json
"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 }
```
:::

---

## 🔍 故障排查

如果配置完成后仍然无法调用，请依次检查：

| 序号 | 检查项 | 说明 |
| :---: | :--- | :--- |
| 1 | `baseUrl` | 服务地址是否正确 |
| 2 | `apiKey` | 密钥是否有效 |
| 3 | `api` | 协议类型是否匹配 |
| 4 | `id` | 模型 ID 是否真实存在 |
| 5 | JSON 格式 | 配置文件是否有语法错误 |
| 6 | 权限 | 当前密钥是否有权访问对应模型 |

---

## 📁 建议的仓库文件组织方式

推荐在项目中区分以下文件：

| 文件 | 用途 | 是否上传仓库 |
| :--- | :--- | :---: |
| `README.md` | 展示配置说明 | ✅ |
| `config.example.json` | 提供示例配置 | ✅ |
| 本地真实配置文件 | 保存实际密钥 | ❌ |

::: details 📋 示例占位配置 config.example.json
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

<a href="/guide/api-examples" style="display:inline-block;padding:8px 16px;background:#3eaf7c;color:#fff;border-radius:6px;text-decoration:none;">← 返回接口示例</a>
