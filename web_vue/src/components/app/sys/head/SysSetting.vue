<template>
  <div
    absolute
    z-10
    grid
    grid-cols-3
    rounded-lg
    p-2
    text-xl
    bg-white
    border-gray-100
    dark:border-gray-700
    dark:bg-gray-700
    text-gray-900
    
    md:pb-4
    dark:text-white
    md:w-96
    md:right-48
    md:text-sm
    class="w-11/12 border"
  >
    <button @click="clickChangeHead()">更改head</button>
    <div>{{ sysStyle.headShow }}</div>
    <div class="theme">
      <!-- 主题 -->
      <div class="theme-one">
        <span>主题</span>
        <el-select
          v-model="theme.themeValue"
          placeholder="Select"
          style="width: 240px"
          @change="changeThemeValue"
        >
          <el-option
            v-for="item in themeOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </div>
      <!-- 下划线 -->
      <el-divider></el-divider>
      <!-- 侧边栏 -->
      <div class="theme-one">
        <span>侧边栏位置</span>
        <el-radio-group v-model="theme.leftControl.tabPosition">
          <el-radio-button label="left">左侧</el-radio-button>
          <el-radio-button label="right">右侧</el-radio-button>
        </el-radio-group>
      </div>
      <!-- 下划线 -->
      <el-divider></el-divider>
      <!-- 导航栏 -->
      <div class="theme-one">
        <span>导航栏宽度(px)</span>
        <el-input-number v-model="num" :min="0" :max="90" @change="handleChange" />
      </div>
      <!-- 下划线 -->
      <el-divider></el-divider>
    </div>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { SysSettingStore } from '@/stores/sys'
const { sysStyle } = storeToRefs(SysSettingStore())

/**
 * 更改导航栏显隐
 */
const clickChangeHead = () => (sysStyle.value.headShow = !sysStyle.value.headShow)

/**
 *
 */
const theme = sysStyle.value.theme
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
 * 更改主题
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
