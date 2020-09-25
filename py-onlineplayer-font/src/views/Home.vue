<template>
    <el-container class="center">
        <el-main style="padding-top: 0;height: 100%">
            <music-tabs class="center_area"></music-tabs>
        </el-main>
        <player></player>

    </el-container>
</template>
<script>
    import MusicTabs from "@/components/musicTabs";
    import Player from "../components/player";

    export default {
        name: 'Home',
        components: {
            Player,
            MusicTabs,
        },
        data: function () {
            return {

            }
        },
        methods: {}

    }
</script>
<style scoped>
    .center {
        position: relative;
        width: 100%;
        height: 100%;
        max-width: 1200px;
        margin: 0 auto;
    }

    .center_area {
        /*position: absolute;*/
        /*left: 0;*/
        /*right: 400px;*/
        /*top: 60px;*/
        /*bottom: 0;*/
        overflow: hidden;
    }
</style>
