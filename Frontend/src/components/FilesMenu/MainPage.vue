<template>
    <div class="files">
        <ul class="cards">
        <FileInfo v-for="file in files" :key="file.title" v-bind:file="file"/>
        </ul>
        <ContextMenuPage v-bind:title="this.title" v-bind:url="this.url"/>
        <CopyUrlHTML v-bind:url="this.url"/>
    </div>
</template>

<script>
    import FileInfo from "@/components/FilesMenu/FileInfo";
    import ContextMenuPage from "@/components/FilesMenu/ContextMenuPage";
    import CopyUrlHTML from "@/components/FilesMenu/CopyUrlHTML";
    import axios from 'axios'
    export default {
        data(){
            return {
                files: this.files,
                title: null,
                url: null
            }
        },
        components: {
            CopyUrlHTML,
            ContextMenuPage,
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
            },
        },
        mounted() {
            this.getFiles();
            document.addEventListener('contextmenu',e => {
                let activeElement = e.target;
                this.title = activeElement.parentNode.children[0].innerHTML;
                let parent = activeElement.parentNode;
                while (parent.getAttribute('class') !== 'card'){
                    parent = parent.parentNode;
                }
                this.url = parent.getAttribute('data-url');
                console.log(this.url);
            });
        },
    }

</script>

<style scoped>

</style>