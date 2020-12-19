<template>
  <div>
    <Title title="Estadísticas"/>
    <div class="container mt-5">
      <h3>Cantidad de Centros por Tipo</h3>
      <h5>Se muestran los distintos tipos de centros y cuantos hay registrados</h5>
      <br>
      <ve-pie  :data="tiposDeCentro"></ve-pie>
    </div>

    <div class="container mt-5">
      <h3>Cantidad de Turnos por Fecha</h3>
      <h5> Se muestran las fechas de los últimos 30 días</h5>
      <br>
      <ve-line class="container" :data="turnosPorDia"></ve-line>
    </div>

    <div class="container mt-5">
      <h3>TOP-10 Centros de Ayuda</h3>
      <h5> Se muestran los 10 Centros de ayuda más concurridos en los últimos 30 días</h5>
      <br>
      <ve-bar :data="top10"></ve-bar>
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
      filas: [],
      tiposDeCentro: {
          columns: ['tipo','cantidad'],
          rows: [
            { 'tipo': 'Sangre', 'cantidad':10 },
            { 'tipo': 'Plasma', 'cantidad':32 },
            { 'tipo': 'Ropa', 'cantidad':5 },
            { 'tipo': 'Comida', 'cantidad':55 },
          ]
        },
      turnosPorDia: {
          columns: ['date', 'turnos'],
          rows: [
            { 'date': '06-01', 'turnos': 233 },
            { 'date': '07-01', 'turnos': 1223 },
            { 'date': '08-01', 'turnos': 2123 },
            { 'date': '09-01', 'turnos': 4123 },
            { 'date': '10-01', 'turnos': 3123},
            { 'date': '11-01', 'turnos': 7123 },
            { 'date': '12-01', 'turnos': 123 },
            { 'date': '13-01', 'turnos': 1223 },
            { 'date': '14-01', 'turnos': 2123 },
            { 'date': '15-01', 'turnos': 4123 },
            { 'date': '16-01', 'turnos': 3123},
            { 'date': '21-01', 'turnos': 123 },
            { 'date': '22-01', 'turnos': 1223 },
            { 'date': '23-01', 'turnos': 2123 },
            { 'date': '24-01', 'turnos': 4123 },
            { 'date': '25-01', 'turnos': 3123},
            { 'date': '26-01', 'turnos': 123 },
            { 'date': '27-01', 'turnos': 1223 },
            { 'date': '28-01', 'turnos': 2123 },
            { 'date': '29-01', 'turnos': 4123 },
            { 'date': '30-01', 'turnos': 3123},
          ]
        },

      top10: {
          columns: ['centro', 'turnos'],
          rows: [
            { 'centro': 'Centro de ayuda Pepito', 'turnos': 10 },
            { 'centro': 'Centro de ayuda Cruz Roja', 'turnos': 40},
            { 'centro': 'Hospital de Niños', 'turnos': 80 },
            { 'centro': 'Comedor La Esperanza', 'turnos': 125 },
            { 'centro': 'Club Deportivo los Saltamontes', 'turnos': 200 },
            { 'centro': 'Escuela Secundaria Nº5', 'turnos': 300 },
            { 'centro': 'Centro de ayuda Pepito', 'turnos': 310 },
            { 'centro': 'Centro de ayuda Cruz Roja', 'turnos': 320},
            { 'centro': 'Hospital de Niños', 'turnos': 330 },
            { 'centro': 'Comedor La Esperanza', 'turnos': 350 },
            { 'centro': 'Club Deportivo los Saltamontes', 'turnos': 400 },
            { 'centro': 'Escuela Secundaria Nº5', 'turnos': 500 }        
          ]
        }

    }
  },  
  mounted() {
    this.getPieDeTipos();
  },
  methods: {
    getPieDeTipos() {
      axios
        .get("https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/estadisticas/tipos")
        .then((response) => {
          this.tiposDeCentro =
          {
            columns: ['tipo','cantidad'],
            rows: response.data.centros_por_tipo
          }
        })
        .catch((e) => console.log(e));
    }
  }
}
</script>