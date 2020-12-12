<template>
  <div class="title">
    <h1>{{ title }}</h1>
  </div>  
</template>
<!-- Aqui estan los componentes que podemos usar en las vistas ? -->



<script>
export default {
  el: 'app',
  name: 'HelloWorld',
  props: {
    title: String
  }
}
</script>

