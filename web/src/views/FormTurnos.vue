<template>
  <div id="FormTurnos">
    <h1>
      Ingrese los datos para el turno id: {{ this.id }} y fecha:
      {{ this.fechas }}
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
      <button v-on:click="saludo()" class="btn btn-primary">Guardar</button>
    </form>
  </div>
</template>

<script>

export default {
  name: 'FormTurnos',
  
  data() {
    return {
      id: "",
      fechas: "",
      nombre: "",
      apellido: "",
      telefono: "",
      email: "",
    };
    
  },
  

  
  
  mounted() {
    this.turno();
    
  },

  methods: {
    saludo: function () {
      console.log(this.nombre);
      console.log(this.apellido);
      console.log(this.telefono);
      console.log(this.email);
    },
    turno: function () {
      this.id = this.$store.state.id;
      this.fechas = this.$store.state.fechas;
      console.log(this.$store.state.id);
      console.log(this.$store.state.fechas);
    },
  },
};
</script>