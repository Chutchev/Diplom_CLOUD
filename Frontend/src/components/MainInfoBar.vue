<template>
    <div id="infobar">
        <ul class="hr">
            <li class="left"><a href="/main">Main</a></li>
            <li class="left"><a href="/files">Files</a></li>
            <li class="left"><a href="/Upload">Upload</a></li>
            <li class="right"><a href="/me">Me</a></li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "MainInfoBar"
    }
</script>

<style scoped>
    ul.hr {
        margin: 0; /* Обнуляем значение отступов */
        padding: 4px; /* Значение полей */
        height: 3em;
        background: #2288dd;
    }
    ul.hr li {
        display: inline; /* Отображать как строчный элемент */
        margin-right: 5px; /* Отступ слева */
        padding: 3px; /* Поля вокруг текста */
        font-size: 40px;
    }
    ul.hr li.right {
        float: right;
    }
    ul.hr li.left {
        float: left;
    }
    a, a:link {
        color: white;
        text-decoration: none;
    }
</style>