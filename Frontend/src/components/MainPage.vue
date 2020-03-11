<template>
    <div>
        <FileInfo v-for="file in files" :key="file.title" v-bind:file="file"/>
    </div>
</template>

<script>
    import FileInfo from "@/components/FileInfo";
    export default {
        props: ["files"],
        components: {
            FileInfo
        }
    }
</script>

<style scoped>

</style>