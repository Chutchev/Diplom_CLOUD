<template>
    <div class="files">
        <ul class="cards">
        <FileInfo v-for="file in files" :key="file.title" v-bind:file="file"/>
        </ul>
        <div class="menu">
            <ul class='custom-menu'>
                <li>Customize</li><hr>
                <li data-action="Delete">Удалить файл</li>
                <li data-action="CopyUrl">Копировать ссылку на файл</li>
            </ul>
        </div>
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
    .custom-menu {
        display: none;
        z-index: 1000;
        position: absolute;
        overflow: hidden;
        border: 1px solid #bdc3c7;
        white-space: nowrap;
        background: #303030;
        color: #fff;
    }
    .custom-menu li {
        padding: 9px 15px;
        cursor: pointer;
        list-style-type: none;
        transition: all .3s ease;
        user-select: none;
        font-weight:200;
    }
    .custom-menu li:nth-child(1){
        pointer-events:none;
        color:#b2b2b2;
    }
    .custom-menu hr{
        margin:0 12px;
        border:none;
        background-color:#545454;
        height:1px;
    }
    .custom-menu li:hover {
        background-color: #545454;
    }
</style>