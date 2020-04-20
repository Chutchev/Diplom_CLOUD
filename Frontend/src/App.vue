<template>
  <div id="app" @click="this.offContextMenu">
    <MainInfoBar v-show="this.getUrl()"/>
    <router-view/>
  </div>
</template>

<script>
  import MainInfoBar from "@/components/MainInfoBar";
export default {
  name: 'App',
  data() {
    return{
        activeElement: null,
    }
  },
  components: {
    MainInfoBar
  },
  methods: {
    getUrl() {
      let url = this.$route.path;
      if (url == '/login' || url == '/register'){
        return false;
      }
      else {
        return true;
      }
    },
    offStandartContextMenu(){
      document.oncontextmenu = function (){return false};
    },
    offContextMenu(){
      try {
        document.querySelector('div.menu').setAttribute('style', 'display: none');
      }catch (e) {
        return
      }

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
