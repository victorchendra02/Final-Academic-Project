<template>
    <div class="d-flex justify-center">
        <div class="pt-8" style="width: 60%">
            <h2 class="mb-1 text-center">Select problem type</h2>
            <v-row class="mb-2" justify="center">
                <v-col cols="10">
                    <p class="text-center text-body-2 text-medium-emphasis">
                        In school-level mathematical Olympiads, there are only 4
                        types of problems that are competed. <br />
                        The 4 types are as follows:
                    </p>
                </v-col>
            </v-row>

            <div class="mb-8">
                <v-row>
                    <v-col>
                        <v-card class="pa-2" link to="/questionbank/algebra">
                            <div class="img-container-css img-algebra"></div>
                            <v-card-title class="text-cyan-darken-4">
                                Algebra
                            </v-card-title>

                            <v-card-subtitle
                                >noun | al·ge·bra | \ˈal-jə-brə\
                            </v-card-subtitle>
                            <v-card-text class="text-left">
                                {{ algebra_definition }}
                            </v-card-text>
                        </v-card>
                    </v-col>

                    <v-col>
                        <v-card
                            class="pa-2"
                            link
                            to="/questionbank/combinatorics"
                        >
                            <div class="img-container-css img-combin"></div>
                            <v-card-title class="text-cyan-darken-4">
                                Combinatorics
                            </v-card-title>

                            <v-card-subtitle
                                >noun | com·bi·na·tor·ics | \ˌkämbənəˈtôriks\
                            </v-card-subtitle>
                            <v-card-text class="text-left">
                                {{ combin_definition }}
                            </v-card-text>
                        </v-card>
                    </v-col>

                    <v-responsive width="100%"></v-responsive>

                    <v-col>
                        <v-card class="pa-2" link to="/questionbank/geometry">
                            <div class="img-container-css img-geomet"></div>
                            <v-card-title class="text-cyan-darken-4">
                                Geometry
                            </v-card-title>

                            <v-card-subtitle
                                >noun | ge·om·e·try | \jēˈämətrē\
                            </v-card-subtitle>
                            <v-card-text class="text-left">
                                {{ geomet_definition }}
                            </v-card-text>
                        </v-card>
                    </v-col>

                    <v-col>
                        <v-card
                            class="pa-2"
                            link
                            to="/questionbank/numbertheory"
                        >
                            <div class="img-container-css img-nt"></div>
                            <v-card-title class="text-cyan-darken-4">
                                Number Theory
                            </v-card-title>

                            <v-card-subtitle
                                >noun | num·ber the·o·ry | \ˈnəmbər ˌTHēərē\
                            </v-card-subtitle>
                            <v-card-text class="text-left">
                                {{ nt_definition }}
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>

                <br /><br />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
        algebra_definition:
            "Deals with variables, constants, and arithmetic operations rather than specific numbers",
        combin_definition:
            "Concerned with problems of selection, arrangement, and operation within a finite or discrete system",
        geomet_definition:
            "Deals with shapes, sizes, angles, and dimensions of objects",
        nt_definition:
            "Discover interesting and unexpected relationships between different sorts of numbers",
    }),
};
</script>

<style scoped>
.v-card:hover {
    background-color: #ecedf6;
}

.img-container-css {
    background-size: cover;
    border-radius: 3px;
    width: auto;
    height: 190px;
}

.img-algebra {
    background-image: url("@/assets/qb/algebra_cover.jpg");
}
.img-combin {
    background-image: url("@/assets/qb/combin_cover2.jpg");
}
.img-geomet {
    background-image: url("@/assets/qb/geomet_cover.jpg");
}
.img-nt {
    background-image: url("@/assets/qb/nt_cover.jpg");
}
</style>
