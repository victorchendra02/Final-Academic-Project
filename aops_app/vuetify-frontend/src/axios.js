import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000";
axios.defaults.baseURL = BASE_URL;

axios.interceptors.request.use((config) => {
    config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`;
    return config
});
