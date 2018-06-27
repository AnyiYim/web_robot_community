
let loadingUserInfo = null

var mixin = {
  data: () => ({
  }),
  created() {
    if (!this.$store.state.user) {
      this.g_loadLoginUserInfo()
    }
  },
  methods: {
    g_loadLoginUserInfo() {
      if (loadingUserInfo === null) {
        loadingUserInfo = this.ajax.get('/login/account/info').then(rsp => {
          this.$store.commit('setUser', rsp.data.data)
          loadingUserInfo = null
        }, err => {
          loadingUserInfo = null
        })
      }
      return loadingUserInfo
    }
  },
  computed: {
    g_allowEdit () {
      return Boolean(this.$store.state.user && this.$store.state.user.allowEdit)
    }
  }
}

mixin.install = function (Vue, options) {
  Vue.mixin(mixin)
}

export default mixin
