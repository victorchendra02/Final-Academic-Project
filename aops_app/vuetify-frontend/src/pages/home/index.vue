<template>
    <div class="d-flex justify-center">
        <div class="pt-6" style="width: 70%">
            <h1 class="text-center">Welcome</h1>
            <h2 class="text-center mb-2">Problems of the day</h2>

            <v-card class="mx-auto mb-6" block>
                <v-img
                    height="200px"
                    src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                    cover
                ></v-img>

                <v-card-title> Top western road trips </v-card-title>

                <v-card-subtitle> 1,000 miles of wonder </v-card-subtitle>

                <v-card-actions>
                    <v-btn
                        :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                        @click="show = !show"
                    ></v-btn>
                    <v-spacer></v-spacer>
                    <v-btn color="orange-lighten-2" text="See More"></v-btn>
                </v-card-actions>

                <v-expand-transition>
                    <div v-show="show">
                        <v-divider></v-divider>

                        <v-card-text>
                            I'm a thing. But, like most politicians, he promised
                            more than he could deliver. You won't have time for
                            sleeping, soldier, not with all the bed making
                            you'll be doing. Then we'll go with that data file!
                            Hey, you add a one and two zeros to that or we walk!
                            You're going to do his laundry? I've got to find a
                            way to escape.
                        </v-card-text>
                    </div>
                </v-expand-transition>
            </v-card>

            <v-card class="mx-auto mb-6" block>
                <v-img
                    height="200px"
                    src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                    cover
                ></v-img>

                <v-card-title> Top western road trips </v-card-title>

                <v-card-subtitle> 1,000 miles of wonder </v-card-subtitle>

                <v-card-actions>
                    <v-btn
                        :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                        @click="show = !show"
                    ></v-btn>
                    <v-spacer></v-spacer>
                    <v-btn color="orange-lighten-2" text="See More"></v-btn>
                </v-card-actions>

                <v-expand-transition>
                    <div v-show="show">
                        <v-divider></v-divider>

                        <v-card-text>
                            I'm a thing. But, like most politicians, he promised
                            more than he could deliver. You won't have time for
                            sleeping, soldier, not with all the bed making
                            you'll be doing. Then we'll go with that data file!
                            Hey, you add a one and two zeros to that or we walk!
                            You're going to do his laundry? I've got to find a
                            way to escape.
                        </v-card-text>
                    </div>
                </v-expand-transition>
            </v-card>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
        show: false,
    }),
};
</script>
