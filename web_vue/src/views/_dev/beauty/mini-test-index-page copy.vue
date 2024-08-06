<template>
    <div flex h-full>
        <ul border-4 border-blue w-20 h-full>
            <li v-for="(item, index) in dataAll" :key="item.key" m-2 flex items-center>
                <a :href="'#' + item.key" :class="item.key === dataSlice.active && 'bg-deep-4'"
                   @click="clickFunc(index)">{{ item.name }}</a>
            </li>
            <!-- <li v-for="(item, index) in dataAll" :key="item.key" m-2 flex items-center>
                <a :href="'#' + item.key" :class="item.key === dataSlice.active && 'bg-deep-4'"
                    @click="clickDataItem(item, index)">{{ item.name }}</a>
            </li> -->
        </ul>
        <main grow h-full border-4 border-black overflow-auto>
            <ul>
                <li v-for="item in list" :key="item" ref="itemRefs">
                    {{ item }}
                </li>
            </ul>
            <section v-for="(item, index) in dataSlice.list" :key="index" h-300 :id="item.key" border-2 b-black
                ref="dataRef">
                <div>{{ item.name }}</div>
                <!-- component -->
                <Suspense v-if="item.component">
                    <!-- 主要内容 -->
                    <component :is="item.component" />
                    <!-- 加载中状态 -->
                    <template #fallback>
                        <WaitAnimate></WaitAnimate>
                    </template>
                </Suspense>
            </section>
        </main>
    </div>
</template>
<script setup lang="ts">
const monacoEditor = defineAsyncComponent(
    () => import('@/components/app/sys/blog/BlogEditor/monacoEditor.vue')
)

const dataRef = ref([])
onMounted(() => {
    // 初始加载
    clickDataItem(dataAll[0], 0)

})



// 所有列表
const dataAll = [
    {
        key: 'one1',
        name: 'one',
        component: monacoEditor
    },
    {
        key: 'two2',
        name: 'two'
    },
    {
        key: 'three3',
        name: 'three',
        component: monacoEditor
    },
    {
        key: 'four4',
        name: 'four'
    },
    {
        key: 'five5',
        name: 'five'
    }
]
const dataSlice = ref({
    active: 'one1',
    list: [dataAll[0]]
})
/**
 * 更新数据
 * @param data 对象
 * @param index 数组索引
 */
const clickDataItem = (data: { key: any }, index: any) => {
    console.log('test!!!!!!!!!!!', 'clickDataItem')
    const indexThis = index - 1
    dataSlice.value = {
        active: data.key,
        list: dataAll.slice(indexThis < 0 ? 0 : indexThis, index + 2)
    }
}
const listAll =[{
    key: '1'
},
{
    key: '2'
},
{
    key: '3'
},
{
    key: '4'
}
]

const list = ref([listAll[0]])

const itemRefs = ref([])
const clickFunc = (index: number) => {
    list.value = listAll.slice(0, index+1)
}
onUpdated(() => {
    console.log('test!!!!!!!!!!!', itemRefs.value)
    console.log('test!!!!!!!!!!!', dataRef.value)
    dataRef.value.forEach((section) => {
        observer.observe(section)
    })
});
const options = {
    // root is only required because this sandbox is in an iframe.
    // root: document,
    // y缩减一半
    rootMargin: '-50% 0px',
    threshold: 0
}
const observer = new IntersectionObserver((entries) => {
    console.log('entries', entries)
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            console.log(entry.target.id)
            // dataSlice.value.active = entry.target.id
        }
    })
}, options)
</script>
<style scoped></style>
