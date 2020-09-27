<template>
  <el-aside width="400px">
    <div class="player">
      <div class="cover">
        <el-image :src=player_img fit="cover" class="music_cover">
          <el-image slot="error" :src="error_img" fit="cover" class="music_cover"></el-image>
        </el-image>
      </div>
      <div class="lyric">
        <ul ref="lyricUL" id="lyric" v-if="playData.song_lyr != 'null'">
          <li v-for="(item, i) in lyricsObjArr" :style="{color: lyricIndex === i ? 'skyblue' : '#ded9d9'}"
              :key="item.uid" :data-index='i' ref="lyric">{{ item.lyric }}
          </li>
        </ul>
        <div v-else>
          <p>
            没有歌词
          </p>
        </div>
      </div>

      <el-popover
          placement="right"
          width="400px"
          trigger="click"
          v-show="playIndex !== -1 "
      >
        <transition name="el-fade-in">
          <div class="pop_info">
            <span class="info_title">歌名：</span>{{ playData.song_name }}<br>
            <span class="info_title">歌手：</span>{{ playData.song_user }}<br>
            <span class="info_title">专辑：</span>{{ playData.song_album }}<br>
            <span class="info_title">时长：</span>{{ playData.song_time }}<br>
            <span class="info_title">操作：</span>
            <a :href=playData.song_url target="#" style="text-decoration: none; color: #31c27c">
              下载
            </a>
            <br>
          </div>
        </transition>
        <el-button type="text"
                   class="music_info"
                   icon="el-icon-menu"
                   slot="reference"
        ></el-button>
      </el-popover>
    </div>
    <div class="footer">
      <div class="footer_container">
        <div class="footer_con_btn">
          <el-button type="text">
            <el-image :src=preMu
                      @click="clickPre"
                      class="btn_pre btn_img"
                      title="上一首"></el-image>
          </el-button>
          <el-button type="text" @click="playSong">
            <el-image v-show="!isPlaying"
                      :src=playMu
                      class="btn_play btn_img"
                      title="暂停/播放"></el-image>
            <el-image v-show="isPlaying"
                      :src=suspendMu
                      class="btn_play btn_img"
                      title="暂停/播放"></el-image>
          </el-button>
          <el-button type="text">
            <el-image :src=nextMu
                      @click="clickNext"
                      class="btn_next btn_img"
                      title="下一首"></el-image>
          </el-button>
          <el-button type="text" @click="changePlayModel">
            <el-image :src=playBackMode
                      class="btn_order btn_img"
                      title="播放模式"></el-image>
          </el-button>
        </div>
        <div class="footer_vol">
          <div class="vol_btn">
            <el-button type="text" @click="silenceVol">
              <el-image v-show="!isSilence" :src=volumeMu class="vol_img"></el-image>
              <el-image v-show="isSilence" :src=silenceMu class="vol_img"></el-image>
            </el-button>
          </div>
          <div class="volume">
            <div class="volume_box">
              <div id="volume-progress" class="mkpgb_area" @click="clickVol">
                <div class="mkpgb-bar"></div>
                <div class="mkpgb-cur" :style="{width: `${volPrecent}`}"></div>
                <div class="mkpgb-dot"
                     :style="{left: `${volPrecent}`}"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="progress_area">
          <div class="progress_box">
            <div id="music-progress" class="mkpgb_area mkpgb-locked" @click="clickProgress">
              <div class="mkpgb-bar"></div>
              <div class="mkpgb-cur" :style="{width: `${musicPrecent}`}"></div>
              <div class="mkpgb-dot"
                   :style="{left: `${musicPrecent}`}"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <audio :src="playData.song_url"
           @timeupdate="updateTime"
           @canplay="getDuration"
           @ended="ended"
           preload id="audioPlay"></audio>
  </el-aside>
</template>

<script>
// import album_cover from '../assets/albumImgs/album_cover_player.png';
import player_cover from '../assets/albumImgs/player_cover.png';
import preMu from '../assets/musicImgs/shangyishou.png';
import nextMu from '../assets/musicImgs/xiayishou.png';
import playMu from '../assets/musicImgs/icon_play.png';
import zantingMu from '../assets/musicImgs/zanting.png';
import sounds from '../assets/musicImgs/V.png';
import jingyin from '../assets/musicImgs/jingyin.png';
import shunxu from '../assets/musicImgs/xunhuanbofang.png';
import danyi from '../assets/musicImgs/danquxunhuan.png';
import suiji from '../assets/musicImgs/ziyuan.png';

// import $ from 'jQuery';

export default {
  name: "player",
  data: function () {
    return {
      player_img: player_cover,
      error_img: player_cover,
      // album_img:album_cover,
      playData: {
        // "song_url": "https://webfs.yun.kugou.com/202009251449/09c9a9ddd348c9a9b34d87e8accd0bd0/G170/M07/16/11/SocBAF3H3aqAUYOEADmpdloW3bU827.mp3",
        // "song_name": "\u5c11\u5e74",
        // "song_user": "\u68a6\u7136",
        // "song_time": "3:56",
        // "song_img": "http://imge.kugou.com/stdmusic/20191110/20191110174405582448.jpg",
        // "song_lyr": "\ufeff[id:$00000000]\r\n[ar:\u68a6\u7136]\r\n[ti:\u5c11\u5e74]\r\n[by:]\r\n[hash:5b7f8dcfb2cb2240d5ee8e917a0b1aef]\r\n[al:]\r\n[sign:]\r\n[qq:]\r\n[total:236146]\r\n[offset:0]\r\n[00:00.30]\u68a6\u7136 - \u5c11\u5e74\r\n[00:00.91]\u4f5c\u8bcd\uff1a\u68a6\u7136\r\n[00:01.06]\u4f5c\u66f2\uff1a\u68a6\u7136\r\n[00:01.16]\u7f16\u66f2\uff1a\u5f20\u4eae\r\n[00:01.27]\u5236\u4f5c\u4eba\uff1a\u5f20\u4eae\u3001\u5f90\u9601\r\n[00:01.52]\u548c\u58f0\u7f16\u5199\uff1a\u6d77\u9752\u3001\u68a6\u7136\r\n[00:01.72]\u548c\u58f0\u6f14\u5531\uff1a\u6d77\u9752\u3001\u68a6\u7136\r\n[00:01.98]rap\uff1a\u68a6\u7136\r\n[00:02.08]\u6df7\u97f3\u5de5\u7a0b\u5e08\uff1a\u8d75\u9756\r\n[00:02.28]\u6bcd\u5e26\u5de5\u7a0b\u5e08\uff1a\u8d75\u9756\r\n[00:02.49]\u76d1\u5236\uff1a\u68a6\u7136\r\n[00:22.17]\u6362\u79cd\u751f\u6d3b\r\n[00:22.98]\u8ba9\u81ea\u5df1\u53d8\u5f97\u5feb\u4e50\r\n[00:24.81]\u653e\u5f03\u6267\u7740\r\n[00:25.62]\u5929\u6c14\u5c31\u4f1a\u53d8\u5f97\u4e0d\u9519\r\n[00:27.45]\u6bcf\u6b21\u8d70\u8fc7\r\n[00:28.41]\u90fd\u662f\u4e00\u6b21\u6536\u83b7\r\n[00:30.19]\u8fd8\u7b49\u4ec0\u4e48 \u505a\u5bf9\u7684\u9009\u62e9\r\n[00:32.78]\u8fc7\u53bb\u7684\r\n[00:33.39]\u5c31\u8ba9\u5b83\u8fc7\u53bb\u5427\r\n[00:35.42]\u522b\u7ba1\u90a3\u662f\u4e00\u4e2a\u73a9\u7b11\u8fd8\u662f\u8c0e\u8bdd\r\n[00:38.10]\u8def\u5728\u811a\u4e0b\r\n[00:39.07]\u5176\u5b9e\u5e76\u4e0d\u590d\u6742\r\n[00:40.74]\u53ea\u8981\u8bb0\u5f97\u4f60\u662f\u4f60\u5440\r\n[00:43.23]Wu oh oh\r\n[00:53.73]Wu oh oh\r\n[01:03.51]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74\r\n[01:06.41]\u6ca1\u6709\u4e00\u4e1d\u4e1d\u6539\u53d8\r\n[01:09.09]\u65f6\u95f4\u53ea\u4e0d\u8fc7\u662f\u8003\u9a8c\r\n[01:11.78]\u79cd\u5728\u5fc3\u4e2d\u4fe1\u5ff5\u4e1d\u6beb\u672a\u51cf\r\n[01:15.08]\u773c\u524d\u8fd9\u4e2a\u5c11\u5e74\r\n[01:17.06]\u8fd8\u662f\u6700\u521d\u90a3\u5f20\u8138\r\n[01:19.75]\u9762\u524d\u518d\u591a\u8270\u9669\u4e0d\u9000\u5374\r\n[01:22.95]Say never never give up\r\n[01:24.68]Like a fire\r\n[01:25.74]Wu oh oh\r\n[01:36.84]\u6362\u79cd\u751f\u6d3b\r\n[01:37.65]\u8ba9\u81ea\u5df1\u53d8\u5f97\u5feb\u4e50\r\n[01:39.46]\u653e\u5f03\u6267\u7740\r\n[01:40.17]\u5929\u6c14\u5c31\u4f1a\u53d8\u5f97\u4e0d\u9519\r\n[01:42.00]\u6bcf\u6b21\u8d70\u8fc7\r\n[01:43.01]\u90fd\u662f\u4e00\u6b21\u6536\u83b7\r\n[01:44.79]\u8fd8\u7b49\u4ec0\u4e48 \u505a\u5bf9\u7684\u9009\u62e9\r\n[01:47.42]\u8fc7\u53bb\u7684\r\n[01:48.08]\u5c31\u8ba9\u5b83\u8fc7\u53bb\u5427\r\n[01:50.14]\u522b\u7ba1\u90a3\u662f\u4e00\u4e2a\u73a9\u7b11\u8fd8\u662f\u8c0e\u8bdd\r\n[01:52.73]\u8def\u5728\u811a\u4e0b\r\n[01:53.69]\u5176\u5b9e\u5e76\u4e0d\u590d\u6742\r\n[01:55.41]\u53ea\u8981\u8bb0\u5f97\u4f60\u662f\u4f60\u5440\r\n[02:08.45]Miya miya miya miya miya\r\n[02:13.16]Call me\r\n[02:13.92]Miya miya miya miya miya\r\n[02:18.15]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74\r\n[02:21.09]\u6ca1\u6709\u4e00\u4e1d\u4e1d\u6539\u53d8\r\n[02:23.73]\u65f6\u95f4\u53ea\u4e0d\u8fc7\u662f\u8003\u9a8c\r\n[02:26.42]\u79cd\u5728\u5fc3\u4e2d\u4fe1\u5ff5\u4e1d\u6beb\u672a\u51cf\r\n[02:29.76]\u773c\u524d\u8fd9\u4e2a\u5c11\u5e74\r\n[02:31.74]\u8fd8\u662f\u6700\u521d\u90a3\u5f20\u8138\r\n[02:34.47]\u9762\u524d\u518d\u591a\u8270\u9669\u4e0d\u9000\u5374\r\n[02:37.57]Say never never give up\r\n[02:39.35]Like a fire\r\n[02:40.93]\u8ffd\u9010\u751f\u547d\u91cc\r\n[02:41.74]\u5149\u4e34\u8eab\u8fb9\u7684\u6bcf\u9053\u5149\r\n[02:43.21]\u8ba9\u4e16\u754c\u56e0\u4e3a\u4f60\u7684\u5b58\u5728\r\n[02:44.78]\u53d8\u7684\u95ea\u4eae\r\n[02:46.01]\u5176\u5b9e\u4f60\u6211\u4ed6\u5e76\u6ca1\u6709\u4ec0\u4e48\u4e0d\u540c\r\n[02:48.75]\u53ea\u8981\u4f60\u613f\u4e3a\u5e0c\u671b\r\n[02:49.83]\u753b\u51fa\u4e00\u9053\u60f3\u8c61\r\n[02:51.39]\u6210\u957f\u7684\u8def\u4e0a\r\n[02:52.20]\u5fc5\u7136\u7ecf\u5386\u5f88\u591a\u98ce\u96e8\r\n[02:53.87]\u76f8\u4fe1\u81ea\u5df1\u7ec8\u6709\u5c5e\u4e8e\u4f60\u7684\u76db\u4e3e\r\n[02:56.59]\u522b\u56e0\u4e3a\u78e8\u96be \u505c\u4f4f\u4f60\u7684\u811a\u6b65\r\n[02:59.13]\u575a\u6301\u4f4f\r\n[02:59.74]\u5c31\u4f1a\u62e5\u6709\u5c5e\u4e8e\u4f60\u7684\u84dd\u56fe\r\n[03:01.77]Wu oh oh\r\n[03:11.46]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74\r\n[03:14.41]\u6ca1\u6709\u4e00\u4e1d\u4e1d\u6539\u53d8\r\n[03:17.05]\u65f6\u95f4\u53ea\u4e0d\u8fc7\u662f\u8003\u9a8c\r\n[03:19.73]\u79cd\u5728\u5fc3\u4e2d\u4fe1\u5ff5\u4e1d\u6beb\u672a\u51cf\r\n[03:23.03]\u773c\u524d\u8fd9\u4e2a\u5c11\u5e74\r\n[03:25.07]\u8fd8\u662f\u6700\u521d\u90a3\u5f20\u8138\r\n[03:27.76]\u9762\u524d\u518d\u591a\u8270\u9669\u4e0d\u9000\u5374\r\n[03:30.93]Say never never give up\r\n[03:32.52]Like a fire\r\n[03:33.13]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74 miya\r\n[03:38.17]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74 miya\r\n[03:43.44]\u6211\u8fd8\u662f\u773c\u524d\u8fd9\u4e2a\u5c11\u5e74 miya\r\n[03:48.82]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74 miya\r\n",
        // "song_album": "\u5c11\u5e74"
      },

      lyricsObjArr: [],
      preMu: preMu,
      nextMu: nextMu,
      playMu: playMu,
      suspendMu: zantingMu,
      volumeMu: sounds,
      silenceMu: jingyin,
      orderMu: shunxu,
      randomMu: suiji,
      singleMu: danyi,

      playBackMode: shunxu,

      playIndex: 0,

      audioPlay: '',
      vol_dot: '',
      pro_dot: '',
      vol_bar: '',
      pro_bar: '',

      isPlaying: false, // 播放和暂停状态
      isSilence: false,
      curTime: '00:00', // 当前播放时间，格式化之后的
      allTime: '00:00', // 当前音频总时长，格式化之后的
      duration: 0, // 音频总时长，单位秒
      currentTime: 0, // 音频当前播放时间， 单位秒
      musicPrecent: '0%', // 当前播放进度百分比
      volPrecent: '100%',
      touchInfo: {}, // 原点滑动时的位置信息
      curMsTime: '', // 当前音频播放的时分毫秒
      lyricIndex: '0', // 当前显示的歌词
      isMuted: false, // 是否静音 默认不静音
      volume: 1, // 音频音量


    }
  },

  methods: {
    paresLyr() {
      const regNewLine = /\r\n/
      const lineArr = this.playData.song_lyr.split(regNewLine) // 每行歌词的数组

      this.lyricsObjArr = []
      const regTime = /\[\d{2}:\d{2}.\d{2,3}\]/ //匹配时间
      lineArr.forEach(item => {
        if (item === '') return
        const obj = {}
        const time = item.match(regTime)

        obj.lyric = item.split(']')[1].trim() === '' ? '' : item.split(']')[1].trim()
        obj.time = time ? this.formatLyricTime(time[0].slice(1, time[0].length - 1)) : 0
        obj.uid = Math.random().toString().slice(-6)
        if (obj.lyric === '') {
          console.log('这一行没有歌词')
        } else {
          this.lyricsObjArr.push(obj)
        }
      })
      // console.log(this.lyricsObjArr)

    },
    getDuration() { // canplay时获取音频总时长
      this.duration = this.audioPlay.duration
      this.allTime = this.formatTime(this.audioPlay.duration)
    },
    formatTime(time) {
      if (time === 0) {
        this.curTime = '00:00'
        return
      }
      const mins = Math.floor(time / 60) < 10 ? `0${Math.floor(time / 60)}` : Math.floor(time / 60)
      const sec = Math.floor(time % 60) < 10 ? `0${Math.floor(time % 60)}` : Math.floor(time % 60)
      return `${mins}:${sec}`
    },

    updateTime(e) { // timeupdate时获取当前播放时间
      const {currentTime} = e.target
      this.currentTime = currentTime
      this.curTime = this.formatTime(currentTime) === 'undefined' ? '00:00' : this.formatTime(currentTime)
      this.updateProgress(currentTime, this.duration, 0)
      if(this.playData.song_lyr !== 'null'){
        // 匹配歌词
        for (let i = 0; i < this.lyricsObjArr.length; i++) {
          if (this.currentTime > (parseInt(this.lyricsObjArr[i].time))) {
            const index = this.$refs.lyric[i].dataset.index
            if (i === parseInt(index)) {
              this.lyricIndex = i
              this.$refs.lyricUL.style.transform = `translateY(${170 - (30 * (i + 1))}px)`
            }
          }
        }
      }
    },

    updateProgress(currentTime, duration, type) { // 更新进度条
      const presents = `${((currentTime / duration) * 100).toFixed(5)}%`
      if (type === 0) {
        this.musicPrecent = presents
      } else {
        this.volPrecent = presents
      }
    },

    //格式化时间
    formatLyricTime(time) { // 格式化歌词的时间 转换成 sss:ms
      const regMin = /.*:/
      const regSec = /:.*\./
      const regMs = /\./

      const min = parseInt(time.match(regMin)[0].slice(0, 2))
      let sec = parseInt(time.match(regSec)[0].slice(1, 3))
      const ms = time.slice(time.match(regMs).index + 1, time.match(regMs).index + 3)
      if (min !== 0) {
        sec += min * 60
      }
      return Number(sec + '.' + ms)
    },

    playSong() {
      if (this.playIndex == -1) {
        this.$store.commit("incrementChangeIndex", {flag: 1})
        return
      }
      if (!this.isPlaying) {
        this.isPlaying = !this.isPlaying
        this.audioPlay.play()
        // this.playMode = this.suspendMu
      } else {
        this.isPlaying = !this.isPlaying
        this.audioPlay.pause()
        // this.playMode = this.playMu
      }
    },

    getLeft(obj) {
      var offset = obj.offsetLeft;
      if (obj.offsetParent != null) offset += this.getLeft(obj.offsetParent);
      return offset;
    },

    clickProgress(e) { // 点击进度条时 更新音频时间和进度条
      const position = e.clientX - this.getLeft(document.getElementById("music-progress"))// 当前点击的位置
      const progressWidth = document.getElementById("music-progress").offsetWidth // 进度条总宽度
      this.audioPlay.currentTime = Math.floor(((position / progressWidth) * this.duration))
      this.updateProgress(((position / progressWidth) * this.duration), this.duration, 0)
      this.isPlaying = true
      this.audioPlay.play()
    },
    // dotStart(e) {
    //   // 点击的初始位置
    //   this.touchInfo.startX = e.clientX - this.getLeft(document.getElementById("music-progress"))// 当前点击的位置
    // },
    // dotMove(e) {
    //   // 移动的距离
    //   let moveX = e.clientX - this.getLeft(document.getElementById("music-progress"))// 当前点击的位置
    //   // 进度条的宽度
    //   const progressWidth = document.getElementById("music-progress").offsetWidth // 进度条总宽度
    //   if (moveX >= progressWidth) moveX = progressWidth
    //   this.audioPlay.currentTime = Math.floor(((moveX / progressWidth) * this.duration))
    //   this.updateProgress(((moveX / progressWidth) * this.duration), this.duration, 0)
    // },
    // dotEnd() {
    //   this.audioPlay.play()
    //   this.isPlaying = true
    // },

    clickVol(e) { // 点击进度条时 更新音频时间和进度条
      const position = e.clientX - this.getLeft(document.getElementById("volume-progress"))// 当前点击的位置
      const volumeWidth = document.getElementById("volume-progress").offsetWidth // 进度条总宽度
      this.audioPlay.volume = position / volumeWidth
      this.volume = position / volumeWidth
      this.updateProgress(((position / volumeWidth) * this.duration), this.duration, 1)
      if (this.volume > 0)
        this.isSilence = false
    },
    // volDotStart(e) {
    //   // 点击的初始位置
    //   this.touchInfo.startX = e.touches[0].pageX - 83
    // },
    // volDotMove(e) {
    //   // 移动的距离
    //   let moveX = e.touches[0].pageX - 83
    //   const volumeWidth = document.getElementById("volume-progress").offsetWidth // 进度条总宽度
    //   if (moveX >= volumeWidth) moveX = volumeWidth
    //   this.volume = moveX / volumeWidth
    //   console.log(moveX)
    //   this.updateProgress(((moveX / volumeWidth) * this.duration), this.duration, 1)
    // },
    // voldotEnd() {
    //   this.audioPlay.volume = this.volume
    // },

    silenceVol() {
      if (!this.isSilence) {
        this.audioPlay.volume = 0;
        this.volPrecent = '0%'
      } else {
        this.audioPlay.volume = this.volume;
        this.volPrecent = this.volume * 100 + '%'
      }

      this.isSilence = !this.isSilence
    },

    getElement() {
      this.audioPlay = document.getElementById("audioPlay")
    },

    ended() {
      switch (this.playBackMode) {
        case shunxu:
          this.audioPlay.autoPlay = true
          this.clickNext()
          break
        case suiji:
          if (this.$store.state.randomFlag)
            this.$store.commit("incrementRandomFlag")
          this.clickNext()
          break
        case danyi:
          this.audioPlay.loop = true
          break
      }
    },

    clickPre() {
      this.playSong()
      this.$store.commit("incrementChangeIndex", {flag: -1})
    },

    clickNext() {
      this.playSong()
      this.$store.commit("incrementChangeIndex", {flag: 1})
    },

    changePlayModel() {
      this.audioPlay.loop = false
      switch (this.playBackMode) {
        case shunxu:
          this.playBackMode = this.randomMu
          this.$store.commit('incrementRandomFlag')
          break
        case suiji:
          this.playBackMode = this.singleMu
          this.$store.commit("incrementCleanRandomFlag")
          this.audioPlay.loop = true
          break
        case danyi:
          this.playBackMode = this.orderMu
          break
      }
      // console.log(this.$store.state.randomFlag)
    },

    redo() {
      this.isPlaying = false
      this.player_img = player_cover
      this.playIndex = -1
      this.lyricsObjArr = []
      this.audioPlay.loop = false
      this.audioPlay.autoPlay = false
    }

  },

  watch: {
    "$store.state.playData.song_flag": function () {
      if (this.$store.state.playData.song_flag) {
        this.playData = this.$store.state.playData
        if (this.playData.song_url === ""){
          this.$store.commit("incrementCleanPlayFlag")
          console.log(this.playData)
          this.redo()
        }
        else {
          if (this.playData.song_time == 'null') {
            this.playData.song_time = this.formatTime(this.audioPlay.duration)
          }
          this.$store.commit("incrementCleanPlayFlag")
          if (this.playData.song_lyr != 'null')
            this.paresLyr()
          this.player_img = this.playData.song_img
          this.playIndex = this.$store.state.playIndex
          setTimeout(() => {
            this.playSong()
          }, 2000)
        }
        // console.log(this.isPlaying)
      }
    },
  },


  mounted() {
    this.getElement()
    this.playIndex = this.$store.state.playIndex
  }
}
</script>

<style scoped>
.player {
  height: 100%;
  width: 100%;
  float: right;
}

.cover {
  position: relative;
  display: block;
  width: 186px;
  height: 186px;
  margin: auto;
}

.music_cover {
  vertical-align: middle;
  width: 186px;
  height: 186px;
}

.music_cover::after {
  content: "";
  position: absolute;
  left: -15px;
  top: 0;
  width: 201px;
  height: 180px;
  background: url(../assets/albumImgs/album_cover_player.png) 0 0 no-repeat;
  pointer-events: none;
}

.lyric {
  position: absolute;
  top: 195px;
  width: 400px;
  bottom: 10px;
  overflow: hidden;
  text-align: center;
  color: rgba(225, 225, 225, .8);
  line-height: 28px;
  padding: 20px 0;
  max-height: 350px;

}

#lyric {
  position: absolute;
  width: 100%;
  padding: 0;
  top: 0;
  bottom: 0;
  /*overflow: hidden;*/
  list-style: none;
}

.footer {
  height: 100px;
  bottom: 0;
  left: 0;
  width: 100%;
  position: absolute;
}

.footer_container {
  position: relative;
  width: 100%;
  height: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.footer_con_btn {
  float: left;
  width: 130px;
  height: 100%;
  position: relative;
  margin: 0 10px;
}

.btn_pre {
  width: 19px;
  height: 20px;
  margin-top: -10px;
  left: 0;
}

.btn_play {
  width: 25px;
  height: 29px;
  margin-top: -14.5px;
  left: 36%;
  margin-left: -10.5px;
}

.btn_next {
  right: 30%;
  width: 19px;
  height: 20px;
  margin-top: -10px;
}

.btn_order {
  background-size: 450%;
  right: 0;
  width: 20px;
  height: 20px;
  margin-top: -10px;
}

.btn_img {
  display: inline-block;
  position: absolute;
  top: 50%;
}

.footer_vol {
  float: right;
  width: 200px;
  height: 100%;
  right: 0;
  position: relative;
}

.vol_btn {
  width: 60px;
  height: 100%;
  position: relative;
  float: left;
}

.vol_img {
  display: inline-block;
  position: absolute;
  width: 21px;
  height: 21px;
  top: 50%;
  right: 0;
  margin-top: -10px;
}

.volume {
  position: relative;
  margin-left: 60px;
  height: 100%;
  overflow: hidden;
}

.volume_box {
  position: absolute;
  height: 20px;
  left: 10px;
  right: 10px;
  top: 50%;
  margin-top: -10px;
}

.mkpgb_area {
  position: relative;
  cursor: pointer;
  height: 100%;
}

.mkpgb-bar {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 2px;
  margin-top: -1px;
  border-radius: 2px;
  background-color: #808284;
  overflow: hidden;
}

.mkpgb-cur {
  position: absolute;
  background-color: #D8D8D8;
  width: 0;
  height: 2px;
  top: 50%;
  margin-top: -1px;
  border-radius: 2px;
  transition: all 0.25s ease;
  -webkit-transition: all 0.25s ease;
  -moz-transition: all 0.25s ease;
  -o-transition: all 0.25s ease;
  -ms-transition: all 0.25s ease;
}

.mkpgb-dot {
  width: 10px;
  height: 10px;
  background-color: #fff;
  border-radius: 5px;
  overflow: hidden;
  position: absolute;
  margin-left: -5px;
  top: 50%;
  margin-top: -5px;
  transition: all 0.25s ease;
  -webkit-transition: all 0.25s ease;
}

.mkpgb-locked {
  cursor: default;
}

.progress_area {
  width: auto;
  margin-left: 150px;
  margin-right: 200px;
  height: 100%;
  position: relative;
}

.progress_box {
  position: absolute;
  height: 20px;
  left: 10px;
  right: 0;
  top: 50%;
  margin-top: -9px;
}

.music_info {
  position: absolute;
  width: 27px;
  border-radius: 13px;
  right: 10px;
  bottom: 150px;
  cursor: pointer;
  color: #fff;
  text-align: center;
  line-height: 26px;
  font-weight: bold;
  background-color: #353535;
  opacity: 0.3;
}

.pop_info {
  position: relative;
  padding: 20px;
  line-height: 24px;
  word-break: break-all;
  overflow: hidden;
  font-size: 14px;
  overflow-x: hidden;
  overflow-y: auto;
}

.info_title {
  color: #B2AFAF
}
</style>
