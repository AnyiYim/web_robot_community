import axios from 'axios';

let ajax = axios.create({
  baseURL: process.env.API,
  timeout: 30000,
  headers: {Jsononly: 1},
  withCredentials: true,
  transformRequest: [function (data) {
    // Do whatever you want to transform the data
    if (typeof(data) === 'object' && !(data instanceof FormData)) {
      let ret = ''
      for (let it in data) {
        if(data[it] === null) {
          ret += encodeURIComponent(it) + '=&'
        } else if (data[it] !== undefined) {
          ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
        }
      }
      return ret
    }
    return data
  }],
});


var vm

ajax.setVue = function (v) {
  vm = v
}

ajax.install = function (Vue, options) {
  Vue.prototype.ajax = ajax

  ajax.interceptors.response.use(response => {
    if (response.data.code === 403 && vm.$route.path !== '/') {
      vm.$router.push('/')
    } else if (response.data.msg) {
      if (response.data.code===0) {
        vm.$Message.info(response.data.msg)
      } else {
        vm.$Message.warning(response.data.msg)
      }
    }
    return response
  })
}


export default ajax
