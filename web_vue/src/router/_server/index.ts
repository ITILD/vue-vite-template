const routerServer = [
  // 已添加
  {
    path: '/_server', component: () => import('@/views/_server/index-page.vue'),

    children: [
      { path: 'dev_state', component: () => import('@/views/_server/index-page/dev_state.vue') },
      { path: 'server_state', component: () => import('@/views/_server/index-page/server_state.vue') },
    ]
  },
]
export { routerServer }
