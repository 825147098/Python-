<template>
  <!--<el-container>-->
    <div id="search-area">
      <div id="radios-group">
      <div id="search-group">
        <el-input size="small"
                  placeholder="搜索歌名"
                  class="search-group-input text_color"
                  v-model="inputData"
                  clearable
                  @keydown.enter.native="setSearchName"
        ></el-input>
        <el-button
            @click="setSearchName"
                class="search-group-button">
          搜索
        </el-button>
      </div>
        <el-radio-group v-model="radio"  >
          <el-radio class="text_color" label="kugou">酷狗</el-radio>
          <el-radio class="text_color" label="kuwo">酷我</el-radio>
          <el-radio class="text_color" label="migu">咪咕</el-radio>
          <el-radio class="text_color" label="qq">QQ音乐</el-radio>
          <el-radio class="text_color" label="xiami">虾米</el-radio>
        </el-radio-group>
      </div>
    </div>
  <!--</el-container>-->
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
      setSearchName(){
          this.$store.commit("incrementName",{newName:this.inputData,newType:this.radio})
      }
  }
}
</script>

<style scoped>
#search-area {
  /*width: 405px;*/
  display: inline;
}
.search-group-input{
  padding: 5px 0 5px 5px;
  height: 35px;
  width: 70%;
  border-radius: 0;
}
.search-group-input /deep/ .el-input__inner{
  background-color: transparent;
}

.text_color{
  color: white;
}

.search-group-button {
  border: 1px solid #a7a1a1;
  background-color: #eee;
  height: 32px;
  margin-left: -1px;
  width: 15%;
  padding: 1px 0;
  white-space: nowrap;
  text-overflow: clip;
  overflow: hidden;
  border-radius: 0;
}

/deep/ .el-input__inner{
  color: white;
}
</style>
