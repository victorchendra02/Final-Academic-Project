<template>
    <v-toolbar border density="default" color="cyan-darken-1" app>
        <template v-slot:title>
            <h2>Admin <span class="mdi mdi-account-check"></span></h2>
        </template>
        <v-btn
            min-height="40px"
            min-width="160px"
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

            <!-- imo -->
            <!-- ####################################################################### -->
            <v-divider class="mb-8 border-opacity-25" thickness="2"></v-divider>

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
            <v-dialog v-model="showAddDialog_imo" max-width="1000px">
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

                        <!-- User select Auto or Manual -->
                        <v-select
                            label="How to label?"
                            v-model="selected_how_to_label_4_newdata_imo"
                            :items="array_options_how_to_label_4_newdata_imo"
                            variant="outlined"
                        ></v-select>

                        <!-- HORIZONTAL LINE -->
                        <h2
                            :class="
                                selected_how_to_label_4_newdata_imo ===
                                array_options_how_to_label_4_newdata_imo[0]
                                    ? 'text-teal-darken-2'
                                    : 'text-indigo-darken-2'
                            "
                            class="mt-2"
                        >
                            {{
                                selected_how_to_label_4_newdata_imo === null
                                    ? "null"
                                    : selected_how_to_label_4_newdata_imo
                            }}
                            <span
                                v-if="
                                    selected_how_to_label_4_newdata_imo ===
                                    array_options_how_to_label_4_newdata_imo[0]
                                        ? true
                                        : false
                                "
                                class="mdi-head-cog"
                            ></span>
                            <span
                                v-if="
                                    selected_how_to_label_4_newdata_imo ===
                                    array_options_how_to_label_4_newdata_imo[1]
                                        ? true
                                        : false
                                "
                                class="mdi-creation"
                            ></span>
                        </h2>
                        <v-divider
                            class="mb-4 border-opacity-25"
                            thickness="4"
                            :color="
                                selected_how_to_label_4_newdata_imo ===
                                array_options_how_to_label_4_newdata_imo[0]
                                    ? 'teal-darken-2'
                                    : 'indigo-darken-2'
                            "
                        ></v-divider>

                        <!-- SELECT LABEL -->
                        <v-select
                            v-if="
                                this.selected_how_to_label_4_newdata_imo ===
                                array_options_how_to_label_4_newdata_imo[0]
                                    ? true
                                    : false
                            "
                            label="label*"
                            v-model="this.newItem_imo.label"
                            :items="this.array_of_labels"
                            variant="outlined"
                            color="teal-darken-2"
                        ></v-select>

                        <!-- SELECT MODEL -->
                        <v-select
                            v-if="
                                this.selected_how_to_label_4_newdata_imo ===
                                array_options_how_to_label_4_newdata_imo[1]
                                    ? true
                                    : false
                            "
                            label="Select model to perform auto label"
                            v-model="this.selected_model_4_newdata_imo"
                            :items="this.array_options_model_4_newdata_imo"
                            variant="outlined"
                            color="indigo-darken-2"
                        ></v-select>

                        <v-btn
                            v-if="
                                this.selected_how_to_label_4_newdata_imo ===
                                array_options_how_to_label_4_newdata_imo[1]
                                    ? true
                                    : false
                            "
                            class="mb-4"
                            min-height="45"
                            color="indigo-darken-1"
                            @click="classify_newdata_imo()"
                            append-icon="mdi-arrow-right"
                            elevation="0"
                            :loading="loading_button_4_newdata_classify_imo"
                            block
                            >Check result</v-btn
                        >

                        <div
                            v-if="
                                this.selected_how_to_label_4_newdata_imo ===
                                array_options_how_to_label_4_newdata_imo[1]
                                    ? true
                                    : false
                            "
                            class="pb-4 text-center"
                        >
                            <h2>
                                {{
                                    this
                                        .classification_label_result_4_newdata_imo
                                }}
                            </h2>

                            Algebra:
                            {{
                                (
                                    this
                                        .classification_proba_result_4_newdata_imo[
                                        "Algebra"
                                    ] * 100
                                ).toFixed(2)
                            }}%<br />
                            Combinatorics:
                            {{
                                (
                                    this
                                        .classification_proba_result_4_newdata_imo[
                                        "Combinatorics"
                                    ] * 100
                                ).toFixed(2)
                            }}%<br />
                            Geometry:
                            {{
                                (
                                    this
                                        .classification_proba_result_4_newdata_imo[
                                        "Geometry"
                                    ] * 100
                                ).toFixed(2)
                            }}%<br />
                            Number Theory:
                            {{
                                (
                                    this
                                        .classification_proba_result_4_newdata_imo[
                                        "Number Theory"
                                    ] * 100
                                ).toFixed(2)
                            }}%<br /><br />

                            <span class="font-italic">{{
                                this.selected_fix_model_4_newdata_imo
                            }}</span>

                            <v-divider
                                class="mt-5 border-opacity-25"
                                thickness="4"
                                color="indigo-darken-2"
                            ></v-divider>
                        </div>
                    </v-card-text>

                    <!-- Alert inside form -->
                    <v-card-text class="py-0 pb-6">
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

                        <!-- post canonical empty nothing to classify alert -->
                        <v-alert
                            v-model="
                                this
                                    .alert_null_post_canonical_newdata_to_classify_imo
                            "
                            title="Nothing to classify!"
                            type="info"
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

                        <!-- Error auto label alert -->
                        <v-alert
                            v-model="this.alert_err_msg_4_newdata_imo"
                            title="Error occur!"
                            :text="this.catch_err_msg_4_newdata_imo"
                            type="error"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>

                        <!-- Success insert data -->
                        <v-alert
                            v-model="this.is_success_insert_new_data_imo"
                            elevation="1"
                            closable
                            title="Success"
                            text="New data has been added!"
                            type="success"
                        >
                        </v-alert>
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
                            :loading="loading_button_4_add_newdata_imo"
                            >Add</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!-- Alert outside dialog -->
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
                    v-model="this.delete_row_success_or_done_imo"
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
                :loading="this.loading_4_all_tables"
                :items-per-page="this.itemsPerPage_4_all"
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
                        @click="
                            this.function_showDialog_linkANDpdf_imo(
                                value,
                                'link'
                            )
                        "
                    ></v-btn>
                </template>
                <!-- pdf -->
                <template v-slot:item.pdf="{ value }">
                    <v-btn
                        icon="mdi-eye-outline"
                        color="deep-purple-lighten-3"
                        density="comfortable"
                        size="small"
                        @click="
                            this.function_showDialog_linkANDpdf_imo(
                                value,
                                'pdf'
                            )
                        "
                    ></v-btn>
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

            <!-- DialogShow link -->
            <v-dialog max-width="810px" v-model="this.showdialogLINK_imo">
                <v-card class="pa-3">
                    <!-- <v-card-title>Preview link</v-card-title> -->
                    <v-card-text>{{ this.tempvalueLINK }}</v-card-text>
                    <v-card-text
                        ><a
                            :href="this.tempvalueLINK"
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
            <!-- DialogShow pdf -->
            <v-dialog max-width="810px" v-model="this.showdialogPDF_imo">
                <v-card class="pa-3">
                    <!-- <v-card-title>Preview link</v-card-title> -->
                    <v-card-text>{{ this.tempvaluePDF }}</v-card-text>
                    <v-card-text
                        ><a
                            :href="this.tempvaluePDF"
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
            <!-- Dialog edit row -->
            <v-dialog v-model="showEditDialog_imo" max-width="1000px">
                <v-card class="pa-3 pb-5">
                    <v-card-title
                        >Update/Edit Row <span class="mdi mdi-pencil"></span
                    ></v-card-title>
                    <v-card-text> Update or edit row to database </v-card-text>

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

                        <!-- User select Auto or Manual -->
                        <v-select
                            label="How to label?"
                            v-model="selected_how_to_label_4_editdata_imo"
                            :items="array_options_how_to_label_4_editdata_imo"
                            variant="outlined"
                        ></v-select>

                        <!-- HORIZONTAL LINE -->
                        <h2
                            :class="
                                selected_how_to_label_4_editdata_imo ===
                                array_options_how_to_label_4_editdata_imo[0]
                                    ? 'text-teal-darken-2'
                                    : 'text-indigo-darken-2'
                            "
                            class="mt-2"
                        >
                            {{
                                selected_how_to_label_4_editdata_imo === null
                                    ? "null"
                                    : selected_how_to_label_4_editdata_imo
                            }}
                            <span
                                v-if="
                                    selected_how_to_label_4_editdata_imo ===
                                    array_options_how_to_label_4_editdata_imo[0]
                                        ? true
                                        : false
                                "
                                class="mdi-head-cog"
                            ></span>
                            <span
                                v-if="
                                    selected_how_to_label_4_editdata_imo ===
                                    array_options_how_to_label_4_editdata_imo[1]
                                        ? true
                                        : false
                                "
                                class="mdi-creation"
                            ></span>
                        </h2>
                        <v-divider
                            class="mb-4 border-opacity-25"
                            thickness="4"
                            :color="
                                selected_how_to_label_4_editdata_imo ===
                                array_options_how_to_label_4_editdata_imo[0]
                                    ? 'teal-darken-2'
                                    : 'indigo-darken-2'
                            "
                        ></v-divider>

                        <!-- SELECT LABEL -->
                        <v-select
                            v-if="
                                this.selected_how_to_label_4_editdata_imo ===
                                array_options_how_to_label_4_editdata_imo[0]
                                    ? true
                                    : false
                            "
                            label="label*"
                            v-model="this.editedItem_imo.label"
                            :items="this.array_of_labels"
                            variant="outlined"
                            color="teal-darken-2"
                        ></v-select>

                        <!-- SELECT MODEL -->
                        <v-select
                            v-if="
                                this.selected_how_to_label_4_editdata_imo ===
                                array_options_how_to_label_4_editdata_imo[1]
                                    ? true
                                    : false
                            "
                            label="Select model to perform auto label"
                            v-model="this.selected_model_4_editdata_imo"
                            :items="this.array_options_model_4_editdata_imo"
                            variant="outlined"
                            color="indigo-darken-2"
                        ></v-select>

                        <v-btn
                            v-if="
                                this.selected_how_to_label_4_editdata_imo ===
                                array_options_how_to_label_4_editdata_imo[1]
                                    ? true
                                    : false
                            "
                            class="mb-4"
                            min-height="45"
                            color="indigo-darken-1"
                            @click="classify_editdata_imo()"
                            append-icon="mdi-arrow-right"
                            elevation="0"
                            :loading="loading_button_4_editdata_classify_imo"
                            block
                            >Check result</v-btn
                        >

                        <div
                            v-if="
                                this.selected_how_to_label_4_editdata_imo ===
                                array_options_how_to_label_4_editdata_imo[1]
                                    ? true
                                    : false
                            "
                            class="pb-4 text-center"
                        >
                            <h2>
                                {{
                                    this
                                        .classification_label_result_4_editdata_imo
                                }}
                            </h2>

                            Algebra:
                            {{
                                (
                                    this
                                        .classification_proba_result_4_editdata_imo[
                                        "Algebra"
                                    ] * 100
                                ).toFixed(2)
                            }}%<br />
                            Combinatorics:
                            {{
                                (
                                    this
                                        .classification_proba_result_4_editdata_imo[
                                        "Combinatorics"
                                    ] * 100
                                ).toFixed(2)
                            }}%<br />
                            Geometry:
                            {{
                                (
                                    this
                                        .classification_proba_result_4_editdata_imo[
                                        "Geometry"
                                    ] * 100
                                ).toFixed(2)
                            }}%<br />
                            Number Theory:
                            {{
                                (
                                    this
                                        .classification_proba_result_4_editdata_imo[
                                        "Number Theory"
                                    ] * 100
                                ).toFixed(2)
                            }}%<br /><br />

                            <span class="font-italic">{{
                                this.selected_fix_model_4_editdata_imo
                            }}</span>

                            <v-divider
                                class="mt-5 border-opacity-25"
                                thickness="4"
                                color="indigo-darken-2"
                            ></v-divider>
                        </div>
                    </v-card-text>

                    <!-- Alert inside form -->
                    <v-card-text class="py-0 pb-6">
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

                        <!-- post canonical empty nothing to classify alert -->
                        <v-alert
                            v-model="
                                this
                                    .alert_null_post_canonical_editdata_to_classify_imo
                            "
                            title="Nothing to classify!"
                            type="info"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>

                        <!-- Error auto label alert -->
                        <v-alert
                            v-model="this.alert_err_msg_4_editdata_imo"
                            title="Error occur!"
                            :text="this.catch_err_msg_4_editdata_imo"
                            type="error"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>
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
                            :loading="loading_button_4_add_editdata_imo"
                            >Update</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <!-- Dialog delete row -->
            <v-dialog
                v-model="showDeleteDialogConfirmation_imo"
                max-width="500px"
            >
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
                            @click="showDeleteDialogConfirmation_imo = false"
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
                            @click="this.deleteItem_imo()"
                            >Delete</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!-- admins -->
            <!-- ####################################################################### -->
            <v-divider class="mb-8 border-opacity-25" thickness="2"></v-divider>

            <!-- Button add item-->
            <div class="d-flex mb-3">
                <h2 class="me-5">Table `admins`</h2>
                <v-btn
                    variant="flat"
                    color="teal"
                    append-icon="mdi-database-plus-outline"
                    @click="this.function_showAddDialog_admins()"
                    >Add New</v-btn
                >
            </div>

            <!-- Dialog new data ADMINS -->
            <v-dialog v-model="showAddDialog_admins" max-width="720px">
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
                            @click="this.reset_form_add_new_item_admins()"
                            >Reset form</v-btn
                        >
                    </v-card-actions>

                    <!-- Alert inside form -->
                    <v-card-text>
                        <!-- Form not yet complete -->
                        <v-alert
                            v-model="
                                this.form_insert_new_data_is_not_complete_admins
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
                            v-model="this.form_insert_new_data_error_admins"
                            title="Error occur!"
                            :text="this.form_insert_new_data_error_msg_admins"
                            type="error"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>

                        <!-- Success insert data -->
                        <v-alert
                            v-model="this.is_success_insert_new_data_admins"
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
                            id="newAdmin"
                            v-model="this.newItem_admins.username"
                            label="username*"
                            variant="outlined"
                            prepend-inner-icon="mdi-account-box-outline"
                            clearable
                        ></v-text-field>

                        <v-text-field
                            id="newAdmin"
                            v-model="this.newItem_admins.password"
                            label="password*"
                            variant="outlined"
                            prepend-inner-icon="mdi-lock-outline"
                            @click:append-inner="
                                this.toggle_visiblity_password_newdata_admin =
                                    !this
                                        .toggle_visiblity_password_newdata_admin
                            "
                            :append-inner-icon="
                                this.toggle_visiblity_password_newdata_admin
                                    ? 'mdi-eye-off'
                                    : 'mdi-eye'
                            "
                            :type="
                                this.toggle_visiblity_password_newdata_admin
                                    ? 'text'
                                    : 'password'
                            "
                            clearable
                        ></v-text-field>

                        <v-text-field
                            v-model="this.newItem_admins.full_name"
                            label="full_name*"
                            variant="outlined"
                            clearable
                        ></v-text-field>

                        <v-textarea
                            v-model="this.newItem_admins.description"
                            label="description*"
                            variant="outlined"
                            clearable
                            auto-grow
                        ></v-textarea>
                    </v-card-text>

                    <!-- Button -->
                    <v-card-actions>
                        <v-btn
                            class="ms-4"
                            min-height="40"
                            min-width="170"
                            color="red"
                            @click="showAddDialog_admins = false"
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
                            @click="this.addItem_admins()"
                            variant="flat"
                            >Add</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!-- Alert outside dialog -->
            <div class="mb-4">
                <!-- Form not yet complete -->
                <v-alert
                    v-model="this.form_insert_new_data_is_not_complete_admins"
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
                    v-model="this.form_insert_new_data_error_admins"
                    title="Error occur!"
                    :text="this.form_insert_new_data_error_msg_admins"
                    type="error"
                    border="start"
                    variant="tonal"
                    closable
                >
                </v-alert>

                <!-- Success insert data -->
                <v-alert
                    v-model="this.is_success_insert_new_data_admins"
                    class="mx-auto mb-6"
                    elevation="1"
                    closable
                    title="Success"
                    text="New data has been added!"
                    type="success"
                >
                </v-alert>
            </div>

            <!-- Table -->
            <v-data-table
                class="mb-10 table-color"
                :loading="this.loading_4_all_tables"
                :items-per-page="this.itemsPerPage_4_all"
                :items-length="totalItems_admins"
                :headers="this.headers_admins"
                :items="this.items_admins"
            >
                <!-- password -->
                <template v-slot:item.password="{ value }">
                    {{ value.slice(0, 48) + "..." }}
                </template>
                <!-- is_active -->
                <template v-slot:item.is_active="{ value }">
                    <v-chip color="indigo-darken-2" density="compact">{{
                        value
                    }}</v-chip>
                </template>
            </v-data-table>

            <!-- home_data -->
            <!-- ####################################################################### -->
            <v-divider class="mb-8 border-opacity-25" thickness="2"></v-divider>

            <!-- Button reset home_data -->
            <div class="d-flex mb-3">
                <h2 class="me-5">Table `home_data`</h2>
                <v-btn
                    variant="flat"
                    color="teal"
                    append-icon="mdi-database-refresh-outline"
                    @click="this.function_showRegenerateDialog_homedata()"
                    >Regenerate</v-btn
                >
            </div>

            <!-- Dialog regenerate homedata -->
            <v-dialog
                v-model="this.showRegenerateDialog_homedata"
                max-width="500px"
            >
                <v-card class="pa-3 pb-5">
                    <v-card-title>Confirm Regenerate</v-card-title>
                    <v-card-text
                        >Are you sure you want to regenerate table
                        `home_data`?</v-card-text
                    >
                    <v-card-actions>
                        <v-btn
                            class="ms-4"
                            min-height="40"
                            min-width="170"
                            color="red"
                            prepend-icon="mdi-close"
                            variant="outlined"
                            @click="this.showRegenerateDialog_homedata = false"
                            >Cancel</v-btn
                        >
                        <v-spacer></v-spacer>
                        <v-btn
                            class="me-4"
                            min-height="40"
                            min-width="190"
                            color="error"
                            append-icon="mdi-database-refresh-outline"
                            variant="flat"
                            @click="this.regenerate_homedata()"
                            >Regenerate</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!-- Alert outside dialog -->
            <div class="mb-4">
                <!-- Fail regenerate homedata -->
                <v-alert
                    v-model="this.is_error_regenerate_homedata"
                    title="Error occur!"
                    :text="this.msg_error_response_regenerate_homedata"
                    type="error"
                    border="start"
                    variant="tonal"
                    closable
                >
                </v-alert>

                <!-- Success regenerate homedata -->
                <v-alert
                    v-model="this.is_success_regenerate_homedata"
                    class="mx-auto mb-6"
                    elevation="1"
                    closable
                    title="Success"
                    :text="this.msg_success_response_regenerate_homedata"
                    type="success"
                >
                </v-alert>
            </div>

            <!-- Table -->
            <v-data-table
                class="mb-10 table-color"
                :loading="this.loading_4_all_tables"
                :items-per-page="this.itemsPerPage_4_all"
                :items-length="totalItems_homedata"
                :headers="this.headers_homedata"
                :items="this.items_homedata"
            >
                <template v-slot:item.year="{ value }">
                    <v-chip color="teal-darken-2" density="compact">{{
                        value
                    }}</v-chip>
                </template>
                <template v-slot:item.label="{ value }">
                    <v-chip
                        :color="this.chips_label_color(value)"
                        density="compact"
                        >{{ value }}</v-chip
                    >
                </template>
            </v-data-table>

            <!-- models -->
            <!-- ####################################################################### -->
            <v-divider class="mb-8 border-opacity-25" thickness="2"></v-divider>

            <!-- Button add item -->
            <div class="d-flex mb-3">
                <h2 class="me-5">Table `models`</h2>
                <v-btn
                    variant="flat"
                    color="teal"
                    append-icon="mdi-database-plus-outline"
                    @click="this.function_showAddDialog_models()"
                    >Add New</v-btn
                >
            </div>

            <!-- Dialog new data -->
            <v-dialog v-model="showAddDialog_models" max-width="720px">
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
                            @click="this.reset_form_add_new_item_models()"
                            >Reset form</v-btn
                        >
                    </v-card-actions>

                    <!-- Alert inside form -->
                    <v-card-text>
                        <!-- Form not yet complete -->
                        <v-alert
                            v-model="
                                this.form_insert_new_data_is_not_complete_models
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
                            v-model="this.form_insert_new_data_error_models"
                            title="Error occur!"
                            :text="this.form_insert_new_data_error_msg_models"
                            type="error"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>

                        <!-- Success insert data -->
                        <v-alert
                            v-model="this.is_success_insert_new_data_models"
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
                            label="id_model"
                            variant="outlined"
                            disabled
                        ></v-text-field>

                        <v-select
                            v-model="this.newItem_models.model_type"
                            label="model_type*"
                            :items="['classification', 'regression']"
                            variant="solo-inverted"
                            clearable
                        ></v-select>

                        <v-text-field
                            v-model="this.newItem_models.model_name"
                            label="model_name*"
                            variant="outlined"
                        ></v-text-field>

                        <v-textarea
                            v-model="this.newItem_models.model_path"
                            label="model_path*"
                            variant="outlined"
                            clearable
                            auto-grow
                        ></v-textarea>

                        <v-textarea
                            v-model="
                                this.newItem_models.vectorizer_or_tokenizer_path
                            "
                            label="vectorizer_or_tokenizer_path"
                            variant="outlined"
                            clearable
                            auto-grow
                        ></v-textarea>

                        <v-select
                            v-model="this.newItem_models.is_active"
                            label="is_active*"
                            :items="[0, 1]"
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
                            @click="showAddDialog_models = false"
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
                            @click="this.addItem_models()"
                            variant="flat"
                            >Add</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>

            <!-- Alert outside dialog -->
            <div class="mb-4">
                <!-- Form not yet complete -->
                <v-alert
                    v-model="this.form_insert_new_data_is_not_complete_models"
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
                    v-model="this.form_insert_new_data_error_models"
                    title="Error occur!"
                    :text="this.form_insert_new_data_error_msg_models"
                    type="error"
                    border="start"
                    variant="tonal"
                    closable
                >
                </v-alert>

                <!-- Success insert data -->
                <v-alert
                    v-model="this.is_success_insert_new_data_models"
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
                    v-model="this.success_update_or_edit_row_models"
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
                    v-model="this.form_update_edit_is_not_complete_models"
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
                    v-model="this.delete_row_success_or_done_models"
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
            <!-- :items-per-page="this.itemsPerPage_4_all" -->
            <v-data-table
                class="mb-10 table-color"
                :loading="this.loading_4_all_tables"
                :items-per-page="20"
                :items-length="totalItems_models"
                :headers="this.headers_models"
                :items="this.items_models"
            >
                <template v-slot:item.model_type="{ value }">
                    <v-chip
                        :color="
                            value === 'regression'
                                ? 'indigo-darken-2'
                                : value === 'classification'
                                ? 'teal-darken-2'
                                : 'black'
                        "
                        density="compact"
                        >{{ value }}</v-chip
                    >
                </template>

                <template v-slot:item.vectorizer_or_tokenizer_path="{ value }">
                    <v-chip
                        v-if="value === null || value === ''"
                        color="red-darken-2"
                        density="compact"
                    ></v-chip>
                    <span v-if="value !== null || value !== ''">{{
                        value
                    }}</span>
                </template>

                <template v-slot:item.is_active="{ value }">
                    <v-chip
                        :color="this.chips_isactive_color(value)"
                        density="compact"
                        >{{ value }}</v-chip
                    >
                </template>

                <!-- action edit -->
                <template v-slot:item.action_edit="{ item }">
                    <v-icon
                        class="me-2"
                        size="small"
                        @click="this.showEditItem_models(item)"
                    >
                        mdi-pencil
                    </v-icon>
                </template>
                <!-- action delete -->
                <template v-slot:item.action_delete="{ item }">
                    <v-icon
                        class="me-2"
                        size="small"
                        @click="this.confirmDeleteRow_models(item.id_model)"
                    >
                        mdi-delete
                    </v-icon>
                </template>
            </v-data-table>

            <!-- Dialog edit row -->
            <v-dialog v-model="showEditDialog_models" max-width="720px">
                <v-card class="pa-3 pb-5">
                    <v-card-title
                        >Update/Edit Row <span class="mdi mdi-pencil"></span
                    ></v-card-title>
                    <v-card-text> Update or edit row to database </v-card-text>

                    <!-- Alert inside form -->
                    <v-card-text>
                        <!-- Fail update or edit -->
                        <v-alert
                            v-model="this.form_update_or_edit_row_error_models"
                            title="Error occur!"
                            :text="
                                this.form_update_or_edit_row_error_mgs_models
                            "
                            type="error"
                            border="start"
                            variant="tonal"
                            closable
                        >
                        </v-alert>

                        <!-- Form not yet complete -->
                        <v-alert
                            v-model="
                                this.form_update_edit_is_not_complete_models
                            "
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
                            v-model="this.editedItem_models.id_model"
                            label="id_model"
                            variant="outlined"
                            disabled
                        ></v-text-field>

                        <v-select
                            v-model="this.editedItem_models.model_type"
                            label="model_type*"
                            :items="['classification', 'regression']"
                            variant="solo-inverted"
                            clearable
                        ></v-select>

                        <v-text-field
                            v-model="this.editedItem_models.model_name"
                            label="model_name*"
                            variant="outlined"
                        ></v-text-field>

                        <v-textarea
                            v-model="this.editedItem_models.model_path"
                            label="model_path*"
                            variant="outlined"
                            clearable
                            auto-grow
                        ></v-textarea>

                        <v-textarea
                            v-model="
                                this.editedItem_models
                                    .vectorizer_or_tokenizer_path
                            "
                            label="vectorizer_or_tokenizer_path"
                            variant="outlined"
                            clearable
                            auto-grow
                        ></v-textarea>

                        <v-select
                            v-model="this.editedItem_models.is_active"
                            label="is_active*"
                            :items="[0, 1]"
                            variant="solo-inverted"
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
                            @click="showEditDialog_models = false"
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
                            @click="this.saveUpdatedOrEditedItem_models()"
                            >Update</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <!-- Dialog delete row -->
            <v-dialog
                v-model="showDeleteDialogConfirmation_models"
                max-width="500px"
            >
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
                            @click="showDeleteDialogConfirmation_models = false"
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
                            @click="this.deleteItem_models()"
                            >Delete</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <br />
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

        items_imo: [],
        totalItems_imo: 0,
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
        tempvalueLINK: null,
        tempvaluePDF: null,
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
        showDeleteDialogConfirmation_imo: false,
        selectedItemIDKEYToDelete_imo: -Infinity,
        delete_row_success_or_done_imo: false,
        // How to label
        loading_button_4_add_newdata_imo: false,
        array_options_how_to_label_4_newdata_imo: [], // on --> mounted
        selected_how_to_label_4_newdata_imo: "", // on --> mounted
        // Available models
        array_options_model_4_newdata_imo: [], // on --> async initialize().. API get all active classifier model name
        selected_model_4_newdata_imo: "", // on --> async initialize()
        selected_fix_model_4_newdata_imo: "",
        alert_null_post_canonical_newdata_to_classify_imo: false,
        loading_button_4_newdata_classify_imo: false,
        classification_proba_result_4_newdata_imo: {}, // dictionary
        classification_label_result_4_newdata_imo: "",
        alert_err_msg_4_newdata_imo: false,
        catch_err_msg_4_newdata_imo: "",

        // How to label
        loading_button_4_add_editdata_imo: false,
        array_options_how_to_label_4_editdata_imo: [], // on --> mounted
        selected_how_to_label_4_editdata_imo: "", // on --> mounted
        // Available models
        array_options_model_4_editdata_imo: [], // on --> async initialize().. API get all active classifier model name
        selected_model_4_editdata_imo: "", // on --> async initialize()
        selected_fix_model_4_editdata_imo: "",
        alert_null_post_canonical_editdata_to_classify_imo: false,
        loading_button_4_editdata_classify_imo: false,
        classification_proba_result_4_editdata_imo: {}, // dictionary
        classification_label_result_4_editdata_imo: "",
        alert_err_msg_4_editdata_imo: false,
        catch_err_msg_4_editdata_imo: "",

        // admins
        items_admins: [],
        totalItems_admins: 0,
        headers_admins: [
            {
                title: "id_admin",
                sortable: true,
                key: "id_admin",
                align: "start",
            },
            {
                title: "username",
                sortable: true,
                key: "username",
                align: "start",
            },
            {
                title: "password",
                sortable: false,
                key: "password",
                align: "start",
            },
            {
                title: "full_name",
                sortable: true,
                key: "full_name",
                align: "start",
            },
            {
                title: "created_at",
                sortable: true,
                key: "created_at",
                align: "start",
            },
            {
                title: "is_active",
                sortable: true,
                key: "is_active",
                align: "start",
            },
            {
                title: "description",
                sortable: true,
                key: "description",
                align: "start",
            },
        ],
        newItem_admins: {
            // id_admin: "",
            username: "",
            password: "",
            full_name: "",
            // created_at: "",
            // is_active: "",
            description: "",
        },
        is_success_insert_new_data_admins: false,
        form_insert_new_data_is_not_complete_admins: false,
        form_insert_new_data_error_admins: false,
        form_insert_new_data_error_msg_admins: "",
        showAddDialog_admins: false,
        toggle_visiblity_password_newdata_admin: false,

        // homedata
        showRegenerateDialog_homedata: false,
        msg_success_response_regenerate_homedata: "",
        msg_error_response_regenerate_homedata: "",
        is_success_regenerate_homedata: false,
        is_error_regenerate_homedata: false,
        items_homedata: [],
        totalItems_homedata: 0,
        headers_homedata: [
            {
                title: "id_home_data",
                sortable: true,
                key: "id_home_data",
                align: "start",
            },
            {
                title: "id_key",
                sortable: true,
                key: "id_key",
                align: "start",
            },
            {
                title: "no",
                sortable: true,
                key: "no",
                align: "start",
            },
            {
                title: "contest_name",
                sortable: true,
                key: "contest_name",
                align: "start",
            },
            {
                title: "year",
                sortable: true,
                key: "year",
                align: "start",
            },
            {
                title: "label",
                sortable: true,
                key: "label",
                align: "start",
            },
            {
                title: "day_created",
                sortable: false,
                key: "day_created",
                align: "start",
            },
            {
                title: "created_at",
                sortable: false,
                key: "created_at",
                align: "start",
            },
            {
                title: "expire_day",
                sortable: false,
                key: "expire_day",
                align: "start",
            },
            {
                title: "expire_on",
                sortable: false,
                key: "expire_on",
                align: "start",
            },
        ],

        // models
        items_models: [],
        totalItems_models: 0,
        headers_models: [
            {
                title: "id_model",
                sortable: true,
                key: "id_model",
                align: "start",
            },
            {
                title: "model_type",
                sortable: true,
                key: "model_type",
                align: "start",
            },
            {
                title: "model_name",
                sortable: true,
                key: "model_name",
                align: "start",
            },
            {
                title: "model_path",
                sortable: true,
                key: "model_path",
                align: "start",
            },
            {
                title: "vectorizer_or_tokenizer_path",
                sortable: true,
                key: "vectorizer_or_tokenizer_path",
                align: "start",
            },
            {
                title: "is_active",
                sortable: true,
                key: "is_active",
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
        newItem_models: {
            // "id_model": "",
            model_type: "",
            model_name: "",
            model_path: "",
            vectorizer_or_tokenizer_path: "",
            is_active: 0,
        },
        is_success_insert_new_data_models: false,
        form_insert_new_data_is_not_complete_models: false,
        form_insert_new_data_error_models: false,
        form_insert_new_data_error_msg_models: "",
        showAddDialog_models: false,
        showEditDialog_models: false,
        editedItem_models: {
            id_model: "",
            model_type: "",
            model_name: "",
            model_path: "",
            vectorizer_or_tokenizer_path: "",
            is_active: 0,
        },
        success_update_or_edit_row_models: false,
        form_update_edit_is_not_complete_models: false,
        form_update_or_edit_row_error_models: false,
        form_update_or_edit_row_error_mgs_models: "",
        showDeleteDialogConfirmation_models: false,
        selectedItemIDMODELToDelete_models: -Infinity,
        delete_row_success_or_done_models: false,

        // Universal
        loading_4_all_tables: false,
        itemsPerPage_4_all: 5,
    }),

    methods: {
        async initialize() {
            // IMO
            this.loading_4_all_tables = true;
            try {
                const raw_response = await axios.get("admin/get_imo_data");
                const response = raw_response.data;
                this.items_imo = response;
                this.totalItems_imo = response.itemsLength;
            } catch (err) {
                console.log(err.message);
            } finally {
                this.loading_4_all_tables = false;
            }

            // ADMINS
            this.loading_4_all_tables = true;
            try {
                const raw_response = await axios.get("admin/get_admins_data");
                const response = raw_response.data;
                this.items_admins = response;
                this.totalItems_admins = response.itemsLength;
            } catch (err) {
                console.log(err.message);
            } finally {
                this.loading_4_all_tables = false;
            }

            // HOME_DATA
            this.loading_4_all_tables = true;
            try {
                const raw_response = await axios.get("/admin/get_homedata");
                const response = raw_response.data;
                this.items_homedata = response;
                this.totalItems_homedata = response.itemsLength;
            } catch (err) {
                console.log(err.message);
            } finally {
                this.loading_4_all_tables = false;
            }

            // MODELS
            this.loading_4_all_tables = true;
            try {
                const raw_response = await axios.get("/admin/get_models");
                const response = raw_response.data;
                this.items_models = response;
                this.totalItems_models = response.itemsLength;
            } catch (err) {
                console.log(err.message);
            } finally {
                this.loading_4_all_tables = false;
            }

            // FOR MODEL AUTO LABEL
            this.loading_4_all_tables = true;
            try {
                const raw_response = await axios.get(
                    "/admin/get_all_active_classifier_models_name"
                );
                const response = raw_response.data;

                this.array_options_model_4_newdata_imo = response;
                this.array_options_model_4_newdata_imo.sort();
                this.selected_model_4_newdata_imo =
                    this.array_options_model_4_newdata_imo[1];

                this.array_options_model_4_editdata_imo = response;
                this.array_options_model_4_editdata_imo.sort();
                this.selected_model_4_editdata_imo =
                    this.array_options_model_4_editdata_imo[1];
            } catch (err) {
                console.log(err.message);
            } finally {
                this.loading_4_all_tables = false;
            }
        },

        // imo
        chips_label_color(label) {
            const colorMap = {
                null: "red-darken-2",
                "": "red-darken-2",
                Algebra: "indigo-darken-2",
                Combinatorics: "green-darken-4",
                Geometry: "grey-darken-4",
                "Number Theory": "amber-darken-3",
            };

            return colorMap[label] || "red-darken-2";
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

            this.alert_err_msg_4_newdata_imo = false;
            this.alert_null_post_canonical_newdata_to_classify_imo = false;

            this.selected_fix_model_4_newdata_imo = "";
            this.classification_proba_result_4_newdata_imo = {};
            this.classification_label_result_4_newdata_imo = "";
        },
        function_showDialog_linkANDpdf_imo(v, indetifier) {
            if (indetifier === "link") {
                this.tempvalueLINK = v;
                this.showdialogLINK_imo = true;
                return;
            }
            if (indetifier === "pdf") {
                this.tempvaluePDF = v;
                this.showdialogPDF_imo = true;
                return;
            }
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

            // it means it equal to MANUAL LABEL
            if (
                this.selected_how_to_label_4_newdata_imo ===
                this.array_options_how_to_label_4_newdata_imo[0]
            ) {
                try {
                    const raw_response = await axios.post(
                        "admin/insert_new_data_imo",
                        this.newItem_imo
                    );
                    const response = raw_response.data;
                    console.log("RESPONSE", response.msg);

                    this.is_success_insert_new_data_imo = true;
                    this.reset_form_add_new_item_imo();
                    this.alert_err_msg_4_newdata_imo = false;
                } catch (error) {
                    console.log("ERROR1:", error.message);
                    console.log("ERROR2:", error.response.data.msg);
                    this.form_insert_new_data_error_imo = true;
                    this.form_insert_new_data_error_msg_imo =
                        error.response.data.msg;
                }
            }
            // else mean AUTO LABEL
            else {
                // 1. Check if selected model is not null
                if (
                    this.selected_model_4_newdata_imo !== null &&
                    this.selected_model_4_newdata_imo !== ""
                ) {
                    if (
                        this.newItem_imo.post_canonical !== null &&
                        this.newItem_imo.post_canonical !== ""
                    ) {
                        this.loading_button_4_add_newdata_imo = true;
                        this.loading_button_4_newdata_classify_imo = true;

                        try {
                            const temp = this.selected_model_4_newdata_imo;
                            const raw_response = await axios.post(
                                "admin/classify_problem",
                                {
                                    classifier_model:
                                        this.selected_model_4_newdata_imo,
                                    problems: this.newItem_imo.post_canonical,
                                }
                            );
                            const response = raw_response.data;
                            this.selected_fix_model_4_newdata_imo = temp;

                            this.classification_proba_result_4_newdata_imo =
                                response.classification;
                            this.classification_label_result_4_newdata_imo =
                                response.label;

                            try {
                                this.newItem_imo.label =
                                    this.classification_label_result_4_newdata_imo;
                                const raw_response = await axios.post(
                                    "admin/insert_new_data_imo",
                                    this.newItem_imo
                                );
                                const response = raw_response.data;
                                console.log("RESPONSE", response.msg);

                                this.is_success_insert_new_data_imo = true;
                                this.reset_form_add_new_item_imo();
                                this.alert_err_msg_4_newdata_imo = false;
                            } catch (error) {
                                console.log("ERROR1:", error.message);
                                console.log("ERROR2:", error.response.data.msg);
                                this.form_insert_new_data_error_imo = true;
                                this.form_insert_new_data_error_msg_imo =
                                    error.response.data.msg;
                            }
                        } catch (error) {
                            console.log("ERROR1:", error);
                            console.log("ERROR2:", error.message);
                            console.log("ERROR3:", error.response.data.msg);

                            this.alert_err_msg_4_newdata_imo = true;
                            this.catch_err_msg_4_newdata_imo =
                                error.response.data.msg;
                        }
                    } else {
                        this.alert_null_post_canonical_newdata_to_classify_imo = true;
                    }
                }
            }

            this.loading_button_4_add_newdata_imo = false;
            this.loading_button_4_newdata_classify_imo = false;
            this.initialize();
        },
        showEditItem_imo(item) {
            this.success_update_or_edit_row_imo = false;
            this.form_update_edit_is_not_complete_imo = false;
            this.form_update_or_edit_row_error_imo = false;
            this.editedItem_imo = Object.assign(this.editedItem_imo, item);
            if (this.editedItem_imo.label === null) {
                this.editedItem_imo.label = this.array_of_labels[0]; // set to str ==> 'None'
            }
            this.showEditDialog_imo = true;

            this.alert_err_msg_4_editdata_imo = false;
            this.alert_null_post_canonical_editdata_to_classify_imo = false;

            this.selected_fix_model_4_editdata_imo = "";
            this.classification_proba_result_4_editdata_imo = {};
            this.classification_label_result_4_editdata_imo = "";
        },
        async saveUpdatedOrEditedItem_imo() {
            for (let key in this.editedItem_imo) {
                if (key === "label") {
                    if (this.editedItem_imo[key] === null) {
                        this.editedItem_imo[key] = "None";
                    }
                }

                if (
                    this.editedItem_imo[key] === "" ||
                    this.editedItem_imo[key] === null
                ) {
                    this.form_update_edit_is_not_complete_imo = true;
                    return;
                }
            }

            // it means it equal to MANUAL LABEL
            if (
                this.selected_how_to_label_4_editdata_imo ===
                this.array_options_how_to_label_4_editdata_imo[0]
            ) {
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
            }
            // else mean AUTO LABEL
            else {
                // 1. Check if selected model is not null
                if (
                    this.selected_model_4_editdata_imo !== null &&
                    this.selected_model_4_editdata_imo !== ""
                ) {
                    // 2. Check if post_canonical is not null
                    if (
                        this.editedItem_imo.post_canonical !== null &&
                        this.editedItem_imo.post_canonical !== ""
                    ) {
                        this.loading_button_4_add_editdata_imo = true;
                        this.loading_button_4_editdata_classify_imo = true;

                        try {
                            const temp = this.selected_model_4_editdata_imo;
                            const raw_response = await axios.post(
                                "admin/classify_problem",
                                {
                                    classifier_model:
                                        this.selected_model_4_editdata_imo,
                                    problems:
                                        this.editedItem_imo.post_canonical,
                                }
                            );
                            const response = raw_response.data;
                            this.selected_fix_model_4_editdata_imo = temp;

                            this.classification_proba_result_4_editdata_imo =
                                response.classification;
                            this.classification_label_result_4_editdata_imo =
                                response.label;

                            try {
                                this.editedItem_imo.label =
                                    this.classification_label_result_4_editdata_imo;
                                const raw_response = await axios.post(
                                    "admin/update_row_imo",
                                    this.editedItem_imo
                                );
                                const response = raw_response.data;
                                console.log("RESPONSE", response.msg);

                                this.showEditDialog_imo = false;
                                this.is_success_insert_new_data_imo = true;
                                this.alert_err_msg_4_editdata_imo = false;
                            } catch (error) {
                                console.log("ERROR1:", error.message);
                                console.log("ERROR2:", error.response.data.msg);
                                this.form_insert_new_data_error_imo = true;
                                this.form_insert_new_data_error_msg_imo =
                                    error.response.data.msg;
                            }
                        } catch (error) {
                            console.log("ERROR1:", error);
                            console.log("ERROR2:", error.message);
                            console.log("ERROR3:", error.response.data.msg);

                            this.alert_err_msg_4_editdata_imo = true;
                            this.catch_err_msg_4_editdata_imo =
                                error.response.data.msg;
                        }
                    } else {
                        this.alert_null_post_canonical_editdata_to_classify_imo = true;
                    }
                }
            }

            this.loading_button_4_add_editdata_imo = false;
            this.loading_button_4_editdata_classify_imo = false;
            this.initialize();
        },
        confirmDeleteRow_imo(id_key) {
            this.delete_row_success_or_done_imo = false;
            this.selectedItemIDKEYToDelete_imo = id_key;
            this.showDeleteDialogConfirmation_imo = true;
        },
        async deleteItem_imo() {
            try {
                const raw_response = await axios.post("admin/delete_row_imo", {
                    id_key: this.selectedItemIDKEYToDelete_imo,
                });
                const response = raw_response.data;
                this.delete_row_success_or_done_imo = true;
                this.initialize();
            } catch (error) {
                console.log("ERROR1:", error.message);
                console.log("ERROR2:", error.response.data.msg);
            }
            this.showDeleteDialogConfirmation_imo = false;
        },
        async classify_newdata_imo() {
            this.classification_proba_result_4_newdata_imo = {};
            this.alert_err_msg_4_newdata_imo = false;
            this.selected_fix_model_4_newdata_imo = "";
            this.classification_label_result_4_newdata_imo = "";

            // 1. Check if how_to_label is chose to automatic
            if (
                this.selected_how_to_label_4_newdata_imo ===
                this.array_options_how_to_label_4_newdata_imo[1]
            ) {
                this.loading_button_4_newdata_classify_imo = true;

                // 2. Check if selected model is not null
                if (
                    this.selected_model_4_newdata_imo !== null &&
                    this.selected_model_4_newdata_imo !== ""
                ) {
                    // 3. check post_canonical is not null
                    if (
                        this.newItem_imo.post_canonical !== null &&
                        this.newItem_imo.post_canonical !== ""
                    ) {
                        try {
                            const temp = this.selected_model_4_newdata_imo;
                            const raw_response = await axios.post(
                                "admin/classify_problem",
                                {
                                    classifier_model:
                                        this.selected_model_4_newdata_imo,
                                    problems: this.newItem_imo.post_canonical,
                                }
                            );
                            const response = raw_response.data;
                            this.selected_fix_model_4_newdata_imo = temp;

                            this.classification_proba_result_4_newdata_imo =
                                response.classification;
                            this.classification_label_result_4_newdata_imo =
                                response.label;
                        } catch (error) {
                            console.log("ERROR1:", error);
                            console.log("ERROR2:", error.message);
                            console.log("ERROR3:", error.response.data.msg);

                            this.alert_err_msg_4_newdata_imo = true;
                            this.catch_err_msg_4_newdata_imo =
                                error.response.data.msg;
                        }
                    } else {
                        this.alert_null_post_canonical_newdata_to_classify_imo = true;
                    }
                }

                this.loading_button_4_newdata_classify_imo = false;
            }
        },
        async classify_editdata_imo() {
            this.classification_proba_result_4_editdata_imo = {};
            this.alert_err_msg_4_editdata_imo = false;
            this.selected_fix_model_4_editdata_imo = "";
            this.classification_label_result_4_editdata_imo = "";

            // 1. Check if how_to_label is chose to automatic
            if (
                this.selected_how_to_label_4_editdata_imo ===
                this.array_options_how_to_label_4_editdata_imo[1]
            ) {
                this.loading_button_4_editdata_classify_imo = true;

                // 2. Check if selected model is not null
                if (
                    this.selected_model_4_editdata_imo !== null &&
                    this.selected_model_4_editdata_imo !== ""
                ) {
                    // 3. check post_canonical is not null
                    if (
                        this.editedItem_imo.post_canonical !== null &&
                        this.editedItem_imo.post_canonical !== ""
                    ) {
                        try {
                            const temp = this.selected_model_4_editdata_imo;
                            const raw_response = await axios.post(
                                "admin/classify_problem",
                                {
                                    classifier_model:
                                        this.selected_model_4_editdata_imo,
                                    problems:
                                        this.editedItem_imo.post_canonical,
                                }
                            );
                            const response = raw_response.data;
                            this.selected_fix_model_4_editdata_imo = temp;

                            this.classification_proba_result_4_editdata_imo =
                                response.classification;
                            this.classification_label_result_4_editdata_imo =
                                response.label;
                        } catch (error) {
                            console.log("ERROR1:", error);
                            console.log("ERROR2:", error.message);
                            console.log("ERROR3:", error.response.data.msg);

                            this.alert_err_msg_4_editdata_imo = true;
                            this.catch_err_msg_4_editdata_imo =
                                error.response.data.msg;
                        }
                    } else {
                        this.alert_null_post_canonical_editdata_to_classify_imo = true;
                    }
                }

                this.loading_button_4_editdata_classify_imo = false;
            }
        },

        // admins
        reset_form_add_new_item_admins() {
            this.newItem_admins = {
                // id_admin: "",
                username: "",
                password: "",
                full_name: "",
                // created_at: "",
                // is_active: "",
                description: "",
            };
        },
        function_showAddDialog_admins() {
            this.showAddDialog_admins = true;
            this.is_success_insert_new_data_admins = false;
            this.form_insert_new_data_is_not_complete_admins = false;
            this.form_insert_new_data_error_admins = false;
        },
        async addItem_admins() {
            this.is_success_insert_new_data_admins = false;
            this.form_insert_new_data_is_not_complete_admins = false;
            this.form_insert_new_data_error_admins = false;

            for (let key in this.newItem_admins) {
                if (
                    this.newItem_admins[key] === "" ||
                    this.newItem_admins[key] === null
                ) {
                    this.form_insert_new_data_is_not_complete_admins = true;
                    return;
                }
            }

            try {
                const raw_response = await axios.post(
                    "admin/add_new_admin",
                    this.newItem_admins
                );
                const response = raw_response.data;
                console.log("RESPONSE", response.msg);

                this.is_success_insert_new_data_admins = true;
                this.reset_form_add_new_item_admins();

                this.initialize();
            } catch (error) {
                console.log("ERROR1:", error.message);
                console.log("ERROR2:", error.response.data.msg);
                this.form_insert_new_data_error_admins = true;
                this.form_insert_new_data_error_msg_admins =
                    error.response.data.msg;
            }
        },

        // homedata
        function_showRegenerateDialog_homedata() {
            this.showRegenerateDialog_homedata = true;
            this.is_success_regenerate_homedata = false;
            this.is_error_regenerate_homedata = false;
        },
        async regenerate_homedata() {
            try {
                const raw_response = await axios.get(
                    `admin/delete_homedata?eR9j07LCQkEwXkTH=uacibxzt`
                );
                const response = raw_response.data;

                try {
                    const raw_response = await axios.get(`home/home_data`);
                    const response = raw_response.data;

                    this.msg_success_response_regenerate_homedata =
                        "Regenerate `home_data` success";
                    this.is_success_regenerate_homedata = true;
                } catch (error2) {
                    console.log("ERROR1:", error2.message);
                    console.log("ERROR2:", error2.response.data.msg);
                }
            } catch (error) {
                console.log("ERROR1:", error.message);
                console.log("ERROR2:", error.response.data.msg);
                this.is_error_regenerate_homedata = true;
            }
            this.showRegenerateDialog_homedata = false;
            this.initialize();
        },

        // models
        reset_form_add_new_item_models() {
            this.newItem_models = {
                // "id_model": "",
                model_type: "",
                model_name: "",
                model_path: "",
                vectorizer_or_tokenizer_path: "",
                is_active: 0,
            };
        },
        function_showAddDialog_models() {
            this.showAddDialog_models = true;
            this.is_success_insert_new_data_models = false;
            this.form_insert_new_data_is_not_complete_models = false;
            this.form_insert_new_data_error_models = false;
        },
        async addItem_models() {
            this.is_success_insert_new_data_models = false;
            this.form_insert_new_data_is_not_complete_models = false;
            this.form_insert_new_data_error_models = false;

            for (let key in this.newItem_models) {
                if (key !== "vectorizer_or_tokenizer_path") {
                    if (
                        this.newItem_models[key] === "" ||
                        this.newItem_models[key] === null
                    ) {
                        this.form_insert_new_data_is_not_complete_models = true;
                        return;
                    }
                }
            }

            try {
                const raw_response = await axios.post(
                    "admin/insert_new_data_models",
                    this.newItem_models
                );
                const response = raw_response.data;
                console.log("RESPONSE", response.msg);

                this.is_success_insert_new_data_models = true;
                this.reset_form_add_new_item_models();

                this.initialize();
            } catch (error) {
                console.log("ERROR1:", error.message);
                console.log("ERROR2:", error.response.data.msg);
                this.form_insert_new_data_error_models = true;
                this.form_insert_new_data_error_msg_models =
                    error.response.data.msg;
            }
        },
        showEditItem_models(item) {
            this.success_update_or_edit_row_models = false;
            this.form_update_edit_is_not_complete_models = false;
            this.form_update_or_edit_row_error_models = false;
            this.editedItem_models = Object.assign(
                this.editedItem_models,
                item
            );
            this.showEditDialog_models = true;
        },
        async saveUpdatedOrEditedItem_models() {
            for (let key in this.editedItem_models) {
                if (key !== "vectorizer_or_tokenizer_path") {
                    if (
                        this.editedItem_models[key] === "" ||
                        this.editedItem_models[key] === null
                    ) {
                        this.form_update_edit_is_not_complete_models = true;
                        return;
                    }
                }
            }

            try {
                const raw_response = await axios.post(
                    "admin/update_row_models",
                    this.editedItem_models
                );
                const response = raw_response.data;
                console.log("RESPONSE", response.msg);
                this.success_update_or_edit_row_models = true;

                this.showEditDialog_models = false;
                this.initialize();
            } catch (error) {
                console.log("ERROR1:", error.message);
                console.log("ERROR2:", error.response.data.msg);
                this.form_update_or_edit_row_error_models = true;
                this.form_update_or_edit_row_error_mgs_models =
                    error.response.data.msg;
            }
        },
        confirmDeleteRow_models(id_model) {
            this.delete_row_success_or_done_models = false;
            this.selectedItemIDMODELToDelete_models = id_model;
            this.showDeleteDialogConfirmation_models = true;
        },
        async deleteItem_models() {
            try {
                const raw_response = await axios.post(
                    "admin/delete_row_models",
                    {
                        id_model: this.selectedItemIDMODELToDelete_models,
                    }
                );
                const response = raw_response.data;
                this.delete_row_success_or_done_models = true;
                this.initialize();
            } catch (error) {
                console.log("ERROR1:", error.message);
                console.log("ERROR2:", error.response.data.msg);
            }
            this.showDeleteDialogConfirmation_models = false;
        },

        // universal
        chips_isactive_color(s) {
            const colorMap = {
                null: "red-darken-2",
                "": "red-darken-2",
                0: "red-darken-2",
                1: "teal-darken-2",
            };

            return colorMap[s] || "red-darken-2";
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

    watch: {
        selected_how_to_label_4_newdata_imo(oldVal, newVal) {
            this.classification_proba_result_4_newdata_imo = {};
            this.selected_fix_model_4_newdata_imo = "";
            this.classification_label_result_4_newdata_imo = "";
            this.alert_null_post_canonical_newdata_to_classify_imo = false;
        },

        selected_how_to_label_4_editdata_imo(oldVal, newVal) {
            this.classification_proba_result_4_editdata_imo = {};
            this.selected_fix_model_4_editdata_imo = "";
            this.classification_label_result_4_editdata_imo = "";
            this.alert_null_post_canonical_editdata_to_classify_imo = false;
        },
    },

    mounted() {
        const temp_options = ["Manual Label", "Auto Label"]; // Always set index[0] = Manual
        this.array_options_how_to_label_4_newdata_imo = temp_options;
        this.selected_how_to_label_4_newdata_imo = temp_options[0];

        this.array_options_how_to_label_4_editdata_imo = temp_options;
        this.selected_how_to_label_4_editdata_imo = temp_options[0];

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
    background-color: #eceff1;
}
</style>
