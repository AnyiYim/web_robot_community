<template>
  <div id="app">
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
