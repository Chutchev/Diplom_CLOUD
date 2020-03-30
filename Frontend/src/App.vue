<template>
  <div id="app">
    <MainInfoBar v-if="getUrl() != '/login'"/>
    <router-view />
  </div>
</template>

<script>
  import MainInfoBar from "@/components/MainInfoBar";
export default {
  name: 'App',
  data() {
    return{

    }
  },
  components: {
    MainInfoBar
  },
  methods: {
    getUrl() {
      return this.$route.path
    }
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
  margin-top: 60px;
}
</style>
