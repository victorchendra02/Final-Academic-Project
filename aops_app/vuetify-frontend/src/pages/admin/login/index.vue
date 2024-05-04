<template>
    <div class="d-flex justify-center">
        <div class="pt-6" style="width: 82%">
            <h1 class="text-center mb-6">
                Log In Admin <span class="mdi mdi-account-arrow-right"></span>
            </h1>

            <!-- Error Wrong Password -->
            <v-alert
                class="mx-auto mb-6"
                max-width="700"
                elevation="2"
                closable
                border="start"
                title="Unable to Log In"
                text="Sorry, but it seems your password is wrong. Please try again!"
                type="error"
                v-model="this.error_msg_password"
                variant="tonal"
            >
            </v-alert>

            <!-- Erro No such username -->
            <v-alert
                class="mx-auto mb-6"
                max-width="700"
                elevation="2"
                closable
                border="start"
                title="Username Not Found"
                text="Username is not even exist. Please try again!"
                type="warning"
                v-model="this.error_msg_username"
                variant="tonal"
            >
            </v-alert>

            <!-- Error invalid or exp token -->
            <v-alert
                v-model="this.error_msg_token_invalid_or_exp"
                class="mx-auto mb-6"
                max-width="700"
                elevation="2"
                border="start"
                title="Token Invalid or Expire!"
                text="Your log in session is invalid or expire! Please log in again to continue."
                type="warning"
                closable
            >
            </v-alert>

            <!-- Error beyond scope -->
            <v-alert
                class="mx-auto mb-6"
                max-width="700"
                elevation="2"
                closable
                border="start"
                title="Unexpected Error Occur!"
                text="Something went wrong!"
                type="error"
                v-model="this.error_beyond_scope"
            >
            </v-alert>

            <!-- Form log in -->
            <v-card
                class="mx-auto pa-12 pb-8 mb-6"
                elevation="8"
                max-width="700"
                rounded="lg"
            >
                <!-- Username field -->
                <div class="text-medium-emphasis">Username</div>
                <v-text-field
                    placeholder="Enter username"
                    density="compact"
                    prepend-inner-icon="mdi-account-box-outline"
                    variant="outlined"
                    v-model="this.username_input"
                    clearable
                ></v-text-field>

                <!-- Password field -->
                <div class="text-medium-emphasis">Password</div>
                <v-text-field
                    placeholder="Enter password"
                    v-model="this.password_input"
                    density="compact"
                    variant="outlined"
                    prepend-inner-icon="mdi-lock-outline"
                    @click:append-inner="
                        this.toggle_visiblity_password =
                            !this.toggle_visiblity_password
                    "
                    :append-inner-icon="
                        this.toggle_visiblity_password
                            ? 'mdi-eye-off'
                            : 'mdi-eye'
                    "
                    :type="this.toggle_visiblity_password ? 'text' : 'password'"
                    clearable
                ></v-text-field>

                <br />

                <!-- Log In -->
                <v-btn
                    :loading="this.loading"
                    class="mb-8"
                    color="blue"
                    size="large"
                    variant="elevated"
                    @click="this.login()"
                    block
                >
                    Log In
                </v-btn>
            </v-card>
        </div>
    </div>

    <!-- snackbar empty username -->
    <v-snackbar v-model="this.is_username_provided" timeout="12000">
        Username cannot be empty!

        <template v-slot:actions>
            <v-btn
                color="red-darken-2"
                variant="text"
                append-icon="mdi mdi-close"
                @click="this.is_username_provided = false"
            >
                Dismiss
            </v-btn>
        </template>
    </v-snackbar>

    <!-- snackbar empty password -->
    <v-snackbar v-model="this.is_password_provided" timeout="12000">
        Password cannot be empty!

        <template v-slot:actions>
            <v-btn
                color="red-darken-2"
                variant="text"
                append-icon="mdi mdi-close"
                @click="this.is_password_provided = false"
            >
                Dismiss
            </v-btn>
        </template>
    </v-snackbar>
</template>

<script setup></script>

<script>
import axios from "axios";
import { useRouter } from "vue-router/auto";

export default {
    data: () => ({
        toggle_visiblity_password: false,
        username_input: null,
        password_input: null,

        is_username_provided: false,
        is_password_provided: false,

        error_msg_username: false,
        error_msg_password: false,
        error_msg_token_invalid_or_exp: false,
        error_beyond_scope: false,

        loading: false,
    }),
    methods: {
        async login() {
            this.loading = true;
            this.error_msg_username = false;
            this.error_msg_password = false;
            this.error_beyond_scope = false;
            if (this.username_input !== null && this.username_input !== "") {
                if (
                    this.password_input !== null &&
                    this.password_input !== ""
                ) {
                    try {
                        const raw_response = await axios.post("admin/login", {
                            username: this.username_input,
                            password: this.password_input,
                        });
                        const response = raw_response.data;
                        localStorage.setItem("token", response.token);

                        this.router.push({ path: `/admin` });
                    } catch (err) {
                        try {
                            if (
                                err.response.data.message === "WRONG_PASSWORD"
                            ) {
                                this.error_msg_password = true;
                                return;
                            }

                            if (
                                err.response.data.message === "NO_SUCH_USERNAME"
                            ) {
                                this.error_msg_username = true;
                                return;
                            }
                        } catch {
                            this.error_beyond_scope = true;
                            console.log(`console.log => ${err.message}`);
                            return;
                        } finally {
                            this.loading = false;
                        }
                    } finally {
                        this.loading = false;
                    }
                } else {
                    this.is_password_provided = true;
                }
            } else {
                this.is_username_provided = true;
            }
            this.loading = false;
        },
    },
    setup() {
        const router = useRouter();
        return { router };
    },
    created() {
        const redirect_because_token_invalid_or_exp = localStorage.getItem(
            "TOKEN_IS_INVALID_OR_EXP"
        );
        if (redirect_because_token_invalid_or_exp === "yes") {
            this.error_msg_token_invalid_or_exp = true;
            localStorage.removeItem("TOKEN_IS_INVALID_OR_EXP");
            return;
        }
    },
};
</script>
