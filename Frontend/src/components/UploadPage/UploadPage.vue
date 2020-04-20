<template>
    <div>
        <form>
            <h1>Upload Page</h1>
            <input type="file" class="inputfile" id="files" ref="files" placeholder="Выберите файл"
                   @change="this.handleFileUploads"
                   multiple/>
            <div id="AddButton" @click="this.addFile"><p id="textAdd">Выбрать файлы</p></div>
            <hr>
        </form>
        <ul class="large-12 medium-12 small-12 cell" id="border">
            <li v-for="(file, key) in files" :key="key" class="file-listing">{{ file.name }} <span
                    class="remove-file" @click="removeFile(key)">X</span></li>
        </ul>
        <progress max="100" v-if="this.loading===true" :value.prop="uploadPercentage"></progress>
        <button v-if="this.files.length > 0" @click="this.uploadFile">Загрузить</button>
    </div>
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
            addFile() {
                this.$refs.files.click()

            },
            removeFile(key) {
                this.files.splice(key, 1);
            },
            handleFileUploads() {
                let uploadedFiles = this.$refs.files.files;
                for (var i = 0; i < uploadedFiles.length; i++) {
                    this.files.push(uploadedFiles[i]);
                }
            },
            async uploadFile() {
                const url = 'http://127.0.0.1:8000/api/files/';

                for (var i = 0; i < this.files.length; i++) {
                    let formData = new FormData();
                    let file = this.files[i];
                    // let filename = file.name.toString();
                    formData.append(`file`, file);
                    await axios.post(url, formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data; charset=utf-8',
                            'authorization': `Token ${localStorage.getItem("TOKEN")}`,
                        },
                        onUploadProgress: function (progressEvent) {
                            this.loading = true;
                            this.uploadPercentage = parseInt(Math.round((progressEvent.loaded / progressEvent.total) * 100));
                        }.bind(this)
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
    .inputfile {
        width: 0.1px;
        height: 0.1px;
        opacity: 0;
        overflow: hidden;
        position: absolute;
        z-index: -1;
    }

    div#AddButton {
        display: inline-block;
        margin: 10px;
        width: 100px;
        height: 100px;
        cursor: pointer;
        border-radius: 50%;

        box-shadow: 0 3px 20px rgba(0, 0, 0, .25),
        inset 0 2px 0 rgba(255, 255, 255, .6),
        0 2px 0 rgba(0, 0, 0, .1),
        inset 0 0 20px rgba(0, 0, 0, .1);
    }

    p#textAdd {
        margin: 33px auto;
        font-family: "Trebuchet MS", "Lucida Sans";
    }

    .remove-file {
        cursor: pointer;
        border-radius: 50%;
    }

    .remove-file:hover {
        opacity: 50%;
    }

    #border {
        list-style: none;
        padding: 0;
        margin: auto;
        width: 70%;
    }

    #border li {
        font-family: "Trebuchet MS", "Lucida Sans";
        padding: 7px 20px;
        border-radius: 5px;
        border-left: 10px solid #f05d22;
        box-shadow: 2px -2px 5px 0 rgba(0, 0, 0, .1),
        -2px -2px 5px 0 rgba(0, 0, 0, .1),
        2px 2px 5px 0 rgba(0, 0, 0, .1),
        -2px 2px 5px 0 rgba(0, 0, 0, .1);
        font-size: 20px;
        letter-spacing: 2px;
        transition: 0.3s all linear;
        margin: auto;
        margin-left: 30%;
        margin-bottom: 10px;
        width: 70%;
    }
    #border li span{
        float: right;
    }
</style>