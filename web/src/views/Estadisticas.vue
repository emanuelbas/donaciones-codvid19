<template>
  <div>
    <Title title="Estadísticas"/>

    <div id="caja-de-graficos">

      <div v-if="current == 0" class="container mt-5">
        <h3>Cantidad de Centros por Tipo</h3>
        <h5>Se muestran los distintos tipos de centros y cuantos hay registrados</h5>
        <br>
        <ve-pie  :data="tiposDeCentro"></ve-pie>
      </div>

      <div v-if="current == 1" class="container mt-5">
        <h3>Cantidad de Turnos por Fecha</h3>
        <h5> Se muestran las fechas de los últimos 30 días</h5>
        <br>
        <ve-line class="container" :data="turnosPorDia"></ve-line>
      </div>

      <div v-if="current == 2" class="container mt-5">
        <h3>TOP-10 Centros de Ayuda</h3>
        <h5> Se muestran los 10 Centros de ayuda más concurridos </h5>
        <br>
        <ve-bar :data="mejoresCentros"></ve-bar>
      </div>
    </div>

    <div id="caja-de-botones">
      <button v-if="current != 0" v-on:click="current -= 1" class="btn btn-primary">◄</button>
      <button v-if="current == 0" disabled class="btn btn-primary">◄</button>
      <button v-if="current != 2" v-on:click="current += 1" class="btn btn-primary">►</button>
      <button v-if="current == 2" disabled class="btn btn-primary">►</button>
    </div>

  </div>
</template>

<script>
import VeLine from 'v-charts/lib/line.common';
import axios from "axios";
import Title from '@/components/Title.vue';
export default {
  name: 'Estadisticas',
  components: { VeLine, Title },
  data () {
    return {
      current       : 0,
      tiposDeCentro : {},
      mejoresCentros: {},
      turnosPorDia  : {}
    }
  },  
  mounted() {
    this.getPieDeTipos();
    this.getTopTen();
    this.getTotalTurnosDelMes();
  },
  methods: {
    getPieDeTipos() {
      axios
        .get("https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/estadisticas/tipos")
        .then((response) => {
          this.tiposDeCentro =
          {
            columns: ['tipo','cantidad'],
            rows   : response.data.centros_por_tipo
          }
        })
        .catch((e) => console.log(e));
    },
    getTopTen(){
      axios
        .get("https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/estadisticas/top10_centros_del_mes")
        .then((response) => {
          this.mejoresCentros =
          {
            columns: ['nombre','cantidad'],
            rows   : response.data.top_10
          }
        })
        .catch((e) => console.log(e));
    },
    getTotalTurnosDelMes(){
      axios
        .get("https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/estadisticas/total_turnos_del_mes")
        .then((response) => {
          this.turnosPorDia =
          {
            columns: ['dia','turnos'],
            rows   : response.data.turnos_por_dia
          }
        })
        .catch((e) => console.log(e));
    }
  }
}
</script>