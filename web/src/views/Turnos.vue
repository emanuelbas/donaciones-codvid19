<template>
  <div id="turnos">
    <ApiCentros/>
    <ApiTurnos/>
  </div>
</template>

<script>
import ApiCentros from '@/components/apiCentros.vue';
import ApiTurnos from '@/components/apiTurnos.vue';

export default {
  data() {
    return {
      fecha: "",
      centros: null,
      select: null,
      turnos: null,
    };
  },
  name: 'turnos',
  components: {
    ApiCentros,
    ApiTurnos
  },
  
}
</script>
