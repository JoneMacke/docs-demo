<template>
  <div class="shop-nav">
    <p class="shop-nav-subtitle">Multi-platform purchase, enjoy limited-time discounts, safe and convenient.</p>
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
    name: 'Official Store',
    badge: 'Recommended',
    price: 'Original Price',
    note: 'Official direct sales, stable and reliable',
    features: [
      'Official direct sales, quality assurance',
      'Multiple payment methods supported',
      'Auto delivery, instant use',
      '24/7 online customer service'
    ],
    btnText: 'Go to Store',
    link: 'https://example.com/store',
    bg: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    badgeBg: '#5a67d8'
  },
  {
    name: 'Hongshu Platform',
    badge: 'Community Choice',
    price: '2% ~ 5% OFF',
    note: 'Discount increases with recharge amount',
    features: [
      'Hongshu guaranteed transaction, safe',
      'Multiple payment methods supported',
      'Auto delivery, instant use',
      'More recharge, more discount'
    ],
    btnText: 'Buy on Hongshu',
    link: 'https://example.com/hongshu',
    bg: 'linear-gradient(135deg, #f5515f 0%, #a1051d 100%)',
    badgeBg: '#e53e3e'
  },
  {
    name: 'Taobao Platform',
    badge: 'Limited Offer',
    price: '2% ~ 5% OFF',
    note: 'Discount increases with recharge amount',
    features: [
      'Taobao guaranteed transaction, safe',
      'Huabei, credit card and more',
      'Auto delivery, instant use',
      'More recharge, more discount'
    ],
    btnText: 'Buy on Taobao',
    link: 'https://example.com/taobao',
    bg: 'linear-gradient(135deg, #ff6a00 0%, #ee0979 100%)',
    badgeBg: '#dd6b20'
  },
  {
    name: 'Xianyu Platform',
    badge: 'Xianyu Exclusive',
    price: '2% ~ 5% OFF',
    note: 'Discount increases with recharge amount',
    features: [
      'Xianyu guaranteed transaction, safe',
      'Huabei, credit card and more',
      'Instant delivery, quick arrival',
      'More recharge, more discount'
    ],
    btnText: 'Buy on Xianyu',
    link: 'https://example.com/xianyu',
    bg: 'linear-gradient(135deg, #f7971e 0%, #ffd200 100%)',
    badgeBg: '#d69e2e'
  }
]
</script>
