---
sidebar: false
prev:
  text: 'Claude Code'
  link: '/en/guide/code/claude-code'
next:
  text: 'Codex CLI'
  link: '/en/guide/code/codex-cli'
---

# ♊ Gemini CLI

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

## Install Gemini CLI

Open a command line (CMD), and install Gemini CLI via npm:

```bash
npm install -g @google/gemini-cli
```

Verify installation:
```bash
gemini --version
```

## Configuration Steps

1. **Select Model Service** → **Select Add** → **Add Provider**
2. **API Address:** `https://ai.katioai.com`
3. **API Key:** Enter your token/API key
4. **Main Model:** Select and add the model


::: warning Notes
- ✅ Make sure the API address is correct — do NOT include `/v1`
- ❌ Do not omit the model prefix/suffix
:::

## 📸 Illustrated Tutorial

### Step 1: Open CC Switch Settings
![Step1](/images/gemini-cli/step-1.png)

![Step1](/images/gemini-cli/step-2.png)

### Step 2: Fill in Configuration Information
![Step2](/images/gemini-cli/step-3.png)

![Step2](/images/gemini-cli/step-4.png)

### Step 3: Launch Gemini CLI
Open CMD, enter `gemini` to launch Gemini CLI:

![Step3](/images/gemini-cli/step-5.png)

### Step 4: Select Model
By default, or enter `/model`, you can select the model you want to use:

![Step4](/images/gemini-cli/step-6.png)

### Step 5: Configuration Complete
![Step5](/images/gemini-cli/step-7.png)
