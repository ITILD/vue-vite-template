<template>
  <div grid-head-center-foot>
    <SysHeader bg-deep-1-op35 />
    <main w-full bg-deep-2>test</main>
    <SysFooter bg-deep-1 />
  </div>
</template>

<script setup lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { storeToRefs } from 'pinia'
import { SysSettingStore } from '@/stores/sys'
const { sysStyle } = storeToRefs(SysSettingStore())
sysStyle.value.headShow = true
console.log('跳转')
</script>
<style scoped>
</style>
