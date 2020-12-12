<!-- Perdon por la pisadita, aca esta el archivo de antes
https://gitlab.catedras.linti.unlp.edu.ar/proyecto2020/grupo22/-/blob/5de60a76b00fcc6bb43592f370c442d3036c5634/web/src/views/Centros.vue
-->
<template>
  <div style="height: 500px; width: 100%">
    <Title title="Mapa de Centros de Ayuda"/>
    <l-map
      v-if="showMap"
      :zoom="zoom"
      :center="center"
      :bounds="bounds"
      :max-bounds="maxBounds"
      :options="mapOptions"
      style="height: 100%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker v-for="centro in centros" :lat-lng="{lat:centro.lat, lng:centro.lng}" :key="centro.id">
        <l-popup>
          <div>
            <h5>{{centro.nombre}}</h5>
            <p>
              <b>Dirección:</b> {{centro.direccion}}<br>
              <b>Horario:</b> {{centro.hora_apertura}} - {{centro.hora_cierre}}<br>
              <b>Teléfono:</b> {{centro.telefono}}<br><br>
              <button style="text-align: right;" @click="innerClick(centro)">Pedir turno</button>
            </p>
          </div>
        </l-popup>
      </l-marker>
    </l-map>
  </div>

</template>

<script>
import axios from "axios";
import Title from '@/components/Title.vue';
import { latLng, latLngBounds } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";//LTooltip



export default {
  name: 'Centros',
  components: {
    Title,
    LMap,
    LTileLayer,
    LMarker,
    LPopup
    //LTooltip
  },
  data() {
    return {
      zoom: 6,
      center: latLng(-34.925033, -57.933933),
      bounds: latLngBounds([
        [-32.26184, -67.108055],
        [-42.988576, -45.74707]
      ]),
      maxBounds: latLngBounds([
        [-32.26184, -67.108055],
        [-42.988576, -45.74707]
      ]),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; Grupo 22 - 2020',
      withPopup: latLng(34.925033, -57.933933),
      withTooltip: latLng(34.925033, -57.933933),
      currentZoom:  12.5,
      currentCenter: latLng(-34.925033, -57.933933),
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5,
        minZoom: 6
      },
      showMap: false
    };
  },
  mounted() {
    this.getCentros();
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    showLongText() {
      this.showParagraph = !this.showParagraph;
    },
    innerClick(centro) {
      alert("Se abre la ventana de turnos para el centro "+centro.nombre);
    },
    getCentros() {
      axios
        .get("https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/Api/centros/todos")
        .then((response) => {
          this.centros = response.data.centros;
          this.showMap = true
        })
        .catch((e) => console.log(e));
    }
  }
};
</script>

