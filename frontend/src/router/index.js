import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import(/* webpackChunkName: "profile" */ '../views/Profile.vue'),
    meta: { 
      requiresAuth: true
    }
  },
  {
    path: '/lines',
    name: 'Lines',
    component: () => import(/* webpackChunkName: "lines" */ '../views/Lines.vue'),
    props: true,
    meta: { 
      requiresAuth: true
    }
  },
  {
    path: '/calls',
    name: 'Calls',
    component: () => import(/* webpackChunkName: "calls" */ '../views/Calls.vue'),
    props: true,
    meta: { 
      requiresAuth: true
    }
  },
  {
    path: '/payment_accounts',
    name: 'PaymentAccounts',
    component: () => import(/* webpackChunkName: "payment_accounts" */ '../views/PaymentAccounts.vue'),
    props: true,
    meta: { 
      requiresAuth: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
