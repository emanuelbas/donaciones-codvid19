import Vue from 'vue'
import VueRouter from 'vue-router'
import Centros from '../views/Centros.vue'
import Home from '../views/Home.vue'
import Turnos from '../views/Turnos.vue'
import Estadisticas from '../views/Estadisticas.vue'
import AltaCentro from '../views/AltaCentro.vue'

Vue.use(VueRouter)
  //Aqui van las rutas de las vistas
const routes = [ 
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Centros',
    name: 'Centros',
    component: Centros
  },
  {
    path: '/turnos',
    name: 'Turnos',
    component: Turnos
  },
  {
    path: '/estadisticas',
    name: 'Estadisticas',
    component: Estadisticas
  },
  {
    path: '/alta_centro',
    name: 'nuevo_centro',
    component: AltaCentro
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
