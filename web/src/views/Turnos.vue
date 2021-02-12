<template>
  <div id="turnos" class="container">
    <div class="pb-5">
      <h1>
        Solicitud de turno para Centro de Ayuda <b>#{{ this.form.cent }}</b>
      </h1>
    </div>

    <br />
    <div>
      <label
        >Por favor, seleccione una fecha para poder ver los horarios
        disponibles</label
      >
      <input
        v-on:change="getTurnos()"
        v-model="form.fecha"
        :min="fecha_hoy"
        type="date"
        :state="false"
        class="form-control"
      />
    </div>

    <div v-if="form.bloques">
      <label
        >Seleccione uno de los siguientes
        <b>bloques de horario disponibles</b></label
      >

      <select v-model="form.hora" class="browser-default custom-select">
        <option v-for="bloque in form.bloques" :key="bloque" :value="bloque">
          {{ bloque }}
        </option>
      </select>
    </div>

    <p v-if="form.hora" class="mt-4">
      Ahora ingrese sus datos personales para completar la solicitud.
    </p>

    <div v-if="form.hora">
      <label>Nombre</label>
      <input
        type="text"
        v-model="form.nombre"
        placeholder="Ingrese el nombre"
        class="form-control"
        required
      />
    </div>
    <div v-if="form.hora">
      <label>Apellido</label>
      <input
        type="text"
        v-model="form.apellido"
        placeholder="Ingrese el apellido"
        class="form-control"
        required
      />
    </div>
    <div v-if="form.hora">
      <label>Email</label>
      <input
        type="email"
        v-model="form.email"
        placeholder="Ingese el email"
        class="form-control "
        required
      />
    </div>
    <div v-if="form.hora">
      <label>Telefono</label>
      <input
        type="number"
        v-model="form.telefono"
        placeholder="Ingrese el telefono"
        class="form-control"
        required
      />
    </div>
    <div id="caja-botones" class="mt-4">
      <a href="/centros" class="btn btn-danger">Cancelar</a>
      <button v-on:click="setTurnos()" class="btn btn-primary" v-if="form.hora">
        Guardar Turno
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import router from "../router";

export default {
  name: "turnos",

  data() {
    return {
      form: {
        bloques: "",
        cent: "", //el centro seleccionado
        fecha: "", //la fecha seleccionada
        hora: "", //hora seleccionada para el turno
        nombre: "", //datos del fomulario
        apellido: "",
        telefono: "",
        email: ""
      },
      fecha_hoy: ""
    };
  },

  mounted() {
    this.initialize();
  },
  methods: {
    getTurnos: function() {
      //"https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/centros/id_centro/"
      //"http://localhost:5000/api/centros/id_centro/"
      var url =
        "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/centros/id_centro/" +
        this.form.cent +
        "/turnos_disponibles/fecha=" +
        this.form.fecha;
      axios
        .get(url)
        .then(response => {
          this.form.bloques = response.data.turnos;
        })
        .catch(e => console.log(e));
    },
    initialize: function() {
      this.form.cent = this.$route.query.centro_id;
      this.fecha_hoy = new Date().toISOString().slice(0, 10);
      console.log(this.fecha_hoy);
    },
    setTurnos: function() {
      console.log("el boton esta funcionando");
      // "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/centros/id_centro/"
      // "http://localhost:5000/api/centros/id_centro/"
      let url =
        "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/centros/id_centro/" +
        this.form.cent +
        "/reserva";
      const parms = {
        centro_id: this.form.cent,
        email_donante: this.form.email,
        fecha: this.form.fecha,
        bloque_horario: this.form.hora,
        telefono_donante: this.form.telefono,
        nombre_donante: this.form.nombre,
        apellido_donante: this.form.apellido
      };
      //let json = JSON.stringify(parms);
      let mensaje = this.validar_formulario();
      if (mensaje != "ok") {
        alert(mensaje);
        return 0;
      }
        axios
          .post(url, parms)
          .then(() => {
            alert("¡Su turno fue reservado con éxito!");
            router.push("/");
            //document.formulario.reset();
            //this.$router.push('/turnos?s=1')
          })
          .catch(e => console.log(e));
    
    },
    validar_formulario: function() {
      if (
        this.form.nombre == "" ||
        this.form.apellido == "" ||
        this.form.email == "" ||
        this.form.telefono == ""
      ) {
        return "Faltan completar uno o mas campos";
      }

      return "ok";
    }
  }
};
</script>
