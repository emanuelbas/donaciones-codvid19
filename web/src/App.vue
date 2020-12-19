<template>
  <div id="app">
    <div id="nav" class="bg-black">
      <router-link to="/">Home</router-link> |
      <router-link to="/centros">Centros</router-link> |
      <router-link to="/estadisticas">Estadisticas</router-link>
      
    </div>
    
    <router-view />
    
  
  </div>
</template>

<script>

export default {
  name: 'app'
}
</script>

<!-- Estos son lo estilos de la pagina pueden ir en un doc separado o directamente unar bootstrap --> 

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
.bg-back {
  background-color: coral;
}

}
</style>
