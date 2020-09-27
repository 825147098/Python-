<template>
  <el-container class="center">
    <el-main style="padding-top: 0;height: 100%">
      <music-tabs class="center_area"
                  :loading="loading"
                  :search-list-in="searchRes"
      ></music-tabs>
    </el-main>
    <player></player>

  </el-container>
</template>
<script>
import MusicTabs from "@/components/musicTabs";
import Player from "../components/player";
import axios from 'axios';

export default {
  name: 'Home',
  components: {
    Player,
    MusicTabs,
  },
  data: function () {
    return {
      searchRes:[],
      loading: -1,
    }
  },
  methods: {
    getData() {
      this.loading = 1
      axios.get(this.$store.state.host + "/search", {
        params: {
          name: this.$store.state.name,
          type: this.$store.state.type,
        }
      }).then(res => {
        this.searchRes = res.data
        // console.log(this.searchRes)
        this.loading = 0
      }).catch(error => {
        console.log(error)
        this.loading = -2
      })
    }
  },

  watch: {
    "$store.state.searchFlag": function () {
      if (this.$store.state.searchFlag) {
        this.getData()
        this.$store.commit("incrementCleanFlag")
      }
    }
  }

}
</script>
<style scoped>
.center {
  position: relative;
  width: 100%;
  height: calc(90vh);
  max-width: 1200px;
  margin: 0 auto;
}

.center_area {
  position: absolute;
  left: 0;
  right: 400px;
  /*top: 60px;*/
  /*bottom: 0;*/
  overflow: hidden;
}
</style>
