<template>
  <div class="title">
    <h1>{{ ide }}</h1>
    <h1>{{ fecha }}</h1>
  </div>  
</template>
<!-- Aqui estan los componentes que podemos usar en las vistas ? -->



<script>
export default {
  el: 'app',
  name: 'Datos',
  props: {
    ide: Number,  
    title: Date
  }
}
</script>