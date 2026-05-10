---
sidebar: false
prev:
  text: 'OpenClaw'
  link: '/en/guide/code/openclaw'
next:
  text: 'Easydict'
  link: '/en/guide/code/easydict'
---

# 🪽 Hermes Agent

Hermes Agent is an open-source AI agent framework by Nous Research. It can run in the terminal and on messaging platforms such as Telegram, Discord, Slack, and Weixin. It supports tool calling, persistent memory, reusable Skills, scheduled jobs, webhooks, MCP, and sub-agent collaboration, making it suitable for coding, server operations, research, content workflows, and automation tasks.

::: info Project Info
**Official Website:** [Hermes Agent Docs (click to visit)](https://hermes-agent.nousresearch.com/docs/)  
**GitHub:** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)  
**Supported Platforms:** Linux / macOS / WSL
:::

::: tip MapleAI Quick Integration Essentials
| Config Item | Value |
|--------|-----|
| API Address | `https://ai.katioai.com/v1` |
| API Key | The key obtained from [MapleAI Console](https://ai.katioai.com/console) |
| Recommended Provider | `custom` |
| Recommended Model | `claude-opus-4-6` |
:::

## Features

- 🧠 **Autonomous Task Execution** — Reads files, runs commands, edits code, calls tools, and keeps working through complex tasks
- 🧩 **Skills System** — Saves successful workflows as reusable skills that can be loaded in future sessions
- 🧠 **Persistent Memory** — Stores user preferences, environment details, and long-term operational knowledge
- 🌉 **Multi-platform Gateway** — Runs the same agent on Telegram, Discord, Slack, Weixin, email, and more
- 🛠️ **Tools and MCP Extensions** — Supports terminal, file tools, browser, search, scheduled tasks, webhooks, MCP, and more
- 🔁 **Sub-agent Collaboration** — Delegates code review, research, debugging, and parallel work to isolated sub-agents

---

## 📝 Local Deployment

### Step 1: Install Environment Dependencies

**Install system dependencies**  
Linux, macOS, or WSL is recommended. Make sure common command-line tools are available.

**Install Git**  
Visit [git-scm.com](https://git-scm.com) to download and install Git. Windows users are recommended to use WSL.

**Verify Installation**  
Open a terminal and run:

```bash
git --version
curl --version
```

If version numbers are displayed, the installation was successful.

### Step 2: Install Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

After installation, reopen your terminal and run:

```bash
hermes --version
```

If a version number is displayed, Hermes Agent has been installed successfully.

### Step 3: Locate Configuration Files

Hermes Agent uses `config.yaml` for main settings and `.env` for secrets:

| File | Default Path | Purpose |
|------|----------|------|
| Main config | `~/.hermes/config.yaml` | Model, tools, gateway, memory, and agent settings |
| Environment variables | `~/.hermes/.env` | API keys and platform tokens |
| Skills directory | `~/.hermes/skills/` | Local Skills files |
| Sessions directory | `~/.hermes/sessions/` | Historical session records |

You can also check the actual paths with:

```bash
hermes config path
hermes config env-path
```

### Step 4: Configure MapleAI (⭐ Key Step)

Hermes Agent supports custom OpenAI-compatible endpoints. For MapleAI, the recommended provider is `custom`.

**① Add API Key**

Find the environment file:

```bash
hermes config env-path
```

Add or update this line in `.env`:

```bash
CUSTOM_API_KEY=sk-xxxxx (replace with your key)
```

::: warning ⚠️ API Key Notes
- ✅ Write the API key as a bare value
- ❌ Do not write `CUSTOM_API_KEY='sk-xxxxx'`
- ❌ Do not write `CUSTOM_API_KEY="sk-xxxxx"`
:::

**② Configure model and endpoint**

You can set the values from the command line:

```bash
hermes config set model.provider custom
hermes config set model.default claude-opus-4-6
hermes config set model.base_url https://ai.katioai.com/v1
```

Or use the interactive model picker:

```bash
hermes model
```

Choose a custom endpoint and enter the MapleAI API address, key, and model name.

::: warning ⚠️ Configuration Notes
- ✅ Set `model.provider` to `custom`
- ✅ Set `model.base_url` to `https://ai.katioai.com/v1`
- ✅ Replace `CUSTOM_API_KEY` with your actual key from the [MapleAI Console](https://ai.katioai.com/console)
- ✅ `model.default` can start with `claude-opus-4-6`
- ❌ Do not commit API keys to Git repositories
:::

### Step 5: Check Configuration

```bash
hermes doctor
hermes config check
```

If the checks pass, you can start using Hermes Agent.

### Step 6: Start Hermes Agent

Interactive session:

```bash
hermes
```

Single query:

```bash
hermes chat -q "Hello, introduce Hermes Agent in one sentence"
```

To connect Telegram, Weixin, Discord, or other platforms, configure the Gateway:

```bash
hermes gateway setup
hermes gateway run
```

---

### 📄 Full Configuration Reference

::: details Click to expand config.yaml example

```yaml
model:
  provider: custom
  default: claude-opus-4-6
  base_url: https://ai.katioai.com/v1

agent:
  max_turns: 90
  tool_use_enforcement: true

terminal:
  backend: local
  timeout: 180

memory:
  memory_enabled: true
  user_profile_enabled: true

compression:
  enabled: true
  threshold: 0.5
  target_ratio: 0.2

delegation:
  max_iterations: 50

security:
  tirith_enabled: true
```

`.env` example:

```bash
CUSTOM_API_KEY=sk-xxxxx (replace with your key)
```

:::

---

## 🌉 Gateway Multi-platform Access

Hermes Agent can run as a multi-platform agent. Common platforms include:

- Telegram
- Discord
- Slack
- Weixin
- Email
- Webhook / API Server

Configuration entry:

```bash
hermes gateway setup
```

Run the Gateway:

```bash
hermes gateway run
```

To install it as a background service:

```bash
hermes gateway install
hermes gateway start
```

---

## 🔧 Common Commands

| Command | Purpose |
|------|------|
| `hermes` | Start an interactive session |
| `hermes chat -q "..."` | Run a single task |
| `hermes model` | Change model or provider |
| `hermes config edit` | Edit configuration |
| `hermes doctor` | Check environment and configuration |
| `hermes tools` | Manage toolsets |
| `hermes skills list` | List installed Skills |
| `hermes gateway setup` | Configure messaging platforms |
| `hermes cron list` | List scheduled jobs |

---

## ❓ FAQ

::: details What if the connection fails?
1. Check that `model.base_url` is set to `https://ai.katioai.com/v1`
2. Confirm that `CUSTOM_API_KEY` in `.env` is valid and has enough balance
3. Make sure the API key is not wrapped in single or double quotes
4. Run `hermes doctor` and `hermes config check`
:::

::: details How do I switch models?
Run `hermes model` to use the interactive picker, or change `model.default` to another model name such as `claude-sonnet-4-20250514`.
:::

::: details Why did my config change not take effect?
For CLI usage, exit and restart `hermes`. For Gateway usage, run `/restart` or restart the Gateway service.
:::
