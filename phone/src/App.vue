<template>
  <RouterView />

  <!--悬浮窗 全局播放/暂停 跳转  机器人急停?-->
  <div>
    <!-- 全局播放/暂停 跳转 -->

    <!-- 机器人急停? -->
  </div>
</template>

<script setup lang="ts">
// 整体的标头标尾 由全局状态动态改变
// 路由内容要有最小高度 默认配置
// 考虑完整页面  可以设置标头显隐
// 考虑单页100% canvas类页面   可以设置标头显隐
// 考虑无限制地图类分块类   123

console.log('VITE_ENV', import.meta.env.VITE_ENV)
console.log('VITE_SOME_KEY', import.meta.env.VITE_SOME_KEY)
</script>

<style>
/* 导入main.css */
@import '@/assets/main.css';

</style>
