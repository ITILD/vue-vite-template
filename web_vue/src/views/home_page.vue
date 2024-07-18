<template>
  <div grid-head-center-foot>
    <SysHeader h-14 />
    <main bg-deep-3 px-1 py-2>
      <div bg-deep-2 h-full rounded-md p-2>
        <!--  -->
        <div>test</div>
      </div>
    </main>
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
