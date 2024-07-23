import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useDark } from '@vueuse/core'

const SysSettingStore = defineStore('sysSetting', () => {
  // state
  const sysStyle = ref({
    headShow: true,
    // 大小屏切分 普通页面不需要考虑横屏，部分三维场景考虑
    $MS: { md: 768 },
    theme: {
      isDark: useDark(),
      // useDark 本地设置 auto light dark
      themeValue: localStorage.getItem("vueuse-color-scheme"),
      head: [
        { height: '35px' }
      ],
      leftControl: {
        tabPosition: 'left'
      }
    },

  })

  const sysObj = {
    $ObjLargeTemp: new Map()
  }

  return { sysStyle, sysObj }
})

export { SysSettingStore }
