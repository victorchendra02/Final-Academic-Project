<template>
    <v-toolbar border density="comfortable" color="cyan-lighten-5" app>
        <template v-slot:title>
            Admin <span class="mdi mdi-account-check"></span>
        </template>
        <v-btn
            min-width="140px"
            color="error"
            variant="flat"
            append-icon="mdi-exit-run"
            @click="this.logout()"
            >Logout</v-btn
        >
    </v-toolbar>

    <div class="d-flex justify-center">
        <div class="mt-5" style="width: 96%">
            <h1 class="text-center mb-2">CRUD DATABASE</h1>

            <!-- Button add item -->
            <div class="d-flex mb-3">
                <h2 class="me-5">Table `imo`</h2>
                <v-btn
                    variant="flat"
                    color="teal"
                    append-icon="mdi-database-plus-outline"
                    @click="this.function_showAddDialog_imo()"
                    >Add New</v-btn
                >
            </div>

            <!-- Dialog new data -->
            <v-dialog v-model="showAddDialog_imo" max-width="1100px">
                <v-card class="pa-3 pb-5">
                    <v-card-title>Insert New Data +</v-card-title>
                    <v-card-text> Add new data to database </v-card-text>
                    <!-- reset form button -->
                    <v-card-actions>
                        <v-btn
                            class="ms-4"
                            append-icon="mdi-trash-can-outline"
                            color="red"
                            variant="tonal"
                            @click="this.reset_form_add_new_item_imo()"
                            >Reset form</v-btn
                        >
                    </v-card-actions>

                    <!-- Alert inside form -->
                    <v-card-text>
                        <!-- Form not yet complete -->
                        <v-alert
                            v-model="
                                this.form_insert_new_data_is_not_complete_imo
                            "
                            title="Form not complete yet!"
                            text="Please complete the form to insert new data."
                            type="warning"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>

                        <!-- Fail insert -->
                        <v-alert
                            v-model="this.form_insert_new_data_error_imo"
                            title="Error occur!"
                            :text="this.form_insert_new_data_error_msg_imo"
                            type="error"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>

                        <!-- Success insert data -->
                        <v-alert
                            v-model="this.is_success_insert_new_data_imo"
                            class="mx-auto mb-6"
                            elevation="1"
                            closable
                            title="Success"
                            text="New data has been added!"
                            type="success"
                        >
                        </v-alert>
                    </v-card-text>

                    <!-- Form -->
                    <v-card-text>
                        <v-text-field
                            model-value="(Auto Increnment)"
                            label="id_key"
                            variant="outlined"
                            disabled
                        ></v-text-field>

                        <v-text-field
                            v-model="this.newItem_imo.no"
                            label="no*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-text-field
                            v-model="this.newItem_imo.contest_category"
                            label="contest_category"
                            variant="outlined"
                            disabled
                        ></v-text-field>

                        <v-text-field
                            v-model="this.newItem_imo.contest_name"
                            label="contest_name*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-text-field
                            v-model="this.newItem_imo.year"
                            label="year (must be integer)*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-text-field
                            v-model="this.newItem_imo.link"
                            label="link*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-text-field
                            v-model="this.newItem_imo.pdf"
                            label="pdf*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-textarea
                            v-model="this.newItem_imo.post_rendered"
                            label="post_rendered*"
                            variant="outlined"
                            clearable
                            auto-grow
                        ></v-textarea>

                        <v-textarea
                            v-model="this.newItem_imo.post_canonical"
                            label="post_canonical*"
                            variant="outlined"
                            clearable
                            auto-grow
                        ></v-textarea>

                        <v-select
                            label="label*"
                            v-model="this.newItem_imo.label"
                            :items="this.array_of_labels"
                            variant="solo-inverted"
                            clearable
                        ></v-select>
                    </v-card-text>

                    <!-- Button -->
                    <v-card-actions>
                        <v-btn
                            class="ms-4"
                            min-height="40"
                            min-width="170"
                            color="red"
                            @click="showAddDialog_imo = false"
                            prepend-icon="mdi-close"
                            variant="outlined"
                            >Close</v-btn
                        >
                        <v-spacer></v-spacer>
                        <v-btn
                            class="me-4"
                            min-height="40"
                            min-width="190"
                            color="teal"
                            append-icon="mdi-database-plus-outline"
                            @click="this.addItem_imo()"
                            variant="flat"
                            >Add</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!-- Alert outisde dialog -->
            <div class="mb-4">
                <!-- Form not yet complete -->
                <v-alert
                    v-model="this.form_insert_new_data_is_not_complete_imo"
                    title="Form not complete yet!"
                    text="Please complete the form to insert new data."
                    type="warning"
                    border="start"
                    variant="tonal"
                    closable
                >
                </v-alert>

                <!-- Fail insert -->
                <v-alert
                    v-model="this.form_insert_new_data_error_imo"
                    title="Error occur!"
                    :text="this.form_insert_new_data_error_msg_imo"
                    type="error"
                    border="start"
                    variant="tonal"
                    closable
                >
                </v-alert>

                <!-- Success insert data -->
                <v-alert
                    v-model="this.is_success_insert_new_data_imo"
                    class="mx-auto mb-6"
                    elevation="1"
                    closable
                    title="Success"
                    text="New data has been added!"
                    type="success"
                >
                </v-alert>

                <!-- EDIT ALERT -->
                <!-- success -->
                <v-alert
                    v-model="this.success_update_or_edit_row_imo"
                    class="mx-auto mb-6"
                    elevation="1"
                    closable
                    title="Success"
                    text="Row updated/edited successfully!"
                    type="success"
                >
                </v-alert>

                <!-- Form not yet complete -->
                <v-alert
                    v-model="this.form_update_edit_is_not_complete_imo"
                    title="Form not complete yet!"
                    text="Please complete the form to update row."
                    type="warning"
                    border="start"
                    variant="tonal"
                    closable
                >
                </v-alert>

                <!-- DELETE ALERT -->
                <v-alert
                    v-model="this.delete_row_success_or_done"
                    class="mx-auto mb-6"
                    elevation="1"
                    closable
                    title="Success"
                    text="Row deleted!"
                    type="success"
                >
                </v-alert>
            </div>

            <!-- Table -->
            <v-data-table
                class="mb-10 table-color"
                :loading="this.loading_imo"
                :items-per-page="this.itemsPerPage_imo"
                :items-length="totalItems_imo"
                :headers="this.headers_imo"
                :items="this.items_imo"
            >
                <!-- post_rendered -->
                <template v-slot:item.post_rendered="{ value }">
                    <div class="py-1" v-html="value"></div>
                </template>
                <!-- contest_name -->
                <template v-slot:item.contest_name="{ value }">
                    <v-chip color="light-blue-darken-2" density="compact">{{
                        value
                    }}</v-chip>
                </template>
                <!-- year -->
                <template v-slot:item.year="{ value }">
                    <v-chip color="teal-darken-2" density="compact">{{
                        value
                    }}</v-chip>
                </template>
                <!-- label -->
                <template v-slot:item.label="{ value }">
                    <v-chip
                        :color="chips_label_color(value)"
                        density="compact"
                        >{{ value }}</v-chip
                    >
                </template>
                <!-- link -->
                <template v-slot:item.link="{ value }">
                    <v-btn
                        icon="mdi-eye-outline"
                        color="deep-purple-lighten-3"
                        density="comfortable"
                        size="small"
                        @click="this.showdialogLINK_imo = true"
                    ></v-btn>
                    <v-dialog
                        max-width="810px"
                        v-model="this.showdialogLINK_imo"
                    >
                        <v-card class="pa-3">
                            <!-- <v-card-title>Preview link</v-card-title> -->
                            <v-card-text>{{ value }}</v-card-text>
                            <v-card-text
                                ><a
                                    :href="value"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    >Click to open link above</a
                                ></v-card-text
                            >
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn
                                    min-width="120px"
                                    append-icon="mdi-close"
                                    variant="outlined"
                                    color="red"
                                    @click="this.showdialogLINK_imo = false"
                                    >close</v-btn
                                >
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </template>
                <!-- pdf -->
                <template v-slot:item.pdf="{ value }">
                    <v-btn
                        icon="mdi-eye-outline"
                        color="deep-purple-lighten-3"
                        density="comfortable"
                        size="small"
                        @click="this.showdialogPDF_imo = true"
                    ></v-btn>
                    <v-dialog
                        max-width="810px"
                        v-model="this.showdialogPDF_imo"
                    >
                        <v-card class="pa-3">
                            <!-- <v-card-title>Preview link</v-card-title> -->
                            <v-card-text>{{ value }}</v-card-text>
                            <v-card-text
                                ><a
                                    :href="value"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    >Click to open link above</a
                                ></v-card-text
                            >
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn
                                    min-width="120px"
                                    append-icon="mdi-close"
                                    variant="outlined"
                                    color="red"
                                    @click="this.showdialogPDF_imo = false"
                                    >close</v-btn
                                >
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </template>

                <!-- action edit -->
                <template v-slot:item.action_edit="{ item }">
                    <v-icon
                        class="me-2"
                        size="small"
                        @click="this.showEditItem_imo(item)"
                    >
                        mdi-pencil
                    </v-icon>
                </template>
                <!-- action delete -->
                <template v-slot:item.action_delete="{ item }">
                    <v-icon
                        class="me-2"
                        size="small"
                        @click="this.confirmDeleteRow_imo(item.id_key)"
                    >
                        mdi-delete
                    </v-icon>
                </template>
            </v-data-table>

            <!-- Dialog edit row -->
            <v-dialog v-model="showEditDialog_imo" max-width="1100px">
                <v-card class="pa-3 pb-5">
                    <v-card-title
                        >Update/Edit Row <span class="mdi mdi-pencil"></span
                    ></v-card-title>
                    <v-card-text> Update or edit row to database </v-card-text>

                    <!-- Alert inside form -->
                    <v-card-text>
                        <!-- Fail update or edit -->
                        <v-alert
                            v-model="this.form_update_or_edit_row_error_imo"
                            title="Error occur!"
                            :text="this.form_update_or_edit_row_error_mgs_imo"
                            type="error"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>

                        <!-- Form not yet complete -->
                        <v-alert
                            v-model="this.form_update_edit_is_not_complete_imo"
                            title="Form not complete yet!"
                            text="Please complete the form to update row."
                            type="warning"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>
                    </v-card-text>

                    <!-- form -->
                    <v-card-text>
                        <v-text-field
                            v-model="this.editedItem_imo.id_key"
                            label="id_key"
                            variant="outlined"
                            disabled
                        ></v-text-field>

                        <v-text-field
                            v-model="this.editedItem_imo.no"
                            label="no*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-text-field
                            v-model="this.editedItem_imo.contest_category"
                            label="contest_category"
                            variant="outlined"
                            disabled
                        ></v-text-field>

                        <v-text-field
                            v-model="this.editedItem_imo.contest_name"
                            label="contest_name*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-text-field
                            v-model="this.editedItem_imo.year"
                            label="year (must be integer)*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-text-field
                            v-model="this.editedItem_imo.link"
                            label="link*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-text-field
                            v-model="this.editedItem_imo.pdf"
                            label="pdf*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-textarea
                            v-model="this.editedItem_imo.post_rendered"
                            label="post_rendered*"
                            variant="outlined"
                            clearable
                            auto-grow
                        ></v-textarea>

                        <v-textarea
                            v-model="this.editedItem_imo.post_canonical"
                            label="post_canonical*"
                            variant="outlined"
                            clearable
                            auto-grow
                        ></v-textarea>

                        <v-select
                            label="label*"
                            v-model="this.editedItem_imo.label"
                            :items="this.array_of_labels"
                            variant="underlined"
                            clearable
                        ></v-select>
                    </v-card-text>

                    <v-card-actions>
                        <v-btn
                            class="ms-4"
                            min-height="40"
                            min-width="170"
                            color="red"
                            prepend-icon="mdi-close"
                            variant="outlined"
                            @click="showEditDialog_imo = false"
                            >Close</v-btn
                        >
                        <v-spacer></v-spacer>
                        <v-btn
                            class="me-4"
                            min-height="40"
                            min-width="190"
                            color="teal"
                            append-icon="mdi-pencil-outline"
                            variant="flat"
                            @click="this.saveUpdatedOrEditedItem_imo()"
                            >Update</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!-- Dialog delete row -->
            <v-dialog v-model="showDeleteConfirmation_imo" max-width="500px">
                <v-card class="pa-3 pb-5">
                    <v-card-title>Confirm Delete</v-card-title>
                    <v-card-text
                        >Are you sure you want to delete this row?</v-card-text
                    >
                    <v-card-actions>
                        <v-btn
                            class="ms-4"
                            min-height="40"
                            min-width="170"
                            color="red"
                            prepend-icon="mdi-close"
                            variant="outlined"
                            @click="showDeleteConfirmation_imo = false"
                            >Cancel</v-btn
                        >
                        <v-spacer></v-spacer>
                        <v-btn
                            class="me-4"
                            min-height="40"
                            min-width="190"
                            color="error"
                            append-icon="mdi-delete-outline"
                            variant="flat"
                            @click="this.deleteItem()"
                            >Delete</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!-- ################################################ -->
            <!-- Button -->
            <div class="d-flex mb-3">
                <h2 class="me-5">Table `admins`</h2>
                <v-btn
                    variant="flat"
                    color="teal"
                    append-icon="mdi-database-plus-outline"
                    >Add New</v-btn
                >
            </div>

            <h1 class="text-center">COMING SOON</h1>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { useRouter } from "vue-router/auto";

export default {
    data: () => ({
        array_of_labels: [
            "None",
            "Algebra",
            "Geometry",
            "Combinatorics",
            "Number Theory",
        ],
        itemsPerPage_imo: 5,
        totalItems_imo: 0,
        items_imo: [],
        headers_imo: [
            {
                title: "id_key",
                sortable: true,
                key: "id_key",
                align: "start",
            },
            { title: "no", sortable: true, key: "no", align: "start" },
            {
                title: "post_rendered",
                sortable: false,
                key: "post_rendered",
                align: "start",
            },
            {
                title: "post_canonical",
                sortable: false,
                key: "post_canonical",
                align: "start",
            },
            {
                title: "label",
                sortable: true,
                key: "label",
                align: "start",
            },
            { title: "year", sortable: true, key: "year", align: "start" },
            {
                title: "contest_name",
                sortable: true,
                key: "contest_name",
                align: "start",
            },
            {
                title: "contest_category",
                sortable: false,
                key: "contest_category",
                align: "start",
            },
            {
                title: "link",
                sortable: false,
                key: "link",
                align: "start",
            },
            {
                title: "pdf",
                sortable: false,
                key: "pdf",
                align: "start",
            },
            {
                title: "Actions",
                sortable: false,
                key: "actions",
                align: "center",
                children: [
                    {
                        title: "Edit",
                        sortable: false,
                        key: "action_edit",
                        align: "center",
                    },
                    {
                        title: "Delete",
                        sortable: false,
                        key: "action_delete",
                        align: "center",
                    },
                ],
            },
        ],
        newItem_imo: {
            no: "",
            contest_category: "International Contest",
            contest_name: "",
            year: "",
            link: "",
            pdf: "",
            post_rendered: "",
            post_canonical: "",
            label: "None",
        },
        is_success_insert_new_data_imo: false,
        form_insert_new_data_is_not_complete_imo: false,
        form_insert_new_data_error_imo: false,
        form_insert_new_data_error_msg_imo: "",
        showAddDialog_imo: false,
        showdialogLINK_imo: false,
        showdialogPDF_imo: false,
        showEditDialog_imo: false,
        editedItem_imo: {
            id_key: "",
            no: "",
            contest_category: "International Contest",
            contest_name: "",
            year: "",
            link: "",
            pdf: "",
            post_rendered: "",
            post_canonical: "",
            label: "None",
        },
        success_update_or_edit_row_imo: false,
        form_update_edit_is_not_complete_imo: false,
        form_update_or_edit_row_error_imo: false,
        form_update_or_edit_row_error_mgs_imo: "",
        showDeleteConfirmation_imo: false,
        selectedItemIDKEYToDelete_imo: -Infinity,
        delete_row_success_or_done: false,

        loading_imo: false,
    }),

    methods: {
        async initialize() {
            this.loading_imo = true;
            try {
                const raw_response = await axios.get("admin/get_imo_data");
                const response = raw_response.data;
                this.items_imo = response;
                this.totalItems_imo = response.itemsLength;
            } catch (err) {
                console.log(err.message);
            } finally {
                this.loading_imo = false;
            }
        },

        chips_label_color(label) {
            if (label === null || label === "") {
                return "red-darken-4";
            }
            if (label === "Algebra") {
                return "deep-purple";
            }
            if (label === "Combinatorics") {
                return "brown";
            }
            if (label === "Geometry") {
                return "purple";
            }
            if (label === "Number Theory") {
                return "blue-grey";
            }
        },
        reset_form_add_new_item_imo() {
            this.newItem_imo = {
                no: "",
                contest_category: "International Contest",
                contest_name: "",
                year: "",
                link: "",
                pdf: "",
                post_rendered: "",
                post_canonical: "",
                label: "None",
            };
        },
        function_showAddDialog_imo() {
            this.showAddDialog_imo = true;
            this.is_success_insert_new_data_imo = false;
            this.form_insert_new_data_is_not_complete_imo = false;
            this.form_insert_new_data_error_imo = false;
        },
        async addItem_imo() {
            this.is_success_insert_new_data_imo = false;
            this.form_insert_new_data_is_not_complete_imo = false;
            this.form_insert_new_data_error_imo = false;

            for (let key in this.newItem_imo) {
                if (
                    this.newItem_imo[key] === "" ||
                    this.newItem_imo[key] === null
                ) {
                    this.form_insert_new_data_is_not_complete_imo = true;
                    return;
                }
            }

            try {
                const raw_response = await axios.post(
                    "admin/insert_new_data_imo",
                    this.newItem_imo
                );
                const response = raw_response.data;
                console.log("RESPONSE", response.msg);

                this.is_success_insert_new_data_imo = true;
                this.reset_form_add_new_item_imo();

                this.initialize();
            } catch (error) {
                console.log("ERROR1:", error.message);
                console.log("ERROR2:", error.response.data.msg);
                this.form_insert_new_data_error_imo = true;
                this.form_insert_new_data_error_msg_imo =
                    error.response.data.msg;
            }
        },

        showEditItem_imo(item) {
            this.success_update_or_edit_row_imo = false;
            this.form_update_edit_is_not_complete_imo = false;
            this.form_update_or_edit_row_error_imo = false;
            this.editedItem_imo = Object.assign(this.editedItem_imo, item);
            this.showEditDialog_imo = true;
        },
        async saveUpdatedOrEditedItem_imo() {
            for (let key in this.editedItem_imo) {
                if (
                    this.editedItem_imo[key] === "" ||
                    this.editedItem_imo[key] === null
                ) {
                    this.form_update_edit_is_not_complete_imo = true;
                    return;
                }
            }

            try {
                const raw_response = await axios.post(
                    "admin/update_row_imo",
                    this.editedItem_imo
                );
                const response = raw_response.data;
                console.log("RESPONSE", response.msg);
                this.success_update_or_edit_row_imo = true;

                this.showEditDialog_imo = false;
                this.initialize();
            } catch (error) {
                console.log("ERROR1:", error.message);
                console.log("ERROR2:", error.response.data.msg);
                this.form_update_or_edit_row_error_imo = true;
                this.form_update_or_edit_row_error_mgs_imo =
                    error.response.data.msg;
            }
        },

        confirmDeleteRow_imo(id_key) {
            this.delete_row_success_or_done = false;
            this.selectedItemIDKEYToDelete_imo = id_key;
            this.showDeleteConfirmation_imo = true;
        },
        async deleteItem() {
            try {
                const raw_response = await axios.post("admin/delete_row_imo", {
                    id_key: this.selectedItemIDKEYToDelete_imo,
                });
                const response = raw_response.data;
                this.delete_row_success_or_done = true;
                this.initialize();
            } catch (error) {
                console.log("ERROR1:", error.message);
                console.log("ERROR2:", error.response.data.msg);
            }
            this.showDeleteConfirmation_imo = false;
        },

        async logout() {
            try {
                const raw_response = await axios.post("admin/logout");

                localStorage.removeItem("token");
                this.router.push({ path: "/admin/login" });
            } catch (err) {
                console.log(err.message);
            }
        },
    },

    mounted() {
        this.initialize();
    },

    setup() {
        const router = useRouter();
        return { router };
    },
};
</script>

<style scoped>
.table-color {
    border-radius: 8px;
    background-color: #e0f2f1;
}
</style>
