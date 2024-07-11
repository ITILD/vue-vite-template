import { createI18n } from 'vue-i18n'
const i18n = createI18n({
  locale: 'ja',
  fallbackLocale: 'zh',
  messages: {}
})
i18n.global.setLocaleMessage('zh', {
  message: {
    language: '简中',
    // 欢迎使用方案讲解机器人
    home_welcome: '欢迎使用方案讲解机器人',
  }
})
i18n.global.setLocaleMessage('ja', {
  message: {
    // '日本語試験'
    language: '日語',
    //  欢迎使用方案讲解机器人
    home_welcome:'ロボットを説明するソリューションへようこそ',
  }
})

export { i18n }
