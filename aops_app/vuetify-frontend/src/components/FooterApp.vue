<template>
    <v-footer app>
        <a
            v-for="item in items"
            :key="item.title"
            :href="item.href"
            :title="item.title"
            class="text-teal-darken-1 d-inline-block mx-2 social-link"
            rel="noopener noreferrer"
            target="_blank"
        >
            <v-icon
                :icon="item.icon"
                :size="
                    item.icon === 'mdi-list-box'
                        ? 24
                        : item.icon === 'mdi-github'
                        ? 24
                        : 16
                "
            />
        </a>

        <div
            class="text-caption text-teal-darken-1"
            style="position: absolute; right: 16px"
        >
            &copy; {{ new Date().getFullYear() }}
            <span class="d-none d-sm-inline-block">Victor Chendra</span>
            — data source:
            <a
                class="text-decoration-none on-surface"
                href="https://artofproblemsolving.com/community/c13_contests"
                rel="noopener noreferrer"
                target="_blank"
            >
                artofproblemsolving
            </a>
        </div>
    </v-footer>
</template>

<script setup>
const items = [
    {
        title: "Questionnaire",
        icon: `mdi-list-box`,
        href: "https://forms.gle/TESJZjrrqUDF7qte7",
    },
    {
        title: "GitHub",
        icon: `mdi-github`,
        href: "https://github.com/victorchendra02",
    },
];
</script>
