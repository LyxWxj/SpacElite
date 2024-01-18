
<style scoped>
@import './CSS/contact.css';
</style>

<template>
  <div class="contact">
    <h1>Contact Me</h1>
    <div> 
        <img src = "./assets/head_img.jpg">
        <a href="#" onclick="openImage('./assets/微信图片_20231018122917.jpg')">
        <img src = "./assets/024_扫一扫.svg" width = "100" height = "100" class="fade-in">
        </a>
        <a href="https://github.com/users/LyxWxj/projects/1" target ="_blank">
        <img src = "./assets/git.svg" width="100" height="100" class="fade-in">
        </a>
        <a href="https://blog.csdn.net/wxj1yx?spm=1000.2115.3001.5343" target ="_blank">
        <img src = "./assets/024_文档.svg" width = "100" height = "100" class="fade-in">
        </a>
    </div>
    <p>你可以通过以下方式联系我们：</p>
    <ul>
      <li><a href="#" class="spac">电话:123-456-7890</a></li>
      <li><a href="#" class="E">邮箱: 936543814@qq.com</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Contact'
}
</script>