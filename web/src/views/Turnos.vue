<template>
  <div id="turnos">
    <div>
      <div class="conteiner">
        <h1>Seleccione un Municipio, un Centro y una Fecha para el turno id:{{ this.cent}} y fecha:{{this.fecha}}</h1>
        <Datos ide="Esto es un id" />
      </div>

      <div>
        <div>
          <label>Municipios:</label>

          <select v-model="muni">
            <option
              v-for="municipio in municipios"
              :key="municipio.id"
              :value="municipio.id"
            >
              {{ municipio.name }}
            </option>
          </select>
        </div>
        <div>
          <label>Centros:</label>

          <select v-model="cent">
            <option
              v-for="centro in centros"
              :key="centro.id_centro"
              :value="centro.id_centro"
            >
              <td v-if="centro.id_municipio == muni">
                {{ centro.nombre }}
              </td>
            </option>
          </select>
        </div>
        <div>
          <label>Fecha:</label>
          <v-row>
            <v-col md="3">
              <input v-model="fecha" type="date" :state="false" />
            </v-col>
          </v-row>
        </div>
        <a href="/" class="btn btn-danger">Cancelar</a>
        <button v-on:click="getTurnos()" class="btn btn-primary">
          Aceptar
        </button>
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
            <a href="/FormTurnos" class="btn btn-info mb-2">Reservar Turno</a>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Datos from '@/components/Datos.vue';

export default {
  name: "turnos",
  components: {
    Datos
  },
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
    this.getCentros();
    this.getMunicipios();
  },
  methods: {

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

    getTurnos: function () {
      
      
      var url =
        "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/id_centro/" +
        this.cent +
        "/turnos_disponibles/fecha=" +
        this.fecha;
      axios
        .get(url)
        .then((response) => {
          this.turnos = response.data.turnos;
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>
