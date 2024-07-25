<template>
  <!-- 场景-->
  <div w-200 h-200 overflow-hidden relative bg-blue>
    <div id="canvasP" w-full h-full absolute>
      <canvas id="glDom" w-full h-full></canvas>
    </div>
  </div>
</template>
<script setup lang="ts">
import { onMounted, onBeforeUnmount } from 'vue'
import {
  Scene,
  Engine,
  FreeCamera,
  Vector3,
  HemisphericLight,
  PointLight,
  MeshBuilder,
  Color3,
  Color4,
  StandardMaterial,
  Texture
} from 'babylonjs'
// img
import earth_0 from '@/assets/img/earth_0.png'
let scene: Scene
let engine: Engine
let camera: FreeCamera
// vue
onMounted(() => {
  initMap()
  // window.$ObjLargeTemp.set('scene', scene)
})
onBeforeUnmount(() => {
  scene && scene.dispose()
  // window.$ObjLargeTemp.delete('scene')
})
const initMap = () => {
  // Get the canvas DOM element
  const canvas = document.getElementById('glDom') as HTMLCanvasElement // 得到canvas对象的引用
  // Load the 3D engine // 初始化 BABYLON 3D engine
  engine = new Engine(canvas, true, {
    preserveDrawingBuffer: true,
    stencil: true
  })
  /******* CreateScene function that creates and return the scene ******/

  // Create a basic BJS Scene object 创建一个场景scene
  scene = new Scene(engine)
  // 背景透明
  scene.clearColor = new Color4(0, 0, 0, 0)
  // Create a FreeCamera, and set its position to {x: 0, y: 5, z: -10}  添加一个相机，并绑定鼠标事件
  camera = new FreeCamera('camera1', new Vector3(0, 5, -10), scene)
  // Target the camera to scene origin
  camera.setTarget(Vector3.Zero())
  // Attach the camera to the canvas
  camera.attachControl(canvas, false)

  // 更改相机鼠标可以随意浏览

  // 相机需要支持自定义    检测屏幕和射线与球面

  // 球面不同级别为单独绘制  考虑先更改相机和简单球面

  // Create a basic light, aiming 0, 1, 0 - meaning, to the sky 添加一组灯光到场景
  const light = new HemisphericLight('light1', new Vector3(0, 1, 0), scene)
  // const light2 = newPointLight('light2', newVector3(0, 1, -1), scene)
  //添加一个球体到场景中 todo 真实三角和多边形
  // https://blog.csdn.net/qq_37891961/article/details/134888583
  // Create a built-in "sphere" shape; its constructor takes 6 params: name, segment, diameter, scene, updatable, sideOrientation
  const sphere = MeshBuilder.CreateSphere('sphere', { diameter: 2, segments: 32 }, scene)

  const myMaterial = new StandardMaterial('myMaterial', scene)

  myMaterial.diffuseTexture = new Texture(earth_0, scene)
  myMaterial.specularTexture = new Texture(earth_0, scene)
  myMaterial.emissiveTexture = new Texture(earth_0, scene)
  // myMaterial.ambientTexture = newTexture(earth_0, scene);

  sphere.material = myMaterial
  // Move the sphere upward 1/2 of its height
  sphere.position.y = 1

  // //
  // const ground = MeshBuilder.CreateGround('ground', { width: 6, height: 6 }, scene)
  // // 设置ground颜色
  // ground.material = new StandardMaterial('ground', scene)
  // // 漫反射
  // ;(ground.material as StandardMaterial).diffuseColor = new Color3(0.5, 0.5, 0.5)
  // Return the created scene
  // loop
  engine.runRenderLoop(() => {
    scene.render()
  })
  // the canvas/window resize event handler 监听浏览器改变大小的事件，通过调用engine.resize()来自适应窗口大小
  // window.addEventListener('resize', function () {
  //   engine.resize()
  // })

  // 监听元素变化
  let tempSetTime: number
  const resizeObserver = new ResizeObserver(() => {
    tempSetTime && clearTimeout(tempSetTime)
    tempSetTime = setTimeout(() => {
      engine.resize()
    }, 15)
  })
  resizeObserver.observe(document.getElementById('canvasP') as HTMLElement)
  //// resizeObserver.unobserve(canvasP)// 取消监听元素
}
</script>

<style scoped></style>
