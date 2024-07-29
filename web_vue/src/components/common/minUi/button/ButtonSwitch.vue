<template>
  <!-- 选择器组件 使用方法 -->
  <!-- <ButtonSwitch v-model="mapEditObj.isWmsShow" @change = "console.log('change')"/> -->
  <label inline-flex items-center cursor-pointer>
    <input type="checkbox" :checked="checked" class="sr-only peer" @change="changeChecked" />
    <div
      relative
      w-14
      h-7
      bg-deep-3
      dark:peer-focus:ring-blue-800
      rounded-full
      peer
      peer-checked:after:translate-x-full
      rtl:peer-checked:after:-translate-x-full
      after:absolute
      after:top-0.5
      after:bg-white
      after:border-gray-300
      after:border
      after:rounded-full
      after:h-6
      after:w-6
      after:transition-all
      dark:border-gray-600
      peer-checked:bg-blue-600
      class="after:content-[''] after:start-[4px]"
    ></div>
  </label>
</template>
<script setup lang="ts">
// 传入值
const checked = defineModel({ type: Boolean, required: false })
const changeChecked = (e: Event) => (checked.value = (e.target as HTMLInputElement).checked)
</script>
<style scoped></style>
