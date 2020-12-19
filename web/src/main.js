import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Icon } from 'leaflet';
import 'bootstrap';
import './assets/app.css';
import 'leaflet/dist/leaflet.css';
import VCharts from 'v-charts'

Vue.config.productionTip = false
Vue.use(VCharts)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});