<template>
  <div class="space-y-6">
    <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
      <div>
        <p class="text-sm uppercase tracking-[0.32em] text-sky-500">People</p>
        <h1 class="mt-3 text-3xl font-semibold text-slate-900">Employee roster</h1>
      </div>
      <button @click="reloadList" class="inline-flex items-center justify-center rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">Refresh list</button>
    </div>

    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Total staff</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">{{ employees.length }}</p>
        <p class="mt-2 text-sm text-slate-500">Active employees loaded.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Departments</p>
        <p class="mt-4 text-4xl font-semibold text-sky-600">5</p>
        <p class="mt-2 text-sm text-slate-500">Recorded departments in the company.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Recent hire</p>
        <p class="mt-4 text-4xl font-semibold text-emerald-600">3</p>
        <p class="mt-2 text-sm text-slate-500">New employees this month.</p>
      </div>
    </div>

    <div class="overflow-hidden rounded-[2rem] border border-slate-200 bg-white shadow-lg">
      <div class="p-6">
        <div class="flex flex-col gap-3 md:flex-row md:justify-between md:items-center">
          <div>
            <h2 class="text-xl font-semibold text-slate-900">Employee records</h2>
            <p class="mt-1 text-sm text-slate-500">Review current staff details and branch assignments.</p>
          </div>
          <div class="rounded-full bg-slate-100 px-4 py-2 text-sm text-slate-600">Updated just now</div>
        </div>
      </div>
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-slate-200">
          <thead class="bg-slate-50">
            <tr>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-[0.18em] text-slate-500">Code</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-[0.18em] text-slate-500">Name</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-[0.18em] text-slate-500">Email</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-[0.18em] text-slate-500">Job</th>
              <th class="px-6 py-4 text-left text-xs font-semibold uppercase tracking-[0.18em] text-slate-500">Branch</th>
            </tr>
          </thead>

          <tbody class="divide-y divide-slate-200 bg-white">
            <tr v-for="employee in employees" :key="employee.id" class="hover:bg-slate-50">
              <td class="px-6 py-4 text-sm text-slate-700">{{ employee.employee_code }}</td>
              <td class="px-6 py-4 text-sm text-slate-700">{{ employee.first_name }} {{ employee.last_name }}</td>
              <td class="px-6 py-4 text-sm text-slate-700">{{ employee.email }}</td>
              <td class="px-6 py-4 text-sm text-slate-700">{{ employee.job_title }}</td>
              <td class="px-6 py-4 text-sm text-slate-700">{{ employee.branch_name }}</td>
            </tr>

            <tr v-if="!employees.length">
              <td colspan="5" class="px-6 py-8 text-center text-slate-500">No employees found yet.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-if="error" class="rounded-3xl border border-rose-200 bg-rose-50 px-6 py-4 text-rose-700">
      {{ error }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '../services/api'

const employees = ref<any[]>([])
const loading = ref(false)
const error = ref('')

async function loadEmployees() {
  loading.value = true
  error.value = ''
  try {
    const response = await api.get('/employees/')
    employees.value = response.data.results || response.data
  } catch (err) {
    error.value = 'Failed to load employees.'
  } finally {
    loading.value = false
  }
}

function reloadList() {
  loadEmployees()
}

onMounted(loadEmployees)
</script>
