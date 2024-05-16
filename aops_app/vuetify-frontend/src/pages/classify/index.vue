<template>
    <div class="d-flex justify-center">
        <div class="pt-8" style="width: 80%">
            <h1 class="mb-4 text-center">
                Classify <span class="mdi mdi-shape"></span>
            </h1>

            <!-- Button & Select -->
            <v-row>
                <v-col cols="12" lg="10" md="9">
                    <v-select
                        label="Select classifier model"
                        v-model="this.selected_mdoel_name"
                        :items="this.available_model_name"
                        variant="outlined"
                        density="comfortable"
                        chips
                        clearable
                    ></v-select>
                </v-col>

                <v-col cols="12" lg="2" md="3">
                    <v-btn
                        min-height="67%"
                        size="small"
                        variant="outlined"
                        color="cyan-darken-4"
                        append-icon="mdi mdi-dice-multiple-outline"
                        @click="this.generate_example()"
                        :loading="this.loading1"
                        block
                    >
                        Generate example
                    </v-btn>
                </v-col>
            </v-row>

            <!-- Text area -->
            <v-row class="mb-1" justify="space-between">
                <!-- TextArea -->
                <v-col cols="12" lg="6">
                    <v-textarea
                        label="Enter math problem to classify"
                        v-model="this.text_area"
                        name="Classification"
                        variant="outlined"
                        clear-icon="mdi-close-circle"
                        rows="10"
                        counter
                        clearable
                        auto-grow
                        no-resize
                    >
                    </v-textarea>
                </v-col>

                <!-- Preview -->
                <v-col cols="12" lg="6" class="pb-9">
                    <v-card
                        class="pa-1"
                        elevation="0"
                        min-height="100%"
                        subtitle="Preview LaTex"
                        color="blue-grey-lighten-5"
                        :text="this.text_area"
                    ></v-card>
                </v-col>
            </v-row>

            <!-- Button classify -->
            <div class="mb-6 d-flex justify-center">
                <v-btn
                    size="large"
                    min-height="48px"
                    min-width="200px"
                    append-icon="mdi-arrow-right"
                    variant="flat"
                    color="teal-darken-2"
                    @click="this.classify()"
                    :loading="this.loading2"
                >
                    Classify
                </v-btn>
            </div>

            <!-- Classification Result -->
            <div
                class="mb-10 pa-3 border-md rounded-lg"
                v-if="this.show_classification_result_div === true"
            >
                <!-- Clear button -->
                <div class="mb-2 d-flex justify-end">
                    <v-btn
                        color="red"
                        append-icon="mdi-close"
                        elevation="0"
                        variant="outlined"
                        @click="this.clear_button()"
                    >
                        close
                    </v-btn>
                </div>

                <h2 class="text-center">{{ this.highest_proba_key }}</h2>
                <v-row class="mb-8" no-gutters>
                    <!-- Algebra -->
                    <v-col cols="12" sm="6" md="3">
                        <v-card
                            class="ma-2"
                            prepend-icon="mdi-function-variant"
                        >
                            <template v-slot:title>
                                <span class="font-weight-blold"> Algebra </span>
                            </template>
                            <v-card-text
                                :class="this.getCardClass('Algebra')"
                                class="pt-4"
                            >
                                {{
                                    (
                                        this.classification_proba_result[
                                            "Algebra"
                                        ] * 100
                                    ).toFixed(2)
                                }}%
                            </v-card-text></v-card
                        >
                    </v-col>

                    <!-- Combinatorics -->
                    <v-col cols="12" sm="6" md="3">
                        <v-card class="ma-2" prepend-icon="mdi-sigma">
                            <template v-slot:title>
                                <span class="font-weight-blold">
                                    Combinatorics
                                </span>
                            </template>
                            <v-card-text
                                :class="this.getCardClass('Combinatorics')"
                                class="pt-4"
                            >
                                {{
                                    (
                                        this.classification_proba_result[
                                            "Combinatorics"
                                        ] * 100
                                    ).toFixed(2)
                                }}%
                            </v-card-text></v-card
                        >
                    </v-col>

                    <!-- Geometry -->
                    <v-col cols="12" sm="6" md="3">
                        <v-card class="ma-2" prepend-icon="mdi-angle-obtuse">
                            <template v-slot:title>
                                <span class="font-weight-blold">
                                    Geometry
                                </span>
                            </template>
                            <v-card-text
                                :class="this.getCardClass('Geometry')"
                                class="pt-4"
                            >
                                {{
                                    (
                                        this.classification_proba_result[
                                            "Geometry"
                                        ] * 100
                                    ).toFixed(2)
                                }}%
                            </v-card-text></v-card
                        >
                    </v-col>

                    <!-- Number Theory -->
                    <v-col cols="12" sm="6" md="3">
                        <v-card class="ma-2" prepend-icon="mdi-numeric">
                            <template v-slot:title>
                                <span class="font-weight-blold">
                                    Number Theory
                                </span>
                            </template>
                            <v-card-text
                                :class="this.getCardClass('Number Theory')"
                                class="pt-4"
                            >
                                {{
                                    (
                                        this.classification_proba_result[
                                            "Number Theory"
                                        ] * 100
                                    ).toFixed(2)
                                }}%
                            </v-card-text></v-card
                        >
                    </v-col>
                </v-row>

                <p class="text-center mb-8 text-medium-emphasis text-body-2">
                    Result by <strong>{{ this.selected_mdoel_name }}</strong>
                </p>

                <v-divider
                    class="mb-8 border-opacity-25"
                    thickness="2"
                ></v-divider>

                <h2 class="mb-2 text-center">
                    {{ this.difficulty_level_result }}
                </h2>
                <v-row class="mb-8" no-gutters>
                    <v-col class="px-2">
                        <v-progress-linear
                            v-model="this.score_result"
                            :color="
                                this.getColorProgressionBar(
                                    this.difficulty_level_result
                                )
                            "
                            min="0"
                            max="10"
                            height="15"
                            rounded
                        >
                        </v-progress-linear>

                        <p class="text-center mt-2 mb-8 text-body-2">
                            {{ this.score_result.toFixed(2) }} out of 10
                        </p>
                        <p class="text-center text-medium-emphasis text-body-2">
                            Result by <strong>MathBERT</strong>
                            <br />
                            *Only <strong>MathBERT</strong> model available at
                            this moment for difficulty classification
                        </p>

                        <div id="scrollToResult" class="text-center">
                            <a
                                class="font-italic text-decoration-underline text-medium-emphasis text-caption text-decoration-none"
                                href="https://arxiv.org/abs/2106.07340"
                                target="_blank"
                                rel="noopener noreferrer"
                                >Learn about MathBERT</a
                            >
                        </div>
                    </v-col>
                </v-row>
            </div>

            <br />
        </div>
    </div>

    <!-- snackbar empty text area -->
    <v-snackbar v-model="this.is_empty_textarea" timeout="1250">
        Nothing to classify!
    </v-snackbar>
    <!-- snackbar no model selected -->
    <v-snackbar v-model="this.no_model_selected" timeout="2750">
        Please select a classifier model.
    </v-snackbar>
</template>

<script>
import axios from "axios";

export default {
    data: () => ({
        loading1: false,
        loading2: false,
        text_area: null,

        show_classification_result_div: false,
        classification_proba_result: null,
        highest_proba_key: null,
        highest_proba_value: null,
        difficulty_level_result: null,
        score_result: null,

        is_empty_textarea: null,

        no_model_selected: false,
        available_model_name: [],
        selected_mdoel_name: null,
    }),
    methods: {
        async generate_example() {
            this.loading1 = true;
            try {
                const response = await axios.get("classify/generate_example");
                this.text_area = response.data.post_canonical;
            } catch (error) {
                console.log("Error on API Calling");
                console.log(error.message);
            } finally {
                this.loading1 = false;
            }
        },

        async classify() {
            this.loading2 = true;

            // no model selected
            if (
                this.selected_mdoel_name === null ||
                this.selected_mdoel_name === ""
            ) {
                this.no_model_selected = true;
                this.loading2 = false;
                return;
            }

            if (this.text_area !== null && this.text_area !== "") {
                try {
                    const raw_response = await axios.post(`classify`, {
                        classifier_model: this.selected_mdoel_name,
                        problems: this.text_area,
                    });
                    const response = raw_response.data;
                    this.classification_proba_result = response.classification;

                    this.highest_proba_value = -Infinity;
                    for (const key in this.classification_proba_result) {
                        if (
                            this.classification_proba_result[key] >
                            this.highest_proba_value
                        ) {
                            this.highest_proba_value =
                                this.classification_proba_result[key];
                            this.highest_proba_key = key;
                        }
                    }

                    this.difficulty_level_result =
                        response.regression.Difficulties;
                    this.score_result = response.regression.Score;

                    this.show_classification_result_div = true;

                    setTimeout(() => {
                        const element =
                            document.getElementById("scrollToResult");
                        console.log("AAAA", element);
                        if (element) {
                            element.scrollIntoView({ behavior: "smooth" });
                        }
                    }, 100);
                } catch (err) {
                    console.log(err.message);
                } finally {
                    this.loading2 = false;
                }
            } else {
                this.is_empty_textarea = true;
                this.loading2 = false;
            }
        },

        clear_button() {
            this.show_classification_result_div = false;
            this.classification_proba_result = null;
        },

        getCardClass(category) {
            return this.highest_proba_key === category
                ? "bg-green-lighten-3"
                : "bg-red-lighten-3";
        },

        getColorProgressionBar(res) {
            const colorMap = {
                Easy: "success",
                Medium: "info",
                Hard: "warning",
                "Very Hard": "error",
            };
            return colorMap[res] || "black";
        },

        initialize() {
            axios
                .get(`/classify/iniziate`)
                .then((response) => {
                    this.available_model_name = response.data;
                })
                .catch((error) => {
                    console.log(error.message);
                });
        },
    },
    mounted() {
        this.initialize();
    },

    created() {
        this.generate_example();
    },
};
</script>

<style scoped></style>
