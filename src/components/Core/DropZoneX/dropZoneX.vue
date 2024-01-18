<template>
    <div class="dropZoneX">
        <span> {{ $t('message.VariableX') }} </span>
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
@import './dropZoneX.css';
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
        console.log(this.droppedItems);
    }, 
    //拖拽结束事件
    onEnd() {
        this.drag=false;
        console.log(this.droppedItems);
        this.$emit('update', this.droppedItems);
    },
  }
};
</script>