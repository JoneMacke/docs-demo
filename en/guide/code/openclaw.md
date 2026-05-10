---
sidebar: false
prev:
  text: 'Copaw'
  link: '/en/guide/code/copaw'
next:
  text: 'Hermes Agent'
  link: '/en/guide/code/hermes-agent'
---

# 🦀 OpenClaw

OpenClaw is an open-source AI programming agent framework that supports local deployment and various cloud platform configurations. It features powerful multi-model integration capabilities, flexible Agent configuration mechanisms, and a rich plugin extension system, making it an ideal choice for developers building AI programming workflows.

::: info Project Info
**Official Website:** [OpenClaw (click to visit)](https://openclaw.ai/)  
**GitHub:** [openclaw/openclaw](https://github.com/openclaw/openclaw)  
**Supported Platforms:** Windows / macOS / Linux
:::

::: tip MapleAI Quick Integration Essentials
| Config Item | Value |
|--------|-----|
| API Address | `https://ai.katioai.com` (Note: do NOT add `/v1`) |
| API Protocol | `anthropic-messages` |
| API Key | The key obtained from [MapleAI Console](https://ai.katioai.com/console) |
| Recommended Model | `claude-opus-4-6` |
:::

## Features

- 🧠 **AI Programming Agent** — Autonomously analyzes requirements, decomposes tasks, and writes code, greatly improving development efficiency
- 🔌 **Flexible Multi-model Integration** — Supports mainstream models like Claude, GPT, with one-click switching
- 🖥️ **Local + Cloud Dual Mode** — Supports both local private deployment and cloud configurations (Alibaba Cloud, Tencent Cloud, etc.)
- 🔧 **Rich Extension Mechanisms** — Built-in Agent configuration, Hook extensions, sub-agent collaboration, and other advanced features
- 🌐 **Community Driven** — Open source and free, with an active community ecosystem and continuous updates

---

## 📝 Local Deployment

### Step 1: Install Environment Dependencies

**Install Node.js**  
Visit [nodejs.org](https://nodejs.org) to download the **LTS (Long-Term Support)** version. The page will automatically detect your operating system.

::: tip Tip
The Node.js installer includes **npm** (package manager), no separate installation needed.
:::

**Install Git**  
Visit [git-scm.com](https://git-scm.com) to download and install. Windows users are recommended to choose the **64-bit version** with default options.

**Verify Installation**  
Open a terminal (CMD / PowerShell on Windows, Terminal on macOS / Linux) and run:

```bash
node -v
npm -v
```

If version numbers are displayed, the installation was successful.

### Step 2: Install OpenClaw

```bash
npm i -g openclaw
```

### Step 3: Locate Configuration File

The OpenClaw configuration file is `openclaw.json`, with default paths as follows:

| OS | Default Path |
|----------------|------------------------------------------------------|
| Windows | `C:\Users\<username>\.openclaw\openclaw.json` |
| macOS / Linux | `~/.openclaw/openclaw.json` |

### Step 4: Configure MapleAI (⭐ Key Step)

Add the following two sections to the configuration file:

**① Add Provider (Model Provider)**

Add the MapleAI configuration under `models.providers`:

```json
"models": {
  "providers": {
    "claude": {
      "baseUrl": "https://ai.katioai.com",
      "apiKey": "sk-xxxxx (replace with your key)",
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

**② Set Default Model (agents.defaults)**

Specify the default model in the configuration file:

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

::: warning ⚠️ Configuration Notes
- ✅ Set `baseUrl` to `https://ai.katioai.com`, **do NOT include the `/v1` suffix**
- ✅ The `api` protocol must be `anthropic-messages`
- ✅ Replace `apiKey` with your actual key from the [MapleAI Console](https://ai.katioai.com/console)
- ❌ Do not arbitrarily modify the format of `model.id` and `model.name` — keep them consistent
:::

### Step 5: Start the Service

```bash
openclaw gateway
```

Once started successfully, open a browser to access the local service.

---

### 📄 Complete Configuration File Reference

::: details Click to expand full openclaw.json configuration example

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
        "apiKey": "sk-xxxxx (replace with your key)",
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
      "token": "your-gateway-token"
    },
    "remote": {
      "token": "your-remote-token"
    },
    "tailscale": {
      "mode": "off",
      "resetOnExit": false
    }
  }
}
```

> **macOS users note:** Change the `workspace` path to `/Users/<your-username>/.openclaw/workspace`, and add `"restart": true` in the `commands` section.

:::

---

## ☁️ Alibaba Cloud Configuration

::: info Reference Documentation
**Official Tutorial:** [Alibaba Cloud Model Studio OpenClaw Configuration Guide](https://help.aliyun.com/zh/model-studio/openclaw)
:::

In the Alibaba Cloud console, replace the `models` and `agents` configuration with the following:

```json
"models": {
  "providers": {
    "claude": {
      "baseUrl": "https://ai.katioai.com",
      "apiKey": "sk-xxxxx (replace with your key)",
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

## ☁️ Tencent Cloud Configuration

::: info Reference Documentation
**Official Tutorial:** [Tencent Cloud OpenClaw Configuration Guide](https://www.tencentcloud.com/techpedia/142432)
:::

1. Open OpenClaw → Custom Server Settings → **Custom Model Configuration**
2. Use the following JSON configuration template:

```json
{
  "provider": "openai",
  "base_url": "https://ai.katioai.com",
  "api": "anthropic-messages",
  "api_key": "sk-xxxxx (replace with your key)",
  "model": {
    "id": "claude-opus-4-6",
    "name": "claude-opus-4-6"
  }
}
```

---

## 🔧 Generic Configuration Template

Applicable to other OpenClaw-compatible platforms or self-hosted services:

```json
{
  "provider": "openai",
  "base_url": "https://ai.katioai.com",
  "api": "anthropic-messages",
  "api_key": "sk-xxxxx (replace with your key)",
  "model": {
    "id": "claude-opus-4-6",
    "name": "claude-opus-4-6"
  }
}
```

**Parameter Description:**

| Parameter | Description |
|------|------|
| `provider` | Provider name (customizable, e.g. `openai` or `claude`) |
| `base_url` | API access address: `https://ai.katioai.com` |
| `api` | Protocol type: `openai-completions` or `anthropic-messages` |
| `api_key` | Key obtained from [MapleAI Console](https://ai.katioai.com/console) |
| `model.id` | Model identifier, e.g. `claude-opus-4-6` |
| `model.name` | Model display name (recommended to keep consistent with `model.id`) |

::: tip 💡 Switching Models
After configuration, restart the OpenClaw service for changes to take effect. To use a different model, simply change `model.id` and `model.name` to the target model name.

Common model references: `claude-opus-4-6`, `claude-sonnet-4-20250514`, `gpt-4o`, etc.
:::

---

## ❓ FAQ

::: details What if the connection fails?
1. Check that `baseUrl` is correctly set to `https://ai.katioai.com` (without `/v1`)
2. Confirm the API key is valid and has sufficient balance
3. Check your network connection
4. Try restarting the OpenClaw service: `openclaw gateway`
:::

::: details How to switch to a different model?
Modify `model.id` and `model.name` in the configuration file to the target model name, then restart the service. You can also add multiple model configurations in the `models` array and switch the default model via `agents.defaults.model.primary`.
:::

::: details macOS startup error?
Make sure to change the `workspace` path to macOS format: `/Users/<username>/.openclaw/workspace`, and add `"restart": true` in the `commands` configuration.
:::
