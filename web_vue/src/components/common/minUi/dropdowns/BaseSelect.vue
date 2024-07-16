<template>
  <!-- text-align-last-justify unocss自定义 文字均匀分布 -->
  <div flex items-center p-3 bg-deep-2 rounded-md text-align-last-justify>
    <!-- 对齐key -->
    <div class="w-4/9" flex items-center>
      <span w-full h-full v-if="name">{{ name }}</span>
      <span mx-2 h-full v-if="name">:</span>
    </div>
    <!-- 下拉选择 -->
    <select
      v-model="model"
      @change="changeValueFunc"
      bg-deep-3
      class="w-5/9"
      h-full
      rounded-md
      outline-none
      px-4
    >
      <!-- <option disabled value="">Please select one</option> -->
      <option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        bg-deep-4
        p-20
      />
    </select>
  </div>
</template>
<script setup lang="ts">
// 传入值
const model = defineModel({ type: Boolean, required: false })
defineProps(['name', 'options', 'changeValueFunc'])
</script>
<style scoped>

</style>
