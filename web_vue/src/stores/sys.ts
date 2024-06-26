import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

const SysSettingStore = defineStore('sysSetting', () => {
  // state
  const sysStyle = ref({
    headShow: true,
    // 大小屏切分 普通页面不需要考虑横屏，部分三维场景考虑
    $MS: { md: 768 }
  })

  const sysObj = {
    $ObjLargeTemp: new Map()
  }

  return { sysStyle, sysObj }
})

export { SysSettingStore }
