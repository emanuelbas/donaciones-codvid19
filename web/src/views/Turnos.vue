<template>
  <div class="turnos">
    <div class="conteiner">
      <p> fecha: {{fecha}}</p>

    </div>
    <div class="container" id="Form">
      <h1>Ingrese la fecha para el turno</h1>
      <form>
        <b-row>
          <b-col md="6">
            <input v-model="fecha" type="date" :state="false" />
                   
          </b-col>
        </b-row>
        <a href="/" class="btn btn-danger">Cancelar</a>
        <button v-on:click="Form" type="submit" class="btn btn-primary">Aceptar</button>
      </form>
    </div>
  </div>
</template>

<script>

export default {
 name: 'Form',
 data(){
   return{
     fecha: ''
   }
   
 } 
}
</script>
