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
    title: '💼 办公',
    items: [
      { name: 'ChatBox', emoji: '💬', desc: 'AI 桌面客户端', link: '/guide/apps/chatbox' },
      { name: 'Cherry Studio', emoji: '🍒', desc: '多模型聚合助手', link: '/guide/apps/cherrystudio' },
      { name: 'RikkaHub', emoji: '🔗', desc: 'AI 对话中心', link: '/guide/apps/rikkahub' },
      { name: 'Kelivo', emoji: '📋', desc: 'AI 知识管理', link: '/guide/apps/kelivo' },
      { name: 'Operit AI', emoji: '⚡', desc: 'AI 自动化工具', link: '/guide/apps/operit-ai' },
      { name: '提示词优化器', emoji: '✨', desc: 'Prompt 智能优化', link: '/guide/apps/prompt-optimizer' }
    ]
  },
  {
    title: '🎭 角色',
    items: [
      { name: 'BotGem', emoji: '💎', desc: '智能角色对话', link: '/guide/apps/botgem' },
      { name: 'SillyTavern', emoji: '🏰', desc: '角色扮演平台', link: '/guide/apps/sillytavern' },
      { name: 'Omate', emoji: '🤝', desc: 'AI 伙伴', link: '/guide/apps/omate' },
      { name: 'Tavo', emoji: '🎪', desc: '角色创作工具', link: '/guide/apps/tavo' }
    ]
  },
  {
    title: '💕 陪伴',
    items: [
      { name: 'DreamLove', emoji: '💖', desc: 'AI 情感陪伴', link: '/guide/apps/dreamlove' },
      { name: '小懿', emoji: '🌸', desc: '智能陪伴助手', link: '/guide/apps/xiaoyi' },
      { name: '小手机', emoji: '📱', desc: '移动端 AI 陪伴', link: '/guide/apps/xiaoshouji' }
    ]
  }
]
</script>
