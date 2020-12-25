 <template>
    <div id="nuevo_centro">
        <div>
          <h1> Nuevo Centro:</h1>
        </div>
        <div class= "container">
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
          <br>
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
          <br>
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
          <br>
          <div>
                <label>Hora de Apertura:</label>
                <input
                  v-model="form.horaA"
                  type="date"
                  required
                  class="form-control my-3"
                 />
          </div>
          <br>
          <div>
                <label>Hora de Cierre:</label>
                <input
                  v-model="form.horaC"
                  type="date"
                  required
                  class="form-control my-3"
                 />
          </div>
          <br>
          <div>
                <label>Tipo de Centro:</label>
                <select v-model="form.tipoC" class="browser-default custom-select" >
                    <option>
                        Todos
                    </option>
                </select>
          </div>
          <br>
          <div>
                <label>Municipio:</label>
                <select v-model="form.municipio" class="browser-default custom-select" >
                    <option>
                        Todos
                    </option>
                </select>
          </div>
          <br>
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
          <br>
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
          <br>
          <div>
                <label>Estado:</label>
                <select v-model="form.estado" class="browser-default custom-select" >
                    <option>
                        Publicado
                    </option>
                    <option>
                        Despublicado
                    </option>
                </select>
          </div>
          <br>
          <div>
              <label>Latitud: </label>
              <input
                  v-model="form.latitud"
                  type="text"
                  class="form-control my-3"
                 />
          </div>
          <br>
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
          <br>
          <button v-on:click="alta_centro()" class="btn btn-primary" type="submit" >
              Aceptar
          </button>
          <a href="/Centros" class="btn btn-danger" type="reset" >Cancelar</a>
        </div>
    </div>
</template>
<script>
//import axios from "axios";
import VueRecaptcha from "vue-recaptcha";
export default 
{
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
        web: "",
        email: "",
        estado: "",
        coordenadas: "",
        latitud: "",
        longitud: "",
        recaptcha: null
           },
    };
  },    
  mounted(){  
  },
  methods: {
    alta_centro: function () {
        alert("el boton aceptar esta funcionando")
        //console.log("el boton aceptar esta funcionando");
    },
    mxVerify( response ) {
      alert("entro");
      this.recaptcha = response
    },
    components: {
      "vue-recaptcha": VueRecaptcha
  }
}
}
</script>