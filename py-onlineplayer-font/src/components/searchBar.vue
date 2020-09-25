<template>
  <el-container>
    <div id="search-area">
      <div id="search-group">
        <el-input size="small"
                  placeholder="搜索歌名"
                  class="search-group-input"
                  v-model="inputData"
        ></el-input>
        <el-button
            class="search-group-button">
          搜索
        </el-button>
      </div>
      <div id="radios-group">
        <el-radio-group v-model="radio" >
          <el-radio label="kugou">酷狗</el-radio>
          <el-radio label="kuwo">酷我</el-radio>
          <el-radio label="migu">咪咕</el-radio>
          <el-radio label="qq">QQ音乐</el-radio>
          <el-radio label="xiami">虾米</el-radio>
        </el-radio-group>
      </div>
    </div>
  </el-container>
</template>

<script>
export default {
  name: "searchBar",
  data: function () {
    return {
      inputData:'',
      radio:"kugou",
    }
  },

  methods:{

  }
}
</script>

<style scoped>
#search-area {
  width: 405px;
}
.search-group-input{
  padding: 5px 0 5px 5px;
  height: 35px;
  width: 70%;
  border-radius: 0;
}
.search-group-button {
  border: 1px solid #a7a1a1;
  background-color: #eee;
  height: 32px;
  margin-left: -1px;
  width: 20%;
  padding: 1px 0;
  white-space: nowrap;
  text-overflow: clip;
  overflow: hidden;
  border-radius: 0;
}
#radios-group div div label span{
  padding-left: 0;
}
</style>
