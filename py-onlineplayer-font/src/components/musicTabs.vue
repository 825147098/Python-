<template>
  <!--<el-main class="data_area">-->
  <el-tabs v-model="activeName" type="card" class="music_content">
    <el-tab-pane label="播放列表" name="播放列表" class="table-wrapper">
      <div v-if="playList.length === 0" class="blank_area">
        <p>
          弄啥呢，怎么啥也没有！！！
        </p>
      </div>
      <el-table
          v-else
          width="100%"
          height="100%"
          max-height="calc(60vh)"
          :data="playList"
      >
        <el-table-column
            type="index"
            width="50px"
        ></el-table-column>
        <el-table-column
            label="歌曲"
            width="440px"
            prop="song_name"
        >
          <template slot-scope="scope">
            <span>{{ scope.row.song_name }}
                <el-image :src=wave
                          v-show="scope.$index === playFlag"
                          style="height: 10px"></el-image>
            </span>
            <el-button-group class="itemButtonGroup">
              <el-button circle size="small"
                         v-show="scope.$index !== playFlag"
                         @click="playSong(scope.$index)"
                         class="itemButton"
                         text="点击播放这首歌"
                         type="text">
                ▶
              </el-button>
              <el-button icon="el-icon-remove-outline"
                         circle size="small"
                         class="itemButton"
                         @click="movePlayData(scope.$index)"
                         text="点击移除这首歌"
                         type="text">
              </el-button>
              <a :href=scope.row.song_url target="#">
                <el-button icon="el-icon-download"
                           circle size="small"
                           type="text"
                           class="itemButton"
                           title="点击下载这首歌"></el-button>
              </a>
            </el-button-group>
          </template>
        </el-table-column>
        <el-table-column
            label="歌手"
            width="150px"
            :show-overflow-tooltip="true"
            prop="song_user"
        ></el-table-column>
        <el-table-column
            label="专辑"
            width="150px"
            :show-overflow-tooltip="true"
            prop="song_album"
        ></el-table-column>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="搜索列表" name="搜索列表" class="table-wrapper">
      <div v-if="searchList.length === 0 || loading !== 0" class="blank_area">
        <p v-if="loading === -1">
          弄啥呢，怎么啥也没有！！！
        </p>
        <p v-if="loading === 1">
          <i class="el-icon-loading"></i>
          正在加载中
        </p>
        <p v-if="loading === -2">
          <i class="el-icon-loading"></i>
          加载失败，请更换平台或搜索其他歌曲
        </p>
      </div>
      <el-table
          v-else
          width="100%"
          height="100%"
          max-height="calc(60vh)"
          :data="searchList"
      >
        <el-table-column
            type="index"
            width="50px"
        ></el-table-column>
        <el-table-column
            label="歌曲"
            width="440px"
            prop="song_name"
        >
          <template slot-scope="scope">
            <span>{{ scope.row.song_name }}</span>
            <el-button-group class="itemButtonGroup">
              <el-button :icon=scope.row.icon
                         circle size="small"
                         class="itemButton"
                         @click="setPlayData(scope.$index)"
                         text="点击播放这首歌"
                         type="text">
              </el-button>
              <el-button icon="el-icon-circle-plus-outline"
                         circle size="small"
                         class="itemButton"
                         @click="addPlayData(scope.$index)"
                         text="点击添加进播放列表"
                         type="text">
              </el-button>
              <a :href=scope.row.song_url target="#">
                <el-button icon="el-icon-download"
                           circle size="small"
                           type="text"
                           class="itemButton"
                           title="点击下载这首歌"></el-button>
              </a>

            </el-button-group>
          </template>
        </el-table-column>
        <el-table-column
            label="歌手"
            width="150px"
            :show-overflow-tooltip="true"
            prop="song_user"
        ></el-table-column>
        <el-table-column
            label="专辑"
            width="150px"
            :show-overflow-tooltip="true"
            prop="song_album"
        ></el-table-column>
      </el-table>
    </el-tab-pane>
    <el-tab-pane
        label="歌曲搜索"
        name="歌曲搜索"
    >
      <!--<el-dialog-->
      <!--:visible.sync="dialogVisible"-->
      <!--width="450px">-->
      <search-bar></search-bar>
      <!--</el-dialog>-->
    </el-tab-pane>
  </el-tabs>
  <!--</el-main>-->

</template>

<script>

import SearchBar from "./searchBar";
import wave from "../assets/musicImgs/wave.gif"

export default {
  name: "musicTabs",
  components: {SearchBar},
  data: function () {
    return {
      activeName: '播放列表',
      wave: wave,
      searchList: [
        // {
        //   "song_url": "https://webfs.yun.kugou.com/202009250914/a2bf29a17a8c092f3e8b6499172240ad/G170/M07/16/11/SocBAF3H3aqAUYOEADmpdloW3bU827.mp3",
        //   "song_name": "\u5c11\u5e74",
        //   "song_user": "\u68a6\u7136",
        //   "song_album": "\u5c11\u5e74",
        //   "icon": "el-icon-video-play"
        // }
      ],

      playFlag: -1,
      playList: [],
      randomList: []

    }
  },

  methods: {
    setPlayData(index) {
      // console.log(index)
      this.playList.unshift(this.searchListIn[index])
      this.$store.commit("incrementPlayData", {playObj: this.searchListIn[index], pindex: 0})
    },

    playSong(index) {
      this.$store.commit("incrementPlayData", {playObj: this.playList[index], pindex: index})
    },

    addPlayData(index) {
      this.playList.push(this.searchListIn[index])
    },

    movePlayData(index) {
      if (this.randomList.length == this.playList)
        this.randomList.splice(this.randomList.indexOf(this.playList[index], 1))
      this.playList.splice(index, 1)
      let play = {
        "song_url": '',
        "song_name": "",
        "song_user": "",
        "song_time": "null",
        "song_img": "",
        "song_lyr": "null",
        "song_album": "player_cover",
        "song_flag": false
      }
      this.$store.commit("incrementPlayData", {playObj: play, pindex: -1})
    },

    getNorIndex() {
      let index = this.$store.state.playIndex
      if (index < 0) {
        index = this.playList.length - 1
      }
      if (index >= this.playList.length) {
        index = 0
      }
      return index
    },

    getRanIndex(flag) {
      let index
      if (flag)
        index = this.$store.state.playIndex - 1
      else
        index = this.$store.state.playIndex
      if (index < 0) {
        index = this.randomList.length - 1
      }
      if (index >= this.randomList.length) {
        index = 0
      }
      return index
    }
  },

  props: [
    "searchListIn",
    "loading"
  ],

  watch: {
    loading: function () {
      if (this.loading === 1) {
        this.activeName = '搜索列表'
      }
    },
    "$store.state.playIndex": function () {
      if(this.playList.length > 0){
        if (!this.$store.state.randomFlag) {
          let index = this.getNorIndex()
          this.playFlag = index
          this.$store.commit("incrementPlayData", {playObj: this.playList[index], pindex: index})
        } else {
          let index = this.getRanIndex(false)
          this.playFlag = this.playList.indexOf(this.randomList[index])
          this.$store.commit("incrementPlayData", {playObj: this.randomList[index], pindex: index})
        }
      }
    },

    "$store.state.randomFlag": function () {
      if (this.$store.state.randomFlag) {
        if (this.$store.state.playIndex != -1) {
          let first = this.getRanIndex(true)
          this.randomList = []
          this.randomList.push(this.playList[first])
        }
        let len = this.playList.length
        while (this.randomList.length < len) {
          let random = Math.floor(Math.random() * len)
          if (this.randomList.indexOf(this.playList[random]) === -1)
            this.randomList.push(this.playList[random])
        }
        // console.log(this.randomList)
      }
    },

    searchListIn:function (){
      if (this.searchListIn != null) {
        this.searchList = this.searchListIn.map(function (item) {
          return {
            "song_url": item.song_url,
            "song_name": item.song_name,
            "song_user": item.song_user,
            "song_album": item.song_album,
            "icon": "el-icon-video-play"
          }
        });
      }
    },

  },

  mounted() {

  }

}
</script>

<style scoped>
.itemButtonGroup {
  position: absolute;
  top: 0;
  right: 20px;
}

.itemButtonGroup:hover .itemButton {
  display: inline-block;
}

.itemButton {
  padding: 5px;
  font-size: 25px;
  color: whitesmoke;
  line-height: 23px;
}

.blank_area {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  width: 100%;
  height: calc(50vh);
}

.music_content {
  height: calc(100vh - 60px);
  color: rgba(225, 225, 225, .8);
}

.music_content /deep/ .el-tabs__header .el-tabs__nav-wrap .el-tabs__nav-scroll .el-tabs__nav .el-tabs__item {
  color: rgba(225, 225, 225, .8) !important;
}

.music_content /deep/ .el-tabs__header .el-tabs__nav-wrap .el-tabs__nav-scroll .el-tabs__nav .el-tabs__item:hover {
  color: whitesmoke !important;
}

.table-wrapper /deep/ .el-table__header-wrapper .has-gutter tr th {
  background-color: transparent;
  color: rgba(225, 225, 225, .8);
}

.table-wrapper /deep/ .el-table, .el-table__expanded-cell {
  background-color: transparent;
  color: rgba(225, 225, 225, .8);
}

.table-wrapper /deep/ .el-table tr {
  background-color: transparent !important;
  color: rgba(225, 225, 225, .8);
}

.table-wrapper /deep/ .el-table--enable-row-transition .el-table__body td, .el-table .cell {
  background-color: transparent;
  color: rgba(225, 225, 225, .8);
}

.table-wrapper /deep/ .el-table--enable-row-transition .el-table__body td .cell {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

/*// 滚动条的宽度*/
/deep/ .el-table__body-wrapper::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

/*// 滚动条的滑块*/
/deep/ .el-table__body-wrapper::-webkit-scrollbar-thumb {
  background-color: #ddd;
  border-radius: 3px;
}

</style>
