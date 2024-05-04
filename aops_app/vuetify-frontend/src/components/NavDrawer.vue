<template>
    <v-navigation-drawer expand-on-hover rail :width="255">
        <v-list density="comfortable" nav>
            <!-- Home -->
            <v-list-item
                color="primary"
                prepend-icon="mdi-home"
                title="Home"
                value="home"
                to="/home"
            ></v-list-item>

            <!-- QuestionBank -->
            <v-list-item
                color="primary"
                prepend-icon="mdi-bank"
                title="Question Bank"
                value="questionbank"
                to="/questionbank"
            ></v-list-item>

            <!-- Random -->
            <v-list-item
                color="primary"
                prepend-icon="mdi-dice-multiple"
                title="Random"
                value="random_menu"
                to="/random"
            ></v-list-item>

            <!-- Classify -->
            <v-list-group value="Classify">
                <!-- classify dropdown -->
                <template v-slot:activator="{ props }">
                    <v-list-item
                        v-bind="props"
                        prepend-icon="mdi-shape"
                        title="Classify"
                    ></v-list-item>
                </template>

                <!-- classify/classification -->
                <v-list-item
                    color="primary"
                    prepend-icon="mdi-family-tree"
                    title="Classification"
                    value="classification"
                    to="/classify/classification"
                ></v-list-item>

                <!-- classify/regression -->
                <v-list-item
                    color="primary"
                    prepend-icon="mdi-chart-line"
                    title="Regression"
                    value="regression"
                    to="/classify/regression"
                ></v-list-item>
            </v-list-group>

            <!-- About -->
            <v-list-item
                color="primary"
                prepend-icon="mdi-information"
                title="About"
                value="about"
                to="/about"
            ></v-list-item>

            <!-- Admin -->
            <v-list-item
                color="primary"
                prepend-icon="mdi-account"
                title="Admin"
                value="admin"
                to="/admin"
            ></v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>
