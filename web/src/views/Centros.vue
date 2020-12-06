<!-- Perdon por la pisadita, aca esta el archivo de antes
https://gitlab.catedras.linti.unlp.edu.ar/proyecto2020/grupo22/-/blob/5de60a76b00fcc6bb43592f370c442d3036c5634/web/src/views/Centros.vue
-->
<template>
  <div>
    <Title title="Mapa de Centros de Ayuda"/>
    <ul>
      <li v-for="centro in centros" :key="centro.id">{{centro.nombre}}</li>
    </ul>
    <l-map
      v-if="showMap"
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 80%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
    </l-map>
  </div>


</template>

<script>
import axios from "axios";
import Title from '@/components/Title.vue';
//import L from 'leaflet';
import { LMap, LTileLayer  } from 'vue2-leaflet';//LMarker
import { latLng } from "leaflet";


export default {
  name: 'Centros',
  components: {
    Title,
    LMap,
    LTileLayer,
    //LMarker
  },
  data() {
    return {
      centros: [],
      zoom: 13,
      center: latLng(47.41322, -1.219482),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      withPopup: latLng(47.41322, -1.219482),
      withTooltip: latLng(47.41422, -1.250482),
      currentZoom: 11.5,
      currentCenter: latLng(47.41322, -1.219482),
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5
      },
      showMap: true
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

