<template>
  <div id="turnos">
    <div>
      <div class="conteiner">
        <h1>
          Seleccione primero un Municipio, un Centro y una Fecha para el turno
        </h1>
      </div>
      <div class="container" id="Form">
        <form>
          <div>
            <label>Municipios:</label>
            <b-col md="3">
              <select v-model="muni">
                <option
                  v-for="municipio in municipios"
                  :key="municipio.id"
                  :value="municipio.name"
                >
                  {{ municipio.name }}
                </option>
              </select>
            </b-col>
          </div>
          <div>
            <label>Centros:</label>
            <b-col md="3">
              <select v-model="cent">
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
    <div>
      <table class="table table-striped table-bordered bg-white table-sm">
        <thead>
          <tr>
            <td>Centro Id</td>
            <td>Fecha</td>
            <td>Hora Inicio</td>
            <td>Hora Fin</td>
            <td>Operaciones</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="turno in turnos" :key="turno.id">
            <td>{{ turno.centro_id }}</td>
            <td>{{ turno.fecha }}</td>
            <td>{{ turno.hora_inicio }}</td>
            <td>{{ turno.hora_fin }}</td>
            <a href="#" class="btn btn-info mb-2">Reservar Turno</a>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "turnos",

  data() {
    return {
      turnos: null,
      centros: null,
      municipios: null,
      fecha: "", //la fecha seleccionada
      cent: null, //el centro seleccionado
      muni: null, //el municipio selecionado
    };
  },
  mounted() {
    this.getTurnos();
    this.getCentros();
    this.getMunicipios();
  },
  methods: {
    getTurnos() {
      axios
        .get(
          "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/id_centro/13/turnos_disponibles/fecha=2020-11-15"
        )
        .then((response) => {
          this.turnos = response.data.turnos;
        })
        .catch((e) => console.log(e));
    },
    getCentros() {
      axios
        .get(
          "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/todos"
        )
        .then((response) => {
          this.centros = response.data.centros;
        })
        .catch((e) => console.log(e));
    },
    getMunicipios() {
      axios
        .get(
          "https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios"
        )
        .then((response) => {
          this.municipios = response.data.data.Town;
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>
