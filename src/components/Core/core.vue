<style scoped>
@import './CSS/core.css';
</style>

<script setup>
import Methodslist from './MethodsList/methodsList.vue'
import Middleblock from './MiddleBlock/middleBlock.vue'
import ParamsZone from './paramsZone/paramsZone.vue'
import ResultBlock from './ResultBlock/resultBlock.vue'
</script>

<template>
    <Transition appear>
        <div class="container">
            <Methodslist @algorithm-selected="handleAlgorithmSelected"></Methodslist>
            <Middleblock/>
            <div class="selectZone">
                <ParamsZone :selectedAlgorithm="selectedAlgorithm"></ParamsZone>
            </div>
            <ResultBlock/>
        </div>
    </Transition>
</template>

<script>
export default {
    data() {
    return {
      name: 'Start', 
      selectedAlgorithm: null,
    };
  },
  methods: {
    handleAlgorithmSelected(algorithm) {
      this.selectedAlgorithm = algorithm;
    },
  },
}
</script>