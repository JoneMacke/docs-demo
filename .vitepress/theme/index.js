// https://vitepress.dev/guide/custom-theme
import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import './style.css'
import HomeHero from './components/HomeHero.vue'
import HomeHeroEn from './components/HomeHeroEn.vue'
import GuideNav from './components/GuideNav.vue'
import GuideNavEn from './components/GuideNavEn.vue'
import AppNav from './components/AppNav.vue'
import CodeNav from './components/CodeNav.vue'
import ShopNav from './components/ShopNav.vue'
import ShopNavEn from './components/ShopNavEn.vue'

/** @type {import('vitepress').Theme} */
export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      // https://vitepress.dev/guide/extending-default-theme#layout-slots
    })
  },
  enhanceApp({ app, router, siteData }) {
    app.component('HomeHero', HomeHero)
    app.component('HomeHeroEn', HomeHeroEn)
    app.component('GuideNav', GuideNav)
    app.component('GuideNavEn', GuideNavEn)
    app.component('AppNav', AppNav)
    app.component('CodeNav', CodeNav)
    app.component('ShopNav', ShopNav)
    app.component('ShopNavEn', ShopNavEn)
  }
}
