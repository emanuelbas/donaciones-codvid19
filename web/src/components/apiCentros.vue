<template>
  <div>
    <div class="conteiner">
      <h1>Seleccione un Centro y una Fecha para el turno</h1>
    </div>
    <div class="container" id="Form">
      <form>
        <div>
          <label>Centros:</label>
          <b-col md="3">
            <select v-model="select">
              <option
                v-for="centro in centros"
                :key="centro.id"
                :value="centro.nombre"
              >
                {{ centro.nombre }}
              </option>
            </select>
          </b-col>
        </div>
        <div>
          <label>Fecha:</label>
          <b-row>
            <b-col md="3">
              <input v-model="fecha" type="date" :state="false" />
            </b-col>
          </b-row>
        </div>
        <a href="/" class="btn btn-danger">Cancelar</a>
        <button v-on:click="Form" type="submit" class="btn btn-primary">
          Aceptar
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      fecha: "",
      centros: null,
      select: null,
      
    };
  },
  mounted() {
    this.getCentros();
   
  },
  methods: {
    
    getCentros() {
      axios
        .get("https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros")
        .then((response) => {
          this.centros = response.data.centros;
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>