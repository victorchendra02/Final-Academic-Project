<template>
    <div class="d-flex justify-center align-center">
        <v-container class="my-8">
            <h1 class="text-center mb-8">About</h1>

            <v-row class="mb-10">
                <v-col cols="12" md="1"></v-col>
                <v-col cols="12" md="5">
                    <div class="about-text">
                        <p>
                            Lorem ipsum dolor sit, amet consectetur adipisicing
                            elit. Libero repellat et, inventore ducimus quos
                            quidem laboriosam fuga quae facilis placeat corrupti
                            nisi at. Dicta eveniet tempora perferendis ut
                            assumenda repellendus error odio voluptas eos est
                            quod corrupti itaque architecto temporibus,
                            consequatur ducimus illum!
                        </p>
                    </div>
                </v-col>
                <v-col cols="12" md="1"> </v-col>

                <v-col cols="12" md="4">
                    <v-img
                        src="https://raw.githubusercontent.com/victorchendra02/img-hosting/main/brady-stoeltzing-pk_LRlO-PMk-unsplash.jpg"
                        max-width="100%"
                        height="auto"
                        rounded="lg"
                    ></v-img>
                </v-col>
                <v-col cols="12" md="1"></v-col>
            </v-row>

            <!-- Photo Gallery -->
            <v-row>
                <v-col cols="6" md="8">
                    <v-img
                        src="https://raw.githubusercontent.com/victorchendra02/img-hosting/main/kit-fsvhXGARtfQ-unsplash.jpg"
                        max-width="100%"
                        height="auto"
                        rounded="lg"
                    ></v-img>
                </v-col>
                <v-col cols="6" md="4">
                    <v-img
                        src="https://raw.githubusercontent.com/victorchendra02/img-hosting/main/alexander-zaytsev-p3tDpW7UX4w-unsplash.jpg"
                        max-width="100%"
                        height="auto"
                        rounded="lg"
                    ></v-img>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="6" md="4">
                    <v-img
                        src="https://raw.githubusercontent.com/victorchendra02/img-hosting/main/david-mkrtchian-UGE_Cvtxcs4-unsplash.jpg"
                        max-width="100%"
                        height="auto"
                        rounded="lg"
                    ></v-img>
                </v-col>
                <v-col cols="6" md="8">
                    <v-img
                        src="https://raw.githubusercontent.com/victorchendra02/img-hosting/main/manel-sean-U-1LOooJXVc-unsplash.jpg"
                        max-width="100%"
                        height="auto"
                        rounded="lg"
                    ></v-img>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    name: "AboutMePage",
};
</script>

<style scoped>
.about-text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
}
</style>
