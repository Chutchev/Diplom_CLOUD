<template>
    <div id="loader" v-if="this.loading"><p>LOADING</p></div>
    <div class="files" v-else>
            <transition-group name="fade" tag="ul" class="cards">
                <FileInfo v-for="file in files" :key="file.id" v-bind:file="file" :id="file.id" @activeFile="chooseFile"/>
            </transition-group>
        <ContextMenuPage @eventFromContextMenu="this.deleteFileFromUI" v-bind:title="this.title" v-bind:url="this.url"
                         v-bind:element="this.element" v-bind:file="this.file"/>
        <CopyUrlHTML v-bind:url="this.url"/>
    </div>
</template>

<script>
    import FileInfo from "@/components/FilesMenu/FileInfo";
    import ContextMenuPage from "@/components/FilesMenu/ContextMenuPage";
    import CopyUrlHTML from "@/components/FilesMenu/CopyUrlHTML";
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
                loading: true
            }
        },
        components: {
            CopyUrlHTML,
            ContextMenuPage,
            FileInfo
        },
        methods: {
            chooseFile(data){
                this.activeFile = data.file;
                console.log('CHOOOSE FILE ', this.activeFile)
            },
            async deleteFileFromUI(data) {
                console.log(data.element);
                console.log(this.files, this.activeFile);
                delete this.files[this.activeFile];
                await this.getFiles();
                // location.reload();
            },
            getUrl() {
                return this.$route.path
            },
            async getFiles() {
                let url = 'http://127.0.0.1:6556/files';
                let token = localStorage.getItem('TOKEN');
                let params = {
                    token
                };
                await axios.post(url, params).then(response => {
                    this.filesinfos = response.data;
                });
                let files = [];
                let i = 0;
                // [filename, path, author, type, md5]
                this.filesinfos.forEach(file => {
                    files.push({
                        title: file[0],
                        author: file[2],
                        filepath: file[1],
                        filetype: file[3],
                        id: i++
                    })
                });
                this.files = files;
            },
        },
        mounted() {
            let self = this;
            setTimeout(function () {
                self.loading = false;
            }, 400);
            console.log('Должно исчезнуть');
            this.getFiles();
            document.addEventListener('contextmenu', e => {
                let activeElement = e.target;
                this.title = activeElement.parentNode.children[0].innerHTML;
                let parent = activeElement.parentNode;
                while (parent.getAttribute('class') !== 'cards__item') {
                    parent = parent.parentNode;
                }
                this.url = parent.getAttribute('data-url');
                this.element = parent;
                console.log(this.url);
            });
        },
    }

</script>

<style scoped>
    .fade-enter-active, .fade-leave-active {
        transition: opacity 1s;
    }

    .fade-leave-to, .fade-enter-to {
        opacity: 0;
    }

    .fade-move{
        transition: transform 0.1s;
        opacity: 0;
    }
    li.cards__item {
        margin-left: auto;
        margin-right: auto
    }
</style>