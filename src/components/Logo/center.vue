<style scoped>
@import './CSS/CenterLogo.css';
</style>

<template>
    <Transition appear>
    <div class="centered">
        <!-- <div class="flex-container">
            <div>
                <p class = 'logoline1'><span class="logoline1_spacE">spacE</span>Lite</p>
                <p class = 'logoline2'> ELite</p>
                <p class = 'logoline3'> Lite</p>
            </div>
            <div>
                <p class = "headtitle"> 空间数据分析平台 </p>
            </div>
        </div> -->
        <router-link to="/">
            <span class="spac">Spac</span><span class="E">E</span><span class="Lite">Lite</span>
            <p class="subline">
                {{ $t("message.subline") }}
            </p>
        </router-link>
        <router-link to="/core">
            <div class="button-container">
                <button class="enter-button">
                    {{ $t("message.start") }}
                </button>
            </div>
        </router-link>
    </div>
    </Transition>
</template>