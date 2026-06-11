<template>
  <div class="space-y-6">
    <div class="rounded-[2rem] bg-white p-8 shadow-lg shadow-slate-200">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <p class="text-sm uppercase tracking-[0.32em] text-sky-500">Evaluations</p>
          <h1 class="mt-3 text-3xl font-semibold text-slate-900">Performance reviews and outcome tracking</h1>
        </div>
        <button class="inline-flex items-center justify-center rounded-full bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">Start review</button>
      </div>
      <p class="mt-4 max-w-2xl text-slate-500">Monitor employee performance cycles, goal completion, and feedback from across the organization.</p>
    </div>

    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Active reviews</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">16</p>
        <p class="mt-2 text-sm text-slate-500">Reviews currently in progress.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Completed</p>
        <p class="mt-4 text-4xl font-semibold text-emerald-600">73</p>
        <p class="mt-2 text-sm text-slate-500">Reviews completed this quarter.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Pending feedback</p>
        <p class="mt-4 text-4xl font-semibold text-amber-600">5</p>
        <p class="mt-2 text-sm text-slate-500">Evaluations awaiting manager comments.</p>
      </div>
      <div class="rounded-3xl bg-white p-6 shadow-sm border border-slate-200">
        <p class="text-sm uppercase tracking-[0.24em] text-slate-500">Goals aligned</p>
        <p class="mt-4 text-4xl font-semibold text-slate-900">88%</p>
        <p class="mt-2 text-sm text-slate-500">Performance goals aligned with targets.</p>
      </div>
    </div>

    <div class="rounded-[2rem] border border-slate-200 bg-white p-6 shadow-sm">
      <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <h2 class="text-xl font-semibold text-slate-900">Latest review items</h2>
          <p class="mt-2 text-sm text-slate-500">Highlights from the most recent performance evaluation cycles.</p>
        </div>
        <span class="rounded-full bg-slate-100 px-4 py-2 text-sm text-slate-600">Updated daily</span>
      </div>
      <div class="mt-6 grid gap-4 sm:grid-cols-2">
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Midyear check-in</p>
          <p class="mt-2 text-sm text-slate-500">Team leaders completed 92% of check-ins.</p>
        </div>
        <div class="rounded-3xl bg-slate-50 p-5">
          <p class="font-semibold text-slate-900">Development goals</p>
          <p class="mt-2 text-sm text-slate-500">Growth plans are on track for 82% of employees.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
