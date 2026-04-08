<template>
  <div class="shop-nav">
    <p class="shop-nav-subtitle">多平台购买，享受限时优惠折扣，安全便捷。</p>
    <div class="shop-grid">
      <div v-for="item in shops" :key="item.name" class="shop-card" :style="{ background: item.bg }">
        <div class="shop-badge" :style="{ background: item.badgeBg }">{{ item.badge }}</div>
        <h3 class="shop-card-name">{{ item.name }}</h3>
        <div class="shop-card-price">{{ item.price }}</div>
        <p class="shop-card-note">{{ item.note }}</p>
        <ul class="shop-card-features">
          <li v-for="f in item.features" :key="f">✓ {{ f }}</li>
        </ul>
        <a :href="item.link" target="_blank" rel="noopener noreferrer" class="shop-card-btn">
          {{ item.btnText }}
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
const shops = [
  {
    name: '自助商城',
    badge: '官方推荐',
    price: '快速购买',
    note: '官方直营，稳定可靠',
    features: [
      '官方直营，品质保障',
      '支持多种支付方式',
      '自动发货，即买即用',
      '24小时在线客服'
    ],
    btnText: '前往自助商城',
    link: 'https://68n.cn/PZkYw',
    bg: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    badgeBg: '#5a67d8'
  },
  {
    name: '红薯平台',
    badge: '社区热推',
    price: '98折 ~ 95折',
    note: '优惠力度随充值金额递增',
    features: [
      '红薯担保交易，安全放心',
      '支持多种支付方式',
      '自动发货，即买即用',
      '充值越多折扣越大'
    ],
    btnText: '前往红薯购买',
    link: 'https://xhslink.com/m/4UeAaHivZrI',
    bg: 'linear-gradient(135deg, #f5515f 0%, #a1051d 100%)',
    badgeBg: '#e53e3e'
  }
  // {
  //   name: '淘宝平台',
  //   badge: '限时优惠',
  //   price: '98折 ~ 95折',
  //   note: '优惠力度随充值金额递增',
  //   features: [
  //     '淘宝担保交易，安全放心',
  //     '支持花呗、信用卡等多种支付',
  //     '自动发货，即买即用',
  //     '充值越多折扣越大'
  //   ],
  //   btnText: '前往淘宝购买',
  //   link: 'https://www.taobao.com/',
  //   bg: 'linear-gradient(135deg, #ff6a00 0%, #ee0979 100%)',
  //   badgeBg: '#dd6b20'
  // },
  // {
  //   name: '闲鱼平台',
  //   badge: '闲鱼专属',
  //   price: '98折 ~ 95折',
  //   note: '优惠力度随充值金额递增',
  //   features: [
  //     '闲鱼担保交易，安全可靠',
  //     '支持花呗、信用卡等多种支付',
  //     '即拍即发，快速到账',
  //     '充值越多折扣越大'
  //   ],
  //   btnText: '前往闲鱼购买',
  //   link: 'https://www.goofish.com/',
  //   bg: 'linear-gradient(135deg, #f7971e 0%, #ffd200 100%)',
  //   badgeBg: '#d69e2e'
  // }
]
</script>
