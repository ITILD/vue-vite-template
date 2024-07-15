import { createRouter, createWebHistory } from 'vue-router'
import home_page from '@/views/home_page.vue'
import { routerDev } from './_dev'
import { routerBlog } from './blog'
const routes = [
  // 首页同步
  { path: '/', component: home_page },
  // blog
  ...routerBlog,
  // 开发测试
  ...routerDev
]

// 生成路由  注意nginx发布配置 添加跳转
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

export default router
