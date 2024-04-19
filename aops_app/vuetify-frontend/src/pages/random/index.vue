<template>
    <div class="d-flex justify-center">
        <div class="pt-6" style="width: 88%">
            <!-- header -->
            <div class="pb-3">
                <h1 class="text-center">Random problem</h1>
            </div>

            <!-- Form -->
            <div class="py-5">
                <div class="d-flex justify-space-between">
                    <!-- LabelInput -->
                    <div style="width: 800px">
                        <v-select
                            label="Label"
                            hint="Pick your desire label"
                            v-model="value_for_labels"
                            :items="array_of_labels"
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
                            :max="10"
                            :model-value="1"
                            persistent-hint
                        ></v-number-input>
                    </div>

                    <!-- ButtonGo -->
                    <div style="width: 210px">
                        <v-btn
                            block
                            append-icon="$vuetify"
                            variant="flat"
                            color="indigo-darken-3"
                            @click="this.go()"
                        >
                            Go
                        </v-btn>
                    </div>
                </div>
            </div>

            <!-- horizontal line -->
            <hr class="mb-2 mt-0" />
            <h3 class="mb-2">Result for</h3>

            <!-- Main content -->
            <div>
                <v-card
                    v-for="i in array_result"
                    class="mb-1"
                    color="surface-variant"
                    variant="outlined"
                    :title="this.label"
                    elevation="1"
                >
                    <template v-slot:subtitle>
                        No. {{ this.no }} | {{ this.contest_name }} |
                        {{ this.year }} |
                        <a
                            :href="this.link"
                            target="_blank"
                            rel="noopener noreferrer"
                            >Source</a
                        >
                    </template>
                    <template v-slot:text>
                        Let $ a$ and $ b$ be non-negative integers such that $
                        ab \geq c^2,$ where $ c$ is an integer. Prove that there
                        is a number $ n$ and integers $ x_1, x_2, \ldots, x_n,
                        y_1, y_2, \ldots, y_n$ such that \[ \sum^n_{i=1} x^2_i =
                        a, \sum^n_{i=1} y^2_i = b, \text{ and } \sum^n_{i=1}
                        x_iy_i = c.\]
                    </template>
                </v-card>
            </div>
        </div>
    </div>

    <br /><br /><br /><br /><br /><br />
</template>

<script setup>
import { ref } from "vue";

const array_of_contest_names = ref([
    "(None)",
    "IMO",
    "APMO",
    "EGMO",
    "Benelux",
]);
const array_of_labels = ref([
    "Algebra",
    "Geometry",
    "Combinatorics",
    "Number Theory",
]);

const value_for_contest_name = ref([]);
const value_for_labels = ref([]);
</script>

<script>
import axios from "axios";
import { VNumberInput } from "vuetify/lib/labs/components.mjs";

export default {
    data: () => ({
        n: null,
        no: "4",
        year: "2020",
        label: "Geometry",
        contest_name: "imo shortlist",
        link: "https://www.google.com",
        array_result: [1, 2, 3, 4],
    }),
    methods: {
        async get_random_data(n, contest_name, year, label) {
            try {
                const response = await axios.get(
                    `http://127.0.0.1:5000/random?n=${n}&contest_name=${contest_name}&year=${year}&label=${label}`
                );
                this.array_result = response.data;
            } catch (error) {
                console.log(error.message);
            }
        },
        go_button() {},
    },
    created() {},
};
</script>
