---
sidebar: false
prev:
  text: 'Copaw'
  link: '/guide/code/copaw'
next:
  text: 'Easydict'
  link: '/guide/code/easydict'
---

# 🦀 OpenClaw

OpenClaw 是一款开源的 AI 编程智能体框架，支持本地部署和多种云端平台配置。它拥有强大的多模型接入能力、灵活的 Agent 配置机制以及丰富的插件扩展体系，是开发者构建 AI 编程工作流的理想选择。

::: info 项目信息
**官方网站：** [OpenClaw（点击跳转）](https://openclaw.ai/)  
**GitHub：** [openclaw/openclaw](https://github.com/openclaw/openclaw)  
**支持平台：** Windows / macOS / Linux
:::

::: tip 枫叶AI 快速接入要素
| 配置项 | 值 |
|--------|-----|
| API 地址 | `https://ai.katioai.com`（注意：不要加 `/v1`） |
| API 协议 | `anthropic-messages` |
| API 密钥 | 你在 [枫叶AI 控制台](https://ai.katioai.com/console) 获取的密钥 |
| 推荐模型 | `claude-opus-4-6` |
:::

## 功能特点

- 🧠 **AI 编程智能体** — 自主分析需求、分解任务、编写代码，大幅提升开发效率
- 🔌 **多模型灵活接入** — 支持 Claude、GPT 等主流模型，一键切换
- 🖥️ **本地 + 云端双模式** — 既可本地私有化部署，也支持阿里云、腾讯云等云端配置
- 🔧 **丰富的扩展机制** — 内置 Agent 配置、Hook 扩展、子代理协作等高级功能
- 🌐 **社区驱动** — 开源免费，活跃的社区生态，持续迭代更新

---

## 📝 本地部署

### 步骤 1：安装环境依赖

**安装 Node.js**  
访问 [nodejs.org](https://nodejs.org) 下载 **LTS 长期支持版**，页面会自动识别你的操作系统。

::: tip 提示
Node.js 安装包已自带 **npm**（包管理器），无需单独安装。
:::

**安装 Git**  
访问 [git-scm.com](https://git-scm.com) 下载安装。Windows 用户建议选择 **64 位版本**，使用默认选项即可。

**验证安装**  
打开终端（Windows 用 CMD / PowerShell，macOS / Linux 用终端），执行：

```bash
node -v
npm -v
```

能正常显示版本号即安装成功。

### 步骤 2：安装 OpenClaw

```bash
npm i -g openclaw
```

### 步骤 3：定位配置文件

OpenClaw 的配置文件为 `openclaw.json`，默认路径如下：

| 操作系统        | 默认路径                                             |
|----------------|------------------------------------------------------|
| Windows        | `C:\Users\<用户名>\.openclaw\openclaw.json`           |
| macOS / Linux  | `~/.openclaw/openclaw.json`                           |

### 步骤 4：配置枫叶 AI（⭐ 关键步骤）

在配置文件中添加以下两部分内容：

**① 添加 Provider（模型提供商）**

在 `models.providers` 中加入枫叶AI的配置：

```json
"models": {
  "providers": {
    "claude": {
      "baseUrl": "https://ai.katioai.com",
      "apiKey": "sk-xxxxx（替换为你的密钥）",
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
```

**② 设置默认模型（agents.defaults）**

在配置文件中指定默认使用的模型：

```json
"agents": {
  "defaults": {
    "model": {
      "primary": "claude/claude-opus-4-6"
    },
    "models": {
      "claude/claude-opus-4-6": {
        "alias": "claude-opus-4-6"
      }
    }
  }
}
```

::: warning ⚠️ 配置注意事项
- ✅ `baseUrl` 填写 `https://ai.katioai.com`，**不要包含 `/v1` 后缀**
- ✅ `api` 协议必须选择 `anthropic-messages`
- ✅ `apiKey` 替换为你在 [枫叶AI 控制台](https://ai.katioai.com/console) 获取的实际密钥
- ❌ 不要随意修改 `model.id` 和 `model.name` 的格式，保持一致即可
:::

### 步骤 5：启动服务

```bash
openclaw gateway
```

启动成功后，打开浏览器访问本地服务即可使用。

---

### 📄 完整配置文件参考

::: details 点击展开完整 openclaw.json 配置示例

```json
{
  "meta": {
    "lastTouchedVersion": "2026.2.1",
    "lastTouchedAt": "2026-02-12T00:00:00.000Z"
  },
  "wizard": {
    "lastRunAt": "2026-02-02T05:38:19.852Z",
    "lastRunVersion": "2026.1.30",
    "lastRunCommand": "onboard",
    "lastRunMode": "local"
  },
  "models": {
    "providers": {
      "claude": {
        "baseUrl": "https://ai.katioai.com",
        "apiKey": "sk-xxxxx（替换为你的密钥）",
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
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "claude/claude-opus-4-6"
      },
      "models": {
        "claude/claude-opus-4-6": {
          "alias": "claude-opus-4-6"
        }
      },
      "workspace": "/root/.openclaw/workspace",
      "compaction": {
        "mode": "safeguard"
      },
      "timeoutSeconds": 6000,
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8
      }
    }
  },
  "messages": {
    "ackReactionScope": "group-mentions"
  },
  "commands": {
    "native": "auto",
    "nativeSkills": "auto"
  },
  "hooks": {
    "internal": {
      "enabled": true,
      "entries": {
        "boot-md": { "enabled": true },
        "command-logger": { "enabled": true },
        "session-memory": { "enabled": true }
      }
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "auth": {
      "mode": "token",
      "token": "你的gateway令牌"
    },
    "remote": {
      "token": "你的remote令牌"
    },
    "tailscale": {
      "mode": "off",
      "resetOnExit": false
    }
  }
}
```

> **macOS 用户注意：** 请将 `workspace` 路径改为 `/Users/<你的用户名>/.openclaw/workspace`，并在 `commands` 中添加 `"restart": true`。

:::

---

## ☁️ 阿里云配置

::: info 参考文档
**官方教程：** [阿里云 Model Studio OpenClaw 配置教程](https://help.aliyun.com/zh/model-studio/openclaw)
:::

在阿里云控制台中，将 `models` 和 `agents` 配置替换为以下内容：

```json
"models": {
  "providers": {
    "claude": {
      "baseUrl": "https://ai.katioai.com",
      "apiKey": "sk-xxxxx（替换为你的密钥）",
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
},
"agents": {
  "defaults": {
    "model": {
      "primary": "claude/claude-opus-4-6"
    },
    "models": {
      "claude/claude-opus-4-6": {
        "alias": "claude-opus-4-6"
      }
    }
  }
}
```

---

## ☁️ 腾讯云配置

::: info 参考文档
**官方教程：** [腾讯云 OpenClaw 配置教程](https://www.tencentcloud.com/techpedia/142432)
:::

1. 打开 OpenClaw → 自定义服务器设置 → **自定义模型配置**
2. 使用以下 JSON 配置模板：

```json
{
  "provider": "openai",
  "base_url": "https://ai.katioai.com",
  "api": "anthropic-messages",
  "api_key": "sk-xxxxx（替换为你的密钥）",
  "model": {
    "id": "claude-opus-4-6",
    "name": "claude-opus-4-6"
  }
}
```

---

## 🔧 通用配置模板

适用于其他兼容 OpenClaw 的平台或自建服务：

```json
{
  "provider": "openai",
  "base_url": "https://ai.katioai.com",
  "api": "anthropic-messages",
  "api_key": "sk-xxxxx（替换为你的密钥）",
  "model": {
    "id": "claude-opus-4-6",
    "name": "claude-opus-4-6"
  }
}
```

**参数说明：**

| 参数 | 说明 |
|------|------|
| `provider` | 提供商名称（可自定义，如 `openai` 或 `claude`） |
| `base_url` | API 接入地址：`https://ai.katioai.com` |
| `api` | 协议类型：`openai-completions` 或 `anthropic-messages` |
| `api_key` | 你在 [枫叶AI 控制台](https://ai.katioai.com/console) 获取的密钥 |
| `model.id` | 模型标识符，如 `claude-opus-4-6` |
| `model.name` | 模型显示名称（建议与 `model.id` 保持一致） |

::: tip 💡 切换模型
配置完成后重启 OpenClaw 服务即可生效。如需使用其他模型，只需修改 `model.id` 和 `model.name` 为目标模型名称即可。

常用模型参考：`claude-opus-4-6`、`claude-sonnet-4-20250514`、`gpt-4o` 等。
:::

---

## ❓ 常见问题

::: details 连接失败怎么办？
1. 检查 `baseUrl` 是否正确填写为 `https://ai.katioai.com`（不含 `/v1`）
2. 确认 API 密钥是否有效且余额充足
3. 检查网络连接是否正常
4. 尝试重启 OpenClaw 服务：`openclaw gateway`
:::

::: details 如何切换不同的模型？
修改配置文件中 `model.id` 和 `model.name` 为目标模型名称，然后重启服务即可。也可以在 `models` 数组中添加多个模型配置，通过 `agents.defaults.model.primary` 切换默认模型。
:::

::: details macOS 启动报错？
确保将 `workspace` 路径修改为 macOS 格式：`/Users/<用户名>/.openclaw/workspace`，并在 `commands` 配置中添加 `"restart": true`。
:::
