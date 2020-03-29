<template>
    <div class="fileInfo">
        <h1>{{file.title}}</h1>
    </div>
</template>

<script>
    export default {
        props: {
            file: {
                    type: Object,
                    required: true
            }
        }
    }
</script>

<style scoped>
.fileInfo {
    border: 4px double black;
    display: inline-block;
    margin-right: 2px;
}
</style>