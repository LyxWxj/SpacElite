<script>
import Navigator from './components/Navigation/navigator.vue'
import Center from './components/Logo/center.vue'
import Core from './components/Core/core.vue'
import createParticles from './common/particles.js'
import Uploadfile from './components/route/upload.vue'

export default {
  components: {
    Navigator,
    Center,
    Core,
    Uploadfile,
  },
  mounted() {
    createParticles('backgroundcanvas')
  },
  computed: {
    className() {
      return {
        'home': this.$route.path === '/',
        'contact': this.$route.path === '/contact',
        'help': this.$route.path === '/help',
        'core': this.$route.path === '/core',
        'uploadfile': this.$route.path === '/uploadfile',
      };
    }
  },
}

</script>

<style scoped>
@import './CSS/mainApp.css';
</style>

<template>
  <div class="app" :class="className">
    <Navigator />
    <canvas id = 'backgroundcanvas'></canvas>
    <RouterView/>
  </div>
</template>