---
sidebar: false
prev:
  text: '使用指南'
  link: '/guide/'
next:
  text: '接口示例'
  link: '/guide/api-examples'
---

# 🚀 快速开始

---

<!-- 快速获取密钥 -->
<div class="qs-key-banner">
  <div class="qs-key-banner-content">
    <div class="qs-key-banner-icon">🔑</div>
    <div class="qs-key-banner-text">
      <h3>快速获取密钥指南</h3>
      <p>一键获取您的 API 密钥，立即开始使用</p>
            <p>新手推荐，快速上手注册和配置流程</p>
    </div>
    <a href="/guide/token" class="qs-key-banner-btn">查看指南 →</a>
  </div>
</div>

## 🌐 官网地址

<div class="qs-address-grid">
  <div class="qs-address-card">
    <div class="qs-address-tag qs-tag-primary">主站</div>
    <div class="qs-address-url">
      <a href="https://api.katioai.com" target="_blank">https://api.katioai.com</a>
    </div>
  </div>
  <div class="qs-address-card">
    <div class="qs-address-tag qs-tag-secondary">备用</div>
    <div class="qs-address-url">
      <a href="https://vip.katioai.com" target="_blank">https://vip.katioai.com</a>
    </div>
  </div>
</div>

## 📡 接口地址

<div class="qs-api-grid">
  <div class="qs-api-card">
    <div class="qs-api-label">主站 API 接口</div>
    <div class="qs-api-url">
      <code>https://api.katioai.com/v1</code>
      <span class="qs-api-badge qs-badge-primary">推荐</span>
    </div>
  </div>
  <div class="qs-api-card">
    <div class="qs-api-label">备用 API 接口</div>
    <div class="qs-api-url">
      <code>https://vip.katioai.com/v1</code>
      <span class="qs-api-badge qs-badge-secondary">备用</span>
    </div>
  </div>
</div>

## ⚡ 快速进入

<div class="qs-quick-grid">
  <a href="https://api.katioai.com/console/topup" target="_blank" class="qs-quick-card">
    <div class="qs-quick-icon">💰</div>
    <div class="qs-quick-name">积分兑换</div>
    <div class="qs-quick-desc">兑换和管理积分</div>
  </a>
  <a href="https://api.katioai.com/console/token" target="_blank" class="qs-quick-card">
    <div class="qs-quick-icon">🎫</div>
    <div class="qs-quick-name">令牌管理</div>
    <div class="qs-quick-desc">创建和管理 API 令牌</div>
  </a>
  <a href="https://api.katioai.com/console" target="_blank" class="qs-quick-card">
    <div class="qs-quick-icon">👤</div>
    <div class="qs-quick-name">个人中心</div>
    <div class="qs-quick-desc">查看账户信息</div>
  </a>
  <a href="https://api.katioai.com/pricing" target="_blank" class="qs-quick-card">
    <div class="qs-quick-icon">📊</div>
    <div class="qs-quick-name">模型价格</div>
    <div class="qs-quick-desc">查看模型定价详情</div>
  </a>
</div>

## 📝 账号注册

<div class="qs-register-section">
  <div class="qs-register-content">
    <h3>注册您的账号</h3>
    <p>只需简单几步，即可完成注册并开始使用枫叶AI的所有服务。注册完成后，您将获得免费的体验额度。</p>
    <div class="qs-register-tip">⚠️ 注意填写QQ邮箱，并在邮箱内收取验证码，收件箱找不到，就到垃圾邮件箱查看</div>
    <a href="https://vip.katioai.com/register" target="_blank" class="qs-register-btn">✨ 点击注册</a>
  </div>
  <div class="qs-register-image">
    <img src="/images/Register/step-1.png" alt="注册流程示意图" class="qs-register-img" />
  </div>
</div>


<style>
/* ============================================================
   Quick Start Page Styles
   ============================================================ */

.qs-subtitle {
  font-size: 1.1rem;
  color: var(--vp-c-text-2);
  margin-top: -16px;
  margin-bottom: 32px;
}

/* Key Banner */
.qs-key-banner {
  background: linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%);
  border-radius: 16px;
  padding: 4px;
  margin-bottom: 36px;
}

.qs-key-banner-content {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 24px 28px;
  border-radius: 13px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.95) 0%, rgba(5, 150, 105, 0.95) 100%);
}

.qs-key-banner-icon {
  font-size: 2.5rem;
  flex-shrink: 0;
}

.qs-key-banner-text {
  flex: 1;
}

.qs-key-banner-text h3 {
  margin: 0 0 4px 0;
  font-size: 1.3rem;
  font-weight: 800;
  color: #fff;
}

.qs-key-banner-text p {
  margin: 0;
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.85);
}

.qs-key-banner-btn {
  display: inline-flex;
  align-items: center;
  padding: 12px 28px;
  border-radius: 28px;
  background: #fff;
  color: #059669 !important;
  font-size: 15px;
  font-weight: 700;
  text-decoration: none !important;
  white-space: nowrap;
  transition: all 0.25s ease;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.qs-key-banner-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

/* Address Grid */
.qs-address-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-top: 16px;
}

.qs-address-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 22px;
  border-radius: 12px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  transition: all 0.25s ease;
}

.qs-address-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.1);
}

.qs-address-tag {
  padding: 4px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 700;
  white-space: nowrap;
  flex-shrink: 0;
}

.qs-tag-primary {
  background: linear-gradient(135deg, #10b981, #059669);
  color: #fff;
}

.qs-tag-secondary {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  color: #fff;
}

.qs-address-url {
  flex: 1;
  min-width: 0;
}

.qs-address-url a {
  color: var(--vp-c-text-1) !important;
  font-size: 15px;
  font-weight: 600;
  text-decoration: none !important;
  word-break: break-all;
}

.qs-address-url a:hover {
  color: var(--vp-c-brand-1) !important;
}

/* API Grid */
.qs-api-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-top: 16px;
}

.qs-api-card {
  padding: 20px 22px;
  border-radius: 12px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  transition: all 0.25s ease;
}

.qs-api-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.1);
}

.qs-api-label {
  font-size: 13px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  margin-bottom: 10px;
}

.qs-api-url {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.qs-api-url code {
  font-size: 14px;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 8px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
  word-break: break-all;
}

.qs-api-badge {
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 700;
  white-space: nowrap;
}

.qs-badge-primary {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}

.qs-badge-secondary {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

/* Quick Grid */
.qs-quick-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 16px;
}

.qs-quick-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 28px 16px 22px;
  border-radius: 14px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  text-decoration: none !important;
  color: inherit !important;
  transition: all 0.3s ease;
}

.qs-quick-card:hover {
  transform: translateY(-4px);
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 12px 32px rgba(16, 185, 129, 0.15);
}

.qs-quick-icon {
  font-size: 2.2rem;
  margin-bottom: 12px;
}

.qs-quick-name {
  font-size: 15px;
  font-weight: 700;
  color: var(--vp-c-text-1) !important;
  margin-bottom: 6px;
}

.qs-quick-desc {
  font-size: 12px;
  color: var(--vp-c-text-3) !important;
  line-height: 1.4;
}

/* Register Section */
.qs-register-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
  margin-top: 16px;
  padding: 28px;
  border-radius: 16px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
}

.qs-register-content h3 {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
  margin: 0 0 12px 0;
}

.qs-register-content p {
  font-size: 0.95rem;
  color: var(--vp-c-text-2);
  line-height: 1.7;
  margin: 0 0 20px 0;
}

.qs-register-tip {
  padding: 12px 16px;
  border-radius: 8px;
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid rgba(245, 158, 11, 0.3);
  color: var(--vp-c-text-1);
  font-size: 0.9rem;
  line-height: 1.6;
  margin-bottom: 20px;
}

.qs-register-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 32px;
  border-radius: 28px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: #fff !important;
  font-size: 15px;
  font-weight: 700;
  text-decoration: none !important;
  transition: all 0.25s ease;
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.3);
}

.qs-register-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.4);
}

.qs-register-image {
  display: flex;
  align-items: center;
  justify-content: center;
}

.qs-register-img {
  width: 100%;
  max-width: 100%;
  border-radius: 12px;
  border: 1px solid var(--vp-c-divider);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  object-fit: contain;
}

.qs-register-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  width: 100%;
  min-height: 200px;
  border-radius: 12px;
  border: 2px dashed var(--vp-c-divider);
  background: var(--vp-c-bg);
}

.qs-placeholder-icon {
  font-size: 2.5rem;
  opacity: 0.5;
}

.qs-placeholder-text {
  font-size: 14px;
  color: var(--vp-c-text-3);
  font-weight: 500;
}

/* Responsive */
@media (max-width: 768px) {
  .qs-key-banner-content {
    flex-direction: column;
    text-align: center;
    gap: 16px;
    padding: 20px;
  }

  .qs-address-grid,
  .qs-api-grid {
    grid-template-columns: 1fr;
  }

  .qs-quick-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }

  .qs-register-section {
    grid-template-columns: 1fr;
    padding: 20px;
  }

  .qs-register-content {
    text-align: center;
  }
}

@media (max-width: 480px) {
  .qs-quick-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }

  .qs-quick-card {
    padding: 20px 12px 16px;
  }

  .qs-quick-icon {
    font-size: 1.8rem;
  }
}
</style>
