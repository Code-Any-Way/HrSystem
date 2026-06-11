<template>
  <div class="space-y-8">
    <section class="rounded-[2rem] bg-slate-900 px-6 py-8 text-white shadow-2xl shadow-slate-900/20">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <p class="text-sm uppercase tracking-[0.3em] text-sky-300">{{ t('controlPanel') }}</p>
          <h1 class="mt-3 text-4xl font-semibold">{{ auth.roleLabel }}</h1>
        </div>
        <div class="rounded-full bg-slate-800 px-4 py-3 text-sm text-slate-300">{{ roleDescription }}</div>
      </div>
      <p class="mt-6 max-w-2xl text-slate-300">{{ t('mainDescription') }}</p>
    </section>

    <section class="grid gap-5 sm:grid-cols-2 xl:grid-cols-3">
      <div class="rounded-3xl bg-slate-50 p-6 shadow-sm border border-slate-200 dark:bg-slate-950 dark:border-slate-700">
        <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100">{{ auth.t('roleManagement') }}</h2>
        <p class="mt-3 text-sm text-slate-500 dark:text-slate-300">{{ roleDescription }}</p>
      </div>
      <div class="rounded-3xl bg-slate-50 p-6 shadow-sm border border-slate-200 dark:bg-slate-950 dark:border-slate-700">
        <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100">{{ auth.t('dashboardSummaryLabel') }}</h2>
        <p class="mt-3 text-sm text-slate-500 dark:text-slate-300">{{ t('dashboardSummarySubtitle') }}</p>
      </div>
      <div class="rounded-3xl bg-slate-50 p-6 shadow-sm border border-slate-200 dark:bg-slate-950 dark:border-slate-700">
        <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100">{{ auth.t('dashboardTeamPulseTitle') }}</h2>
        <p class="mt-3 text-sm text-slate-500 dark:text-slate-300">{{ t('dashboardPulseSubtitle') }}</p>
      </div>
    </section>

    <section class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <div v-for="feature in roleFeatures" :key="feature.title" class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200 dark:bg-slate-950 dark:border-slate-700">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">{{ feature.title }}</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900 dark:text-slate-100">{{ feature.value }}</p>
        <p class="mt-2 text-sm text-slate-500 dark:text-slate-300">{{ feature.description }}</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import SectionCard from '../components/SectionCard.vue'
import { computed } from 'vue'
import { useAuthStore } from '../store'

const auth = useAuthStore()

const roleDescription = computed(() => {
  if (auth.isSuperAdmin) return auth.t('rolePanelDescriptionSuperAdmin')
  if (auth.isManager) return auth.t('rolePanelDescriptionManager')
  if (auth.isHR) return auth.t('rolePanelDescriptionHR')
  return auth.t('rolePanelDescriptionEmployee')
})

const roleFeatures = computed(() => {
  if (auth.isSuperAdmin) {
    return [
      { title: auth.t('roleCardEmployees'), value: '324', description: auth.t('dashboardEmployeesText') },
      { title: auth.t('roleCardAttendance'), value: '98.4%', description: auth.t('dashboardAttendanceText') },
      { title: auth.t('roleCardPending'), value: '12', description: auth.t('dashboardPendingLeavesText') },
      { title: auth.t('roleCardPayroll'), value: '3', description: auth.t('dashboardPayrollRunsText') }
    ]
  }

  if (auth.isManager) {
    return [
      { title: auth.t('roleCardEmployees'), value: '54', description: auth.t('dashboardEmployeesText') },
      { title: auth.t('roleCardPending'), value: '8', description: auth.t('dashboardPendingLeavesText') },
      { title: auth.t('roleCardAttendance'), value: '96.2%', description: auth.t('dashboardAttendanceText') },
      { title: auth.t('roleCardPayroll'), value: '2', description: auth.t('dashboardPayrollRunsText') }
    ]
  }

  if (auth.isHR) {
    return [
      { title: auth.t('roleCardEmployees'), value: '86', description: auth.t('dashboardEmployeesText') },
      { title: auth.t('roleCardAttendance'), value: '97.8%', description: auth.t('dashboardAttendanceText') },
      { title: auth.t('roleCardLeaveBalance'), value: '14', description: auth.t('dashboardPendingLeavesText') },
      { title: auth.t('roleCardPayroll'), value: '5', description: auth.t('dashboardPayrollRunsText') }
    ]
  }

  return [
    { title: auth.t('roleCardAttendance'), value: '98.4%', description: auth.t('dashboardAttendanceText') },
    { title: auth.t('roleCardLeaveBalance'), value: '10', description: auth.t('dashboardPendingLeavesText') },
    { title: auth.t('roleCardPayroll'), value: '3', description: auth.t('dashboardPayrollRunsText') },
    { title: auth.t('roleCardAssets'), value: '4', description: auth.t('sectionAssetsText') }
  ]
})

const t = (key: string) => auth.t(key as any)
</script>
