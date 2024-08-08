<template>
  <div grid-head-center-foot>
    <SysHeader h-14 bg-deep-1 z-999  shadow shadow-gray/>
    <!-- :style="'clip-path: polygon(0 0, 100% 0, 100% 100%, 0 '+clipPath[0]+'%)'"  -->
    <main bg-deep-3 px-1 py-2 >
      <div bg-deep-2 h-full rounded-md p-2 >
        <!-- 类似知乎抖音刷 -->
        <div >
          图数据库选择 下拉 大类   跳转后子类


          考虑桌面风格文件和列表
        </div>
        
        <div >
          过滤
          list
        </div>
        
        <div >页码  </div>
        <div> 地球 飞船 黑洞     编辑 新建 删除</div>

        <div>语义化Semanticization</div>
        <div>设计代码器 2  editblog后面</div>

      </div>

      <MoveWindow  right-8 bottom-30 >
        <div w-30 h-30 rounded-3xl flex-center btn-deep-6 shadow-md shadow-gray > 

          <!-- <div  @click="addPage">新建</div> -->
          <!-- /blog/blog-new 路由 -->
           <RouterLink font-600 text-4xl  font-serif  to="/blog/blog-new" >新建</RouterLink>
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
