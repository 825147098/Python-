<template>
  <el-container>
    <el-button type="text" @click="dialogVisible = true">点击打开 Dialog</el-button>

    <el-dialog
        :visible.sync="dialogVisible"
        width="30%">
      <searchBar></searchBar>
    </el-dialog>
    <music-tabs></music-tabs>
  </el-container>
</template>

<script>
import searchBar from '../components/searchBar';
import MusicTabs from "@/components/musicTabs";

export default {
  name: 'Home',
  components: {
    MusicTabs,
    searchBar,
  },
  data: function () {
    return {
      dialogVisible: false
    }
  },
  methods: {

  }

}
</script>
