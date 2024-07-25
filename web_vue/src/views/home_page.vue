<template>
  <div grid-head-center-foot>
    <SysHeader h-14 bg-deep-1 />
    <!-- :style="'clip-path: polygon(0 0, 100% 0, 100% 100%, 0 '+clipPath[0]+'%)'"  -->
    <main bg-deep-3 px-1 py-2>
      <div bg-deep-2 h-full rounded-md p-2>
        <!--  -->
        <div>
          过滤
          list
        </div>
        <div>页码</div>
        <div>
          
          增 删 改（链接）
        </div>
      </div>

      <MoveWindow  >
        <div w-30 h-30 rounded-3xl flex-center btn-deep-6> 

          <div font-600 text-4xl  font-serif @click="addPage">新建</div>
        </div>
       </MoveWindow>
    </main>
    <SysFooter  mx-auto w-full p-2 lg:py-2 bg-deep-0  />
  </div>
</template>

<script setup lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { storeToRefs } from 'pinia'
import { SysSettingStore } from '@/stores/sys'
const { sysStyle } = storeToRefs(SysSettingStore())
sysStyle.value.headShow = true
console.log('跳转')
const clipPath =ref( [100])
// offset-path是用来实现路径动画  可以考虑流星浪花藤曼
const addPage = () => {
  console.log('addPage')
}
</script>
<style scoped></style>
