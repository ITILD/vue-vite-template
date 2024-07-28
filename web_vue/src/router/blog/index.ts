const routerBlog = [
  // 已添加
  { path: '/blog', component: () => import('@/views/blog/index-page.vue') },
  // gl
  { path: '/blog/blog-instruction', component: () => import('@/views/blog/blog-instruction-page.vue') },
  { path: '/blog/blog-new', component: () => import('@/views/blog/blog-new-page.vue') },
  { path: '/blog/blog-read', component: () => import('@/views/blog/blog-read-page.vue') },

]
export { routerBlog }
