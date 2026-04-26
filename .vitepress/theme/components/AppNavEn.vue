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
    title: '💼 Productivity',
    items: [
      { name: 'ChatBox', emoji: '💬', desc: 'AI Desktop Client', link: '/en/guide/apps/chatbox' },
      { name: 'Cherry Studio', emoji: '🍒', desc: 'Multi-Model Aggregation Assistant', link: '/en/guide/apps/cherrystudio' },
      { name: 'RikkaHub', emoji: '🔗', desc: 'AI Chat Hub', link: '/en/guide/apps/rikkahub' },
      { name: 'Kelivo', emoji: '📋', desc: 'AI Knowledge Management', link: '/en/guide/apps/kelivo' },
      { name: 'Operit AI', emoji: '⚡', desc: 'AI Automation Tool', link: '/en/guide/apps/operit-ai' },
      { name: 'Prompt Optimizer', emoji: '✨', desc: 'Smart Prompt Optimization', link: '/en/guide/apps/prompt-optimizer' }
    ]
  },
  {
    title: '🎭 Characters',
    items: [
      { name: 'BotGem', emoji: '💎', desc: 'Smart Character Chat', link: '/en/guide/apps/botgem' },
      { name: 'SillyTavern', emoji: '🏰', desc: 'Role-Playing Platform', link: '/en/guide/apps/sillytavern' },
      { name: 'Omate', emoji: '🤝', desc: 'AI Companion', link: '/en/guide/apps/omate' },
      { name: 'Tavo', emoji: '🎪', desc: 'Character Creation Tool', link: '/en/guide/apps/tavo' }
    ]
  },
  {
    title: '💕 Companion',
    items: [
      { name: 'DreamLove', emoji: '💖', desc: 'AI Emotional Companion', link: '/en/guide/apps/dreamlove' },
      { name: 'XiaoYi', emoji: '🌸', desc: 'Smart Companion Assistant', link: '/en/guide/apps/xiaoyi' },
      { name: 'XiaoShouJi', emoji: '📱', desc: 'Mobile AI Companion', link: '/en/guide/apps/xiaoshouji' }
    ]
  }
]
</script>
