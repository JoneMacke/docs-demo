---
sidebar: false
prev:
  text: 'OpenClaw'
  link: '/guide/code/openclaw'
next:
  text: 'Easydict'
  link: '/guide/code/easydict'
---

# 🪽 Hermes Agent

Hermes Agent 是 Nous Research 开源的 AI 智能体框架，可以在终端、Telegram、Discord、Slack、微信等多平台中运行。它支持工具调用、长期记忆、Skills 技能沉淀、定时任务、Webhook、MCP、子智能体协作等能力，适合用于代码开发、服务器运维、资料整理、内容生产和自动化工作流。

::: info 项目信息
**官方网站：** [Hermes Agent Docs（点击跳转）](https://hermes-agent.nousresearch.com/docs/)  
**GitHub：** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)  
**支持平台：** Linux / macOS / WSL
:::

::: tip 枫叶AI 快速接入要素
| 配置项 | 值 |
|--------|-----|
| API 地址 | `https://ai.katioai.com/v1` |
| API Key | 你在 [枫叶AI 控制台](https://ai.katioai.com/console) 获取的密钥 |
| 推荐 Provider | `custom` |
| 推荐模型 | `claude-opus-4-6` |
:::

## 功能特点

- 🧠 **自主任务执行** — 支持读取文件、运行命令、修改代码、调用工具，并持续推进复杂任务
- 🧩 **Skills 技能系统** — 可把成功经验沉淀为可复用技能，后续任务自动加载相关流程
- 🧠 **长期记忆** — 可以保存用户偏好、环境信息和长期有用的操作经验
- 🌉 **多平台 Gateway** — 同一个智能体可接入 Telegram、Discord、Slack、微信、邮件等平台
- 🛠️ **工具与 MCP 扩展** — 支持终端、文件、浏览器、搜索、定时任务、Webhook、MCP 等扩展能力
- 🔁 **多智能体协作** — 可派生子智能体并行处理代码审查、调研、排错等任务

---

## 📝 本地部署

### 步骤 1：安装环境依赖

**安装系统环境**  
建议使用 Linux、macOS 或 WSL 环境，并确保已安装常用命令行工具。

**安装 Git**  
访问 [git-scm.com](https://git-scm.com) 下载安装。Windows 用户建议在 WSL 中使用。

**验证安装**  
打开终端执行：

```bash
git --version
curl --version
```

能正常显示版本号即安装成功。

### 步骤 2：安装 Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装完成后，重新打开终端，执行：

```bash
hermes --version
```

如果能显示版本号，说明 Hermes Agent 已安装成功。

### 步骤 3：定位配置文件

Hermes Agent 的主配置文件为 `config.yaml`，密钥通常放在 `.env` 中：

| 文件 | 默认路径 | 用途 |
|------|----------|------|
| 主配置 | `~/.hermes/config.yaml` | 模型、工具、Gateway、记忆等配置 |
| 环境变量 | `~/.hermes/.env` | API Key、平台 Token 等敏感信息 |
| 技能目录 | `~/.hermes/skills/` | 本地 Skills 技能文件 |
| 会话目录 | `~/.hermes/sessions/` | 历史会话记录 |

也可以用命令查看实际路径：

```bash
hermes config path
hermes config env-path
```

### 步骤 4：配置枫叶 AI（⭐ 关键步骤）

Hermes Agent 支持自定义 OpenAI 兼容接口。使用枫叶 AI 时，推荐将模型提供商设置为 `custom`。

**① 写入 API Key**

打开环境变量文件：

```bash
hermes config env-path
```

在 `.env` 中添加或修改：

```bash
CUSTOM_API_KEY=sk-xxxxx（替换为你的密钥）
```

::: warning ⚠️ 密钥注意事项
- ✅ API Key 直接写裸值即可
- ❌ 不要写成 `CUSTOM_API_KEY='sk-xxxxx'`
- ❌ 不要写成 `CUSTOM_API_KEY="sk-xxxxx"`
:::

**② 配置模型与接口地址**

可以通过命令写入：

```bash
hermes config set model.provider custom
hermes config set model.default claude-opus-4-6
hermes config set model.base_url https://ai.katioai.com/v1
```

也可以执行交互式配置：

```bash
hermes model
```

在模型选择中选择自定义接口，并填入枫叶 AI 的地址、密钥和模型名。

::: warning ⚠️ 配置注意事项
- ✅ `model.provider` 推荐填写 `custom`
- ✅ `model.base_url` 填写 `https://ai.katioai.com/v1`
- ✅ `CUSTOM_API_KEY` 替换为你在 [枫叶AI 控制台](https://ai.katioai.com/console) 获取的实际密钥
- ✅ `model.default` 可先使用 `claude-opus-4-6`
- ❌ 不要把 API Key 直接提交到 Git 仓库
:::

### 步骤 5：检查配置

```bash
hermes doctor
hermes config check
```

如果检查通过，即可开始使用。

### 步骤 6：启动 Hermes Agent

交互式启动：

```bash
hermes
```

单次提问：

```bash
hermes chat -q "你好，请用一句话介绍 Hermes Agent"
```

如果需要接入 Telegram、微信、Discord 等平台，可以继续配置 Gateway：

```bash
hermes gateway setup
hermes gateway run
```

---

### 📄 完整配置文件参考

::: details 点击展开 config.yaml 配置示例

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

`.env` 示例：

```bash
CUSTOM_API_KEY=sk-xxxxx（替换为你的密钥）
```

:::

---

## 🌉 Gateway 多平台接入

Hermes Agent 可以作为多平台智能体运行。常见平台包括：

- Telegram
- Discord
- Slack
- 微信 / Weixin
- 邮件
- Webhook / API Server

配置入口：

```bash
hermes gateway setup
```

启动 Gateway：

```bash
hermes gateway run
```

如需安装为后台服务，可使用：

```bash
hermes gateway install
hermes gateway start
```

---

## 🔧 常用命令

| 命令 | 作用 |
|------|------|
| `hermes` | 启动交互式会话 |
| `hermes chat -q "..."` | 执行单次任务 |
| `hermes model` | 切换模型或 Provider |
| `hermes config edit` | 编辑配置文件 |
| `hermes doctor` | 检查环境和配置 |
| `hermes tools` | 管理工具集 |
| `hermes skills list` | 查看已安装 Skills |
| `hermes gateway setup` | 配置消息平台 |
| `hermes cron list` | 查看定时任务 |

---

## ❓ 常见问题

::: details 连接失败怎么办？
1. 检查 `model.base_url` 是否填写为 `https://ai.katioai.com/v1`
2. 确认 `.env` 中的 `CUSTOM_API_KEY` 是否有效且余额充足
3. 确认 API Key 没有被单引号或双引号包裹
4. 运行 `hermes doctor` 和 `hermes config check` 查看问题
:::

::: details 如何切换不同的模型？
可以运行 `hermes model` 进入交互式选择，也可以修改 `model.default` 为目标模型名称，例如 `claude-sonnet-4-20250514`。
:::

::: details 修改配置后为什么没生效？
CLI 场景下退出并重新运行 `hermes`；Gateway 场景下执行 `/restart` 或重启 Gateway 服务。
:::
