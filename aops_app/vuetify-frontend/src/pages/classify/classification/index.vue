<template>
    <div class="d-flex justify-center">
        <div class="pt-8" style="width: 82%">
            <h1 class="mb-1 text-center">
                Classification <span class="mdi mdi-family-tree"></span>
            </h1>

            <!-- Button generate example -->
            <div class="mb-1 d-flex justify-end">
                <v-btn
                    size="small"
                    density="default"
                    variant="text"
                    color="indigo-darken-3"
                    append-icon="mdi mdi-dice-multiple-outline"
                    @click="this.generate_example()"
                    :loading="this.loading1"
                >
                    Generate example
                </v-btn>
            </div>

            <!-- TextArea -->
            <div>
                <v-textarea
                    label="Enter math problem to classify"
                    v-model="this.text_area"
                    name="Classification"
                    variant="outlined"
                    clear-icon="mdi-close-circle"
                    rows="6"
                    clearable
                    no-resize
                >
                </v-textarea>
            </div>

            <!-- Button classify -->
            <div class="d-flex justify-center mb-5">
                <v-btn
                    append-icon="mdi-arrow-right"
                    variant="flat"
                    color="indigo-darken-3"
                    @click="this.classify()"
                    :loading="this.loading2"
                >
                    Classify
                </v-btn>
            </div>

            <p class="text-center">{{ this.text_area }}</p>

            <!-- Classification Result -->
            <div v-if="this.classify_result">
                <!-- Clear button -->
                <div class="d-flex justify-end">
                    <v-btn
                        color="red"
                        append-icon="mdi-trash-can-outline"
                        elevation="0"
                        variant="outlined"
                        @click="this.clear_button()"
                    >
                        clear
                    </v-btn>
                </div>

                <h2 class="text-center">{{ this.highest_proba_key }}</h2>

                <v-row class="mb-6" no-gutters>
                    <v-col cols="3">
                        <v-card
                            class="ma-2"
                            prepend-icon="mdi-function-variant"
                        >
                            <template v-slot:title>
                                <span class="font-weight-blold"> Algebra </span>
                            </template>
                            <v-card-text class="bg-surface-light pt-4">
                                {{
                                    (
                                        this.classify_result["Algebra"] * 100
                                    ).toFixed(2)
                                }}%
                            </v-card-text></v-card
                        >
                    </v-col>
                    <v-col cols="3">
                        <v-card class="ma-2" prepend-icon="mdi-sigma">
                            <template v-slot:title>
                                <span class="font-weight-blold">
                                    Combinatorics
                                </span>
                            </template>
                            <v-card-text class="bg-surface-light pt-4">
                                {{
                                    (
                                        this.classify_result["Combinatorics"] *
                                        100
                                    ).toFixed(2)
                                }}%
                            </v-card-text></v-card
                        >
                    </v-col>
                    <v-col cols="3">
                        <v-card class="ma-2" prepend-icon="mdi-angle-obtuse">
                            <template v-slot:title>
                                <span class="font-weight-blold">
                                    Geometry
                                </span>
                            </template>
                            <v-card-text class="bg-surface-light pt-4">
                                {{
                                    (
                                        this.classify_result["Geometry"] * 100
                                    ).toFixed(2)
                                }}%
                            </v-card-text></v-card
                        >
                    </v-col>
                    <v-col cols="3">
                        <v-card class="ma-2" prepend-icon="mdi-numeric">
                            <template v-slot:title>
                                <span class="font-weight-blold">
                                    Number Theory
                                </span>
                            </template>
                            <v-card-text class="bg-surface-light pt-4">
                                {{
                                    (
                                        this.classify_result["Number Theory"] *
                                        100
                                    ).toFixed(2)
                                }}%
                            </v-card-text></v-card
                        >
                    </v-col>
                </v-row>
            </div>
        </div>
    </div>

    <!-- snackbar empty text area -->
    <v-snackbar v-model="this.is_empty_textarea" timeout="1250">
        Nothing to classify!
    </v-snackbar>
</template>

<script>
import axios from "axios";

export default {
    data: () => ({
        loading1: false,
        loading2: false,
        text_area: null,

        classify_result: null,
        highest_proba_key: null,
        highest_proba_value: null,

        is_empty_textarea: null,
    }),
    methods: {
        async generate_example() {
            this.loading1 = true;
            try {
                const response = await axios.get(
                    "classify/classification/generate_example"
                );
                this.text_area = response.data.post_canonical;
            } catch (error) {
                console.log("Error on API Calling");
                console.log(error.message);
            } finally {
                this.loading1 = false;
            }
        },

        classify() {
            this.loading2 = true;

            if (this.text_area !== null && this.text_area !== "") {
                axios
                    .get(`classify/classification?problem=${this.text_area}`)
                    .then((response) => {
                        this.classify_result = response.data;

                        this.highest_proba_value = -Infinity;
                        for (const key in this.classify_result) {
                            if (
                                this.classify_result[key] >
                                this.highest_proba_value
                            ) {
                                this.highest_proba_value =
                                    this.classify_result[key];
                                this.highest_proba_key = key;
                            }
                        }

                        console.log(this.highest_proba_key);
                        console.log(this.highest_proba_value);
                    })
                    .catch((err) => {
                        console.log(err.message);
                    })
                    .finally((_) => {
                        this.loading2 = false;
                    });
            } else {
                this.is_empty_textarea = true;
                this.loading2 = false;
            }
        },

        clear_button() {
            this.classify_result = null;
        },
    },
    created() {
        this.generate_example();
    },
};
</script>
