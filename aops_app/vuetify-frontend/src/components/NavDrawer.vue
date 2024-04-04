<template>
    <v-navigation-drawer expand-on-hover rail :width="255">
        <v-list density="compact" nav>
            <v-list-item color="primary" prepend-icon="mdi-home" title="Home" value="home" to="/"></v-list-item>

            <v-list-item color="primary" prepend-icon="mdi-account-multiple" title="Question Bank" value="questionbank"
                to="/questionbank"></v-list-item>

            <v-list-item color="primary" prepend-icon="mdi-account-multiple" title="Random" value="random_menu"
                to="/random"></v-list-item>

            <v-list-group value="Classify">
                <template v-slot:activator="{ props }">
                    <v-list-item v-bind="props" prepend-icon="mdi-account-circle" title="Classify"></v-list-item>
                </template>

                <v-list-item color="primary" prepend-icon="mdi-account-multiple" title="Classification" value="classification"
                    to="/classify/classification"></v-list-item>
                <v-list-item color="primary" prepend-icon="mdi-account-multiple" title="Regression" value="regression"
                    to="/classify/regression"></v-list-item>
            </v-list-group>


            <v-list-item color="primary" prepend-icon="mdi-information" title="About" value="about"
                to="/about"></v-list-item>
        </v-list>

        <template v-slot:append>
            <div class="pa-2">
                <v-btn block prepend-icon="mdi-account">
                    Admin
                </v-btn>
            </div>
        </template>

    </v-navigation-drawer>
</template>