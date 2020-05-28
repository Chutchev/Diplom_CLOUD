<template>
    <v-container>
        <v-content>
            <h1 class="display-3">Загрузка файлов</h1>
            <v-file-input multiple label="Выберите файлы" id="files" ref="files"
                          @change="this.handleFileUploads"></v-file-input>
            <hr>

            <v-list-item
                    v-for="(item, index) in files"
                    :key="item.id"
            >
                <v-list-item-content>
                    <v-list-item-title v-text="item.file.name"></v-list-item-title>
                </v-list-item-content>
                <v-list-item-icon>
                    <v-btn icon @click="removeFile(index)">
                        <v-icon>mdi-delete</v-icon>
                    </v-btn>
                </v-list-item-icon>
            </v-list-item>
        </v-content>
        <v-btn x-large color="blue-grey" dark @click="uploadFile">
            Загрузить
            <v-icon x-large right>
                mdi-file-upload
            </v-icon>
        </v-btn>
    </v-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "UploadPage",
        data() {
            return {
                files: [],
                uploadPercentage: 0,
                loading: false
            }
        },
        methods: {
            removeFile(key) {
                console.log(key);
                this.files.splice(key, 1);
            },
            handleFileUploads() {
                let uploadedFiles = this.$refs.files.lazyValue;
                for (var i = 0; i < uploadedFiles.length; i++) {
                    this.files.push({file: uploadedFiles[i], id: i});
                }
            },
            async uploadFile() {
                const url = 'http://127.0.0.1:8000/api/files/';

                for (var i = 0; i < this.files.length; i++) {
                    let formData = new FormData();
                    let file = this.files[i].file;
                    console.log(this.files);
                    // let filename = file.name.toString();
                    formData.append(`file`, file);
                    await axios.post(url, formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data; charset=utf-8',
                            'authorization': `Token ${sessionStorage.getItem("TOKEN")}`,
                        }
                    }).then(response => {
                        console.log(response.data)
                    });
                }

                location.reload()
            }
        },
        mounted() {
            console.log(this.files.length)
        }
    }
</script>

<style scoped>

</style>