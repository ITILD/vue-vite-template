<template>
  <div >
    <!-- 黑白主题 -->
    <div flex >
      <div>主题:</div>
      <select v-model="theme.themeValue" @change="changeThemeValue" bg-deep-2>
        <!-- <option disabled value="">Please select one</option> -->
        <option v-for="item in themeOptions" :key="item.value" :label="item.label" :value="item.value" />
      </select>
    </div>
    <!-- 黑白主题 -->
    <div flex >
      <div>{{ $t('message.language') }}:</div>
      <select v-model="sysStyle.language" @change="i18n.global.locale = sysStyle.language" bg-deep-2>
        <!-- <option disabled value="">Please select one</option> -->
        <option v-for="item in languageOptions" :key="item.value" :label="item.label" :value="item.value" />
      </select>
    </div>

  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { SysSettingStore } from '@/stores/sys'
 import { i18n } from '@/i18n/language'
const { sysStyle } =SysSettingStore()


/////////////////////////////////////////////////////////主题控制/////////////////////////////////////////////////////////
const theme = sysStyle.theme
/**
 * 主题选择
 */
const themeOptions = [
  {
    value: 'light',
    label: '亮'
  },
  {
    value: 'dark',
    label: '暗'
  },
  {
    value: 'auto',
    label: '跟随系统'
  }
]
/**
 * 手动更改主题
 */
function changeThemeValue() {
  switch (theme.themeValue) {
    case 'light':
      theme.isDark = false
      break
    case 'dark':
      theme.isDark = true
      break
    case 'auto':
      // 媒体查询检测夜晚/黑暗模式
      theme.isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
      break
  }
}
/////////////////////////////////////////////////////////语言修改/////////////////////////////////////////////////////////
/**
 * 主题选择
 */
const languageOptions = [
  {
    value: 'zh',
    label: '中文'
  },
  {
    value: 'en',
    label: 'English'
  },
  {
    value: 'ja',
    label: '日本語'
  }
]

/**
 * 侧边栏方位设置
 */
const optionsTabPosition = [
  {
    value: 'right',
    label: '右侧'
  },
  {
    value: 'left',
    label: '左侧'
    // disabled: true,
  }
]

/**
 * 导航宽度
 */
const num = ref(theme.head[0].height.replace('px', ''))
const handleChange = (value: number) => {
  theme.head[0].height = value + 'px'
}
</script>

<style>
.theme {
  position: relative;
  top: 20px;
}

.theme-one {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-left: 40px;
}
</style>
