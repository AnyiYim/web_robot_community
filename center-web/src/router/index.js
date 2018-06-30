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
]

export const kk = [
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/pages/home'),
    menu: ['管理机器人'],
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
      path: '/k',
      name: 'kLogin',
      component: () => import('@/pages/k_login.vue')
    },
    {
      path: '/home',
      name: 'MainLayout',
      component: () => import('@/layouts/main.vue'),
      children: pages

    }
  ]
})
