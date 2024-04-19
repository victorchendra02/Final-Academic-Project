<template>
    <div class="d-flex justify-center">
        <div class="pt-6" style="width: 88%">
            <h1 class="pb-3 text-center">Classification</h1>

            <!-- Button -->
            <div class="mb-2">
                <v-btn
                    size="small"
                    density="default"
                    variant="text"
                    color="indigo-darken-3"
                    @click="this.generate_example()"
                >
                    Generate example
                </v-btn>
            </div>

            <!-- TextArea -->
            <div class="mb-2">
                <v-textarea
                    label="Enter math problem to classify"
                    :model-value="this.example_random_problem"
                    name="Classification"
                    variant="outlined"
                    clear-icon="mdi-close-circle"
                    clearable
                    auto-grow
                >
                </v-textarea>
            </div>

            <!-- Button -->
            <div class="mb-5 d-flex justify-center">
                <v-btn
                    append-icon="$vuetify"
                    variant="flat"
                    color="indigo-darken-3"
                    @click="this.classify(this.example_random_problem)"
                >
                    Classify problem
                </v-btn>
            </div>

            <!-- TextResult -->
            <div class="text-center">
                <h1>Result:</h1>
                <h2>{{ this.classify_result }}</h2>
            </div>

            <br /><br /><br />
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data: () => ({
        text_area: null,
        example_random_problem: null,
        classify_result: null,
    }),
    methods: {
        async generate_example() {
            try {
                const response = await axios.get(
                    "http://127.0.0.1:5000/classify/classification/generate_example"
                );
                this.example_random_problem = response.data.post_canonical;
            } catch (error) {
                console.log("Error on API Calling");
                console.log(error.message);
            }
        },
        classify(text) {
            let label = [
                "Algebra",
                "Geometry",
                "Combinatorics",
                "Number Theory",
            ];
            this.classify_result =
                label[Math.floor(Math.random() * label.length)];
        },
    },
    created() {
        this.generate_example();
    },
};
</script>
