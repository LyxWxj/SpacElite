<style scoped>
@import './CSS/navigatorCSS.css';
</style>

<script lang = "js" setup>
import Logo from '../Logo/logo.vue'
</script>

<template>
    <Transition appear>
    <div class="header">
        <div class="logo-style">
            <Logo />
        </div>
        <div class="nav-style" :style="{ fontSize: fontSize }">
            <ul class="nav-list">
                <div class="nav-left">
                    <li><router-link to="/">{{ $t('message.home') }}</router-link></li>
                    <li><router-link to="/contact">{{ $t('message.contact') }}</router-link></li>
                    <li><router-link to="/help">{{ $t('message.help') }}</router-link></li>
                </div>
                <div class="nav-right">
                    <div class="language-switch" @click="switchLanguage">
                        <img class="language-icon" src="./assets/interational.svg" />
                        <span>{{ $t('message.language') }}</span>
                    </div>
                    <li><router-link to="/uploadfile">{{ $t('message.uploadfile') }}</router-link></li>
                    <li><router-link to="/core">{{ $t('message.start') }}</router-link></li>
                </div>
            </ul>
        </div>
    </div>
    </Transition>
</template>

<script lang="js">
export default {
  data() {
    return {
      fontSize: '16px', // 默认字体大小
    };
  },
  methods: {
    switchLanguage() {
      this.$i18n.locale = this.$i18n.locale === 'en' ? 'cn' : 'en';
      this.fontSize = this.$i18n.locale === 'en' ? '18px' : '16px'; // 切换字体大小
    }
  }
}
</script>
