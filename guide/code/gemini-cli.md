---
sidebar: false
prev:
  text: 'Claude Code'
  link: '/guide/code/claude-code'
next:
  text: 'Codex CLI'
  link: '/guide/code/codex-cli'
---

# ♊ Gemini CLI

## 安装环境依赖

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

## 安装 gemini-CLI

打开 cmd 命令行，通过 npm 安装 gemini-CLI

```bash
npm install -g @google/gemini-cli
```

验证安装成功
```bash
gemini --version
```

## 配置步骤

1. **选择模型服务** → **选择添加** → **添加提供商**
2. **API 地址：** `https://api.katioai.com`
3. **API Key：** 填入您的令牌/密钥
4. **主模型：** 选择模型添加


::: warning 注意事项
- ✅ 确保 API 地址填写正确，不包含 `/v1`
- ❌ 不要遗漏模型的前后缀
:::

## 📸 图文教程

### 步骤 1：打开cc switch设置
![步骤1](/images/gemini-cli/step-1.png)

![步骤1](/images/gemini-cli/step-2.png)

### 步骤 2：填入配置信息
![步骤2](/images/gemini-cli/step-3.png)

![步骤2](/images/gemini-cli/step-4.png)

### 步骤 3：启动 gemini CLI
打开CMD,输入gemini,启动gemini CLI

![步骤3](/images/gemini-cli/step-5.png)

### 步骤 4：选择模型
默认或者输入/model,可以选择需要使用的模型

![步骤4](/images/gemini-cli/step-6.png)

### 步骤 5：完成配置
![步骤5](/images/gemini-cli/step-7.png)
