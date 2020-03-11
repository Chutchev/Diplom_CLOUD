<template>
    <div class="fileInfo">
        <p>{{file.title}}</p>
        <p>{{file.size}}</p>
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