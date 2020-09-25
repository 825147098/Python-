<template>
    <el-aside  width="400px">
        <div class="player">
            <div class="cover">
                <el-image :src=player_img fit="cover" class="music_cover"></el-image>
            </div>
            <div class="lyric">
                <ul ref="lyricUL" id="lyric">
                    <li v-for="(item, i) in lyricsObjArr" :style="{color: lyricIndex === i ? 'skyblue' : '#ded9d9'}"
                        :key="item.uid" :data-index='i' ref="lyric">{{item.lyric}}
                    </li>
                </ul>
            </div>
        </div>
    </el-aside>
</template>

<script>
    // import album_cover from '../assets/albumImgs/album_cover_player.png';
    import player_cover from '../assets/albumImgs/player_cover.png';

    export default {
        name: "player",
        data: function () {
            return {
                player_img: player_cover,
                // album_img:album_cover,
                playData: {
                    "song_url": "https://webfs.yun.kugou.com/202009251449/09c9a9ddd348c9a9b34d87e8accd0bd0/G170/M07/16/11/SocBAF3H3aqAUYOEADmpdloW3bU827.mp3",
                    "song_name": "\u5c11\u5e74",
                    "song_user": "\u68a6\u7136",
                    "song_time": "3:56",
                    "song_img": "http://imge.kugou.com/stdmusic/20191110/20191110174405582448.jpg",
                    "song_lyr": "\ufeff[id:$00000000]\r\n[ar:\u68a6\u7136]\r\n[ti:\u5c11\u5e74]\r\n[by:]\r\n[hash:5b7f8dcfb2cb2240d5ee8e917a0b1aef]\r\n[al:]\r\n[sign:]\r\n[qq:]\r\n[total:236146]\r\n[offset:0]\r\n[00:00.30]\u68a6\u7136 - \u5c11\u5e74\r\n[00:00.91]\u4f5c\u8bcd\uff1a\u68a6\u7136\r\n[00:01.06]\u4f5c\u66f2\uff1a\u68a6\u7136\r\n[00:01.16]\u7f16\u66f2\uff1a\u5f20\u4eae\r\n[00:01.27]\u5236\u4f5c\u4eba\uff1a\u5f20\u4eae\u3001\u5f90\u9601\r\n[00:01.52]\u548c\u58f0\u7f16\u5199\uff1a\u6d77\u9752\u3001\u68a6\u7136\r\n[00:01.72]\u548c\u58f0\u6f14\u5531\uff1a\u6d77\u9752\u3001\u68a6\u7136\r\n[00:01.98]rap\uff1a\u68a6\u7136\r\n[00:02.08]\u6df7\u97f3\u5de5\u7a0b\u5e08\uff1a\u8d75\u9756\r\n[00:02.28]\u6bcd\u5e26\u5de5\u7a0b\u5e08\uff1a\u8d75\u9756\r\n[00:02.49]\u76d1\u5236\uff1a\u68a6\u7136\r\n[00:22.17]\u6362\u79cd\u751f\u6d3b\r\n[00:22.98]\u8ba9\u81ea\u5df1\u53d8\u5f97\u5feb\u4e50\r\n[00:24.81]\u653e\u5f03\u6267\u7740\r\n[00:25.62]\u5929\u6c14\u5c31\u4f1a\u53d8\u5f97\u4e0d\u9519\r\n[00:27.45]\u6bcf\u6b21\u8d70\u8fc7\r\n[00:28.41]\u90fd\u662f\u4e00\u6b21\u6536\u83b7\r\n[00:30.19]\u8fd8\u7b49\u4ec0\u4e48 \u505a\u5bf9\u7684\u9009\u62e9\r\n[00:32.78]\u8fc7\u53bb\u7684\r\n[00:33.39]\u5c31\u8ba9\u5b83\u8fc7\u53bb\u5427\r\n[00:35.42]\u522b\u7ba1\u90a3\u662f\u4e00\u4e2a\u73a9\u7b11\u8fd8\u662f\u8c0e\u8bdd\r\n[00:38.10]\u8def\u5728\u811a\u4e0b\r\n[00:39.07]\u5176\u5b9e\u5e76\u4e0d\u590d\u6742\r\n[00:40.74]\u53ea\u8981\u8bb0\u5f97\u4f60\u662f\u4f60\u5440\r\n[00:43.23]Wu oh oh\r\n[00:53.73]Wu oh oh\r\n[01:03.51]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74\r\n[01:06.41]\u6ca1\u6709\u4e00\u4e1d\u4e1d\u6539\u53d8\r\n[01:09.09]\u65f6\u95f4\u53ea\u4e0d\u8fc7\u662f\u8003\u9a8c\r\n[01:11.78]\u79cd\u5728\u5fc3\u4e2d\u4fe1\u5ff5\u4e1d\u6beb\u672a\u51cf\r\n[01:15.08]\u773c\u524d\u8fd9\u4e2a\u5c11\u5e74\r\n[01:17.06]\u8fd8\u662f\u6700\u521d\u90a3\u5f20\u8138\r\n[01:19.75]\u9762\u524d\u518d\u591a\u8270\u9669\u4e0d\u9000\u5374\r\n[01:22.95]Say never never give up\r\n[01:24.68]Like a fire\r\n[01:25.74]Wu oh oh\r\n[01:36.84]\u6362\u79cd\u751f\u6d3b\r\n[01:37.65]\u8ba9\u81ea\u5df1\u53d8\u5f97\u5feb\u4e50\r\n[01:39.46]\u653e\u5f03\u6267\u7740\r\n[01:40.17]\u5929\u6c14\u5c31\u4f1a\u53d8\u5f97\u4e0d\u9519\r\n[01:42.00]\u6bcf\u6b21\u8d70\u8fc7\r\n[01:43.01]\u90fd\u662f\u4e00\u6b21\u6536\u83b7\r\n[01:44.79]\u8fd8\u7b49\u4ec0\u4e48 \u505a\u5bf9\u7684\u9009\u62e9\r\n[01:47.42]\u8fc7\u53bb\u7684\r\n[01:48.08]\u5c31\u8ba9\u5b83\u8fc7\u53bb\u5427\r\n[01:50.14]\u522b\u7ba1\u90a3\u662f\u4e00\u4e2a\u73a9\u7b11\u8fd8\u662f\u8c0e\u8bdd\r\n[01:52.73]\u8def\u5728\u811a\u4e0b\r\n[01:53.69]\u5176\u5b9e\u5e76\u4e0d\u590d\u6742\r\n[01:55.41]\u53ea\u8981\u8bb0\u5f97\u4f60\u662f\u4f60\u5440\r\n[02:08.45]Miya miya miya miya miya\r\n[02:13.16]Call me\r\n[02:13.92]Miya miya miya miya miya\r\n[02:18.15]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74\r\n[02:21.09]\u6ca1\u6709\u4e00\u4e1d\u4e1d\u6539\u53d8\r\n[02:23.73]\u65f6\u95f4\u53ea\u4e0d\u8fc7\u662f\u8003\u9a8c\r\n[02:26.42]\u79cd\u5728\u5fc3\u4e2d\u4fe1\u5ff5\u4e1d\u6beb\u672a\u51cf\r\n[02:29.76]\u773c\u524d\u8fd9\u4e2a\u5c11\u5e74\r\n[02:31.74]\u8fd8\u662f\u6700\u521d\u90a3\u5f20\u8138\r\n[02:34.47]\u9762\u524d\u518d\u591a\u8270\u9669\u4e0d\u9000\u5374\r\n[02:37.57]Say never never give up\r\n[02:39.35]Like a fire\r\n[02:40.93]\u8ffd\u9010\u751f\u547d\u91cc\r\n[02:41.74]\u5149\u4e34\u8eab\u8fb9\u7684\u6bcf\u9053\u5149\r\n[02:43.21]\u8ba9\u4e16\u754c\u56e0\u4e3a\u4f60\u7684\u5b58\u5728\r\n[02:44.78]\u53d8\u7684\u95ea\u4eae\r\n[02:46.01]\u5176\u5b9e\u4f60\u6211\u4ed6\u5e76\u6ca1\u6709\u4ec0\u4e48\u4e0d\u540c\r\n[02:48.75]\u53ea\u8981\u4f60\u613f\u4e3a\u5e0c\u671b\r\n[02:49.83]\u753b\u51fa\u4e00\u9053\u60f3\u8c61\r\n[02:51.39]\u6210\u957f\u7684\u8def\u4e0a\r\n[02:52.20]\u5fc5\u7136\u7ecf\u5386\u5f88\u591a\u98ce\u96e8\r\n[02:53.87]\u76f8\u4fe1\u81ea\u5df1\u7ec8\u6709\u5c5e\u4e8e\u4f60\u7684\u76db\u4e3e\r\n[02:56.59]\u522b\u56e0\u4e3a\u78e8\u96be \u505c\u4f4f\u4f60\u7684\u811a\u6b65\r\n[02:59.13]\u575a\u6301\u4f4f\r\n[02:59.74]\u5c31\u4f1a\u62e5\u6709\u5c5e\u4e8e\u4f60\u7684\u84dd\u56fe\r\n[03:01.77]Wu oh oh\r\n[03:11.46]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74\r\n[03:14.41]\u6ca1\u6709\u4e00\u4e1d\u4e1d\u6539\u53d8\r\n[03:17.05]\u65f6\u95f4\u53ea\u4e0d\u8fc7\u662f\u8003\u9a8c\r\n[03:19.73]\u79cd\u5728\u5fc3\u4e2d\u4fe1\u5ff5\u4e1d\u6beb\u672a\u51cf\r\n[03:23.03]\u773c\u524d\u8fd9\u4e2a\u5c11\u5e74\r\n[03:25.07]\u8fd8\u662f\u6700\u521d\u90a3\u5f20\u8138\r\n[03:27.76]\u9762\u524d\u518d\u591a\u8270\u9669\u4e0d\u9000\u5374\r\n[03:30.93]Say never never give up\r\n[03:32.52]Like a fire\r\n[03:33.13]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74 miya\r\n[03:38.17]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74 miya\r\n[03:43.44]\u6211\u8fd8\u662f\u773c\u524d\u8fd9\u4e2a\u5c11\u5e74 miya\r\n[03:48.82]\u6211\u8fd8\u662f\u4ece\u524d\u90a3\u4e2a\u5c11\u5e74 miya\r\n",
                    "song_album": "\u5c11\u5e74"
                },

                lyricsObjArr: [],
            }
        },

        methods: {
            pares() {
                const regNewLine = /\r\n/
                const lineArr = this.playData.song_lyr.split(regNewLine) // 每行歌词的数组

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
            }
        },

        props:["playDataIn"],

        mounted() {
            if(this.playDataIn != null)
                this.playData = this.playDataIn
            this.pares()
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

    }
    #lyric{
        position: absolute;
        width: 100%;
        padding: 0;
        top: 0;
        bottom: 0;
        overflow: hidden;
        list-style:none;

    }
</style>