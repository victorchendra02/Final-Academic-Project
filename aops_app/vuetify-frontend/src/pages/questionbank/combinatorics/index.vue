<template>
    <div class="d-flex justify-center">
        <div class="pt-10" style="width: 84%">
            <v-btn
                prepend-icon="mdi-arrow-left"
                color="cyan-darken-4"
                variant="text"
                density="comfortable"
                @click="$router.push('/questionbank')"
            </v-btn>
            <h2 class="text-center mb-4">Problems Combinatorics</h2>

            <v-data-table
                class="table-color"
                :items-per-page="itemsPerPage"
                :headers="headers"
                :items="items"
                :items-length="totalItems"
                :loading="loading"
                @update:options="fetchData"
            >
                <template v-slot:item.post_rendered="{ value }">
                    <div class="py-1" v-html="value"></div>
                </template>
                <template v-slot:item.link="{ value }">
                    <a :href="value" target="_blank" rel="noopener noreferrer">Source</a>
                </template>
                <template v-slot:item.contest_name="{ value }">
                    <v-chip color="light-blue-darken-2" density="compact">{{
                        value.toUpperCase().replace(/_/g, " ")
                    }}</v-chip>
                </template>
                <template v-slot:item.year="{ value }">
                    <v-chip color="teal-darken-2" density="compact">{{ value }}</v-chip>
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
    data() {
        return {
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
        };
    },
    methods: {
        fetchData() {
            this.loading = true;
            axios
                .get(`questionbank/Combinatorics`)
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
        this.fetchData();
    },
};
</script>

<style scoped>
.table-color {
    border-radius: 8px;
    background-color: #fefefe;
}
</style>
