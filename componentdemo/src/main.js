import Vue from 'vue'
import App from './App.vue'
import Hello from './Hello.vue'


new Vue({
  el: '#app',
  components:{
    App
  }
})

new Vue({
  el:'#hello',
  components:{
    Hello
  }
})