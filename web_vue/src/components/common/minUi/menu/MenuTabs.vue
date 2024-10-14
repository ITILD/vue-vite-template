<template>
  <div flex  bg-deep-3>
    <ul h-full text-sm p-2 bg-deep-0>
      <!-- 循环列表tabs -->
      <li v-for="item in tabs" :key="item.key" m-2>
        <!--hover:bg-deep-2 -->
        <router-link :to="item.routeUrl" @click="activeKey = item.key" inline-flex items-center p-4 rounded-lg w-full
          :class="activeKey === item.key ? 'bg-deep-3' : 'bg-deep-2'">
          <img :src="item.img" alt="" w-5 h-5 />
          <span ml-2>{{ item.label }}</span>
        </router-link>
      </li>
    </ul>
    <div h-full p-3 grow bg-deep-2>
      <RouterView />
    </div>
  </div>
</template>
<script setup lang='ts'>
const activeKey = ref('1')
const tabs = ref([
  {
    key: '1',
    label: 'test1',
    img: '@/assets/img/ion/sy_w.svg',
    routeUrl: '/_server/dev_state'
  },
  {
    key: '2',
    label: 'test2',
    img: '@/assets/img/ion/sy_w.svg',
    routeUrl: '/_server/server_state'
  },
])
</script>
<style scoped></style>