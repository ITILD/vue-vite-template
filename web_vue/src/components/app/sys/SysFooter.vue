<template>
  <footer mx-auto w-full p-2  lg:py-2  bg-deep-1>
    <hr  border-gray-200 sm:mx-auto dark:border-gray-5 lg:mb-2 />
    <!-- 关联账号 本站 备案 -->
    <div sm:flex sm:items-center sm:justify-between>
      <!-- 关联账号 -->
      <div text-gray-500 flex mt-4 space-x-6 sm:justify-center sm:mt-0>
        <a href="#" hover:text-gray-900 dark:hover:text-white>
          <GmailSVG />
          <span sr-only>Gmail</span>
        </a>
        <a href="#" hover:text-gray-900 dark:hover:text-white>
          <GithubSVG />
          <span sr-only>GitHub account</span>
        </a>
        <a href="#" hover:text-gray-900 dark:hover:text-white>
          <DribbbleSVG />
          <span sr-only>Dribbble account</span>
        </a>
      </div>
      <!-- 年份提示 -->
      <span text-sm text-gray-500 sm:text-center dark:text-gray-400
        >© 2023-{{ yearNow }} <a href="https://wx1s.com/" hover:underline>ITILD</a>. All Rights
        Reserved.<br />
      </span>
      <!-- 备案 -->
      <span text-xs text-gray-500 sm:text-center dark:text-gray-400
        >© 备案号: <a href="https://beian.miit.gov.cn/" target="_blank">辽ICP备2022000388号-1</a>
      </span>
    </div>
  </footer>
</template>

<script setup lang="ts">
import GithubSVG from '@/assets/img/svg/GithubSVG.vue'
import DribbbleSVG from '@/assets/img/svg/DribbbleSVG.vue'
import GmailSVG from '@/assets/img/svg/GmailSVG.vue'
const yearNow = new Date().getFullYear()
</script>

<style></style>
