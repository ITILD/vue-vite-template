import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import VueDevTools from 'vite-plugin-vue-devtools'

// css 辅助
import UnoCSS from 'unocss/vite'

// 自动导入按需引入 vue ion router
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import Icons from 'unplugin-icons/vite'
import IconsResolver from 'unplugin-icons/resolver'
import VueRouter from 'unplugin-vue-router/vite'
// 
import path from 'path'
const pathSrc = path.resolve(__dirname, 'src')

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    VueRouter({}),
    vue(),
    VueDevTools(),
    UnoCSS(),
    AutoImport({
      // 自动导入 Vue 相关函数，如：ref, reactive, toRef 等
      imports: ['vue', 'vue-router', 'pinia'], // eslint报错解决
      eslintrc: {
        // 一旦生成配置文件之后，最好把enable关掉，即改成false。否则这个文件每次会在重新加载的时候重新生成，这会导致eslint有时会找不到这个文件。
        enabled: false, // Default `false`
        filepath: './.eslintrc-auto-import.json', // Default `./.eslintrc-auto-import.json`
        globalsPropValue: true, // Default `true`, (true | false | 'readonly' | 'readable' | 'writable' | 'writeable')
      },
      resolvers: [
        // 自动导入图标组件
        IconsResolver({ prefix: 'Icon' })
      ],
      dts: path.resolve(pathSrc, 'auto-imports.d.ts')
    }),
    Components({
      resolvers: [
        // 自动注册图标组件  edit引入格式 <i-ep-edit />
        IconsResolver({ enabledCollections: ['ep'] })
      ],
      dts: path.resolve(pathSrc, 'components.d.ts')
    }),
    // 自动引入图标资源
    Icons({ autoInstall: true })
  ],
  // 路径别名
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  // 开发服务设置
  server: {
    port: 1666,
    strictPort: true,
    host: '0.0.0.0',
    headers: {
      'Access-Control-Allow-Origin': '*'
    }
  }
})
