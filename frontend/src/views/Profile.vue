<template>
<div class="bg-white">

  <div class="container">
    <div class="d-flex justify-content-between align-items-center py-4">
      <!-- <div>
        <a href="#" class="btn btn-success btn-sm">
          Follow
        </a>
        <a href="#" class="btn btn-default icon-btn md-btn-flat btn-sm ml-1">
          <i class="ion ion-md-mail"></i>
        </a>
      </div> -->
    </div>
  </div>
  <hr class="m-0">

  <div class="container">
    <div class="text-center py-5">
      <img src="https://bootdey.com/img/Content/avatar/avatar6.png" alt class="ui-w-100 rounded-circle">

      <div class="col-md-8 col-lg-6 col-xl-5 p-0 mx-auto">
        <h4 class="font-weight-bold my-4">{{ profile.name }}</h4>
        <h4 class="font-weight-bold my-4">Email:{{ profile.email }}</h4>
        <h4 class="font-weight-bold my-4">Баланс: {{ profile.balance }}руб.</h4>
        <h4 class="font-weight-bold my-4">Зарегистрирован: {{ profile.created_on }}</h4>
        <div class="text-muted mb-4">
          Здесь будут ссылка на подключение Oauth.
        </div>
      </div>
    </div>
  </div>
  <hr class="m-0">
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Profile',
  data() {
    return {
      profile: [],
    };
  },
  methods: {
    getProfile() {
      const path = 'http://127.0.0.1:5000/api/profile/me/';
      axios.get(path)
        .then((res) => {
          this.profile = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getProfile();
  }
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
