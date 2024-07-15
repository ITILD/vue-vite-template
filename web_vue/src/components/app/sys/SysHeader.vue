<template>
  <!-- 网站页首 -->
  <header v-show="sysStyle.headShow" bg-deep-1>
    <div flex flex-wrap justify-between p-4>
      <router-link to="/" flex>
        <img src="@/assets/img/ion/sy_w.svg" h-8 mr-3 />
        <span self-center text-2xl font-semibold whitespace-nowrap>XYZ</span>
      </router-link>
      <!-- 空标题 可以加装饰 -->
      <span left-0 right-0 m-auto></span>
      <!-- 网站导航栏 -->
      <UserSVG @click="isUserControlShow = !isUserControlShow" />
      <MinPopover v-model="isUserControlShow">
        <ShowHidden v-show="isUserControlShow">
          <UserControl
            absolute
            z-10
            w-50
            right-2
            top-4
            rounded-lg
            bg-deep-0
            p-4
            text-xl
            shadow-xl
            @click="isUserControlShow = false"
          />
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
//
import UserSVG from '@/assets/img/svg/UserSVG.vue'
// 显隐控制
import { SysSettingStore } from '@/stores/sys'
const sysSettingStore = SysSettingStore()
// 样式控制
const sysStyle = sysSettingStore.sysStyle
// 小屏幕下拉列表
const isMenuOpen = ref(false)
//

const showFun1 = ref(false)
const isSysSettingShow = ref(false)
const isUserControlShow = ref(false)
</script>

<style></style>
