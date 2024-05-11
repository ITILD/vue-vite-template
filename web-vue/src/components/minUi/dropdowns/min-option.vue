<template>
    <li v-if="item">
        <a href="#" block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white
            @click="$emit('click', item)">{{ item.label }}</a>
    </li>
</template>
<script setup lang='ts'>
defineProps({ item: Object })
</script>