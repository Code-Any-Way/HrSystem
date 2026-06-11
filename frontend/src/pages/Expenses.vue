<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] bg-white p-8 shadow-lg shadow-slate-200">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <p class="text-sm uppercase tracking-[0.32em] text-sky-500">Expenses</p>
          <h1 class="mt-3 text-3xl font-semibold text-slate-900">Claims review and reimbursement tracking</h1>
        </div>
        <button class="inline-flex items-center justify-center rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">Submit claim</button>
      </div>
      <p class="mt-4 max-w-2xl text-slate-500">Manage expense approvals, outstanding reimbursements, and claim history across departments.</p>
    </div>

    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Pending</p>
        <p class="mt-4 text-4xl font-semibold text-amber-600">18</p>
        <p class="mt-2 text-sm text-slate-500">Claims waiting approval.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Paid</p>
        <p class="mt-4 text-4xl font-semibold text-emerald-600">42</p>
        <p class="mt-2 text-sm text-slate-500">Claims settled this month.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Total reimbursement</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">$11.2k</p>
        <p class="mt-2 text-sm text-slate-500">Full amount approved for payout.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">High priority</p>
        <p class="mt-4 text-4xl font-semibold text-rose-600">4</p>
        <p class="mt-2 text-sm text-slate-500">Claims needing urgent attention.</p>
      </div>
    </div>

    <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 class="text-xl font-semibold text-slate-900">Recent claims</h2>
          <p class="mt-2 text-sm text-slate-500">Latest expense submissions and their current status.</p>
        </div>
        <span class="rounded-full bg-slate-100 px-4 py-2 text-sm text-slate-600">Sorted by date</span>
      </div>
      <div class="mt-6 grid gap-4 sm:grid-cols-2">
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Travel claim</p>
          <p class="mt-2 text-sm text-slate-500">$620 | Submitted by Lina | Pending finance</p>
        </div>
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Equipment reimbursement</p>
          <p class="mt-2 text-sm text-slate-500">$245 | Submitted by Isaac | Approved</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
