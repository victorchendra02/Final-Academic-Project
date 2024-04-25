<template>
    <div class="d-flex justify-center">
        <div class="pt-6" style="width: 82%">
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
                >
                    Generate example
                </v-btn>
            </div>

            <!-- TextArea -->
            <div>
                <v-textarea
                    label="Enter math problem to classify"
                    v-model="this.generated_example_problem"
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
            <div class="d-flex justify-center">
                <v-btn
                    append-icon="mdi-arrow-right"
                    variant="flat"
                    color="indigo-darken-3"
                    @click="this.classify(this.generated_example_problem)"
                >
                    Classify
                </v-btn>
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
        generated_example_problem: null,
        classify_result: null,
    }),
    methods: {
        async generate_example() {
            try {
                const response = await axios.get(
                    "http://127.0.0.1:5000/classify/classification/generate_example"
                );
                this.generated_example_problem = response.data.post_canonical;
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
