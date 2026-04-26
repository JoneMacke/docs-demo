---
sidebar: false
prev:
  text: 'CC Switch'
  link: '/en/guide/cc-switch'
next:
  text: 'Gemini CLI'
  link: '/en/guide/code/gemini-cli'
---

# 🤖 Claude Code

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

## Install Claude-Code

Open a command line (CMD), and install claude-code via npm:

```bash
npm install -g @anthropic-ai/claude-code
```

Verify installation:
```bash
claude --version
```

## Configuration Steps

1. **Select Tool Type** → **Select Add** → **Add Provider**
2. **API Address:** `https://ai.katioai.com`
3. **API Key:** Enter your token/API key
4. **Main Model:** Manually add the model
5. **API Format:** anthropic messages (native)


::: warning Notes
- ✅ Make sure the API address is correct — do NOT include `/v1`
- ❌ Do not omit the model prefix/suffix
:::

## 📸 Illustrated Tutorial

### Step 1: Open CC Switch Settings
![Step1](/images/claude-code/step-1.png)

![Step1](/images/claude-code/step-2.png)

### Step 2: Fill in Configuration Information
![Step2](/images/claude-code/step-3.png)

![Step2](/images/claude-code/step-4.png)

### Step 3: Launch Claude Code
Open CMD, enter `claude` to launch Claude Code:

![Step3](/images/claude-code/step-5.png)

### Step 4: Select Model
Enter `/model` and select the model you added:

![Step4](/images/claude-code/step-6.png)

### Step 5: Configuration Complete
![Step5](/images/claude-code/step-7.png)

