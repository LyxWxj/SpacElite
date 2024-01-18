import { createApp } from 'vue'
import './common/style.css'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import Contact from './components/route/contact.vue'
import Help from './components/route/help.vue'
import Center from './components/Logo/center.vue'
import Core from './components/Core/core.vue'
import Uploadfile from './components/route/upload.vue'
import ParamsZone from './components/Core/paramsZone/paramsZone.vue'
import i18n from './i18n' // 引入 i18n
import Vuex from 'vuex'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/center' },
    { path: '/center', name: 'center', component: Center },
    { path: '/contact', component: Contact },
    { path: '/help', component: Help },
    { path: '/core', component: Core, beforeEnter: (to, from, next) => {
      // 检查用户是否已经上传了文件
      if (!store.state.hasUploadedFile) {
        // 如果用户没有上传文件，先提示未上传文件, 然后重定向到 'uploadfile'
        alert("请先上传文件 Please Upload File before Start !")
        next('/uploadfile');
      } else {
        // 如果用户已经上传了文件，则允许导航
        next();
      }
    }},
    { path: '/uploadfile', component: Uploadfile},
  ]
})



const store = new Vuex.Store({
  state: {
    fileData: null,
    hasUploadedFile: false,
    responseData: null,
  },
  mutations: {
    setfileData(state, data) {
      state.fileData = data;
    }, 
    setHasUploadedFile(state, hasUploadedFile) {
      state.hasUploadedFile = hasUploadedFile;
    },
    setResponseData(state, data) {
      state.responseData = data;
    }
  }
});

createApp(App)
  .use(i18n)
  .use(store)
  .use(router)
  .mount('#app')