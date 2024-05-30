import axios from "axios";

// const BASE_URL = "http://127.0.0.1:5000";
const BASE_URL =
    "https://9099-2001-448a-2014-9c2-e8c8-2cfa-d365-ec51.ngrok-free.app";
axios.defaults.baseURL = BASE_URL;

axios.interceptors.request.use((config) => {
    config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
    config.headers["ngrok-skip-browser-warning"] = true;
    return config;
});
