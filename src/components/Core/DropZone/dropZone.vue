<template>
    
</template>

<style scoped>
@import './dropZone.css';
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
    },
  }
};
</script>