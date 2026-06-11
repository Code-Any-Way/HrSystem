<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] bg-white p-8 shadow-lg shadow-slate-200">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <p class="text-sm uppercase tracking-[0.32em] text-sky-500">Payroll</p>
          <h1 class="mt-3 text-3xl font-semibold text-slate-900">Pay runs, deductions, and approvals</h1>
        </div>
        <button class="inline-flex items-center justify-center rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">Generate pay run</button>
      </div>
      <p class="mt-4 max-w-2xl text-slate-500">Manage payroll cycles, review payroll summaries, and confirm deposits for upcoming salary payments.</p>
    </div>

    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Next payroll</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">Apr 30</p>
        <p class="mt-2 text-sm text-slate-500">Next scheduled salary run.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Total net</p>
        <p class="mt-4 text-4xl font-semibold text-emerald-600">$218k</p>
        <p class="mt-2 text-sm text-slate-500">Current payroll estimate.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Pending approvals</p>
        <p class="mt-4 text-4xl font-semibold text-amber-600">2</p>
        <p class="mt-2 text-sm text-slate-500">Pay runs waiting confirmation.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Deductions</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">$5.4k</p>
        <p class="mt-2 text-sm text-slate-500">Total payroll deductions this cycle.</p>
      </div>
    </div>

    <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 class="text-xl font-semibold text-slate-900">Payroll summary</h2>
          <p class="mt-2 text-sm text-slate-500">Review payroll run status for the current pay period.</p>
        </div>
        <span class="rounded-full bg-slate-100 px-4 py-2 text-sm text-slate-600">Ready to approve</span>
      </div>
      <div class="mt-6 grid gap-4 sm:grid-cols-2">
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Salary transfers</p>
          <p class="mt-2 text-sm text-slate-500">All employee payments scheduled for next business day.</p>
        </div>
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Review notes</p>
          <p class="mt-2 text-sm text-slate-500">Confirm overtime adjustments and tax corrections.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
