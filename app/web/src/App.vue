<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view />
    <div>
      <table class="table table-striped table-bordered bg-white table-sm">
        <thead>
            <tr>
                <td>Direccion</td>
                <td>Email</td>
                <td>Hora Apertura</td>
                <td>Hora Cierre</td>
                <td>Nombre/td>
                <td>Telefono</td>
                <td>Tipos</td>
                
            </tr>
        </thead>
        <tbody>
          <tr v-for="todo in todos" :key="todo.id">

            <td>{{ todo.direccion }} </td>
            <td>{{ todo.email }} </td>
            <td>{{ todo.hora_apertura }} </td>
            <td>{{ todo.hora_cierre }} </td>
            <td>{{ todo.nombre }} </td>
            <td>{{ todo.telefono }} </td>
            <td v-for="tipo in todo.tipos" :key="tipo.id">{{ tipo.id }}--{{ tipo.nombre }} </td>
          </tr>
        </tbody>
      </table>
    <button class="btn btn-primary">Agregar Centro</button>
    </div>
  
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      todos: [],
    };
  },
  mounted() {
    console.log("hola mundo desde mounted");
    this.getTodos();
  },
  methods: {
    getTodos() {
      
      axios
        .get(
          "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros"
        )
        .then((response) => {
          console.log(response)
          this.todos = response.data.centros;
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>

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
}
</style>
