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
        </div>
    </div>
</template>
<script>
//import axios from "axios";
export default 
{
  name: "nuevo_centro",
  data() {
    return {
      form: {
        nombre: "",
           },
    };
  },    
  mounted(){  
  },
  methods: {
    altaCentro: function () {
        alert(this.form.nombre)
    }
  }
}
</script>
