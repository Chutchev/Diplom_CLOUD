<template>
    <div style="display: inline-block;
                   margin-right: 10px;
                   margin-top: 10px">
        <transition name="fade">
            <v-card
                    class="mx-auto"
                    max-width="344"
                    elevation="6"
                    v-show="this.show"
            >
                <v-img
                        src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                        height="200px"
                ></v-img>

                <v-card-title class="d-inline-block text-truncate text-uppercase" style="max-width: 320px;">
                    {{file.title}}
                </v-card-title>
                <v-card-actions>
                    <v-btn icon @click="this.downloadWithAxios">
                        <v-icon large>mdi-file-download</v-icon>
                    </v-btn>
                    <v-btn icon @click.stop="dialog = true">
                        <v-icon large>mdi-share-variant</v-icon>
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-btn icon @click="this.deleteFileFunc">
                        <v-icon large>mdi-delete</v-icon>
                    </v-btn>
                </v-card-actions>
            </v-card>
        </transition>
        <v-dialog
                v-model="dialog"
                width="500"
        >

            <v-card>
                <v-card-title
                        class="headline grey lighten-2"
                        primary-title
                >
                    URL - для общего доступа
                </v-card-title>
                <br>
                <v-card-text>
                    {{this.file.url}}
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                            color="primary"
                            text
                            @click="dialog = false"
                    >
                        Закрыть
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>

</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                show: true,
                dialog: false,
            }
        },
        props: {
            file: {
                type: Object,
                required: true
            },
            deleteFile: null,
        },
        methods: {
            async deleteFileFunc() {
                const url = 'http://127.0.0.1:8000/api/files/';
                await axios.delete(url, {
                    headers: {
                        'authorization': `Token ${localStorage.getItem("TOKEN")}`,
                    },
                    data: {
                        id: this.file.id
                    }
                }).then(response => {
                    console.log('FILE DELETED', response.data);
                });
                this.show = false;
            },
            downloadFile(response) {
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', this.file.title);
                document.body.appendChild(link);
                link.click()
            },
            downloadWithAxios() {
                axios({
                    method: 'get',
                    url: this.file.url,
                    responseType: 'arraybuffer'
                })
                    .then(response => {
                        this.downloadFile(response)
                    })
                    .catch(() => console.log('error occured'))
            },
            showDialog() {
                this.dialog_show = true;
                console.log('нажато!')
            }
        },
        mounted() {

        }
    }
</script>

<style scoped>
    .fade-enter-active, .fade-leave-active {
        transition: opacity 1s;
    }

    .fade-leave-to, .fade-enter-to {
        opacity: 0;
    }

    .fade-move {
        transition: transform 1s;
    }

    li#cards__item {
        float: left;
        transition: all 1s;
    }
</style>