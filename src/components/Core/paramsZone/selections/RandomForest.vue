<template>
    <div>
        <DropZoneX @update="handleUpdateX"/>
        <DropZoneY @update="handleUpdateY"/>
        <div class="controls">
            <button class="applybutton" @click="sendRequest">apply</button>
            <div class="paramsfield">
                <label for="criterion">Criterion:</label>
                <select id="criterion" class="selections" v-model="criterion">
                    <option value="gini">Gini</option>
                    <option value="entropy">Entropy</option>
                </select>
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
let criterion = ref('gini');

const handleUpdateX = (newData) => {
  dataX.value = newData;
};

const handleUpdateY = (newData) => {
  dataY.value = newData;
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
        request: 'RandomForest',
        Xs: x_data,
        Ys: y_data,
        criterion: criterion.value,
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