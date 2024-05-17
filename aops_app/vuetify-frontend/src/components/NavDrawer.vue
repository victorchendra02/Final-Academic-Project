<template>
    <v-navigation-drawer expand-on-hover rail :width="255">
        <v-list density="comfortable" nav>
            <!-- Home -->
            <v-list-item
                color="teal"
                prepend-icon="mdi-home"
                title="Home"
                value="home"
                to="/home"
            ></v-list-item>

            <!-- QuestionBank -->
            <v-list-item
                color="teal"
                prepend-icon="mdi-bank"
                title="Question Bank"
                value="questionbank"
                to="/questionbank"
            ></v-list-item>

            <!-- Random -->
            <v-list-item
                color="teal"
                prepend-icon="mdi-dice-multiple"
                title="Random"
                value="random_menu"
                to="/random"
            ></v-list-item>

            <!-- Classify -->
            <v-list-item
                color="teal"
                prepend-icon="mdi-shape"
                title="Classify"
                value="classify"
                to="/classify"
            ></v-list-item>

            <!-- About -->
            <v-list-item
                color="teal"
                prepend-icon="mdi-information"
                title="About"
                value="about"
                to="/about"
            ></v-list-item>

            <!-- Admin -->
            <v-list-item
                color="teal"
                prepend-icon="mdi-account"
                title="Admin"
                value="admin"
                to="/admin"
            ></v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>
