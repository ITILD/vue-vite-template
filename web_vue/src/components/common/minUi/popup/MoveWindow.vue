<template>
  <div fixed ref="outDom" class="botm_year">
    <div class="con1_title" @mousedown="mouseDown($event)">
      <div>标题111，拖拽它即可使整个div移动</div>
    </div>
    <div>这是内容</div>
  </div>
</template>
<script setup lang="ts">
const outDom = ref()

const mouseDown = (e: MouseEvent) => {
  let moveEl: any = outDom.value
  // 鼠标的位置 e.clientX e.clientY
  // 元素的位置 moveEl.offsetLeft moveEl.offsetTop
  // 元素的大小
  let domW = moveEl.offsetWidth
  let domH = moveEl.offsetHeight
  // 窗口大小
  let width = window.innerWidth
  let height = window.innerHeight

  // 鼠标到元素左边距离
  let moveX = e.clientX - moveEl.offsetLeft
  let moveY = e.clientY - moveEl.offsetTop
  document.onmousemove = (e) => {
    let dropX = width - (e.clientX - moveX) - domW
    let dropY = height - (e.clientY - moveY) - domH

    if (dropX > width - domW) {
      dropX = width - domW
    } else if (dropX < 0) {
      dropX = 0
    }
    if (dropY > height - domH) {
      dropY = height - domH
    } else if (dropY < 0) {
      dropY = 0
    }
    moveEl.style.right = dropX + 'px'
    moveEl.style.bottom = dropY + 'px'
  }
  document.onmouseup = () => (document.onmousemove = document.onmouseup = null)
  // 防止鼠标松开元素仍然可以拖动;
  document.ondragstart = document.ondragend = (ev) => ev.preventDefault()
}
</script>
<style scoped></style>
