<template>
    <div flex h-full>
        <ul border-4 border-blue w-20 h-full>
            <li v-for="item in tabs.list" :key="item.key" m-2 flex items-center>
                <a :href="'#' + item.key" :class="item.key === tabs.active && 'bg-deep-4'"
                    @click="tabs.active = item.key">{{
                        item.name }}</a>
            </li>

        </ul>
        <main grow h-full border-4 border-black overflow-auto>
            <section v-for="item in tabs.list" :key="item.key" h-300 :id="item.key" border-2 b-black>{{ item.name }}
            <div w-full class="h-1/2" bg-deep-3></div>
            <div w-full class="h-1/2" bg-deep-5></div>
            </section>
        </main>
    </div>
</template>
<script setup lang='ts'>
onMounted(() => {
    //console.log('3.-组件挂载到页面之后执行-------onMounted')
    // IntersectionObserver
    const options = {
        // root is only required because this sandbox is in an iframe.
        // root: document,
        // y缩减一半
        rootMargin: "-50% 0px",
        threshold: 0
    };
    const observer = new IntersectionObserver((entries) => {
        console.log('entries', entries);
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                console.log(entry.target.id)
                tabs.value.active = entry.target.id
            }
        })
    },options)
    const sections = document.querySelectorAll('section')
    sections.forEach(section => {
        observer.observe(section)
    })

})


const tabs = ref({
    active: 'one1',
    list: [
        { key: 'one1', name: 'one' },
        { key: 'two2', name: 'two' },
        { key: 'three3', name: 'three' }
    ]
}
)


</script>
<style scoped></style>