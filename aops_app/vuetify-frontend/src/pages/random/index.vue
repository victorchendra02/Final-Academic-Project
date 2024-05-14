<template>
    <div class="d-flex justify-center">
        <div class="pt-8" style="width: 82%">
            <!-- header -->
            <div class="pb-3">
                <h1 class="text-center">
                    Random problem
                    <v-icon icon="mdi mdi-dice-multiple"></v-icon>
                </h1>
            </div>

            <!-- Form -->
            <div class="py-5">
                <div class="d-flex justify-space-between">
                    <!-- LabelInput -->
                    <div style="width: 700px">
                        <v-select
                            label="Label"
                            hint="Pick your desire label"
                            v-model="this.selected_labels"
                            :items="this.array_of_labels"
                            variant="outlined"
                            density="compact"
                            clearable
                            multiple
                            persistent-hint
                        ></v-select>
                    </div>

                    <!-- N: NumberInput -->
                    <div style="width: 200px">
                        <v-number-input
                            label="n"
                            hint="Number of sample"
                            controlVariant="split"
                            density="compact"
                            variant="outlined"
                            :reverse="false"
                            :hideInput="false"
                            :inset="false"
                            :min="1"
                            :max="this.max_n_input"
                            v-model="this.n"
                            persistent-hint
                        ></v-number-input>
                    </div>

                    <!-- ButtonGo -->
                    <div style="width: 200px">
                        <v-btn
                            block
                            append-icon="mdi mdi-dice-multiple"
                            variant="flat"
                            color="indigo-darken-3"
                            @click="this.go_button()"
                            :loading="this.loading"
                        >
                            Go
                        </v-btn>
                    </div>
                </div>
            </div>

            <!-- horizontal line -->
            <hr class="mb-2 mt-0" />
            <h3 class="mb-2" v-if="this.result_for">Result for:</h3>

            <!-- Main content -->
            <div>
                <v-card
                    v-for="(item, index) in this.result"
                    class="mb-2"
                    color="surface-variant"
                    variant="outlined"
                    elevation="1"
                >
                    <template v-slot:title>
                        {{ index + 1 }} | {{ item.label }}
                    </template>
                    <template v-slot:subtitle>
                        No. {{ item.no }} | {{ item.contest_name }} |
                        {{ item.year }} |
                        <a
                            :href="item.link"
                            target="_blank"
                            rel="noopener noreferrer"
                            >Source</a
                        >
                    </template>
                    <template v-slot:text>
                        <div v-html="item.post_rendered"></div>
                    </template>
                </v-card>
            </div>
        </div>
    </div>

    <!-- snackbar invalid n -->
    <v-snackbar v-model="this.invalid_n">
        Please input "number of sample" that in range of 1
        <span class="mdi mdi-greater-than-or-equal"></span> n
        <span class="mdi mdi-greater-than-or-equal"></span>
        {{ this.max_n_input }}

        <template v-slot:actions>
            <v-btn
                color="red-darken-2"
                variant="text"
                append-icon="mdi mdi-close"
                @click="this.invalid_n = false"
            >
                Dismiss
            </v-btn>
        </template>
    </v-snackbar>

    <!-- snackbar invalid label -->
    <v-snackbar v-model="this.invalid_label">
        Please select at least 1 label

        <template v-slot:actions>
            <v-btn
                color="red-darken-2"
                variant="text"
                append-icon="mdi mdi-close"
                @click="this.invalid_label = false"
            >
                Dismiss
            </v-btn>
        </template>
    </v-snackbar>

    <br /><br /><br /><br /><br />
</template>

<script setup>
console.log("Start");
</script>

<script>
import axios from "axios";
import { VNumberInput } from "vuetify/lib/labs/components.mjs";

export default {
    data: () => ({
        array_of_labels: [
            "Algebra",
            "Geometry",
            "Combinatorics",
            "Number Theory",
        ],
        max_n_input: 50,

        selected_labels: [],
        n: null,

        result: [],

        invalid_n: false,
        invalid_label: false,
        result_for: false,

        loading: false,
    }),
    methods: {
        async get_random_data(n_, label_) {
            this.loading = true;
            try {
                const response = await axios.get(
                    `random?label=${label_}&n=${n_}`
                );
                this.result = response.data;
                this.result_for = true;
            } catch (error) {
                console.log(error.message);
            } finally {
                this.loading = false;
            }
        },
        go_button() {
            if (this.selected_labels.length == 0) {
                this.invalid_label = true;
            } else if (this.n <= 0 || this.n > this.max_n_input) {
                this.invalid_n = true;
            } else {
                this.get_random_data(this.n, this.selected_labels);
            }
        },
    },
    created() {},
};
</script>
