<template>
  <!-- 网站页首 -->
  <header v-show="sysStyle.headShow">
    <div flex flex-wrap justify-between items-center mx-auto p-4>
      <router-link to="/" class="flex items-center">
        <!-- <img src="@/assets/star.svg" class="h-8 mr-3" alt="Flowbite Logo" /> -->
        <span class="self-center text-2xl font-semibold whitespace-nowrap">欢迎页</span>
      </router-link>
      <!-- 网站导航栏 -->
      <!-- 小屏幕设备 下拉列表开关 -->
      <button
        @click="isMenuOpen = !isMenuOpen"
        id="mega-menu-full-image-button"
        data-collapse-toggle="mega-menu-full-image"
        type="button"
        aria-controls="mega-menu-full-image"
        aria-expanded="false"
        inline-flex
        items-center
        p-2
        ml-1
        text-sm
        text-gray-500
        rounded-lg
        md:hidden
        hover:bg-gray-100
        focus:outline-none
        focus:ring-2
        focus:ring-gray-200
        dark:text-gray-400
        dark:hover:bg-gray-700
        dark:focus:ring-gray-600
      >
        <span class="sr-only">下拉列表</span>
        <ListSVG />
      </button>
      <!--导航栏 水平靠右(pc屏幕)下拉居中(小屏设备) -->
      <MinPopover
        v-model="isMenuOpen"
        id="mega-menu-full-image"
        items-center
        justify-between
        w-full
        md:w-auto
        md:order-1
      >
        <ShowHidden>
          <span v-show="isMenuOpen || isMd || showFun1">
            <ul flex flex-col mt-4 font-medium md:flex-row md:space-x-8 md:mt-0>
              <li>
                <router-link
                  to="/_dev"
                  class="block py-2 pl-3 pr-4 text-gray-900 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
                  >_开发测试</router-link
                >
              </li>
              <!-- 用户头像 -->
              <li>
                <button
                  @click="isUserControlShow = !isUserControlShow"
                  id="mega-menu-full-cta-image-button"
                  data-collapse-toggle="mega-menu-full-image-dropdown"
                  class="flex items-center justify-between w-full py-2 pl-3 pr-4 font-medium text-gray-900 border-b border-gray-100 md:w-auto hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
                >
                  用户图标
                </button>

                <MinPopover v-model="isUserControlShow">
                  <ShowHidden v-show="isUserControlShow">
                    <UserControl absolute z-1 md:right-10 />
                  </ShowHidden>
                </MinPopover>
              </li>
              <!-- setting -->
              <li>
                <button
                  @click="isSysSettingShow = !isSysSettingShow"
                  id="mega-menu-full-cta-image-button"
                  data-collapse-toggle="mega-menu-full-image-dropdown"
                  class="flex items-center justify-between w-full py-2 pl-3 pr-4 font-medium text-gray-900 border-b border-gray-100 md:w-auto hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700"
                >
                  设置
                </button>
                <SimplePopover :show="isSysSettingShow" :bg="true">
                  <ShowHidden v-show="isSysSettingShow">
                    <div
                      z-99
                      position-center
                      rounded-lg
                      p-2
                      text-xl
                      bg-deep-0
                      class="w-4/5 h-4/5 border"
                    >
                      <button @click="isSysSettingShow = !isSysSettingShow">X</button>
                      <SysSetting />
                    </div>
                  </ShowHidden>
                </SimplePopover>
              </li>
            </ul>
          </span>
        </ShowHidden>
      </MinPopover>
    </div>
  </header>
</template>

<script setup lang="ts">
import ListSVG from '@/assets/img/svg/ListSVG.vue'
import { ref } from 'vue'
import MinPopover from '@/components/common/minUi/button/MinPopover.vue'
import Func_1 from './head/Func_1.vue'
import SysSetting from './head/SysSetting.vue'
import ShowHidden from '@/components/common/minUi/animation/ShowHidden.vue'
// 显隐控制
import { storeToRefs } from 'pinia'
import { SysSettingStore } from '@/stores/sys'
const sysSettingStore = SysSettingStore()
// 样式控制
const sysStyle = sysSettingStore.sysStyle
// 小屏幕下拉列表
const isMenuOpen = ref(false)
//
const isMd = ref(window.innerWidth > sysStyle.$MS.md)
window.onresize = () => (isMd.value = window.innerWidth > sysStyle.$MS.md)
const showFun1 = ref(false)
const isSysSettingShow = ref(false)
const isUserControlShow = ref(false)
</script>

<style></style>
