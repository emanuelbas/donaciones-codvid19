<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>  
</template>
<!-- Aqui estan los componentes que podemos usar en las vistas ? -->



<script>
export default {
  el: 'app',
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

