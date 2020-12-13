import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    id: '',
    fecha: '',
    hora: '',
    nombre:'',
    apellido:'',
    email:'',
    telefono:'',
  },
  getters: {
    nombre: state => state.nombre
  }
})



//export default new Vuex.Store({
//  state: {
//  },
//  mutations: {
//  },
//  actions: {
//  },
//  modules: {
//  }
//})
