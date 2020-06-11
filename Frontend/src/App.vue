<template>
    <div id="app">
        <MainInfoBar v-show="this.getUrl()"/>
        <v-app>
            <router-view/>
        </v-app>
    </div>
</template>

<script>
    import MainInfoBar from "@/components/MainInfoBar";

    export default {
        name: 'App',
        data() {
            return {
                activeElement: null,
            }
        },
        components: {
            MainInfoBar,
        },
        methods: {
            getUrl() {
                let url = this.$route.path;
                if (url == '/login' || url == '/register') {
                    return false;
                } else {
                    return true;
                }
            },

        },
        mounted() {
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 0px;
    }
</style>
