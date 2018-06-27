<template>
  <Layout id="main-layout">
    <TopHeader />
    <Layout  style="" class="sub-layout">
      <Sider style="background: #fff">
        <LeftSiderMenu />
      </Sider>
      <Content class="content">
        <router-view class="container" :key="$route.fullPath"/>
      </Content>
    </Layout>
  </Layout>
</template>
<script>
import TopHeader from '@/components/topHeader'
import LeftSiderMenu from '@/components/leftSiderMenu'
export default {
  components: {
    TopHeader,
    LeftSiderMenu,
  },
  data: () => ({

  }),
}
</script>
<style lang="less" scoped>
  .sub-layout {
    min-height: 100vh;
  }
  .content {
    padding: 20px 20px;
  }
</style>
