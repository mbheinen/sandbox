import Vue from 'vue'
import App from './App.vue'
import ServerStatus from './components/ServerStatus.vue'
import ServerList from './components/ServerList.vue'
import ServerDetails from './components/ServerDetails.vue'
import AppFooter from './components/AppFooter.vue'

Vue.component("server-status", ServerStatus);
Vue.component("server-list", ServerList);
Vue.component("server-details", ServerDetails);
Vue.component("app-footer", AppFooter);

new Vue({
  el: '#app',
  render: h => h(App)
})
