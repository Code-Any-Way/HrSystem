import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import App from './App.vue'
import './index.css'

const app = createApp(App)
const pinia = createPinia()
app.use(pinia)
app.use(router)

import { useAuthStore } from './store'
const auth = useAuthStore(pinia)
auth.initialize()
if (auth.isAuthenticated) {
  auth.loadProfile().catch(() => auth.logout())
}

app.mount('#app')
