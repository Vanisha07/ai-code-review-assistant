import axios from "axios";

export const api = axios.create({
  baseURL: "https://ai-code-review-assistant-production-73f5.up.railway.app",
  headers: {
    "Content-Type": "application/json",
  },
});