<template>
  <div>
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
        <div class="relative flex items-center max-w-[8rem]">
        <button type="button" id="decrement-button" data-input-counter-decrement="quantity-input" class="bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none">
            <svg class="w-3 h-3 text-gray-900 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 2">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h16"/>
            </svg>
        </button>
        <input type="text" id="quantity-input" data-input-counter aria-describedby="helper-text-explanation" class="bg-gray-50 border-x-0 border-gray-300 h-11 text-center text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full py-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="999" required />
        <button type="button" id="increment-button" data-input-counter-increment="quantity-input" class="bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none">
            <svg class="w-3 h-3 text-gray-900 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
            </svg>
        </button>
    </div>
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
