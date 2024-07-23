<template>
  <div>
    <ul flex flex-col>
      <li>
        <div mini-text-center-between>
          <UserLogin />
          <div @click="sysStyle.isUserControlShow = false">X</div>
        </div>
      </li>
      <li>
        <button @click="showFun1 = !showFun1" mini-text-center-between w-full p-2 text-gray-900 border-b border-gray-200
          dark:border-gray-500 bg-deep-0 hover:bg-deep-2>
          项目列表1
          <svg class="w-5 h-5 ml-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"></path>
          </svg>
        </button>
        <MinPopover v-model="showFun1">
          <ShowHidden>
            <div v-show="showFun1" mini-text-center-between w-full p-2 text-gray-900 border-b border-gray-200
              dark:border-gray-500 bg-deep-0 hover:bg-deep-2>
              <Func_1></Func_1>
            </div>
          </ShowHidden>
        </MinPopover>
      </li>
      <li>
        <router-link to="/blog" mini-text-center-between w-full p-2 text-gray-900 border-b border-gray-200
          dark:border-gray-500 bg-deep-0 hover:bg-deep-2>blog</router-link>
      </li>
      <li>
        <router-link to="/_dev" mini-text-center-between w-full p-2 text-gray-900 border-b border-gray-200
          dark:border-gray-500 bg-deep-0 hover:bg-deep-2>_开发测试</router-link>
      </li>
      <!-- setting -->
      <li>
        <button @click="openSysSettingShow" mini-text-center-between w-full p-2 text-gray-900 border-b border-gray-200
          dark:border-gray-500 bg-deep-0 hover:bg-deep-2>
          <SettingSVG />设置
        </button>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import MinPopover from '@/components/common/minUi/button/MinPopover.vue'
import Func_1 from './Func_1.vue'
import ShowHidden from '@/components/common/minUi/animation/ShowHidden.vue'
//
import SettingSVG from '@/components/common/miniSvg/SettingSVG.vue'
// 显隐控制
import { SysSettingStore } from '@/stores/sys'
const sysSettingStore = SysSettingStore()
const sysStyle = sysSettingStore.sysStyle
const showFun1 = ref(false)
const closeUserControlShow = () => sysStyle.isUserControlShow = false

const openSysSettingShow = () => {
  sysSettingStore.isSysSettingShow = true
  closeUserControlShow()
}
</script>

<style></style>
