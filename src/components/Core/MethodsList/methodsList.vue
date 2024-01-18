<template>
    <div class="algorithmTabel">
      <div class="searchbox">
        <input v-model="search" type="text" class="inputBox" @keydown.enter="search" placeholder="Search For Algorithm"/>
        <img src="./assets/search.svg" @click="search" class="searchIcon" />
      </div>
      <div class="selectedAlgorithm">{{ selectedAlgorithm || '' }}</div>
      <div class="algorithmList">
        <div v-for="(module, index) in filteredModules" :key="index">
          <div class="module-header">
            <img :src="module.icon" alt="Icon" />
            <h4>{{ module.name }}</h4>
          </div>
          <ul style="list-style-type:none">
            <li v-for="(algorithm, index) in module.algorithms" :key="index">
              <button class="algorithmButton" :class="{ 'selected': selectedAlgorithm === algorithm }" @click="selectAlgorithm(algorithm)">{{algorithm}}</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
</template>


<style scoped>
@import "./methodsList.css";
</style>

<script lang="js">
export default {
  data() {
    return {
      search: '',
      selectedAlgorithm: null, // 当前选择的算法
      modules: [
        {
          name: 'Visualize',
          icon: 'src/assets/dataVisualiz.svg',
          algorithms: ['Barplot', 'Scatterplot','Polylineplot'],
        },
        {
          name: 'Clustering',
          icon: 'src/assets/clustering.svg',
          algorithms: ['KMeans', 'DBSCAN', 'MeanShift', 'GaussianMixture',],
        },
        {
          name: 'Classify',
          icon: 'src/assets/classify.svg',
          algorithms: ['KNN', 'SVM', 'DecisionTree', 
                    'LogisticRegression',],
        },
        {
          name: 'Regression',
          icon: 'src/assets/regression.svg',
          algorithms: ['Linear',
                      'SVR', 'RandomForest', 'GeoWeighted',],
        },
        {
          name: 'Spacial Analysis',
          icon: 'src/assets/spacialAnalysis.svg',
          algorithms: ["MoransI",
                       "LocalMoransI",
                       "LocalG", "LocalJointCount", "ODMatrix"],
        }
      ],
    };
  },
  methods: {
    selectAlgorithm(algorithm) {
      this.selectedAlgorithm = algorithm;
      this.$emit('algorithm-selected', algorithm);
    },
  }, 
  computed: {
    groupedAlgorithms(algorithms) {
      let groups = [];
      for (let i = 0; i < algorithms.length; i += 2) {
        groups.push(algorithms.slice(i, i + 2));
      }
      return groups;
    },
    filteredModules() { // 添加计算属性
      if (!this.search) {
        return this.modules;
      }
      return this.modules.map(module => {
        return {
          ...module,
          algorithms: module.algorithms.filter(algorithm => algorithm.toLowerCase().includes(this.search.toLowerCase())),
        };
      });
    },
  }
}
</script>