<template>
    <div>
        <DropZoneX @update="handleUpdateX"/>
        <div class="controls">
            <button class="applybutton" @click="sendRequest">apply</button>
            <div class="paramsfield">
                
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

const store = useStore();

const handleUpdateX = (newData) => {
  dataX.value = newData;
  console.log(dataX.value);
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
        request: 'GaussianMixture',
        Xs: x_data,
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