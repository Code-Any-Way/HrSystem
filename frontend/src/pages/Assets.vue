<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] bg-white p-8 shadow-lg shadow-slate-200">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <p class="text-sm uppercase tracking-[0.32em] text-sky-500">Assets</p>
          <h1 class="mt-3 text-3xl font-semibold text-slate-900">Inventory and assignment tracking</h1>
        </div>
        <button class="inline-flex items-center justify-center rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">Add new asset</button>
      </div>
      <p class="mt-4 max-w-2xl text-slate-500">Keep asset inventory up to date and monitor which devices are assigned to employees.</p>
    </div>

    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Total assets</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">142</p>
        <p class="mt-2 text-sm text-slate-500">Items tracked in inventory.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Assigned</p>
        <p class="mt-4 text-4xl font-semibold text-emerald-600">95</p>
        <p class="mt-2 text-sm text-slate-500">Assets currently in use.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Due returns</p>
        <p class="mt-4 text-4xl font-semibold text-amber-600">7</p>
        <p class="mt-2 text-sm text-slate-500">Assets expected back soon.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Condition alerts</p>
        <p class="mt-4 text-4xl font-semibold text-rose-600">4</p>
        <p class="mt-2 text-sm text-slate-500">Items flagged for maintenance.</p>
      </div>
    </div>

    <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 class="text-xl font-semibold text-slate-900">Recently assigned</h2>
          <p class="mt-2 text-sm text-slate-500">Latest asset assignments issued to staff members.</p>
        </div>
        <span class="rounded-full bg-slate-100 px-4 py-2 text-sm text-slate-600">Refresh every hour</span>
      </div>
      <div class="mt-6 grid gap-4 sm:grid-cols-2">
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Work laptop</p>
          <p class="mt-2 text-sm text-slate-500">Assigned to Riya Shah | Due return in 30 days.</p>
        </div>
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Office phone</p>
          <p class="mt-2 text-sm text-slate-500">Assigned to Naveen | Under warranty.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
