<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Lista de centros con Vue"/>
  <div>
      <table class="table table-striped table-bordered bg-white table-sm">
        <thead>
            <tr>
                <td>Direccion</td>
                <td>Email</td>
                <td>Hora Apertura</td>
                <td>Hora Cierre</td>
                <td>Nombre</td>
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
import HelloWorld from '@/components/HelloWorld.vue'
export default {
   name: 'Home',
  components: {
    HelloWorld
  },
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

