<template>
    <div class="menu">
        <ul class='custom-menu'>
            <li>Меню файла</li><hr>
            <li data-action="Delete" @click="this.deleteFile">Удалить файл</li>
            <li data-action="CopyUrl" @click="this.copyFileUrl">Копировать ссылку на файл</li>
            <li data-action="Download" @click="this.downloadFile">Скачать файл</li>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "ContextMenuPage",
        props: {
          title: {
              type: String,
          },
            url: {
              type: String
            }
        },
        data(){
            return {
                activeElement: 'bfg'
            }
        },
        methods: {
            deleteFile() {
                const url = 'http://127.0.0.1:6556/files';
                const token = localStorage.getItem('TOKEN');
                let params = {
                    filename: this.title,
                    token: token,
                    'DELETE': true
                };
                axios.post(url, params).then(response => {
                    console.log('FILE DELETED', response.data);
                    location.reload()
                })
            },
            copyFileUrl(eventObject) {
                let copyForm = document.getElementsByClassName('row_pop-up')[0];
                console.log(copyForm);
                copyForm.setAttribute('style', `top: ${eventObject.y}px;
                                                                    display: inline-block;
                                                                    left: ${eventObject.x}px`);
            },
            downloadFile(){
                let link = document.createElement('a');
                link.href = this.url;
                document.body.appendChild(link);
                link.click();
                link.remove();
            }
        },
        mounted(){

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