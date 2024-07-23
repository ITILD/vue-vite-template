<template>
  <div w-full h-full>
    <!-- 重要路由 -->
    <!-- 所有路由 -->
    <div>
      <template v-for="L1 in routerAll.rootAll" :key="L1.name">
        <div v-if="L1 && L1.child && L1.child.length > 0">
          <!-- 1级大类 -->
          <h1 class="text-xl bg-blue-700">{{ L1.name }}</h1>
          <!-- 2级分类 -->
          <div class="grid grid-cols-5">
            <div v-for="L2 in L1.child" :key="L2.name">
              <h2 class="text-lg bg-blue-300">{{ L2.name }}</h2>
              <!-- 3级具体 -->
              <div v-for="L3 in L2.child" :key="L3.name">
                <router-link :to="L3.url" class="text-lg bg-blue-100 hover:invert">{{
                  L3.name
                }}</router-link>
              </div>
              <!--  -->
            </div>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
/**
 * 大类一块   块内每行四分小块  没有就换行    小块只有一个则单占    例子可以放第一大块二次展示
 */

const routerAll = reactive({
  rootMain: [
    {
      name: 'think',
      child: []
    },
    {
      name: 'math',
      child: []
    },
    {
      name: 'Graphics',
      child: [
        {
          img: '',
          name: 'gl'
        },
        {
          img: '',
          name: 'gis'
        },
        {
          img: '',
          name: 'cad'
        }
      ]
    },
    {
      name: 'voice',
      child: [
        {
          img: '',
          name: 'test0'
        },
        {
          img: '',
          name: 'test1'
        },
        {
          img: '',
          name: 'test2'
        }
      ]
    },
    {
      name: 'fun'
    }
  ],
  rootAll: [
    // 不知道什么分类
    {
      name: 'waaa',
      child: [
        {
          img: '',
          name: '插件测试',
          child: [
            {
              name: '平板摄像头测试',
              url: '/_dev/beauty/web-design-base'
            },
            {
              name: '网页滚动轴设计',
              url: '/_dev/beauty/web-scroll-base-page'
            }
          ]
        },
        {
          // L2
          img: '',
          name: '组件样式',
          child: []
        }
      ]
    }
  ]
})
</script>
