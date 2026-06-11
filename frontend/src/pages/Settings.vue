<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] bg-white p-8 shadow-lg shadow-slate-200 dark:bg-slate-900 dark:shadow-slate-800">
      <h1 class="text-3xl font-semibold text-slate-900 dark:text-slate-100">{{ t('settingsTitle') }}</h1>
      <p class="mt-3 max-w-2xl text-slate-500 dark:text-slate-300">{{ t('settingsSystemText') }}</p>
    </div>

    <div class="grid gap-4 lg:grid-cols-2">
      <section class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-700 dark:bg-slate-900">
        <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100">{{ t('settingsProfile') }}</h2>
        <p class="mt-2 text-sm text-slate-500 dark:text-slate-300">{{ t('settingsProfileText') }}</p>
        <div class="mt-5 space-y-4">
          <button class="w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-left text-sm text-slate-700 hover:bg-slate-100 dark:border-slate-700 dark:bg-slate-950 dark:text-slate-200 dark:hover:bg-slate-800">{{ t('editProfile') }}</button>
          <button class="w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-left text-sm text-slate-700 hover:bg-slate-100 dark:border-slate-700 dark:bg-slate-950 dark:text-slate-200 dark:hover:bg-slate-800">{{ t('changePassword') }}</button>
        </div>
      </section>

      <section class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-700 dark:bg-slate-900">
        <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100">{{ t('settingsSystem') }}</h2>
        <p class="mt-2 text-sm text-slate-500 dark:text-slate-300">{{ t('settingsSystemText') }}</p>
        <div class="mt-5 space-y-4">
          <div class="rounded-3xl bg-slate-50 p-4 dark:bg-slate-950">
            <div class="flex items-center justify-between gap-4">
              <div>
                <p class="text-sm font-semibold text-slate-900 dark:text-slate-100">{{ t('language') }}</p>
                <p class="mt-1 text-sm text-slate-500 dark:text-slate-300">{{ locale === 'en' ? 'English' : 'العربية' }}</p>
              </div>
              <select v-model="locale" @change="updateLocale" class="rounded-2xl border border-slate-300 bg-white px-4 py-2 text-sm text-slate-900 outline-none dark:border-slate-700 dark:bg-slate-950 dark:text-slate-100">
                <option value="en">English</option>
                <option value="ar">العربية</option>
              </select>
            </div>
          </div>
          <div class="rounded-3xl bg-slate-50 p-4 dark:bg-slate-950">
            <div class="flex items-center justify-between gap-4">
              <div>
                <p class="text-sm font-semibold text-slate-900 dark:text-slate-100">{{ themeLabel }}</p>
                <p class="mt-1 text-sm text-slate-500 dark:text-slate-300">{{ themeDescription }}</p>
              </div>
              <button @click="toggleTheme" class="rounded-full bg-slate-900 px-4 py-2 text-sm font-semibold text-white transition hover:bg-slate-800">{{ themeAction }}</button>
            </div>
          </div>
        </div>
      </section>
    </div>

    <section class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-700 dark:bg-slate-900">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 class="text-xl font-semibold text-slate-900 dark:text-slate-100">{{ t('roleManagement') }}</h2>
          <p class="mt-2 text-sm text-slate-500 dark:text-slate-300">{{ t('roleManagementText') }}</p>
        </div>
        <button @click="addRoleHandler" class="rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">{{ t('addRole') }}</button>
      </div>

      <div class="mt-6 grid gap-4 sm:grid-cols-2">
        <div class="rounded-3xl bg-slate-50 p-5 dark:bg-slate-950">
          <label class="block text-sm font-semibold text-slate-900 dark:text-slate-100">{{ t('roleNameEn') }}</label>
          <input v-model="newRoleEn" class="mt-2 w-full rounded-2xl border border-slate-300 bg-white px-4 py-3 text-sm text-slate-900 outline-none dark:border-slate-700 dark:bg-slate-950 dark:text-slate-100" />
        </div>
        <div class="rounded-3xl bg-slate-50 p-5 dark:bg-slate-950">
          <label class="block text-sm font-semibold text-slate-900 dark:text-slate-100">{{ t('roleNameAr') }}</label>
          <input v-model="newRoleAr" class="mt-2 w-full rounded-2xl border border-slate-300 bg-white px-4 py-3 text-sm text-slate-900 outline-none dark:border-slate-700 dark:bg-slate-950 dark:text-slate-100" />
        </div>
      </div>

      <div class="mt-6 space-y-4">
        <div v-if="!roles.length" class="rounded-3xl border border-dashed border-slate-300 bg-slate-50 p-6 text-sm text-slate-500 dark:border-slate-700 dark:bg-slate-950 dark:text-slate-300">{{ t('noRoles') }}</div>
        <div v-for="role in roles" :key="role.id" class="rounded-3xl bg-slate-50 p-5 dark:bg-slate-950">
          <div class="flex items-center justify-between gap-4">
            <div>
              <p class="text-lg font-semibold text-slate-900 dark:text-slate-100">{{ locale === 'en' ? role.name.en : role.name.ar }}</p>
              <p class="mt-1 text-sm text-slate-500 dark:text-slate-300">{{ t('role') }} • {{ role.id }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useAuthStore } from '../store'

const auth = useAuthStore()
const locale = computed({
  get: () => auth.locale,
  set: (value: 'en' | 'ar') => auth.setLocale(value),
})

const roles = computed(() => auth.roles)
const newRoleEn = ref('')
const newRoleAr = ref('')

const themeLabel = computed(() => auth.theme === 'dark' ? auth.t('themeDark') : auth.t('themeLight'))
const themeDescription = computed(() => auth.theme === 'dark' ? auth.t('themeDark') : auth.t('themeLight'))
const themeAction = computed(() => auth.theme === 'dark' ? auth.t('themeLight') : auth.t('themeDark'))

function toggleTheme() {
  auth.toggleTheme()
}

function updateLocale() {
  auth.setLocale(locale.value)
}

function addRoleHandler() {
  if (!newRoleEn.value.trim() || !newRoleAr.value.trim()) {
    return
  }
  auth.addRole(newRoleEn.value.trim(), newRoleAr.value.trim())
  newRoleEn.value = ''
  newRoleAr.value = ''
}

const t = (key: string) => auth.t(key as any)
</script>
