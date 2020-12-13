<template>
  <div class="datos">
    <h1>{{ ide }}</h1>
    <h1>{{ fecha }}</h1>
  </div>  
</template>
<!-- Aqui estan los componentes que podemos usar en las vistas ? -->



<script>
export default {
  el: 'datos',
  name: 'Datos',
  props: {
    ide: String,  
    fecha: Date
  }
}
</script>