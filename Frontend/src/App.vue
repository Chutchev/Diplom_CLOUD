<template>
  <div id="app">
    <h1>Облако</h1>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return{
      files: [
        {id: 1, title: 'Фото 1', size: 7},
        {id: 2, title: 'Фото 2', size: 3},
        {id: 3, title: 'Документ', size: 5},
      ]
    }
  },
  components: {
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
