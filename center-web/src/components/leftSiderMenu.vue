<template>
  <Menu
    ref="menu"
    :active-name="menuActiveName"
    :open-names="menuOpenNames"
    theme="light"
    width="auto"
    @on-select="onMenuSelect"
  >
    <template v-for="item in menuTree">
      <Submenu v-if="item.children" :name="item.name">
        <template slot="title">
          {{item.name}}
        </template>
        <MenuItem v-for="subitem in item.children" :name="subitem.path" :key="item.path">
          {{ subitem.name }}
        </MenuItem>
      </Submenu>
      <MenuItem v-else :name="item.path">
        {{ item.name }}
      </MenuItem>
    </template>
    <!--<MenuItem name="old_href_0" v-if="g_allowEdit">-->
      <!--<a :href="oldHref('todos/flows')" class="old-href">审批流模板</a>-->
    <!--</MenuItem>-->
    <!--<MenuItem name="old_href_1" v-if="g_allowEdit">-->
      <!--<a :href="oldHref('tracks/tracks/_DEFAULT')" class="old-href">日志配置</a>-->
    <!--</MenuItem>-->
    <!--<MenuItem name="old_href_2" v-if="g_allowEdit">-->
      <!--<a :href="oldHref('messages/list')" class="old-href">消息模板</a>-->
    <!--</MenuItem>-->
    <!--<MenuItem name="old_href_3">-->
      <!--<a :href="oldHref('observer/vehicle_access/doing')" class="old-href">审批流查看</a>-->
    <!--</MenuItem>-->
  </Menu>
</template>
<script>
import {page} from '@/router'
import {admin} from '@/router'
export default {
  data: () => ({
    menuTree: null,
    menuActiveName: null,
    menuOpenNames: [],
  }),
  created() {
    console.log(page);
    console.log(admin);
    var menuMap = {}
    this.menuTree = []
    var roo;
    if (this.$store.state.user.role === 'ADMIN') {
      roo = admin;
    } else {
      roo = page;
    }
    for (var item of roo) {
      if (item.menu === undefined) { continue }

      if (item.menu.length === 1) {
        // 一级菜单
        this.menuTree.push({
          name: item.menu[0],
          path: item.path,
        })
      } else {
        // 两级菜单
        if (menuMap[item.menu[0]] === undefined) {
          // 创建子菜单
          var subMenu = {
            name: item.menu[0],
            children: [],
          }
          menuMap[item.menu[0]] = subMenu
          this.menuTree.push(subMenu)
        }
        // 把路由节点放进子菜单
        menuMap[item.menu[0]].children.push({
          name: item.menu[1],
          path: item.path,
        })
      }
    }
    console.log(this.menuTree)
    this.setActionMenu()
  },
  methods: {
    setActionMenu() {
      //首次打开页面的时候，根据path设置激活的菜单
      this.menuActiveName = this.$route.path
      for (var submenu of this.menuTree) {
        if (submenu.children) {
          for (var subitem of submenu.children) {
            if (subitem.path === this.$route.path) {
              this.menuOpenNames.push(submenu.name)
            }
          }
        }
      }
    },
    onMenuSelect(path) {
      if (path.indexOf('old_href') === 0) {
        return
      }
      this.menuActiveName = path
      this.$router.push(path)
      this.$nextTick(() => {
        this.$refs.menu.updateActiveName()
      })
    },
    oldHref(path) {
      return (new URL(path, new URL(process.env.API, location.origin))).href
    }
  }
}
</script>
<style lang="less" scoped>
  .old-href {
    color: #495060;
  }
</style>
