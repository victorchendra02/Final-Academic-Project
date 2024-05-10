<template>
    <div class="d-flex justify-center">
        <div class="pt-6" style="width: 65%">
            <h1 class="text-center">
                Welcome <span class="mdi mdi-human-greeting-variant"></span>
            </h1>

            <div v-if="this.is_error == false">
                <div class="d-flex justify-space-between">
                    <h2 class="text-center">Problems of the day</h2>
                    <h3 class="text-cyan-darken-4">
                        <span class="mdi mdi-calendar"></span>
                        {{ this.today_day }},
                        {{ this.today_date }}
                    </h3>
                </div>

                <v-divider
                    class="border-opacity-75 mb-4"
                    :thickness="1"
                ></v-divider>
            </div>

            <v-alert
                v-if="this.is_error"
                density="compact"
                title="Network Error!"
                text="Request blocked, fail to retrieve data. Can't connect to database."
                border="start"
                variant="tonal"
                type="error"
            ></v-alert>

            <v-card v-for="(item, i) in this.items" class="mx-auto mb-6" block>
                <div
                    class="img-container-css img-algebra"
                    v-if="item['label'] === 'Algebra'"
                ></div>
                <div
                    class="img-container-css img-combin"
                    v-if="item['label'] === 'Combinatorics'"
                ></div>
                <div
                    class="img-container-css img-geomet"
                    v-if="item['label'] === 'Geometry'"
                ></div>
                <div
                    class="img-container-css img-nt"
                    v-if="item['label'] === 'Number Theory'"
                ></div>

                <v-card-title class="text-cyan-darken-4">
                    Can you solve this {{ item["label"] }} problem?
                </v-card-title>
                <v-card-subtitle>
                    From
                    {{ item["contest_name"].toUpperCase() }} | No.
                    {{ item["no"] }} |
                    {{ item["year"] }}
                </v-card-subtitle>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        :append-icon="
                            shows[i] ? 'mdi-chevron-up' : 'mdi-chevron-down'
                        "
                        @click="shows[i] = !shows[i]"
                        color="cyan-darken-4"
                        text="See More"
                    ></v-btn>
                </v-card-actions>

                <v-expand-transition>
                    <div v-show="shows[i]">
                        <v-divider :thickness="2"></v-divider>

                        <v-card-text>
                            <div v-html="item['post_rendered']"></div>
                        </v-card-text>

                        <v-divider :thickness="2"></v-divider>
                        <v-list-item
                            append-icon="mdi-chevron-right"
                            lines="two"
                            link
                            :href="item['link']"
                            target="_blank"
                            rel="noopener noreferrer"
                            base-color="cyan-darken-4"
                        >
                            <template v-slot:subtitle>
                                See original source
                                <span class="mdi mdi-web"></span>
                            </template>
                        </v-list-item>
                    </div>
                </v-expand-transition>
            </v-card>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data: () => ({
        shows: [],
        items: [],

        today_day: null,
        today_date: null,

        is_error: null,
    }),
    methods: {
        shuffle_array(array) {
            for (let i = array.length - 1; i > 0; i--) {
                // Generate a random index between 0 and i
                const j = Math.floor(Math.random() * (i + 1));

                // Swap elements array[i] and array[j]
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
        },
    },
    created() {
        axios
            .get(`home/home_data`)
            .then((res) => {
                this.items = res.data;
                this.shows = Array(this.items.length).fill(false);
                this.items = this.shuffle_array(this.items);

                const monthNames = [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December",
                ];
                // console.log("AAAAA", this.items);
                const dateStringFromDatabase = this.items[0]["created_at"];
                const date_ = new Date(dateStringFromDatabase);

                const day = date_.getDate();
                const monthIndex = date_.getMonth();
                const year = date_.getFullYear();

                const formattedDateString =
                    day + " " + monthNames[monthIndex] + " " + year;

                this.today_date = formattedDateString;
                this.today_day = this.items[0]["day_created"];
                this.is_error = false;
            })
            .catch((error) => {
                console.log(error.message);
                this.is_error = true;
            });
    },
};
</script>

<style scoped>
.img-container-css {
    background-size: cover;
    width: auto;
    height: 190px;
}

.img-algebra {
    background-image: url("@/assets/home/algebra_cover.jpg");
}
.img-combin {
    background-image: url("@/assets/home/combin_cover.jpg");
}
.img-geomet {
    background-image: url("@/assets/home/geomet_cover.jpg");
}
.img-nt {
    background-image: url("@/assets/home/nt_cover.jpg");
}
</style>
