import axios from "axios";
import { createRouter, createWebHistory } from "vue-router/auto";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
});

router.beforeEach(async (to, from, next) => {
    const to_path = to.path;
    console.log(to_path);

    if (to_path === "/") {
        next({ path: "/home" });
        return;
    }

    if (to_path === "/admin") {
        const token = localStorage.getItem("token");

        // TOKEN NOT EXIST
        if (token === null) {
            next({ path: "/admin/login" });
            return;
        }

        // TOKEN EXIST
        if (token !== null) {
            try {
                // TOKEN VALID
                await axios.get(`admin/is_authorized`);
                next();
                return;
            } catch {
                // TOKEN NOT VALID
                localStorage.removeItem("token")
                localStorage.setItem("TOKEN_IS_INVALID_OR_EXP", "yes")
                next({ path: "/admin/login" });
                return;
            }
        }
    }

    if (to_path === "/admin/login") {
        const token = localStorage.getItem("token");

        if (token === null) {
            next();
            return;
        }

        if (token !== null) {
            try {
                // TOKEN VALID
                await axios.get(`admin/is_authorized`);
                next({ path: "/admin" });
                return;
            } catch {
                // TOKEN NOT VALID
                localStorage.removeItem("token")
                next();
                return;
            }
        }
    }
    next();
});

export default router;
