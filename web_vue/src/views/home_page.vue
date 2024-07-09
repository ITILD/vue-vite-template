<template>
    <div grid-head-center-foot>
    <SysHeader />
    <main class="bg-white dark:bg-gray-2 m-5">test</main>
    <SysFooter />
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
<style scoped></style>
