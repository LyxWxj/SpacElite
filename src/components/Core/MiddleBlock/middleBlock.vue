<template>
    <div class="MiddleBlock">
        <span>{{ $t('message.middleBlock') }}</span>
        <div class="tabelHeads" @dragover.prevent>
            <draggable v-model="heads" group="site" @start="onStart" @end="onEnd">
                <transition-group>
                    <li class="tableFiled" v-for="(value, key) in heads" :key="key">
                        {{ value }}
                    </li>
                </transition-group>
            </draggable>
        </div>
    </div>
</template>

<style scoped>
@import './middleBlock.css';
</style>

<script lang="js">
import { VueDraggableNext } from 'vue-draggable-next'

export default {
    components: {
        draggable: VueDraggableNext
    },
    data() {
        return {
            heads:null,
            drag:false,
        }
    },

    name:'Middleblock',
    mounted() {
        if (this.$store.state.fileData) {
            this.heads = this.$store.state.fileData[0];
        }
    },
    methods: {
        onStart(){
            this.drag=true;
            console.log(this.heads);
        }, 
        //拖拽结束事件
        onEnd() {
            this.drag=false;
            console.log(this.heads);
        },
    }
}
</script>