<template>
  <div flex items-center w-30 h-11 relative>
    <button
      border-1
      bg-deep-1
      hover:bg-deep-2
      active:bg-deep-3
      border-gray-300
      rounded-s-lg
      p-3
      h-full
    >
      <svg w-3 h-3 text-deep-1 aria-hidden="true" fill="none" viewBox="0 0 18 2">
        <path
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M1 1h16"
        />
      </svg>
    </button>
    <input
      v-model="value"
      bg-deep-0
      h-full
      text-center
      w-full
      py-2.5
      placeholder="111"
      outline-none
      border-1
      border-gray-300
    />
    <button
      border-1
      bg-deep-1
      hover:bg-deep-2
      active:bg-deep-3
      border-gray-300
      rounded-e-lg
      p-3
      h-full
    >
      <svg w-3 h-3 text-gray-900 dark:text-white aria-hidden="true" fill="none" viewBox="0 0 18 18">
        <path
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M9 1v16M1 9h16"
        />
      </svg>
    </button>
  </div>
</template>
<script setup lang="ts">
// 传入值
const value = defineModel({ type: Boolean, required: false })
</script>
<style scoped></style>
