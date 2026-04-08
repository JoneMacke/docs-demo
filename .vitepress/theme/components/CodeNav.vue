<template>
  <div class="app-nav">
    <div v-for="group in groups" :key="group.title" class="app-nav-group">
      <h2 class="app-nav-group-title">{{ group.title }}</h2>
      <div class="app-nav-grid">
        <a
          v-for="item in group.items"
          :key="item.name"
          :href="item.link"
          class="app-nav-card"
        >
          <div class="app-nav-card-icon">
            <img v-if="item.icon" :src="item.icon" :alt="item.name" />
            <span v-else class="app-nav-card-emoji">{{ item.emoji || '📦' }}</span>
          </div>
          <div class="app-nav-card-info">
            <h3 class="app-nav-card-name">{{ item.name }}</h3>
            <p v-if="item.desc" class="app-nav-card-desc">{{ item.desc }}</p>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
const groups = [
  {
    title: '🏛️ 官方工具',
    items: [
      { name: 'CC Switch', emoji: '🔀', desc: '多模型切换工具', link: '/guide/code/cc-switch' },
      { name: 'Claude Code', emoji: '🤖', desc: 'Anthropic 官方编程助手', link: '/guide/code/claude-code' },
      { name: 'Gemini CLI', emoji: '♊', desc: 'Google Gemini 命令行工具', link: '/guide/code/gemini-cli' },
      { name: 'Codex CLI', emoji: '📝', desc: 'OpenAI Codex 命令行工具', link: '/guide/code/codex-cli' }
    ]
  },
  {
    title: '🔄 工作流',
    items: [
      { name: 'Dify', emoji: '🧩', desc: 'AI 应用开发平台', link: '/guide/code/dify' },
      { name: 'n8n', emoji: '⚙️', desc: '工作流自动化工具', link: '/guide/code/n8n' }
    ]
  },
  {
    title: '🛠️ 三方工具',
    items: [
      { name: 'AionUi', emoji: '🎨', desc: 'AI 界面开发工具', link: '/guide/code/aionui' },
      { name: 'VS Code (Cline)', emoji: '💻', desc: 'VS Code AI 编程插件', link: '/guide/code/vscode-cline' },
      { name: 'OpenCode', emoji: '📂', desc: '开源 AI 编程工具', link: '/guide/code/opencode' },
      { name: 'Cursor', emoji: '🖱️', desc: 'AI 驱动的代码编辑器', link: '/guide/code/cursor' }
    ]
  },
  {
    title: '🤖 智能体',
    items: [
      { name: 'Copaw', emoji: '🐾', desc: 'AI 编程智能体', link: '/guide/code/copaw' },
      { name: 'OpenClaw', emoji: '🦀', desc: '开源 AI 智能体', link: '/guide/code/openclaw' }
    ]
  },
  {
    title: '📦 其他',
    items: [
      { name: 'Easydict', emoji: '📖', desc: '智能翻译词典', link: '/guide/code/easydict' },
      { name: 'Python SDK', emoji: '🐍', desc: 'Python 开发工具包', link: '/guide/code/python-sdk' }
    ]
  }
]
</script>
