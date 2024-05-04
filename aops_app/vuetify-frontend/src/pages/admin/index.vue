<template>
    <v-app>
        <v-toolbar border density="compact" color="blue-grey-lighten-1" title="Admin" app>
            <v-btn append-icon="mdi-exit-run" @click="this.logout()"
                >Logout</v-btn
            >
        </v-toolbar>

        <h1 class="text-center">Halaman setelah Log in</h1>
    </v-app>
</template>

<script>
import axios from "axios";
import { useRouter } from "vue-router/auto";

export default {
    data() {
        return {
            drawer: false,
        };
    },
    methods: {
        async logout() {
            try {
                const raw_response = await axios.post("admin/logout");
                const response = raw_response.data;

                console.log("LOGOUT");
                console.log(response);

                localStorage.removeItem("token");
                this.router.push({ path: "/admin/login" });
            } catch (err) {
                console.log(err.message);
            }
        },
    },
    setup() {
        const router = useRouter();
        return { router };
    },
};
</script>
