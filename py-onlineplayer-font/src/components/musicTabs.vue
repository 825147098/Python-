<template>
  <el-container class="data_area">
    <el-tabs v-model="activeName" type="card">
      <el-tab-pane label="播放列表" name="first">
        <div v-if="playList.length == 0">
          弄啥呢，怎么啥也没有！！！
        </div>
        <el-table v-else
            width="100%"
            :data="playList"
        >
          <el-table-column
              type="index"
              width="50"
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
                           text="点击播放这首歌"
                           type="text">
                </el-button>
                <a :download=scope.row.song_url target="#">
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
              prop="song_user"
          ></el-table-column>
          <el-table-column
              label="专辑"
              width="150px"
              prop="song_album"
          ></el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="搜索列表" name="second">
        <el-table width="100%"
                  :data="searchList"
        >
          <el-table-column
              type="index"
              width="50"
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
                           text="点击播放这首歌"
                           type="text">
                </el-button>
                <a :download=scope.row.song_url target="#">
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
              prop="song_user"
          ></el-table-column>
          <el-table-column
              label="专辑"
              width="150px"
              prop="song_album"
          ></el-table-column>
        </el-table>
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
      searchList: [{
        "song_url": "https://webfs.yun.kugou.com/202009250914/a2bf29a17a8c092f3e8b6499172240ad/G170/M07/16/11/SocBAF3H3aqAUYOEADmpdloW3bU827.mp3",
        "song_name": "\u5c11\u5e74",
        "song_user": "\u68a6\u7136",
        "song_album": "\u5c11\u5e74",
        "icon": "el-icon-video-play"
      }],
      playList: [],

    }
  },

  methods: {},

  props: [
    "searchListIn",
    "playListIn"
  ],

  mounted() {
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
    if (this.playListIn != null) {
      this.playListIn = this.playList;
    }

  }

}
</script>

<style scoped>
.data_area {
  position: relative;
  width: 100%;
  height: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.itemButtonGroup {
  position: absolute;
  top: 0;
  right: 20px;
}

.itemButton {
  padding: 5px;
  font-size: 25px;
  color: whitesmoke;
  line-height: 23px;
}
</style>
