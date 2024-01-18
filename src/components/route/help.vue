<template>
    <div>
      <h1 class="helpTitle">帮助中心</h1>
      <p class="helpSubtitle">这里是一些常见问题和解答：</p>
      <span class="helpText">
        spacElite是一个在线数据分析平台
      </span>
      <p class="helpSubtitle">为什么叫spacElite?</p>
      <span class="helpText">
        spacElite是space,elite,lite的组合，space代表空间，elite代表精英，lite代表轻量级
        <br>
        意味着spacElite项目是一个轻量级的数据分析平台，可以帮助你在数据分析的空间中找到你想要的算法。
      </span>
      <p class="helpSubtitle">如何使用spacElite?</p>
      <span class="helpText">
        你可以通过上传数据文件，然后选择你想要的分析方法，将你需要分析的字段拖入对应的框中, 然后选择一些参数, 最后点击提交按钮，等待分析结果。
      </span>
      <p class="helpSubtitle">spacElite支持哪些分析方法?</p>
      <span class="helpText">
        spacElite目前支持的分析方法有: 散点图，折线图，多项式拟合，SVM，线性回归，逻辑回归，KNN，K-means，层次聚类等。
      </span>
      <p class="helpSubtitle">spacElite支持哪些数据格式?</p>
      <span class="helpText">
        目前只支持csv, excel格式的数据文件。
      </span>
      <p class="helpSubtitle">如何快速查找我需要的算法?</p>
      <span class="helpText">
        你可以通过点击左侧的搜索框，输入你想要的算法的名字，然后点击搜索按钮，就可以快速找到你想要的算法。
        <br>
        并且搜索框支持模糊搜索, 你并不需要输入完整的算法名字，只需要输入部分名字就可以搜索到你想要的算法。
      </span>

    </div>
</template>

<script>
export default {
  name: 'Help'
}
</script>

<style scoped>
@import './CSS/help.css';
</style>