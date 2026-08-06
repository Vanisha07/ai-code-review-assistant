import axios from "axios";

export const api = axios.create({
  baseURL: "https://ai-code-review-assistant-backend-wqv5.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});