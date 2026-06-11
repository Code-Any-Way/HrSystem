import api from './api'

export interface LoginPayload {
  email: string
  password: string
}

export interface LoginResponse {
  access: string
  refresh: string
  user: Record<string, unknown>
}

export function login(payload: LoginPayload) {
  return api.post<LoginResponse>('/auth/login/', payload)
}

export function refreshToken(refresh: string) {
  return api.post('/auth/refresh/', { refresh })
}

export function fetchProfile() {
  return api.get('/auth/profile/')
}
