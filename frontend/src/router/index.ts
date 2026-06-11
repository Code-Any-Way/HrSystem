import { createRouter, createWebHistory } from 'vue-router'
import AdminLayout from '../layouts/AdminLayout.vue'
import AuthLayout from '../layouts/AuthLayout.vue'
import Dashboard from '../pages/Dashboard.vue'
import Employees from '../pages/Employees.vue'

const routes = [
  {
    path: '/',
    component: AdminLayout,
    children: [
      { path: '', name: 'dashboard', component: Dashboard },
      { path: 'employees', name: 'employees', component: Employees }
    ]
  },
  {
    path: '/auth',
    component: AuthLayout,
    children: [
      { path: 'login', name: 'login', component: () => import('../pages/auth/Login.vue') }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
