<template>
  <div id="turnos">
    
      <div class="conteiner">
        <h1>
          Seleccione un Municipio, un Centro y una Fecha para el turno id:{{
            this.cent
          }}
          y fecha:{{ this.fecha }} y Hora: {{ this.hora }}
        </h1>
        
      </div>

      <div>
        <label>Municipios:</label>

        <select v-model="muni" class="browser-default custom-select">
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

        <select v-model="cent" class="browser-default custom-select">
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
        <label>Fecha para el turno:</label>
        <input v-model="fecha" type="date" :state="false" class="form-control my-3" />
         
      </div>
    <a href="/" class="btn btn-danger">Cancelar</a>
    <button v-on:click="getTurnos()" class="btn btn-primary">Aceptar</button>
    <div>
      <label>Hora de turno:</label>

      <select v-model="hora" class="browser-default custom-select">
        <option
          v-for="turno in turnos"
          :key="turno.id"
          :value="turno.hora_inicio"
        >
          {{ turno.hora_inicio }}
        </option>
      </select>
    </div>
    
  
  <div id="FormTurnos">
    <h1>
      Ingrese los datos para el turno nombre: {{ this.nombre }} y apellido:
      {{ this.apellido }} , telefono: {{ this.telefono}} y mail: {{this.email}}
    </h1>

    <form>
      <div>
        <label>Nombre:</label>
        <input
          type="text"
          v-model="nombre"
          placeholder="Ingrese el nombre"
          class="form-control my-3"
          required
        />
      </div>
      <div>
        <label>Apellido:</label>
        <input
          type="text"
          v-model="apellido"
          placeholder="Ingrese el apellido"
          class="form-control my-3"
          required
        />
      </div>
      <div>
        <label>Email:</label>
        <input
          type="text"
          v-model="email"
          placeholder="Ingese el email"
          class="form-control my-3"
          required
        />
      </div>
      <div>
        <label>Telefono:</label>
        <input
          v-model="telefono"
          placeholder="Ingrese el telefono"
          class="form-control my-3"
          required
        />
      </div>
      <a href="/turnos" class="btn btn-danger">Cancelar</a>
      <button v-on:click="setTurnos()" class="btn btn-primary">Guardar Turno</button>
    </form>
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
      hora: null, //hora seleccionada para el turno
      nombre: "", //datos del fomulario
      apellido: "",
      telefono: "",
      email: "",
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
    setTurnos: function(){
      var url =  "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/id_centro/"+this.centro+"/reserva";
      axios
        .post(url)
        


    },
  },
};
</script>
