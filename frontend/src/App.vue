<template>
  <div id="nav" v-if="isLoggedIn">
    <router-link to="/profile">Профиль</router-link> |
    <router-link to="/lines">Линии</router-link> |
    <router-link to="/calls">Звонки</router-link> |
    <router-link to="/payment_accounts">Счета</router-link> |
    <router-link v-if="isLoggedIn" to="/" @click="logout">Выйти</router-link>
  </div>
  <router-view/>
</template>

<script>
  import axios from 'axios'
  export default {
    computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn }
    },
    methods: {
      logout: function () {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/')
        })
      }
    },
    created () {
      axios.interceptors.response.use(undefined, function (err) {
        return new Promise(function (resolve, reject) {
      if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
        this.$store.dispatch("logout")
        resolve()}
      reject(err)
      throw err;
      })
    })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #b96e42;
}
</style>
