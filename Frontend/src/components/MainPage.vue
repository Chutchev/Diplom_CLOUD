<template>
    <div>
        <button @click="getFiles()"></button>
        <FileInfo v-for="file in files" :key="file.title" v-bind:file="file"/>
    </div>
</template>

<script>
    import FileInfo from "@/components/FileInfo";
    import axios from 'axios'
    export default {
        props: ["files"],
        components: {
            FileInfo
        },
        methods: {
            async getFiles(){
                let url = 'http://127.0.0.1:6556/files';
                let token = localStorage.getItem('TOKEN');
                await axios.post(url, token).then(response => {
                    this.filesinfos = response.data;
                    console.log(this.filesinfos);
                });
                let files = [];
                // [filename, path, author, type, md5]
                this.filesinfos.forEach(file => {
                    files.push({
                        title: file[0],
                        author: file[2],
                        filetype: file[3]
                    })
                });
                this.files = files;
            }
        }
    }
</script>

<style scoped>

</style>