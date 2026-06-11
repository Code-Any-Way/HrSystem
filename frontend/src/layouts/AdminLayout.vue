<template>
  <div class="min-h-screen bg-slate-50 text-slate-900">
    <div class="flex min-h-screen">
      <aside class="hidden w-72 flex-col bg-slate-900 text-slate-100 md:flex">
        <div class="px-6 py-8 border-b border-slate-700">
          <div class="text-2xl font-semibold">HRMS</div>
          <p class="text-sm text-slate-400 mt-1">Unified admin workspace</p>
        </div>

        <nav class="flex-1 px-4 py-6 space-y-2">
          <router-link
            v-for="item in menuItems"
            :key="item.name"
            :to="{ name: item.name }"
            class="group flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium transition hover:bg-slate-800"
            :class="{ 'bg-slate-800 text-white': routeName === item.name, 'text-slate-300': routeName !== item.name }"
          >
            <span v-html="item.icon" class="w-5 h-5"></span>
            <span>{{ item.label }}</span>
          </router-link>
        </nav>
      </aside>

      <div class="flex-1">
        <header class="sticky top-0 z-20 border-b border-slate-200 bg-white/95 backdrop-blur-sm px-4 py-4 shadow-sm md:px-8">
          <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
            <div>
              <p class="text-sm uppercase tracking-[0.24em] text-slate-500">{{ auth.t('adminHeaderSubtitle') }}</p>
              <h1 class="text-2xl font-semibold text-slate-900">{{ auth.t('adminHeaderTitle') }}</h1>
            </div>
            <div class="flex flex-col gap-3 sm:flex-row sm:items-center">
              <button class="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-700 shadow-sm transition hover:bg-slate-50">
                <span class="text-sky-500">●</span>
                {{ auth.t('dashboardLiveTag') }}
              </button>
              <div class="rounded-full bg-slate-100 px-4 py-2 text-sm text-slate-700">{{ auth.t('adminStatusBadge') }}</div>
              <button @click="handleLogout" class="rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-700 shadow-sm transition hover:bg-slate-50">
                {{ auth.t('navLogout') }}
              </button>
            </div>
          </div>
        </header>

        <main class="px-4 py-6 md:px-8">
          <router-view />
        </main>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../store'

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()
const routeName = computed(() => route.name as string)

const menuItems = computed(() => {
  const allItems = [
    { name: 'main-interface', label: auth.t('navHome'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9.75L12 3l9 6.75V21a.75.75 0 01-.75.75H3.75A.75.75 0 013 21V9.75z"/></svg>' },
    { name: 'dashboard', label: auth.t('navDashboard'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M4.5 12a7.5 7.5 0 1115 0v5.25a2.25 2.25 0 01-2.25 2.25H6.75A2.25 2.25 0 014.5 17.25V12z"/></svg>' },
    { name: 'employees', label: auth.t('navEmployees'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 12a4 4 0 100-8 4 4 0 000 8z"/><path fill-rule="evenodd" d="M4.5 18a7.5 7.5 0 0115 0v.75A2.25 2.25 0 0117.25 21h-10.5A2.25 2.25 0 014.5 18.75V18z" clip-rule="evenodd"/></svg>' },
    { name: 'attendance', label: auth.t('navAttendance'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 7a1 1 0 011 1v3.58l2.29 1.36a1 1 0 11-1 1.72L12 12.15V8a1 1 0 011-1z"/><path fill-rule="evenodd" d="M2.25 11.25A9.75 9.75 0 0112 1.5a9.75 9.75 0 019.75 9.75 9.75 9.75 0 01-9.75 9.75A9.75 9.75 0 012.25 11.25zm9.75-8.25a8.25 8.25 0 100 16.5 8.25 8.25 0 000-16.5z" clip-rule="evenodd"/></svg>' },
    { name: 'leaves', label: auth.t('navLeaves'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M4.5 12a7.5 7.5 0 0113.5-5.916A6 6 0 0012 18a6 6 0 01-7.5-6z"/></svg>' },
    { name: 'payroll', label: auth.t('navPayroll'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3.75c-4.127 0-7.5 3.373-7.5 7.5 0 3.715 2.624 6.807 6 7.33v1.92a.75.75 0 001.5 0v-1.92c3.376-.523 6-3.615 6-7.33 0-4.127-3.373-7.5-7.5-7.5zm0 1.5a6 6 0 016 6 6 6 0 01-6 6 6 6 0 01-6-6 6 6 0 016-6z"/></svg>' },
    { name: 'assets', label: auth.t('navAssets'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M4.5 5.25A2.25 2.25 0 016.75 3h10.5A2.25 2.25 0 0119.5 5.25v13.5A2.25 2.25 0 0117.25 21H6.75A2.25 2.25 0 014.5 18.75V5.25z"/><path d="M8.25 7.5h7.5v1.5h-7.5V7.5z"/></svg>' },
    { name: 'expenses', label: auth.t('navExpenses'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M6 3.75A2.25 2.25 0 018.25 1.5h7.5A2.25 2.25 0 0118 3.75v16.5A2.25 2.25 0 0115.75 22.5H8.25A2.25 2.25 0 016 20.25V3.75zm2.25 2.25v2.25h7.5V6H8.25zm0 4.5v2.25h7.5V10.5h-7.5z"/></svg>' },
    { name: 'evaluations', label: auth.t('navEvaluations'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.25a8.25 8.25 0 018.25 8.25 8.25 8.25 0 01-8.25 8.25 8.25 8.25 0 01-8.25-8.25 8.25 8.25 0 018.25-8.25zm0 1.5a6.75 6.75 0 100 13.5 6.75 6.75 0 000-13.5z"/><path d="M12.75 7.5h-1.5v5.25l4.125 2.475.75-1.23-3.375-2.025V7.5z"/></svg>' },
    { name: 'settings', label: auth.t('navSettings'), icon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 8.25a3.75 3.75 0 100 7.5 3.75 3.75 0 000-7.5zm0 1.5a2.25 2.25 0 110 4.5 2.25 2.25 0 010-4.5z"/><path d="M12 1.5a1.5 1.5 0 011.48 1.3l.06.2a7.04 7.04 0 011.183.28l.16-.16a1.5 1.5 0 012.12 0l.72.72a1.5 1.5 0 010 2.12l-.16.16c.107.263.197.536.28.815l.2.06A1.5 1.5 0 0122.5 9.75v1.5a1.5 1.5 0 01-1.3 1.48l-.2.06a7.04 7.04 0 01-.28.815l.16.16a1.5 1.5 0 010 2.12l-.72.72a1.5 1.5 0 01-2.12 0l-.16-.16a7.04 7.04 0 01-.815.28l-.06.2A1.5 1.5 0 0113.5 22.5h-1.5a1.5 1.5 0 01-1.48-1.3l-.06-.2a7.04 7.04 0 01-1.183-.28l-.16.16a1.5 1.5 0 01-2.12 0l-.72-.72a1.5 1.5 0 010-2.12l.16-.16a7.04 7.04 0 01-.28-.815l-.2-.06A1.5 1.5 0 011.5 11.25v-1.5a1.5 1.5 0 011.3-1.48l.2-.06a7.04 7.04 0 01.28-.815l-.16-.16a1.5 1.5 0 010-2.12l.72-.72a1.5 1.5 0 012.12 0l.16.16c.263-.107.536-.197.815-.28l.06-.2A1.5 1.5 0 0110.5 1.5h1.5z"/></svg>' }
  ]

  if (auth.isSuperAdmin) {
    return allItems
  }

  if (auth.isHR) {
    return allItems.filter((item) => ['main-interface', 'dashboard', 'employees', 'attendance', 'leaves', 'payroll', 'settings'].includes(item.name))
  }

  if (auth.isManager) {
    return allItems.filter((item) => ['main-interface', 'dashboard', 'employees', 'attendance', 'leaves', 'settings'].includes(item.name))
  }

  if (auth.isEmployee) {
    return allItems.filter((item) => ['main-interface', 'attendance', 'leaves', 'payroll', 'settings'].includes(item.name))
  }

  return allItems
})

function handleLogout() {
  auth.logout()
  router.push({ name: 'login' })
}
</script>
