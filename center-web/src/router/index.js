import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export const admin = [
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/pages/home'),
    menu: ['管理机器人'],
  },
  {
    path: '/resident',
    name: 'Resident',
    component: () => import('@/admin/resident'),
    menu: ['居民管理'],
  },
  {
    path: '/role',
    name: 'Role',
    component: () => import('@/admin/role'),
    menu: ['安保管理'],
  },
  {
    path: '/camera',
    name: 'camera',
    component: () => import('@/admin/camera'),
    menu: ['车辆监控'],
  },
  {
    path: '/call',
    name: 'call',
    component: () => import('@/admin/call'),
    menu: ['居民反馈'],
  },
  {
    path: '/vehicle',
    name: 'VehicleList',
    component: () => import('@/pages/vehicle/vehicle-list'),
    menu: ['数据修改', '车辆信息修改']
  },
]

export const page = [
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/pages/home'),
    menu: ['首页'],
  },
  {
    path: '/chat',
    name: 'chat',
    component: () => import('@/user/chat'),
    menu: ['问题反馈'],
  },
  // {
  //   path: '/vehicle',
  //   name: 'VehicleList',
  //   component: () => import('@/pages/vehicle/vehicle-list'),
  //   menu: ['数据修改', '车辆信息修改']
  // },
]
// 普通的页面放在这里，有menu字段的会显示在左侧菜单
export const pages = [
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/pages/home'),
    menu: ['首页'],
  },
  {
    path: '/call',
    name: 'call',
    component: () => import('@/admin/call'),
    menu: ['居民反馈'],
  },
  {
    path: '/chat',
    name: 'chat',
    component: () => import('@/user/chat'),
    menu: ['问题反馈'],
  },
  {
    path: '/vehicle',
    name: 'VehicleList',
    component: () => import('@/pages/vehicle/vehicle-list'),
    menu: ['数据修改', '车辆信息修改']
  },
  {
    path: '/resident',
    name: 'Resident',
    component: () => import('@/admin/resident'),
    menu: ['居民管理'],
  },
  {
    path: '/role',
    name: 'Role',
    component: () => import('@/admin/role'),
    menu: ['安保管理'],
  },
  {
    path: '/camera',
    name: 'camera',
    component: () => import('@/admin/camera'),
    menu: ['车辆监控'],
  },
  // {
  //   path: '/users/user',
  //   name: 'UsersList',
  //   component: () => import('@/pages/user/user-list'),
  //   menu: ['数据修改', '分配用户角色']
  // },
  // {
  //   path: '/users/store',
  //   name: 'StoreList',
  //   component: () => import('@/pages/user/store-list'),
  //   menu: ['数据修改', '分配门店角色']
  // },
  // {
  //   path: '/place/tree',
  //   name: 'PlaceTree',
  //   component: () => import('@/pages/place/place_tree'),
  //   menu: ['数据修改', '分配仓库']
  // },
  // {
  //   path: '/vehicle/:vid',
  //   name: 'VehicleDetail',
  //   component: () => import('@/pages/vehicle/vehicle-detail'),
  // },
  // {
  //   path: '/log/vehicle',
  //   name: 'LogVehicle',
  //   component: () => import('@/pages/log/log-vehicle'),
  //   menu: ['修改日志', '车辆日志']
  // },
  // {
  //   path: '/log/role',
  //   name: 'LogVehicle',
  //   component: () => import('@/pages/log/log-role'),
  //   menu: ['修改日志', '角色日志']
  // }
]


export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: () => import('@/pages/login.vue')
    },
    {
      path: '/a',
      name: 'aLogin',
      component: () => import('@/pages/a_login.vue')
    },
    {
      path: '/home',
      name: 'MainLayout',
      component: () => import('@/layouts/main.vue'),
      children: pages

    }
  ]
})
