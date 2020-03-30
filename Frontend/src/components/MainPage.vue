<template>
    <div @load="getFiles">
        <FileInfo v-for="file in files" :key="file.title" v-bind:file="file"/>
    </div>
</template>

<script>
    import FileInfo from "@/components/FileInfo";
    import axios from 'axios'
    export default {
        data(){
            return {
                files: this.files
            }
        },
        components: {
            FileInfo
        },
        methods: {
            getUrl() {
                return this.$route.path
            },
            async getFiles(){
                let url = 'http://127.0.0.1:6556/files';
                let token = localStorage.getItem('TOKEN');
                let params = {
                    token
                };
                await axios.post(url, params).then(response => {
                    this.filesinfos = response.data;
                    console.log(this.filesinfos);
                });
                let files = [];
                // [filename, path, author, type, md5]
                this.filesinfos.forEach(file => {
                    files.push({
                        title: file[0],
                        author: file[2],
                        filepath: file[1],
                        filetype: file[3]
                    })
                });
                this.files = files;
            }
        },
        mounted() {
            this.getFiles();
        }
    }

</script>

<style scoped>

</style>