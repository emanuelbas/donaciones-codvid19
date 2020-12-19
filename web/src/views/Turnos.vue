<template>
  <div id="turnos">
    <div>
      <h1>
        Eligió las opciones para el turno del centro:
        {{ this.form.cent }} para la fecha: {{ this.form.fecha }} y hora:
        {{ this.form.hora }}
      </h1>
    </div>

    <div v-if="!form.hora">
      <label>Fecha para el turno:</label>
      <input
        v-model="form.fecha"
        type="date"
        :state="false"
        class="form-control my-3"
      />
    </div>
    <button v-on:click="getTurnos()" class="btn btn-primary" v-if="!form.hora">
      Buscar turnos
    </button>

    <div v-if="!form.hora">
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
      <p class="alert alert-danger" v-if="form.fecha && !form.hora">
        No hay turnnos para esta fecha
      </p>
    </div>

    <h1 v-if="form.hora">
      Ingrese sus datos personales para el turno nombre:
      {{ this.form.nombre }} y apellido: {{ this.form.apellido }} , telefono:
      {{ this.form.telefono }} y mail:
      {{ this.form.email }}
    </h1>

    <div v-if="form.hora">
      <label>Nombre:</label>
      <input
        type="text"
        v-model="form.nombre"
        placeholder="Ingrese el nombre"
        class="form-control my-3"
        required
      />
    </div>
    <div v-if="form.hora">
      <label>Apellido:</label>
      <input
        type="text"
        v-model="form.apellido"
        placeholder="Ingrese el apellido"
        class="form-control my-3"
        required
      />
    </div>
    <div v-if="form.hora">
      <label>Email:</label>
      <input
        type="email"
        v-model="form.email"
        placeholder="Ingese el email"
        class="form-control my-3"
        required
      />
    </div>
    <div v-if="form.hora">
      <label>Telefono:</label>
      <input
        type="number"
        v-model="form.telefono"
        placeholder="Ingrese el telefono"
        class="form-control my-3"
        required
      />
    </div>
    <a href="/turnos" class="btn btn-danger" v-if="form.hora">Cancelar</a>
    <button v-on:click="setTurnos()" class="btn btn-primary" v-if="form.hora">
      Guardar Turno
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "turnos",

  data() {
    return {
      form: {
        turnos: "",
        cent: "", //el centro seleccionado
        fecha: "", //la fecha seleccionada
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
  },
  methods: {
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
    test: function () {
      this.form.cent = this.$route.query.centro_id;
    },
    setTurnos: function () {
      console.log("el boton esta funcionando");
      let url =
        "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/id_centro/13/reserva";
      const parms = {
        centro_id: 13,
        email_donante: "ejemplo.post@gmail.com",
        fecha: "2020-11-15",
        hora_fin: "11:00:00",
        hora_inicio: "11:30:00",
        telefono_donante: "2214444444",
      };
      let json = JSON.stringify(parms);

      console.log(json);
      alert(json);

      //let config = {
      // headers:{
      // "Content-Type": "application/json",
      // },

      //};
      axios
        .post(url, json)
        .then((response) => {
          console.log(response);
          console.log("ENTRO!!");
          alert(parms);

          //document.formulario.reset();
          //this.$router.push('/turnos?s=1')
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>
