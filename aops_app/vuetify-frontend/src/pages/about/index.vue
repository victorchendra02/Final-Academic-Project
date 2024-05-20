<template>
    <div class="d-flex justify-center align-center">
        <v-container class="my-8">
            <h1 class="text-center mb-8">About</h1>

            <v-row class="mb-16">
                <v-col cols="12" md="1"></v-col>
                <v-col cols="12" md="5">
                    <div class="about-text">
                        <p>
                            Hello! My name is Victor, and I am a final year
                            bachelor student majoring in IT and Big Data
                            Analytics. My passion for technology and data has
                            driven me to explore the vast possibilities that lie
                            within these fields, and I am excited to share my
                            journey with you. Over the past few years, I have
                            developed a strong foundation in programming, with
                            Python being my primary language.

                            <br /><br />
                            Moreover, I wouldn't have made it this far without
                            the support of my friends who have also faced the
                            challenges of these four years at university
                            alongside me. Their companionship and contributions
                            have been invaluable to my life.
                        </p>
                    </div>
                </v-col>
                <v-col cols="12" md="1"> </v-col>

                <v-col cols="12" md="4">
                    <v-img
                        src="https://raw.githubusercontent.com/victorchendra02/img-hosting/main/about_1.JPG"
                        max-width="100%"
                        height="auto"
                        rounded="lg"
                    ></v-img>
                </v-col>
                <v-col cols="12" md="1"></v-col>
            </v-row>

            <br /><br /><br />
            <h1 class="text-center mb-5">Photos</h1>

            <!-- Photo Gallery -->
            <v-row>
                <v-col
                    v-for="photo in photos"
                    :key="photo.id"
                    :cols="photo.cols || 6"
                    :md="photo.md || 4"
                >
                    <v-img
                        :src="`https://raw.githubusercontent.com/${this.username_github}/${this.repo_name}/main/${photo.file_name}`"
                        aspect-ratio="1"
                        rounded="lg"
                    >
                        <template v-slot:placeholder>
                            <v-row
                                class="fill-height ma-0"
                                align="center"
                                justify="center"
                            >
                                <v-progress-circular
                                    indeterminate
                                    color="grey lighten-5"
                                ></v-progress-circular>
                            </v-row>
                        </template>
                    </v-img>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    data: () => ({
        username_github: "victorchendra02",
        repo_name: "img-hosting",
        photos: [
            { id: 1, file_name: "about_1.JPG" },
            { id: 2, file_name: "about_2.JPG" },
            { id: 3, file_name: "about_3.jpg" },
            { id: 4, file_name: "about_4.jpg" },
            { id: 5, file_name: "about_5.jpg" },
            { id: 6, file_name: "about_6.JPG" },
            { id: 7, file_name: "about_7.JPG" },
            { id: 8, file_name: "about_8.JPG" },
            { id: 9, file_name: "about_9.jpg" },
            { id: 10, file_name: "about_10.JPG" },
            { id: 11, file_name: "about_11.jpg" },
            { id: 12, file_name: "about_12.jpg" },
            { id: 13, file_name: "about_13.jpg" },
            { id: 14, file_name: "about_14.jpg" },
            { id: 15, file_name: "about_15.jpg" },
            { id: 16, file_name: "about_16.jpg" },
            { id: 17, file_name: "about_17.jpg" },
            { id: 18, file_name: "about_18.jpg" },
        ],
    }),

    methods: {
        shufflePhotos() {
            for (let i = this.photos.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [this.photos[i], this.photos[j]] = [
                    this.photos[j],
                    this.photos[i],
                ];
            }
        },
    },

    mounted() {
        this.shufflePhotos();
    },
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
