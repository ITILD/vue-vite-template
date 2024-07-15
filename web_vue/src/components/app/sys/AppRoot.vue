<template>
  <SimplePopover
    fixed
    left-0
    top-0
    w-full
    h-full
    :show="sysSettingStore.isSysSettingShow"
    :bg="true"
  >
    <ShowHidden v-show="sysSettingStore.isSysSettingShow">
      <div
        z-100
        position-center
        rounded-lg
        text-xl
        shadow-xl
        bg-deep-0
        class="w-4/5 h-4/5 md:w-3/5 md:h-3/5"
      >
        <div relative h-10>
          <button
            absolute
            right-0
            m-3
            @click="sysSettingStore.isSysSettingShow = !sysSettingStore.isSysSettingShow"
          >
            X
          </button>
        </div>
        <SysSetting bg-deep-1 />
      </div>
    </ShowHidden>
  </SimplePopover>
</template>
<script setup lang="ts">
// 显隐控制
import { SysSettingStore } from '@/stores/sys'
const sysSettingStore = SysSettingStore()
</script>
<style scoped></style>
