<template>
    <div>
        <DropZoneX @update="handleUpdateX"/>
        <DropZoneY @update="handleUpdateY"/>
        <div class="controls">
            <button class="applybutton" @click="sendRequest">apply</button>
            <div class="paramsfield">

            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useStore } from 'vuex';
import $ from 'jquery';
import DropZoneX from '../../DropZoneX/dropZoneX.vue'
import DropZoneY from '../../DropZoneY/dropZoneY.vue'

let dataX = ref([]);
let dataY = ref([]);

const store = useStore();

const handleUpdateX = (newData) => {
  dataX.value = newData;
  console.log(dataX.value);
};

const handleUpdateY = (newData) => {
  dataY.value = newData;
  console.log(dataY.value);
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
        request: 'Polylineplot',
        Xs: x_data,
        Ys: y_data,
        Xname: x_head,
        Yname: y_head,
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