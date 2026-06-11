<template>
  <div class="bg-white p-6 rounded shadow">
    <h2 class="text-xl mb-4">Sign in</h2>
    <form @submit.prevent="login">
      <input v-model="email" placeholder="Email" class="w-full mb-3 p-2 border rounded" />
      <input v-model="password" type="password" placeholder="Password" class="w-full mb-3 p-2 border rounded" />
      <button class="w-full bg-blue-600 text-white py-2 rounded">Sign in</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const email = ref('')
const password = ref('')
function login() {
  // placeholder
  console.log('login', email.value)
}
</script>
