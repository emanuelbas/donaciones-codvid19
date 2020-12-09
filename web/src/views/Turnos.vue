<template>
  <div id="turnos">
    <div>
      <div class="conteiner">
        <h1>Seleccione un Municipio, un Centro y una Fecha para el turno</h1>
      </div>

      <div>
        <div>
          <label>Municipios:</label>
          <v-col md="3">
            <select v-model="muni">
              <option
                v-for="municipio in municipios"
                :key="municipio.id"
                :value="municipio.id"
              >
                {{ municipio.name }}
              </option>
            </select>
          </v-col>
        </div>
        <div>
          <label>Centros:</label>
          <v-col md="3">
            <select v-model="cent">
              <option
                v-for="centro in centros"
                :key="centro.id"
                :value="centro.id"
              >
                
                 {{ centro.nombre }}
        
              </option>
            </select>
          </v-col>
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
        <button  v-on:click="saludo()" class="btn btn-primary">
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
      c: null,
    };
  },
  mounted() {
    this.getTurnos();
    this.getCentros();
    this.getMunicipios();
    
  },
  methods: {
    saludo: function (){
      console.log("fecha", this.fecha)
      console.log("centro", this.cent)
      console.log("municipalidad", this.muni)

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

    getTurnos() {
      var url = "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/id_centro/13/turnos_disponibles/fecha=2020-11-15"
      axios
        .get(
          url
        )
        .then((response) => {
          this.turnos = response.data.turnos;
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>
