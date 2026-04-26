---
sidebar: false
prev:
  text: 'VS Code (Cline)'
  link: '/en/guide/code/vscode-cline'
next:
  text: 'Cursor'
  link: '/en/guide/code/cursor'
---

# 📂 OpenCode

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

## Install OpenCode

Open a command line (CMD), and install OpenCode via npm:

```bash
npm install -g opencode-ai@latest
```
Verify installation:
```bash
opencode --version
```

## Configuration Steps

1. **Select Model Service** → **Select Add** → **Add Provider**
2. **API Address:** `https://ai.katioai.com/v1`
3. **API Key:** Enter your token/API key
4. **Model Configuration:** Manually add the model


::: warning Notes
- ✅ Make sure the API address is correct — include `/v1`
- ❌ Do not omit the model prefix/suffix
:::

## 📸 Illustrated Tutorial

### Step 1: Open CC Switch Settings
![Step1](/images/opencode/step-1.png)

![Step1](/images/opencode/step-2.png)

### Step 2: Fill in Configuration Information
![Step2](/images/opencode/step-3.png)

![Step2](/images/opencode/step-4.png)

### Step 3: Launch OpenCode
Open CMD, enter `opencode` to launch OpenCode:

![Step3](/images/opencode/step-5.png)

### Step 4: Select Model
Enter `/model` to select the model you want to use:

![Step4](/images/opencode/step-6.png)

![Step4](/images/opencode/step-7.png)

### Step 5: Configuration Complete
![Step5](/images/opencode/step-8.png)

