import axios from 'axios'
import { useAuthStore } from '../store'

const API_BASE_URL = (import.meta as any).env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

const getAuthStore = () => useAuthStore()

api.interceptors.request.use((config) => {
  const store = getAuthStore()
  if (store.accessToken) {
    config.headers = config.headers || {}
    config.headers.Authorization = `Bearer ${store.accessToken}`
  }
  return config
})

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const store = getAuthStore()
    const originalRequest = error.config

    if (
      error.response?.status === 401 &&
      !originalRequest._retry &&
      store.refreshToken
    ) {
      originalRequest._retry = true
      try {
        const response = await axios.post(
          `${API_BASE_URL}/auth/refresh/`,
          { refresh: store.refreshToken },
          { headers: { 'Content-Type': 'application/json' } }
        )
        store.setTokens(response.data.access, store.refreshToken)
        originalRequest.headers.Authorization = `Bearer ${response.data.access}`
        return axios(originalRequest)
      } catch (_refreshError) {
        store.logout()
      }
    }

    return Promise.reject(error)
  }
)

export default api
