---
sidebar: false
prev:
  text: 'Gemini CLI'
  link: '/en/guide/code/gemini-cli'
next:
  text: 'Dify'
  link: '/en/guide/code/dify'
---

# 📝 Codex CLI

## Install Environment Dependencies

**Install Node.js**  
Visit [nodejs.org](https://nodejs.org) to download the **LTS (Long-Term Support)** version. The page will automatically detect your operating system.

::: tip Tip
The Node.js installer already includes **npm** (package manager), no separate installation needed.
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

## Install Codex CLI

Open a command line (CMD), and install Codex CLI via npm:

```bash
npm install -g @openai/codex
```

Verify installation:
```bash
codex --version
```

## Configuration Steps

1. **Select Model Service** → **Select Add** → **Add Provider**
2. **API Address:** `https://ai.katioai.com/v1`
3. **API Key:** Enter your token/API key
4. **Main Model:** Select and add the model


::: warning Notes
- ✅ Make sure the API address is correct — include `/v1`
- ❌ Do not omit the model prefix/suffix
:::

## 📸 Illustrated Tutorial

### Step 1: Open CC Switch Settings
![Step1](/images/codex-cli/step-1.png)

![Step1](/images/codex-cli/step-2.png)

### Step 2: Fill in Configuration Information
![Step2](/images/codex-cli/step-3.png)

![Step2](/images/codex-cli/step-4.png)

### Step 3: Launch Codex CLI
Open CMD, enter `codex` to launch Codex CLI:

![Step3](/images/codex-cli/step-5.png)

### Step 4: Select Model
By default, or enter `/model`, you can select the model you want to use:

![Step4](/images/codex-cli/step-6.png)

### Step 5: Configuration Complete
![Step5](/images/codex-cli/step-7.png)
