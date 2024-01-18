<template>
    <div>
        <DropZoneX @update="handleUpdateX"/>
        <div class="controls">
            <button class="applybutton" @click="sendRequest">apply</button>
            <div class="paramsfield">
                <label for="K">K:</label>
                <input id="K" class="input" type="number" min="1" v-model.number="K">
                <br>
                <select id="distmeas" class="selections" v-model="distmeas" >
                    <option value="dist_eucl">Euclidean Distance</option>
                    <option value="dist_cos">Cosine Distance</option>
                    <option value="dist_Manht">Manhattan Distance</option>
                </select>
            </div>
        </div>
    </div>
</template>

<script setup>
import DropZoneX from '../../DropZoneX/dropZoneX.vue'
import { ref } from 'vue';
import { useStore } from 'vuex';
import $ from 'jquery';

let dataX = ref([]);

const K = ref(1);
const distmeas = ref('dist_eucl')

const store = useStore();

const handleUpdateX = (newData) => {
  dataX.value = newData;
};

const sendRequest = async () => {
    if (dataX.value.length === 0 || dataY.value.length === 0) {
        alert('Please select variables')
        return;
    }
    let x_head = dataX.value[0]
    let fileData = store.state.fileData;
    let x_index = fileData[0].indexOf(x_head);
    let x_data = fileData.slice(1).map(row => row[x_index]);
    const data = {
        request: 'KMeans',
        Xs: x_data,
        K: K,
        distmeas: distmeas,
    };
    $.ajax({
        url: 'http://localhost:8080/data',
        type: 'POST',
        data: JSON.stringify(data),
        success: function(response) {
            store.commit('setResponseData', response);
        },
        error: function(error) {
            console.error(error);
        }
        });
};
</script>

<style scoped>
@import './common.css';
</style>