<template>

    <button id="dropdownDelayButton" @click.stop="dropdown = !dropdown" px-5 py-2.5 text-center inline-flex items-center
        btn-2>
        {{ valueSelect && valueSelect.label || ' 空 ' }}
        <svg w-2.5 h-2.5 ms-3 xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="m1 1 4 4 4-4" />
        </svg>
    </button>
    <!-- Dropdown menu -->
    <div ref="dropdown" v-if="dropdown && data.length > 0" z-10 bg-white divide-y divide-gray-100 rounded-lg shadow w-44
        dark:bg-gray-700>
        <ul py-2 text-sm text-gray-700 dark:text-gray-200>
            <slot></slot>
        </ul>
    </div>


</template>
<script setup lang='ts'>
/**
 * 用法
 const data = reactive([
     { label: 'Dropdown 1', value: 1 },
     { label: 'Dropdown 2', value: 2 },
     { label: 'Dropdown 3', value: 3 },
     { label: 'Dropdown 4', value: 4 },
     { label: 'Dropdown 5', value: 5 },
     { label: 'Dropdown 6', value: 6 },
     { label: 'Dropdown 7', value: 7 },
     { label: 'Dropdown 8', value: 8 },
 ])
 const valueSelect = ref(list[0])
 */

//  下拉
import { onClickOutside } from '@vueuse/core'
const dropdown = ref(false)
onClickOutside(
    dropdown as any,
    (event) => {
        console.log(event)
        dropdown.value = false
    },
)

const props = defineProps({
    data: {
        type: Array<{ label: string, value: number }>,
        default: [{ label: '空', value: 0 }]
    }
})

// 传入值
const valueSelect = defineModel({ type: Object, required: false })

const emit = defineEmits(['change'])
const select = (item: any) => {
    if (item.value != valueSelect.value.value) emit('change', item)
    valueSelect.value = item;
    dropdown.value = !dropdown.value
}

</script>
<style scoped></style>