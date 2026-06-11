import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../store'
import AdminLayout from '../layouts/AdminLayout.vue'
import AuthLayout from '../layouts/AuthLayout.vue'
import HomePage from '../pages/HomePage.vue'
import Dashboard from '../pages/Dashboard.vue'
import Employees from '../pages/Employees.vue'
import MainInterface from '../pages/MainInterface.vue'
import Assets from '../pages/Assets.vue'
import Attendance from '../pages/Attendance.vue'
import Evaluations from '../pages/Evaluations.vue'
import Expenses from '../pages/Expenses.vue'
import Leaves from '../pages/Leaves.vue'
import Payroll from '../pages/Payroll.vue'
import Settings from '../pages/Settings.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/app',
    component: AdminLayout,
    children: [
      { path: '', name: 'main-interface', component: MainInterface },
      { path: 'dashboard', name: 'dashboard', component: Dashboard },
      { path: 'employees', name: 'employees', component: Employees },
      { path: 'attendance', name: 'attendance', component: Attendance },
      { path: 'leaves', name: 'leaves', component: Leaves },
      { path: 'payroll', name: 'payroll', component: Payroll },
      { path: 'assets', name: 'assets', component: Assets },
      { path: 'expenses', name: 'expenses', component: Expenses },
      { path: 'evaluations', name: 'evaluations', component: Evaluations },
      { path: 'settings', name: 'settings', component: Settings }
    ]
  },
  {
    path: '/auth',
    component: AuthLayout,
    children: [
      { path: 'login', name: 'login', component: () => import('../pages/auth/Login.vue') }
    ]
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/' 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  const isAuthRoute = to.path.startsWith('/auth')
  const isPublicPage = to.name === 'home'

  if (!auth.isAuthenticated && !isAuthRoute && !isPublicPage) {
    return next({ name: 'login' })
  }

  if (auth.isAuthenticated && isAuthRoute) {
    return next({ name: 'main-interface' })
  }

  return next()
})

export default router
