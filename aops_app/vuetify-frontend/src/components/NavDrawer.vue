<template>
    <v-navigation-drawer expand-on-hover rail :width="255">
        <v-list density="compact" nav>
            <v-list-item prepend-icon="mdi-home" title="Home" value="myfiles" to="/"></v-list-item>
            <v-list-item prepend-icon="mdi-account-multiple" title="Classify" value="shared"></v-list-item>
            <v-list-item prepend-icon="mdi-star" title="About" value="starred" to="/about"></v-list-item>
        </v-list>

        <template v-slot:append>
            <div class="pa-2">
                <v-btn block>
                    Logout
                </v-btn>
            </div>
        </template>

    </v-navigation-drawer>
</template>