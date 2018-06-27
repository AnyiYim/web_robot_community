<template>
  <Header>
    <!--<div></div>-->
    <div class="top-bar">
      <span style="font-size: 20px; color: #fff; font-weight: bold">{{ $store.state.user.role | duang}}</span>
      <Dropdown v-if="$store.state.user"
        class="account-info"
        @on-click="ddClick">
          {{ $store.state.user.user_name }}
          ({{ $store.state.user.role }})
          <Icon type="arrow-down-b"></Icon>
        <DropdownMenu slot="list">
            <DropdownItem name="logout">安全退出</DropdownItem>
        </DropdownMenu>
      </Dropdown>
    </div>
  </Header>
</template>
<script>
export default {
  data: () => ({

  }),
  methods: {
    ddClick(name) {
      switch (name) {
        case 'logout':
          this.ajax.post('login/logout').then(rsp => {
            this.$store.commit('setUser', null)
            this.$router.push('/login')
          })
          break;
        default:

      }
    }
  },
  filters: {
    duang: function (value) {
      const status_dict = {
        USER: '用户端', ADMIN: '管理端',
      };
      return value && status_dict[value] || null;
    }
  },
}
</script>
<style lang="less" scoped>
  .top-logo {
    width: 152px;
    margin: 8px 0 0 -26px;
    float: left;
    img {
      width: 100%;
    }
  }
  .top-bar {
    color: #fff;
    .account-info {
      float: right;
    }
  }
</style>
