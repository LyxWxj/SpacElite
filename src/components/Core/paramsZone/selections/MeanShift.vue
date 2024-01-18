<template>
    <div>
        <DropZoneX @update="handleUpdateX"/>
        <div class="controls">
            <button class="applybutton" @click="sendRequest">apply</button>
            <div class="paramsfield">
                <label for="K">K:</label>
                <input id="K" class="input" type="number" min="1" v-model.number="K">
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

let K = ref(1);

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
    let y_head = dataY.value[0]
    let fileData = store.state.fileData;
    let x_index = fileData[0].indexOf(x_head);
    let y_index = fileData[0].indexOf(y_head);
    let x_data = fileData.slice(1).map(row => row[x_index]);
    let y_data = fileData.slice(1).map(row => row[y_index]);
    const data = {
        request: 'MeanShift',
        Xs: x_data,
        Ys: y_data,
        K: K,
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