 <template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12 text-center">
        <div class="col-md-12 col-sm-12">
          <div id="nuevo_centro">
            <div>
              <h1>Nuevo Centro:</h1>
            </div>
            <div class="container">
              <div>
                <label>Nombre del Centro:</label>
                <input
                  v-model="form.nombre"
                  type="text"
                  placeholder="Ingrese el nombre del centro"
                  required
                  class="form-control my-3"
                />
              </div>
              <br />
              <div>
                <label>Direccion:</label>
                <input
                  v-model="form.direccion"
                  type="text"
                  placeholder="Ingrese una direccion"
                  required
                  class="form-control my-3"
                />
              </div>
              <br />
              <div>
                <label>Telefono:</label>
                <input
                  v-model="form.telefono"
                  type="number"
                  placeholder="Ingrese un telefono"
                  required
                  class="form-control my-3"
                />
              </div>
              <br />
              <div>
                <label>Hora de Apertura:</label>
                <input
                  v-model="form.horaA"
                  type="time"
                  required
                  class="form-control my-3"
                />
              </div>
              <br />
              <div>
                <label>Hora de Cierre:</label>
                <input
                  v-model="form.horaC"
                  type="time"
                  required
                  class="form-control my-3"
                />
              </div>
              <br />
              <div>
                <label>Tipo de Centro:</label>
                <select
                  v-model="form.tipoC"
                  class="browser-default custom-select"
                >
                  <option>
                    Todos
                  </option>
                </select>
              </div>
              <br />
              <div>
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
              <br />
              <div>
                <label>Web:</label>
                <input
                  v-model="form.web"
                  type="text"
                  placeholder="Ingrese una web"
                  required
                  class="form-control my-3"
                />
              </div>
              <br />
              <div>
                <label>Email:</label>
                <input
                  v-model="form.email"
                  type="email"
                  placeholder="Ingrese un E-mail"
                  required
                  class="form-control my-3"
                />
              </div>
              <br />
              <div>
                <label>Estado:</label>
                <select
                  v-model="form.estado"
                  class="browser-default custom-select"
                >
                  <option value="1">
                    Publicado
                  </option>
                  <option value="2">
                    Despublicado
                  </option>
                </select>
              </div>
              <br />
              <div>
                <label>Latitud: </label>
                <input
                  v-model="form.latitud"
                  type="text"
                  class="form-control my-3"
                />
              </div>
              <br />
              <div>
                <label>Longitud: </label>
                <input
                  v-model="form.longitud"
                  type="text"
                  class="form-control my-3"
                />
              </div>
              <div>
                <label>Geolocalizacion: </label>
              </div>
              <div>
                <label> CAPTCHA </label>
                <vue-recaptcha
                  sitekey="6Le9WAEVAAAAAO-U7wI50TYIP5nKAxb7VkbkyoSY"
                  @verify="mxVerify"
                >
                </vue-recaptcha>
                <br />
              </div>
              <br />
              <button
                v-on:click="alta_centro()"
                class="btn btn-primary"
                type="submit"
              >
                Aceptar
              </button>
              <a href="/Centros" class="btn btn-danger" type="reset"
                >Cancelar</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
//import VueRecaptcha from "vue-recaptcha";
export default {
  name: "nuevo_centro",
  data() {
    return {
      form: {
        nombre: "",
        direccion: "",
        telefono: "",
        horaA: "",
        horaC: "",
        tipoC: "",
        municipio: "",
        municipios: "",
        web: "",
        email: "",
        estado: "",
        coordenadas: "",
        latitud: "",
        longitud: "",
        recaptcha: null
      }
    };
  },
  mounted() {
    this.getMunicipios();
  },
  methods: {
    getMunicipios: function() {
      var url =
        "https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios";
      axios
        .get(url)
        .then(response => {
          this.form.municipios = response.data.data.Town;
          console.log(this.form.municipios);
        })
        .catch(e => console.log(e));
    },
    alta_centro: function() {
      console.log("el boton esta funcionando");
      // "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/centros/id_centro/"
      // "http://localhost:5000/api/centros/id_centro/"
      let url =
        "https://admin-grupo22.proyecto2020.linti.unlp.edu.ar/api/crear_centro";
      const parms = {
        nombre: "hugo",
        direccion: "hugo",
        telefono: "22222222",
        hora_de_apertura: "20:00",
        hora_de_cierre: "21:00",
        email: "hugo@gmail.com",
        sitio_web: "hugo.com",
        corx: "-38",
        cory: "-58",
        lista_de_tipos: 1,
        id_municipio: 2,
        id_estado: 1,
        protocolo: "PDF",
        historico: 0,
      };
      //let json = JSON.stringify(parms);

      axios
        .post(url, parms)
        .then(response => {
          console.log(response);
          alert("Alta exitosa");
          //document.formulario.reset();
          //this.$router.push('/turnos?s=1')
        })
        .catch(e => console.log(e));
    }
  }
};
</script>