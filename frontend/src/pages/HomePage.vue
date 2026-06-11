<template>
  <div class="min-h-screen bg-slate-50 text-slate-900 dark:bg-slate-950 dark:text-slate-100">
    <div class="mx-auto flex min-h-screen max-w-7xl flex-col justify-center px-4 py-16 sm:px-6 lg:px-8">
      <div class="grid gap-12 lg:grid-cols-[1.05fr_0.95fr] lg:items-center">
        <div class="space-y-8">
          <span class="inline-flex items-center rounded-full bg-sky-100 px-4 py-1 text-sm font-semibold text-sky-700 dark:bg-sky-900/20 dark:text-sky-300">{{ t('overviewLabel') }}</span>
          <div class="space-y-4">
            <h1 class="text-4xl font-semibold tracking-tight text-slate-900 dark:text-slate-100 sm:text-5xl">{{ t('homepageHeadline') }}</h1>
            <p class="max-w-2xl text-lg text-slate-600 dark:text-slate-300">{{ t('homepageSubtitle') }}</p>
          </div>
          <div class="flex flex-col gap-3 sm:flex-row">
            <router-link :to="{ name: 'login' }" class="inline-flex items-center justify-center rounded-full bg-slate-900 px-6 py-3 text-base font-semibold text-white transition hover:bg-slate-800">{{ t('homepageButton') }}</router-link>
            <router-link :to="{ name: 'main-interface' }" class="inline-flex items-center justify-center rounded-full border border-slate-200 bg-white px-6 py-3 text-base font-semibold text-slate-900 transition hover:bg-slate-100 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100 dark:hover:bg-slate-800">{{ t('navDashboard') }}</router-link>
          </div>
        </div>

        <div class="grid gap-4 sm:grid-cols-2">
          <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-700 dark:bg-slate-900">
            <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100">{{ t('featureOne') }}</h2>
            <p class="mt-3 text-sm text-slate-500 dark:text-slate-300">{{ t('companyMission') }}</p>
          </div>
          <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-700 dark:bg-slate-900">
            <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100">{{ t('featureTwo') }}</h2>
            <p class="mt-3 text-sm text-slate-500 dark:text-slate-300">{{ t('featureTwo') }}</p>
          </div>
          <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-700 dark:bg-slate-900">
            <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100">{{ t('featureThree') }}</h2>
            <p class="mt-3 text-sm text-slate-500 dark:text-slate-300">{{ t('featureThree') }}</p>
          </div>
          <div class="rounded-[2rem] border border-slate-200 bg-sky-50 p-6 shadow-sm dark:border-slate-700 dark:bg-slate-800">
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white">{{ t('navSettings') }}</h2>
            <p class="mt-3 text-sm text-slate-500 dark:text-slate-300">{{ t('roleManagementText') }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '../store'

const auth = useAuthStore()
const t = (key: string) => auth.t(key as any)
</script>
