import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'


const store = {}

store.install = function (Vue, options) {
  Vue.use(Vuex)
  Vue.prototype.$store = new Vuex.Store({
    state: {
      user: null
    },
    mutations: {
      setUser (state, userInfo) {
        state.user = userInfo
      },
    },
    plugins: [
      createPersistedState({
        storage: {
          getItem: key => Cookies.get(key),
          setItem: (key, value) => Cookies.set(key, value),
          removeItem: key => Cookies.remove(key)
        }
      })
    ]
  })
}

export default store
