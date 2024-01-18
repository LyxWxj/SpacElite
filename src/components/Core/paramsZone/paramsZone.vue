<template>
    <component v-for="algorithm in filteredAlgorithms" :is="algorithm" :key="algorithm"></component>
</template>

<style scoped>
@import "./paramsZone.css";
</style>

<script setup>
import Barplot from './selections/Barplot.vue'
import Scatterplot from './selections/Scatterplot.vue'
import Polylineplot from './selections/Polylineplot.vue'
import KMeans from './selections/KMeans.vue'
import DBSCAN from './selections/DBSCAN.vue'
import MeanShift from './selections/MeanShift.vue'
import GaussianMixture from './selections/GaussianMixture.vue'
import KNN from './selections/KNN.vue'
import SVM from './selections/SVM.vue'
import DecisionTree from './selections/DecisionTree.vue'
import LogisticRegression from './selections/LogisticRegression.vue'
import Linear from './selections/Linear.vue'
import SVR from './selections/SVR.vue'
import RandomForest from './selections/RandomForest.vue'
import GeoWeighted from './selections/GeoWeighted.vue'
import MoransI from './selections/MoransI.vue'
import LocalMoransI from './selections/LocalMoransI.vue'
import LocalG from './selections/LocalG.vue'
import LocalJointCount from './selections/LocalJointCount.vue'
import ODMatrix from './selections/ODMatrix.vue'
</script>

<script>
export default {
    props: ['selectedAlgorithm'],
    components: {
        Barplot,
        Scatterplot,
        Polylineplot,
        KMeans,
        DBSCAN,
        MeanShift,
        GaussianMixture,
        KNN,
        SVM,
        DecisionTree,
        LogisticRegression,
        Linear,
        SVR,
        RandomForest,
        GeoWeighted,
        MoransI,
        LocalMoransI,
        LocalG,
        LocalJointCount,
        ODMatrix,
    },
    data() {
        return {
            name: 'paramsZone',
            algorithms: ['Barplot', 'Scatterplot','Polylineplot', 
                        'KMeans', 'DBSCAN', 'OPTICS', 
                        'MeanShift', 'GaussianMixture', 
                        'KNN', 'SVM', 'DecisionTree', 
                        'LogisticRegression', 'Linear', 'Ridge', 'Lasso', 
                        'SVR', 'RandomForest', 'GeoWeighted',
                        "MoransI","LocalMoransI",
                        "LocalG", "LocalJointCount", "ODMatrix",]
            // algorithms: [
            //     { name: 'KMeans', component: KMeans},
            //     { name: 'DBSCAN', component: DBSCAN},
            //     { name: 'OPTICS', component: OPTICS},
            //     { name: 'MeanShift', component: MeanShift},
            //     { name: 'GaussianMixture', component: GaussianMixture},
            //     { name: 'KNN', component: KNN},
            //     { name: 'SVM', component: SVM},
            //     { name: 'DecisionTree', component: DecisionTree},
            //     { name: 'LogisticRegression', component: LogisticRegression},
            //     { name: 'Linear', component: Linear},
            //     { name: 'Ridge', component: Ridge},
            //     { name: 'Lasso', component: Lasso},
            //     { name: 'SVR', component: SVR},
            //     { name: 'RandomForest', component: RandomForest},
            //     { name: 'GeoWeighted', component: GeoWeighted},
            //     { name: 'MoransI', component: MoransI},
            //     { name: 'LocalMoransI', component: LocalMoransI},
            //     { name: 'LocalG', component: LocalG},
            //     { name: 'LocalJointCount', component: LocalJointCount},
            //     { name: 'Barplot', component: Barplot},
            //     { name: 'Scatterplot', component: Scatterplot},
            //     { name: 'Polylineplot', component: Polylineplot},
            // ],
        }
    }, 
    computed: {
    filteredAlgorithms() {
      return this.algorithms.filter(algorithm => algorithm === this.selectedAlgorithm);
    },
  },
}
</script>