<!-- Perdon por la pisadita, aca esta el archivo de antes
https://gitlab.catedras.linti.unlp.edu.ar/proyecto2020/grupo22/-/blob/5de60a76b00fcc6bb43592f370c442d3036c5634/web/src/views/Centros.vue
-->
<template>
  <div>
    <Title title="Mapa de Centros de Ayuda"/>
    <ul>
      <li v-for="centro in centros" :key="centro.id">{{centro.nombre}}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import Title from '@/components/Title.vue';

export default {
  name: 'Centros',
  components: {
    Title
  },
  data() {
    return {
      centros: [],
    };
  },
  mounted() {
    this.getCentros();
  },
  methods: {
    getCentros() {      
      axios
        .get(
          "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros"
        )
        .then((response) => {
          console.log(response)
          this.centros = response.data.centros;
        })
        .catch((e) => alert(e));
    },
  },
};
</script>

