<template>
  <div id="turnos">
    
      <div class="conteiner">
        <h1>
          Seleccione un Municipio, un Centro y una Fecha para el turno id:{{
            this.form.cent
          }}
          y fecha:{{ this.form.fecha }} y Hora: {{ this.form.hora }}
        </h1>
        
      </div>

      <div>
        <label>Municipios:</label>

        <select v-model="form.muni" class="browser-default custom-select">
          <option
            v-for="municipio in form.municipios"
            :key="municipio.id"
            :value="municipio.id"
          >
            {{ municipio.name }}
          </option>
        </select>
      </div>
      <div>
        <label>Centros:</label>

        <select v-model="form.cent" class="browser-default custom-select">
          <option
            v-for="centro in form.centros"
            :key="centro.id_centro"
            :value="centro.id_centro"
          >
            <td v-if="centro.id_municipio == form.muni">
              {{ centro.nombre }}
            </td>
          </option>
        </select>
      </div>
      <div>
        <label>Fecha para el turno:</label>
        <input v-model="form.fecha" type="date" :state="false" class="form-control my-3" />
         
      </div>
    <a href="/" class="btn btn-danger">Cancelar</a>
    <button v-on:click="getTurnos()" class="btn btn-primary">Aceptar</button>
    <div>
      <label>Hora de turno:</label>

      <select v-model="form.hora" class="browser-default custom-select">
        <option
          v-for="turno in form.turnos"
          :key="turno.id"
          :value="turno.hora_inicio"
        >
          {{ turno.hora_inicio }}
        </option>
      </select>
    </div>
    
  
  <div id="FormTurnos">
    <h1>
      Ingrese los datos para el turno nombre: {{ this.form.nombre }} y apellido:
      {{ this.form.apellido }} , telefono: {{ this.form.telefono}} y mail: {{this.form.email}}
    </h1>

    <form name="formulario">
      <div>
        <label>Nombre:</label>
        <input
          type="text"
          v-model="form.nombre"
          placeholder="Ingrese el nombre"
          class="form-control my-3"
          required
        />
      </div>
      <div>
        <label>Apellido:</label>
        <input
          type="text"
          v-model="form.apellido"
          placeholder="Ingrese el apellido"
          class="form-control my-3"
          required
        />
      </div>
      <div>
        <label>Email:</label>
        <input
          type="email"
          v-model="form.email"
          placeholder="Ingese el email"
          class="form-control my-3"
          required
        />
      </div>
      <div>
        <label>Telefono:</label>
        <input
          type="number"
          v-model="form.telefono"
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
       
      form:{
        turnos: "",
        centros: "",
        municipios: "",  
        cent: "", //el centro seleccionado
        fecha: "", //la fecha seleccionada
        muni: "", //el municipio selecionado
        hora: "", //hora seleccionada para el turno
        nombre: "", //datos del fomulario
        apellido: "",
        telefono: "",
        email: "",
      },  
    };
  
  },

  mounted() {
    this.test();
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
          this.form.municipios = response.data.data.Town;
        })
        .catch((e) => console.log(e));
    },
    getCentros() {
      axios
        .get(
          "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/todos"
        )
        .then((response) => {
          this.form.centros = response.data.centros;
        })
        .catch((e) => console.log(e));
    },

    getTurnos: function () {
      var url =
        "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/id_centro/" +
        this.form.cent +
        "/turnos_disponibles/fecha=" +
        this.form.fecha;
      axios
        .get(url)
        .then((response) => {
          this.form.turnos = response.data.turnos;
        })
        .catch((e) => console.log(e));
    },
    test: function(){
      this.form.cent = this.$route.query.centro_id
      alert(this.$route.query.centro_id)
    },
    setTurnos: function(){
      console.log("el boton esta funcionando")
      let url =  "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/id_centro/8/reserva";
      const parms = {
        centro_id : "13",
        email_donante : "probando.post@gmail.com",
        fecha : "2020-11-15",
        hora_fin : "11:00:00",
        hora_inicio : "11:30:00",
        telefono_donante : "2214444444"  
      }
      let json = JSON.stringify(parms)

      console.log(json)
      alert(json)

      //let config = {
       // headers:{
         // "Content-Type": "application/json",
       // },

      //};
      axios
        .post(url, JSON.stringify(parms))
          .then((response) => {
           console.log(response);
           console.log(parms)
            alert(parms)
          
            //document.formulario.reset();
            //this.$router.push('/turnos?s=1')
          
        })
          .catch((e) => console.log(e));
        


    },
  },
};
</script>
