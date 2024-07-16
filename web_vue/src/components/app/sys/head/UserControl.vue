<template>
  <div>
    <ul flex flex-col>
      <li>
        <RouterLink to="/">XYZ</RouterLink>
      </li>
      <li>
        <button
          @click="showFun1 = !showFun1"
          id="mega-menu-full-cta-image-button"
          data-collapse-toggle="mega-menu-full-image-dropdown"
          class="flex items-center justify-between w-full py-2 pl-3 pr-4 font-medium text-gray-900 border-b border-gray-100 md:w-auto hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
        >
          项目列表1
          <svg
            class="w-5 h-5 ml-1"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </button>
        <MinPopover v-model="showFun1">
          <ShowHidden>
            <div
              v-show="showFun1"
              class="absolute z-10 grid grid-cols-3 rounded-lg p-2 w-11/12 text-xl bg-white border border-gray-100 dark:border-gray-700 dark:bg-gray-700 text-gray-900 md:pb-4 dark:text-white md:w-96 md:right-48 md:text-sm"
            >
              <Func_1></Func_1>
            </div>
          </ShowHidden>
        </MinPopover>
      </li>
      <li>
        <router-link
          to="/blog"
          class="block py-2 pl-3 pr-4 text-gray-900 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
          >blog</router-link
        >
      </li>
      <li>
        <router-link
          to="/_dev"
          class="block py-2 pl-3 pr-4 text-gray-900 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
          >_开发测试</router-link
        >
      </li>
      <!-- setting -->
      <li>
        <button
          @click="sysSettingStore.isSysSettingShow = !sysSettingStore.isSysSettingShow"
          id="mega-menu-full-cta-image-button"
          data-collapse-toggle="mega-menu-full-image-dropdown"
          class="flex items-center justify-between w-full py-2 pl-3 pr-4 font-medium text-gray-900 border-b border-gray-100 md:w-auto hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
        >
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
import SysSetting from './SysSetting.vue'
import ShowHidden from '@/components/common/minUi/animation/ShowHidden.vue'
//
import SettingSVG from '@/components/common/miniSvg/SettingSVG.vue'
// 显隐控制
import { SysSettingStore } from '@/stores/sys'
const sysSettingStore = SysSettingStore()

const showFun1 = ref(false)
const isUserControlShow = ref(false)
</script>

<style></style>
