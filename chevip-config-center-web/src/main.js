// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import './libs/polyfills'
import Ajax from './libs/ajax'
import Store from './libs/store'
import mixin from './libs/mixin'
import * as filters from './libs/filters'

import iView from 'iview';
import 'iview/dist/styles/iview.css';

Vue.config.productionTip = false

Vue.use(iView);

Vue.use(Ajax)
Vue.use(Store)
Vue.use(mixin)
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})


/* eslint-disable no-new */
var vm = new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
