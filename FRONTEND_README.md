Frontend (Vue 3 + Vite + Tailwind) quick start

Development:

1. cd frontend
2. npm install
3. npm run dev

Build and run with Docker (production-like):

1. docker build -t hrms-frontend:latest ./frontend
2. docker run -p 3000:80 hrms-frontend:latest

The frontend expects the backend API under /api/ when proxied via nginx in docker-compose.
