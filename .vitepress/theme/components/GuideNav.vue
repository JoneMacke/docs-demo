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
    title: '快速开始',
    enTitle: 'QUICK START',
    desc: '环境要求 / 安装步骤 / 第一个请求',
    link: '/guide/quickstart',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #065f46 100%)'
  },
  {
    icon: '📡',
    title: '接口示例',
    enTitle: 'API EXAMPLES',
    desc: '对话接口 / 图像生成 / 流式输出',
    link: '/guide/api-examples',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #1e40af 100%)'
  },
  {
    icon: '🔑',
    title: '获取令牌',
    enTitle: 'TOKEN',
    desc: '获取 API Key / 计费规则 / 用量查询',
    link: '/guide/token',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #7c2d12 100%)'
  },
  {
    icon: '💻',
    title: '代码配置',
    enTitle: 'CODE CONFIG',
    desc: 'SDK 安装 / 初始化 / 环境变量 / 代理配置',
    link: '/guide/code-config',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #164e63 100%)'
  },
  {
    icon: '⚙️',
    title: '应用配置',
    enTitle: 'APP CONFIG',
    desc: '模型选择 / 参数调优 / 速率限制 / 错误处理',
    link: '/guide/app-config',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #581c87 100%)'
  },
  {
    icon: '🛒',
    title: '前往商城',
    enTitle: 'STORE',
    desc: '套餐购买 / 充值续费 / 优惠活动',
    link: '/guide/shop',
    bg: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #991b1b 100%)'
  }
]
</script>
