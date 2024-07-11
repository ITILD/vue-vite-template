<template>
  <div>
    <div>{{ $t('message.language') }}</div>
    <div @click="changeLang('ja')">日本語</div>
    <div @click="changeLang('zh')">中文</div>
  </div>
</template>
<script setup lang="ts">
import { i18n } from '@/i18n/language'

const changeLang = (lang: string) => {
  i18n.global.locale = lang
  // localStorage.setItem('lang', lang)
}
</script>
