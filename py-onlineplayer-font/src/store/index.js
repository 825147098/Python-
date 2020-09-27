import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    type:'',
    name:'',
    host:"http://localhost:8000",
    searchFlag:false,

    randomFlag:false,

    playData:{
      "song_url": '',
      "song_name": "",
      "song_user": "",
      "song_time": "",
      "song_img": "",
      "song_lyr": "",
      "song_album": "",
      "song_flag": false
    },
    playIndex:-1,

  },
  mutations: {
    incrementName(state,payload){
      state.name = payload.newName;
      state.type = payload.newType;
      state.searchFlag = true
    },

    incrementCleanFlag(state){
      state.searchFlag = false
    },

    incrementPlayData(state,payload){
      state.playData.song_album = payload.playObj.song_album
      state.playData.song_url = payload.playObj.song_url
      state.playData.song_user = payload.playObj.song_user
      state.playData.song_time = payload.playObj.song_time
      state.playData.song_img = payload.playObj.song_img
      state.playData.song_lyr = payload.playObj.song_lyr
      state.playData.song_name = payload.playObj.song_name

      state.playData.song_flag = true

      state.playIndex = payload.pindex
    },

    incrementCleanPlayFlag(state){
      state.playData.song_flag = false
    },

    incrementChangeIndex(state,payload){
      state.playIndex += payload.flag
    },

    incrementRandomFlag(state){
      state.randomFlag = true
    },

    incrementCleanRandomFlag(state){
      state.randomFlag= false
    },
  },
  actions: {
  },
  modules: {
  }
})
