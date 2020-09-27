import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
import './plugins/wyz-echarts/wyz-echarts.js'
import 'default-passive-events'
import 'element-ui/lib/theme-chalk/base.css';
import CollapseTransition from 'element-ui/lib/transitions/collapse-transition';

Vue.config.productionTip = false
Vue.component(CollapseTransition.name, CollapseTransition)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
