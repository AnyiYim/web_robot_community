<template style="background: #2baee9">
  <div id="app" style="height:962px; padding-top: 170px; margin-top: -170px;
   background: url(https://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1530372496&di=b8474b6ad24d593b2252ae3d7df8706b&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F2%2F53f1916158d97.jpg)">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  created() {
    this.ajax.setVue(this)
  }
}
</script>
<style lang="less">
  @import './public/css/main.less';
</style>
