<template>
  <div class="guide-grid">
    <a v-for="item in items" :key="item.title" :href="item.link" class="guide-card">
      <div class="guide-card-cover" :style="{ background: item.bg }">
        <div class="guide-card-icon">{{ item.icon }}</div>
        <div class="guide-card-label">
          <span class="guide-card-zh">{{ item.title }}</span>
          <span class="guide-card-en">{{ item.enTitle }}</span>
        </div>
      </div>
      <div class="guide-card-body">
        <h3 class="guide-card-title">{{ item.title }}</h3>
        <p class="guide-card-desc">{{ item.desc }}</p>
      </div>
    </a>
  </div>
</template>

<script setup>
const items = [
  {
    icon: '🚀',
    title: 'Quick Start',
    enTitle: 'GET STARTED',
    desc: 'Requirements / Installation / First Request',
    link: '/en/guide/quickstart',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #065f46 100%)'
  },
  {
    icon: '📡',
    title: 'API Examples',
    enTitle: 'ENDPOINTS',
    desc: 'Chat API / Image Generation / Streaming',
    link: '/en/guide/api-examples',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #1e40af 100%)'
  },
  {
    icon: '🔑',
    title: 'Get Token',
    enTitle: 'AUTHENTICATION',
    desc: 'Get API Key / Pricing / Usage Query',
    link: '/en/guide/token',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #7c2d12 100%)'
  },
  {
    icon: '💻',
    title: 'Code Config',
    enTitle: 'SDK SETUP',
    desc: 'SDK Install / Initialize / Env Variables / Proxy',
    link: '/en/guide/code-config',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #164e63 100%)'
  },
  {
    icon: '⚙️',
    title: 'App Config',
    enTitle: 'SETTINGS',
    desc: 'Model Selection / Parameters / Rate Limits / Errors',
    link: '/en/guide/app-config',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #581c87 100%)'
  },
  {
    icon: '🛒',
    title: 'Store',
    enTitle: 'PURCHASE',
    desc: 'Plans / Top-up / Promotions',
    link: '/en/guide/shop',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #991b1b 100%)'
  }
]
</script>
