<template>
<div class="container">
    <div class="omb_login">
      <h3 class="omb_authTitle">Вход</h3>
    <div class="row omb_socialButtons">	
          <div class="col-xs-4">
            <a href="#" class="btn btn-lg btn-block omb_btn-google">
              <i class="fa fa-google-plus visible-xs"></i>
              <span class="hidden-xs">Google+</span>
            </a>
          </div>	
    </div>

    <div class="row omb_row-sm-offset-3 omb_loginOr">
      <div class="col-xs-12 col-sm-6">
        <hr class="omb_hrOr">
        <span class="omb_spanOr">или</span>
      </div>
    </div>

    <div class="row omb_row-sm-offset-3">
      <div class="col-xs-12 col-sm-6" @submit.prevent="login" >	
          <form class="omb_loginForm" action="" autocomplete="off" method="POST">
          <div class="input-group">
            <span class="input-group-addon"><i class="fa fa-user"></i></span>
            <input required v-model="username" type="text" class="form-control" name="username" placeholder="Username">
          </div>
          <span class="help-block"></span>
          <div class="input-group">
            <span class="input-group-addon"><i class="fa fa-lock"></i></span>
            <input required v-model="password" type="password" class="form-control" name="password" placeholder="Password">
          </div>
          <br>
          <button class="btn btn-lg btn-primary btn-block" type="submit">Войти</button>
        </form>
      </div>
    </div>
  </div>
</div>
</template>

<script>
  export default {
    data(){
      return {
        username : "",
        password : ""
      }
    },
    methods: {
      login: function () {
        let username = this.username 
        let password = this.password
        this.$store.dispatch('login', { username, password })
       .then(() => this.$router.push('/profile'))
       .catch(err => console.log(err))
      }
    }
  }
</script>

<style>
@media (min-width: 768px) {
    .omb_row-sm-offset-3 div:first-child[class*="col-"] {
        margin-left: 25%;
    }
}

.omb_login .omb_authTitle {
    text-align: center;
  line-height: 300%;
}
  
.omb_login .omb_socialButtons a {
  color: white;
  opacity:0.9;
}

.omb_login .omb_socialButtons a:hover {
    color: white;
  opacity:1;    	
}
.omb_login .omb_socialButtons .omb_btn-facebook {background: #3b5998;}
.omb_login .omb_socialButtons .omb_btn-twitter {background: #00aced;}
.omb_login .omb_socialButtons .omb_btn-google {background: #c32f10;}


.omb_login .omb_loginOr {
  position: relative;
  font-size: 1.5em;
  color: #aaa;
  margin-top: 1em;
  margin-bottom: 1em;
  padding-top: 0.5em;
  padding-bottom: 0.5em;
}
.omb_login .omb_loginOr .omb_hrOr {
  background-color: #cdcdcd;
  height: 1px;
  margin-top: 0px !important;
  margin-bottom: 0px !important;
}
.omb_login .omb_loginOr .omb_spanOr {
  display: block;
  position: absolute;
  left: 50%;
  top: -0.6em;
  margin-left: -1.5em;
  background-color: white;
  width: 3em;
  text-align: center;
}			

.omb_login .omb_loginForm .input-group.i {
  width: 2em;
}
.omb_login .omb_loginForm  .help-block {
    color: red;
}


@media (min-width: 768px) {
    .omb_login .omb_forgotPwd {
        text-align: right;
    margin-top:10px;
   }		
}
</style>