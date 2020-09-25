<template>
  <el-container>
    <el-tabs v-model="activeName" type="card">
      <el-tab-pane label="播放列表" name="first">
        播放列表
      </el-tab-pane>
      <el-tab-pane label="搜索列表" name="second">
        搜索列表
      </el-tab-pane>
    </el-tabs>
  </el-container>
</template>

<script>
export default {
  name: "musicTabs",
  data: function () {
    return {
      activeName: '播放列表',


    }
  },

  methods: {}
}
</script>

<style scoped>

</style>
