<template>
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
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      turnos: null,
    };
  },
  mounted() {
    this.getTurnos();
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
  },
};
</script>