<template>
  <div id="app" @click="this.offContextMenu">
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
    },
    offStandartContextMenu(){
      document.oncontextmenu = function (){return false};
    },
    offContextMenu(){
      document.querySelector('div.menu').setAttribute('style', 'display: none');
    }
  },
  mounted() {
    this.offStandartContextMenu();
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
  .menu {
    display: none;
  }
</style>
