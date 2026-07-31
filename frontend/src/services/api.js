import axios from "axios";

const API_BASE = (import.meta.env.VITE_API_URL || 'http://localhost:8001').replace(/\/+$/, '');

const api = axios.create({
  baseURL: API_BASE,
});

export default api;