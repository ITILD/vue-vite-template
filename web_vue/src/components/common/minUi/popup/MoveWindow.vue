<template>
  <div fixed ref="outDom">
    <div class="con1_title" @mousedown="mouseOrTouchDown($event)" @touchstart="mouseOrTouchDown($event)">
      <!-- <div>标题111，拖拽它即可使整个div移动</div> -->
      <slot></slot>
    </div>
    <!-- 内容插槽 -->
    <slot name="content"></slot>
  </div>
</template>
<script setup lang="ts">
/**
 * 鼠标按下,不经过移动 moveEl.dragFlag = false;
 * 用法
 * 
    <MoveWindow ref="dragRef" right-8 bottom-30>
        <div w-30 h-30 rounded-3xl flex-center>
            <div w-full h-full @click="addPage">新建</div>
        </div>
        <template v-slot:content>
          <div w-30 h-30 rounded-3xl flex-center >内容</div>
        </template>
    </MoveWindow>
    const dragRef = ref();
    const addPage = () => {
    if(dragRef.value.$el.dragFlag)return
    console.log('addPage')
    }
 */
const outDom = ref()

const mouseOrTouchDown = (e: MouseEvent | TouchEvent) => {
  let moveEl: any = outDom.value
  //拖拽标记还原 阻止外部点击
  moveEl.dragFlag = false;
  // 元素的大小
  let domW = moveEl.offsetWidth
  let domH = moveEl.offsetHeight
  // 窗口大小
  let width = window.innerWidth
  let height = window.innerHeight
  // 鼠标到元素左边距离
  let moveX = getMouseOrTouchXY(e).x - moveEl.offsetLeft
  let moveY = getMouseOrTouchXY(e).y - moveEl.offsetTop
  const onMove = (e: MouseEvent | TouchEvent) => {
    console.log('l2', e.type)
    //设置拖拽标记   
    moveEl.dragFlag = true;
    let dropX = width - (getMouseOrTouchXY(e).x - moveX) - domW
    let dropY = height - (getMouseOrTouchXY(e).y - moveY) - domH
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
  // 判断触摸还是鼠标
  if (e instanceof MouseEvent) {
    document.onmousemove = onMove
    document.onmouseup = () => {
      console.log('MouseEvent抬起')
      document.onmousemove = document.onmouseup = null
    }
    // 鼠标
  } else {
    console.log('l1', e.type)
    // 触摸 移动端失效
    // document.ontouchmove = onMove
    // document.ontouchend = () => (document.ontouchmove = document.ontouchend = null)
    const touchend = () => {
      // console.log('touchDown抬起')
      document.removeEventListener('touchmove', onMove)
      document.removeEventListener('touchend', touchend)
      moveEl.dragFlag = false;
    }
    document.addEventListener('touchmove', onMove)
    document.addEventListener('touchend', touchend)
  }
  // 防止鼠标松开元素仍然可以拖动;
  document.ondragstart = document.ondragend = (ev) => ev.preventDefault()
}
/**
 * 获取鼠标或触摸坐标
 * @param e 
 */
const getMouseOrTouchXY = (e: MouseEvent | TouchEvent) => {
  let x = null, y = null
  // 判断触摸还是鼠标
  if (e instanceof MouseEvent) {
    x = e.clientX
    y = e.clientY
  } else {
    x = e.targetTouches[0].pageX
    y = e.targetTouches[0].pageY
  }
  return { x, y }
}


</script>
<style scoped></style>
