 <template>
<div id="alta_centro" class="container" >
  <h1>Registra tu centro</h1>
  <p class="mb-5"> Una vez registrado quedará pendiente de aprobación por el personal </p>
  <div id="formulario" class="container">
    
    <div class="mb-4">
      <label>Nombre del Centro:</label>
      <input
        v-model="form.nombre"
        type="text"
        placeholder="Ingrese el nombre del centro"
        required
        class="form-control"
      />
    </div>

    <div class="mb-5">
      <label>Direccion:</label>
      <input
        v-model="form.direccion"
        type="text"
        placeholder="Ingrese una direccion"
        required
        class="form-control"
      />
    </div>

    <div class="mb-5">
      <label>Telefono:</label>
      <input
        v-model="form.telefono"
        type="number"
        placeholder="Ingrese un telefono"
        required
        class="form-control"
      />
    </div>

    <div class="mb-5">
      <label>Hora de Apertura:</label>
      <input
        id="hora_apertura"
        name="hora_apertura"
        v-model="form.hora_de_apertura"
        type="time"
        required
        class="form-control"
      />
    </div>

    <div class="mb-5">
      <label>Hora de Cierre:</label>
      <input
        v-model="form.hora_de_cierre"
        type="time"
        required
        class="form-control"
      />
    </div>

    <div class="mb-5" hidden>
      <label>Tipo de Centro:</label>
      <select
        v-model="form.tipo"
        class="browser-default custom-select"
      >
        <option>
          Todos
        </option>
      </select>
    </div>

    <div class="mb-5">
      <label>Municipio:</label>
      <select
        v-model="form.municipio"
        class="browser-default custom-select"
      >
        <option v-for="m in form.municipios" :key="m" :value="m.id">
          {{ m.name }}
        </option>
      </select>
    </div>

    <div class="mb-5">
      <label>Web:</label>
      <input
        v-model="form.web"
        type="text"
        placeholder="Ingrese una web"
        required
        class="form-control"
      />
    </div>

    <div class="mb-5">
      <label>Email:</label>
      <input
        v-model="form.email"
        type="email"
        placeholder="Ingrese un E-mail"
        required
        class="form-control"
      />
    </div>

    <div class="mb-5" hidden>
      <label>Latitud: </label>
      <input
        v-model="form.latitud"
        type="text"
        class="form-control"
      />
    </div>

    <div class="mb-5" hidden>
      <label>Longitud: </label>
      <input
        v-model="form.longitud"
        type="text"
        class="form-control"
      />
    </div>

    <div class="mb-5" style="height: 400px; width: 100%">
      <label>Seleccione la ubiccación del centro</label>
      <l-map 
        v-if="showMap"
        @click="actualizaPosicion"
        :zoom="zoom"
        :center="center"
        :max-bounds="maxBounds"
        :options="mapOptions"
        style="height: 100%"
      >
        <l-tile-layer
          :url="url"
          :attribution="attribution"
        ></l-tile-layer>
        <!--l-marker :lat-lng="marker_position">
          <p>A verrrrr</p>
        </l-marker-->
      </l-map>
    </div>

    <!-- div class="mb-5" hidden>
      <label> CAPTCHA </label>
      <vue-recaptcha
        sitekey="6Le9WAEVAAAAAO-U7wI50TYIP5nKAxb7VkbkyoSY"
        @verify="mxVerify"
      >
      </vue-recaptcha>
    </div-->

    <div class="pt-5 mb-5" id="botones">
      <button
        v-on:click="alta_centro()"
        class="btn btn-primary"
        type="submit"
      >Aceptar</button>
      <a href="/Centros" class="btn btn-danger" type="reset">Cancelar</a>
    </div>
  </div>
</div>
</template>


<script>
import axios from "axios";
import router from '../router'
import { latLng, latLngBounds } from "leaflet";
import { LMap, LTileLayer  } from "vue2-leaflet"; //, LPopupLMarker,
//import VueRecaptcha from "vue-recaptcha";
export default {
  name: "alta_centro",
  components: {
    LMap,
    LTileLayer,
    //LMarker
    //LPopup
    //LTooltip
  },
  data() {
    return {
      form           : {
        nombre          : "",
        direccion       : "",
        telefono        : "",
        hora_de_apertura: "",
        hora_de_cierre  : "",
        tipo            : "",
        municipio       : "",
        web             : "",
        email           : "",
        latitud         : "",
        longitud        : "",
      },
      municipios     :[],
      recaptcha      : null,
      //Variables del mapa
      marker_position: latLng(-34.921127, -57.937775),
      showMap        : true,
      zoom           : 13,
      center         : latLng(-34.921127, -57.937775),
      bounds         : latLngBounds([ [-32.26184, -67.108055],[-42.988576, -45.74707] ]),
      maxBounds      : latLngBounds([ [-32.26184, -67.108055],[-42.988576, -45.74707] ]),
      url            : 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution    : '&copy; Grupo 22 - 2020',
      showParagraph  : false,
      mapOptions     : {
        zoomSnap        : 0.5,
        minZoom         : 6
      }
    };
  },
  mounted() {
    this.getMunicipios();
  },
  methods: {
    actualizaPosicion(event) {
      
      this.form.latitud  = event.latlng.lat
      this.form.longitud = event.latlng.lng
      alert("¡Posición actualizada! Lat-"+this.form.latitud+" Lng-"+this.form.longitud)
    },
    addMarker(event) {
      console.log(event)
      //Habría que actualizar el marker actual this.marker y hacer que se vea
    },  
    getMunicipios: function() {
      var url = "https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios";
      axios
        .get(url)
        .then(response => {
          this.form.municipios = response.data.data.Town;
          console.log(this.form.municipios);
        })
        .catch(e => console.log(e));
    },
    alta_centro: function() {
      // "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/crear_centro"
      // "http://localhost:5000/api/crear_centro"
      let url     = "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/crear_centro";
      const parms = {
        direccion       : this.form.direccion,
        email           : this.form.email,
        hora_de_apertura: this.form.hora_de_apertura,
        hora_de_cierre  : this.form.hora_de_cierre,
        id_municipio    : this.form.municipio,
        nombre          : this.form.nombre,
        sitio_web       : this.form.web,
        telefono        : this.form.telefono,
        tipos           : [],
        latitud         : this.form.latitud,
        longitud        : this.form.longitud
      };
      //let json = JSON.stringify(parms);

      let msj = this.validar_formulario()
      if (msj != "ok"){
        alert(msj)
        return 0
      }
      axios
        .post(url, parms)
        .then(response => {
          console.log(response);
          alert("Se envió la solicitud para registrar su Centro de Ayuda, pronto un administrador revisará la solicitud. ¡Muchas gracias!");
          router.push("/")
        })
        .catch(e => console.log(e));
    },
    validar_formulario: function() {

      if (this.form.nombre == "" 
        || this.form.direccion == "" 
        || this.form.telefono == "" 
        || this.form.email == ""
        || this.form.web == ""
        || this.form.latitud == ""
        || this.form.longitud == ""
        || this.form.hora_de_cierre == ""
        || this.form.hora_de_apertura == "") {
        return "Por favor, complete todos los campos."
      }

      return "ok"
    }
  }
};
</script>