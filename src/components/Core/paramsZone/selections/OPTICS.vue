<template>
    <div>
        <DropZoneX @update="handleUpdateX"/>
        <div class="controls">
            <button class="applybutton" @click="sendRequest">apply</button>
            <div class="paramsfield">
                <label for="minpts">MinPts:</label>
                <input id="minpts" class="input" type="number" min="1" v-model.number="minpts">
                <br>
                <label for="r">R:</label>
                <input id="r" class="input" type="number" min="0.01" step="0.01" v-model.number="r">
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
let dataY = ref([]);
let minpts = ref(0)
let r = ref(0.0)

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
        request: 'OPTICS',
        Xs: x_data,
        minpts: minpts.value,
        r: r.value,
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