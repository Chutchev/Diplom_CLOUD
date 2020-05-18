<template>
    <div id="loader" v-if="this.loading"><img src="../../assets/images/loader.gif"/></div>
    <div class="files" v-else-if="files.length() > 0">
            <FileInfo  v-for="file in files" :key="file.id" v-bind:file="file" :id="file.id" @activeFile="chooseFile"/>
    </div>
    <div v-else>
        <v-label></v-label>
    </div>
</template>

<script>
    import FileInfo from "@/components/FilesMenu/FileInfo";
    import axios from 'axios'

    export default {
        props: ['eventFromContextMenu'],
        data() {
            return {
                files: this.files,
                title: null,
                url: null,
                element: null,
                show: true,
                file: null,
                activeFile: null,
                loading: true,
                id: null
            }
        },
        components: {
            FileInfo
        },
        methods: {
            chooseFile(data) {
                this.activeFile = data.file;
                console.log('CHOOOSE FILE ', this.activeFile)
            },
            getUrl() {
                return this.$route.path
            },
            async getFiles() {
                let url = 'http://127.0.0.1:8000/api/files/';
                let token = sessionStorage.getItem('TOKEN');
                await axios.get(url, {
                    headers: {
                        'authorization': `Token ${token}`
                    }
                }).then(response => {
                    this.filesinfos = response.data;
                });
                let files = [];
                this.filesinfos.forEach((file) => {
                    files.push({
                        url: file['file'],
                        title: file['name'],
                        id: file['id']
                    });
                });
                this.files = files;
            },
        },
        mounted() {
            let self = this;
            this.getFiles();
            console.log(this.files);
            setTimeout(function () {
                self.loading = false;
            }, 1000);
        },
    }

</script>

<style scoped>

</style>