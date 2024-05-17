import 'virtual:uno.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// 初始化css 用来重置边距 margin等0
import '@unocss/reset/tailwind.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
