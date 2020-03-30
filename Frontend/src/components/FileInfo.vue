<template>
    <div class="fileInfo">
        <a :href="`http://127.0.0.1:6556/files/${file.title}`">{{file.title}}</a>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        props: {
            file: {
                    type: Object,
                    required: true
            }
        },
        methods: {
            download_file(){
                let url = `http://127.0.0.1:6556/files/${this.file.title}`;
                let params = {
                    path: this.file.filepath
                };
                axios.post(url, params).then(response => {
                    console.log(response)
                });
            }
        }
    }
</script>

<style scoped>
</style>