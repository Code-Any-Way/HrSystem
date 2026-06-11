<template>
  <div class="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-lg">
    <div class="flex items-center gap-3 text-slate-900">
      <span v-html="icon" class="inline-flex h-10 w-10 items-center justify-center rounded-2xl bg-sky-100 text-sky-700"></span>
      <div>
        <h3 class="text-lg font-semibold">{{ title }}</h3>
        <p class="text-sm text-slate-500">{{ description }}</p>
      </div>
    </div>
    <div class="mt-4">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'

const props = defineProps({
  title: String,
  description: String,
  icon: String
})
</script>
