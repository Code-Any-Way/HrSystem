<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] bg-white p-8 shadow-lg shadow-slate-200">
      <div class="flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
        <div>
          <p class="text-sm uppercase tracking-[0.32em] text-sky-500">Executive Summary</p>
          <h1 class="mt-3 text-3xl font-semibold text-slate-900">Operational health at a glance</h1>
        </div>
        <button class="inline-flex items-center justify-center rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white shadow-sm transition hover:bg-slate-800">Refresh overview</button>
      </div>
      <p class="mt-4 max-w-2xl text-slate-500">Track recent activity, approvals pending, and department performance across your HR ecosystem.</p>
    </div>

    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Employees</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">264</p>
        <p class="mt-2 text-sm text-slate-500">Active staff across all branches.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Attendance</p>
        <p class="mt-4 text-4xl font-semibold text-sky-600">98.4%</p>
        <p class="mt-2 text-sm text-slate-500">This week’s on-time check-ins.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Pending leaves</p>
        <p class="mt-4 text-4xl font-semibold text-amber-600">12</p>
        <p class="mt-2 text-sm text-slate-500">Awaiting manager approval.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Payroll runs</p>
        <p class="mt-4 text-4xl font-semibold text-emerald-600">3</p>
        <p class="mt-2 text-sm text-slate-500">Payments queued for processing.</p>
      </div>
    </div>

    <div class="grid gap-4 xl:grid-cols-[1.2fr_0.8fr]">
      <div class="rounded-[2rem] bg-white p-6 shadow-sm border border-slate-200">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-xl font-semibold text-slate-900">Recent approvals</h2>
            <p class="mt-2 text-sm text-slate-500">Latest leave requests, expense approvals, and asset assignments.</p>
          </div>
          <span class="rounded-full bg-slate-100 px-3 py-1 text-xs uppercase tracking-[0.24em] text-slate-600">Live</span>
        </div>
        <div class="mt-6 space-y-4">
          <div class="rounded-3xl bg-slate-50 p-4">
            <p class="font-semibold text-slate-900">Leave request</p>
            <p class="mt-1 text-sm text-slate-500">Carlos Mendoza | 2 days | Pending manager approval</p>
          </div>
          <div class="rounded-3xl bg-slate-50 p-4">
            <p class="font-semibold text-slate-900">Expense claim</p>
            <p class="mt-1 text-sm text-slate-500">Marketing team | $1,280 | Waiting finance review</p>
          </div>
          <div class="rounded-3xl bg-slate-50 p-4">
            <p class="font-semibold text-slate-900">Asset return</p>
            <p class="mt-1 text-sm text-slate-500">Laptop | Pending IT confirmation</p>
          </div>
        </div>
      </div>

      <div class="rounded-[2rem] bg-sky-700/5 p-6 shadow-sm border border-sky-100">
        <h2 class="text-xl font-semibold text-slate-900">Team pulse</h2>
        <p class="mt-3 text-sm text-slate-600">Keep track of employee engagement, approval times, and payroll readiness.</p>
        <div class="mt-6 space-y-4">
          <div class="rounded-3xl bg-white p-4 border border-slate-200">
            <p class="text-sm text-slate-500">Average response time</p>
            <p class="mt-2 text-2xl font-semibold text-slate-900">1.8 days</p>
          </div>
          <div class="rounded-3xl bg-white p-4 border border-slate-200">
            <p class="text-sm text-slate-500">Pending HR tasks</p>
            <p class="mt-2 text-2xl font-semibold text-slate-900">19</p>
          </div>
        </div>
      </div>
    </div>

    <div class="grid gap-4 xl:grid-cols-2">
      <div class="rounded-[2rem] bg-white p-6 shadow-sm border border-slate-200">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-xl font-semibold text-slate-900">{{ t('dashboardAttendanceAnalytics') }}</h2>
            <p class="mt-2 text-sm text-slate-500">{{ t('dashboardAttendanceAnalyticsText') }}</p>
          </div>
          <span class="rounded-full bg-slate-100 px-3 py-1 text-xs uppercase tracking-[0.24em] text-slate-600">{{ t('dashboardLiveTag') }}</span>
        </div>
        <div class="mt-6 h-[320px]">
          <canvas ref="attendanceCanvas" aria-label="Attendance trend chart"></canvas>
        </div>
      </div>

      <div class="rounded-[2rem] bg-white p-6 shadow-sm border border-slate-200">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-xl font-semibold text-slate-900">{{ t('dashboardDepartmentPerformance') }}</h2>
            <p class="mt-2 text-sm text-slate-500">{{ t('dashboardDepartmentPerformanceText') }}</p>
          </div>
          <span class="rounded-full bg-slate-100 px-3 py-1 text-xs uppercase tracking-[0.24em] text-slate-600">{{ t('dashboardInsightTag') }}</span>
        </div>
        <div class="mt-6 h-[320px]">
          <canvas ref="departmentCanvas" aria-label="Department share chart"></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useAuthStore } from '../store'
import {
  Chart,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  ArcElement,
  Tooltip,
  Legend,
  Title,
} from 'chart.js'

const auth = useAuthStore()
const t = (key: string) => auth.t(key as any)

Chart.register(CategoryScale, LinearScale, PointElement, LineElement, ArcElement, Tooltip, Legend, Title)

const attendanceCanvas = ref<HTMLCanvasElement | null>(null)
const departmentCanvas = ref<HTMLCanvasElement | null>(null)
let attendanceChart: Chart<'line'> | null = null
let departmentChart: Chart<'doughnut'> | null = null

onMounted(() => {
  if (attendanceCanvas.value) {
    attendanceChart = new Chart(attendanceCanvas.value, {
      type: 'line',
      data: {
        labels: auth.locale === 'ar' ? ['الاثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت', 'الأحد'] : ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [
          {
            label: t('attendanceSeriesLabel'),
            data: [94, 96, 97, 98, 98.4, 97.5, 98.1],
            borderColor: '#0ea5e9',
            backgroundColor: 'rgba(14,165,233,0.2)',
            fill: true,
            tension: 0.35,
            pointRadius: 4,
            pointBackgroundColor: '#0ea5e9',
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          title: {
            display: true,
            text: t('attendanceTrendTitle'),
            color: '#334155',
            font: { size: 14 },
          },
        },
        scales: {
          x: {
            ticks: { color: '#64748b' },
            grid: { display: false },
          },
          y: {
            beginAtZero: true,
            max: 100,
            ticks: { color: '#64748b' },
            grid: { color: 'rgba(148,163,184,0.2)' },
          },
        },
      },
    })
  }

  if (departmentCanvas.value) {
    departmentChart = new Chart(departmentCanvas.value, {
      type: 'doughnut',
      data: {
        labels: auth.locale === 'ar' ? ['الموارد البشرية', 'المبيعات', 'الهندسة', 'العمليات'] : ['HR', 'Sales', 'Engineering', 'Operations'],
        datasets: [
          {
            data: [18, 28, 35, 19],
            backgroundColor: ['#0ea5e9', '#38bdf8', '#7dd3fc', '#93c5fd'],
            borderWidth: 0,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { color: '#475569' },
          },
          title: {
            display: true,
            text: t('departmentChartTitle'),
            color: '#334155',
            font: { size: 14 },
          },
        },
      },
    })
  }
})

onBeforeUnmount(() => {
  attendanceChart?.destroy()
  departmentChart?.destroy()
})
</script>
