import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { useAuthStore } from './store/auth'

const app = createApp(App)

app.use(router)

const pinia = createPinia()
app.use(pinia)

const authStore = useAuthStore()
authStore.setCsrfToken()

app.mount('#app')
