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
    title: '🏛️ Official Tools',
    items: [
      { name: 'CC Switch', emoji: '🔀', desc: 'Multi-Model Switching Tool', link: '/en/guide/code/cc-switch' },
      { name: 'Claude Code', emoji: '🤖', desc: 'Anthropic Official Coding Assistant', link: '/en/guide/code/claude-code' },
      { name: 'Gemini CLI', emoji: '♊', desc: 'Google Gemini CLI Tool', link: '/en/guide/code/gemini-cli' },
      { name: 'Codex CLI', emoji: '📝', desc: 'OpenAI Codex CLI Tool', link: '/en/guide/code/codex-cli' }
    ]
  },
  {
    title: '🔄 Workflows',
    items: [
      { name: 'Dify', emoji: '🧩', desc: 'AI App Development Platform', link: '/en/guide/code/dify' },
      { name: 'n8n', emoji: '⚙️', desc: 'Workflow Automation Tool', link: '/en/guide/code/n8n' }
    ]
  },
  {
    title: '🛠️ Third-Party Tools',
    items: [
      { name: 'AionUi', emoji: '🎨', desc: 'AI Interface Development Tool', link: '/en/guide/code/aionui' },
      { name: 'VS Code (Cline)', emoji: '💻', desc: 'VS Code AI Coding Plugin', link: '/en/guide/code/vscode-cline' },
      { name: 'OpenCode', emoji: '📂', desc: 'Open-Source AI Coding Tool', link: '/en/guide/code/opencode' },
      { name: 'Cursor', emoji: '🖱️', desc: 'AI-Powered Code Editor', link: '/en/guide/code/cursor' }
    ]
  },
  {
    title: '🤖 Agents',
    items: [
      { name: 'Copaw', emoji: '🐾', desc: 'AI Coding Agent', link: '/en/guide/code/copaw' },
      { name: 'OpenClaw', emoji: '🦀', desc: 'Open-Source AI Agent', link: '/en/guide/code/openclaw' },
      { name: 'Hermes Agent', emoji: '🪽', desc: 'Multi-platform AI Agent', link: '/en/guide/code/hermes-agent' }
    ]
  },
  {
    title: '📦 Others',
    items: [
      { name: 'Easydict', emoji: '📖', desc: 'Smart Translation Dictionary', link: '/en/guide/code/easydict' },
      { name: 'Python SDK', emoji: '🐍', desc: 'Python Development Kit', link: '/en/guide/code/python-sdk' }
    ]
  }
]
</script>
