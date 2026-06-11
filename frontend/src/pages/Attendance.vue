<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] bg-white p-8 shadow-lg shadow-slate-200">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <p class="text-sm uppercase tracking-[0.32em] text-sky-500">Attendance</p>
          <h1 class="mt-3 text-3xl font-semibold text-slate-900">Daily presence and check-in analytics</h1>
        </div>
        <button class="inline-flex items-center justify-center rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">Sync attendance</button>
      </div>
      <p class="mt-4 max-w-2xl text-slate-500">Monitor real-time attendance, GPS check-in trends, and employee presence in one easy view.</p>
    </div>

    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Today present</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">211</p>
        <p class="mt-2 text-sm text-slate-500">Employees checked in so far.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Late arrivals</p>
        <p class="mt-4 text-4xl font-semibold text-amber-600">8</p>
        <p class="mt-2 text-sm text-slate-500">Late check-ins recorded today.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Absent</p>
        <p class="mt-4 text-4xl font-semibold text-rose-600">14</p>
        <p class="mt-2 text-sm text-slate-500">Employees marked absent.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">GPS checks</p>
        <p class="mt-4 text-4xl font-semibold text-sky-600">96%</p>
        <p class="mt-2 text-sm text-slate-500">Verified location-based check-ins.</p>
      </div>
    </div>

    <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 class="text-xl font-semibold text-slate-900">Attendance highlights</h2>
          <p class="mt-2 text-sm text-slate-500">Recent events and status updates from today’s attendance data.</p>
        </div>
        <span class="rounded-full bg-slate-100 px-4 py-2 text-sm text-slate-600">Updated moments ago</span>
      </div>
      <div class="mt-6 grid gap-4 sm:grid-cols-2">
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Morning rush</p>
          <p class="mt-2 text-sm text-slate-500">82% of employees checked in before 9:30 AM.</p>
        </div>
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Unauthorized entry</p>
          <p class="mt-2 text-sm text-slate-500">2 check-ins flagged outside expected locations.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
