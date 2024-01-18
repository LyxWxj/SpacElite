<template>
    <div class="dropZoneY">
        <span> {{ $t('message.VariableY') }}</span>
        <div class="fieldPlace"  @dragover.prevent>
        <draggable v-model="droppedItems" group="site" @start="onStart" @end="onEnd">
            <transition-group>
                <li class="tableField" v-for="(value, key) in droppedItems" :key="key">
                    {{ value }}
                </li>
            </transition-group>
        </draggable>
    </div>
    </div>
</template>

<style scoped>
@import './dropZoneY.css';
</style>

<script lang="js">
import { VueDraggableNext } from 'vue-draggable-next'

export default {
  components: {
      draggable: VueDraggableNext
  },
  data() {
    return {
      droppedItems: [],
      drag:false,
    };
  },
  methods: {
    onStart(){
        this.drag=true;
    }, 
    //拖拽结束事件
    onEnd() {
        this.drag=false;
        this.$emit('update', this.droppedItems);
    },
  }
};
</script>