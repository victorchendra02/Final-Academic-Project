<template>
    <div class="d-flex justify-center">
        <div class="pt-10" style="width: 84%">
            <v-alert
                class="my-4"
                type="info"
                color="light-blue-darken-2"
                closable
            >
                Click on <b>table headers</b> to sort the data.
            </v-alert>

            <v-btn
                prepend-icon="mdi-arrow-left"
                color="cyan-darken-4"
                variant="tonal"
                density="default"
                @click="$router.push('/questionbank')"
            >
            </v-btn>
            <h2 class="text-center mb-4">Problems Combinatorics</h2>

            <div class="px-0">
                <v-select
                    label="Select contest"
                    v-model="this.selected_contest_name"
                    :items="this.unique_contest_name"
                    variant="outlined"
                    density="comfortable"
                    chips
                    clearable
                    multiple
                ></v-select>
            </div>

            <v-data-table
                class="table-color"
                :items-per-page="itemsPerPage"
                :headers="headers"
                :items="items"
                :items-length="totalItems"
                :loading="loading"
            >
                <template v-slot:item.post_rendered="{ value }">
                    <div class="py-1" v-html="value"></div>
                </template>
                <template v-slot:item.link="{ value }">
                    <a :href="value" target="_blank" rel="noopener noreferrer"
                        >Source</a
                    >
                </template>
                <template v-slot:item.contest_name="{ value }">
                    <v-chip color="light-blue-darken-2" density="compact">{{
                        value.toUpperCase().replace(/_/g, " ")
                    }}</v-chip>
                </template>
                <template v-slot:item.year="{ value }">
                    <v-chip color="teal-darken-2" density="compact">{{
                        value
                    }}</v-chip>
                </template>
            </v-data-table>

            <br />
            <br />
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data: () => ({
        headers: [
            { title: "Id", sortable: true, key: "id_key", align: "start" },
            {
                title: "No",
                sortable: true,
                key: "no",
                align: "start",
            },
            {
                title: "Problem",
                sortable: true,
                key: "post_rendered",
                align: "start",
            },
            {
                title: "Contest",
                sortable: true,
                key: "contest_name",
                align: "start",
            },
            { title: "Year", sortable: true, key: "year", align: "start" },
            { title: "Link", sortable: false, key: "link", align: "start" },
        ],
        items: [],
        totalItems: 0,
        loading: false,
        itemsPerPage: 10,
        currentPage: 1,

        unique_contest_name: [],
        selected_contest_name: [],
    }),
    watch: {
        selected_contest_name(newVal, oldVal) {
            if (newVal.length === 0) {
                this.headers[3].sortable = true;
                return this.fetchData_original();
            }
            this.headers[3].sortable = false;
            return this.fetchData_forspecific_contest_name();
        },
    },
    methods: {
        fetchData_original() {
            this.loading = true;
            axios
                .get(`questionbank_original/Combinatorics`)
                .then((response) => {
                    this.items = response.data.problems;
                    this.unique_contest_name =
                        response.data.unique_contest_name;
                    this.totalItems = response.data.problems.length;
                    this.loading = false;
                })
                .catch((error) => {
                    console.error("Error fetching data:", error);
                    this.loading = false;
                });
        },
        fetchData_forspecific_contest_name() {
            this.loading = true;
            axios
                .get(
                    `questionbank_specific_contestname/Combinatorics?contest_name=${this.selected_contest_name}`
                )
                .then((response) => {
                    this.items = response.data;
                    this.totalItems = response.data.length;
                    this.loading = false;
                })
                .catch((error) => {
                    console.error("Error fetching data:", error);
                    this.loading = false;
                });
        },
    },
    mounted() {
        this.fetchData_original();
    },
};
</script>

<style scoped>
.table-color {
    border-radius: 8px;
    background-color: #fdfdfd;
}
</style>
