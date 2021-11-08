import { createApp } from 'vue'
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue-3';
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from 'axios'

const app = createApp(App)
app.use(store)
app.use(router)
app.use(BootstrapVue)
app.mount('#app')

const token = localStorage.getItem('token')

if (token) {
    Axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
}
