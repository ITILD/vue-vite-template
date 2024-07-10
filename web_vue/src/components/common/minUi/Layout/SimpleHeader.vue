<template>
  <div w-full h-15 flex flex-wrap justify-between items-center mx-auto p-4 bg-deep-1-op35>
    <!-- 回退路由 -->
    <div @click="router.back()">图标1</div>
    <!-- 居中小标题 -->
    <span left-0 right-0 m-auto> <slot></slot></span>
    <router-link to="/"> 图标2 </router-link>
  </div>
  <!-- 用法 -->
  <!-- <div grid-head-center-foot>
      <SimpleHeader>设置</SimpleHeader>
      <main w-full bg-deep-2>
        <a-button>Add</a-button>
      </main>
      <div>foot</div>
    </div> -->
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
const router = useRouter()
</script>

<style scoped></style>
