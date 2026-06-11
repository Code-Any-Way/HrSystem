<template>
  <div class="bg-white p-6 rounded-3xl shadow-lg shadow-slate-200 dark:bg-slate-950 dark:shadow-slate-900">
    <h2 class="text-2xl font-semibold mb-6 text-slate-900 dark:text-slate-100">{{ t('loginTitle') }}</h2>
    <form @submit.prevent="loginHandler" class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300">{{ t('loginEmailLabel') }}</label>
        <input v-model="email" :placeholder="t('loginEmailPlaceholder')" class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100" />
      </div>
      <div>
        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300">{{ t('loginPasswordLabel') }}</label>
        <input v-model="password" type="password" :placeholder="t('loginPasswordPlaceholder')" class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 outline-none dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100" />
      </div>
      <button type="submit" class="w-full rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">{{ t('loginButton') }}</button>
    </form>
    <p v-if="error" class="mt-4 text-sm text-rose-600">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../store'

const router = useRouter()
const auth = useAuthStore()
const email = ref('')
const password = ref('')
const error = ref('')

const t = (key: string) => auth.t(key as any)

async function loginHandler() {
  try {
    error.value = ''
    await auth.login(email.value, password.value)
    router.push({ name: 'dashboard' })
  } catch (err) {
    error.value = t('loginError')
  }
}
</script>
