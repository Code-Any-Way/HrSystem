<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-950 text-slate-100">
    <div class="mx-auto flex min-h-screen max-w-5xl items-center justify-center px-4 py-12 sm:px-6 lg:px-8">
      <div class="grid w-full gap-10 rounded-[2rem] bg-white/10 p-6 shadow-xl shadow-slate-900/20 backdrop-blur-xl sm:p-10 lg:grid-cols-[1.4fr_1fr]">
        <div class="space-y-6 text-slate-100">
          <div>
            <p class="text-sm uppercase tracking-[0.32em] text-sky-300">{{ t('loginTitle') }}</p>
            <h1 class="mt-4 text-4xl font-semibold">{{ t('loginTitle') }}</h1>
          </div>
          <p class="text-slate-300">{{ t('loginSubtitle') }}</p>
          <div class="grid gap-4 sm:grid-cols-2">
            <div class="rounded-3xl bg-slate-900/70 px-4 py-5 shadow-lg shadow-slate-900/20">
              <p class="text-sm text-slate-400">{{ t('featureOne') }}</p>
              <p class="mt-2 text-lg font-semibold">{{ t('featureOne') }}</p>
            </div>
            <div class="rounded-3xl bg-slate-900/70 px-4 py-5 shadow-lg shadow-slate-900/20">
              <p class="text-sm text-slate-400">{{ t('featureTwo') }}</p>
              <p class="mt-2 text-lg font-semibold">{{ t('featureThree') }}</p>
            </div>
          </div>
        </div>

        <div class="rounded-3xl bg-white p-8 shadow-2xl shadow-slate-900/10">
          <router-view />
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
