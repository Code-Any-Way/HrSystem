<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] bg-white p-8 shadow-lg shadow-slate-200">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <p class="text-sm uppercase tracking-[0.32em] text-sky-500">Leave management</p>
          <h1 class="mt-3 text-3xl font-semibold text-slate-900">Leave requests and balance tracking</h1>
        </div>
        <button class="inline-flex items-center justify-center rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">Approve request</button>
      </div>
      <p class="mt-4 max-w-2xl text-slate-500">Review all leave requests, approval history, and remaining balance across teams.</p>
    </div>

    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Pending</p>
        <p class="mt-4 text-4xl font-semibold text-amber-600">12</p>
        <p class="mt-2 text-sm text-slate-500">Requests awaiting review.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Approved</p>
        <p class="mt-4 text-4xl font-semibold text-emerald-600">38</p>
        <p class="mt-2 text-sm text-slate-500">Leaves approved this month.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Declined</p>
        <p class="mt-4 text-4xl font-semibold text-rose-600">3</p>
        <p class="mt-2 text-sm text-slate-500">Requests declined due to policy.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Available balance</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">124</p>
        <p class="mt-2 text-sm text-slate-500">Remaining leave days for the year.</p>
      </div>
    </div>

    <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 class="text-xl font-semibold text-slate-900">Recent leave requests</h2>
          <p class="mt-2 text-sm text-slate-500">Pending leaves most recently submitted by employees.</p>
        </div>
        <span class="rounded-full bg-slate-100 px-4 py-2 text-sm text-slate-600">Updated recently</span>
      </div>
      <div class="mt-6 grid gap-4 sm:grid-cols-2">
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Sick leave</p>
          <p class="mt-2 text-sm text-slate-500">Amira Patel | 2 days | Pending approval</p>
        </div>
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Vacation</p>
          <p class="mt-2 text-sm text-slate-500">Julian Kim | 5 days | Approved</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
