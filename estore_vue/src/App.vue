<template>
  <div id="wrapper">
    <nav class="navbar">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>eStore</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="Looking for something?" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
          <router-link to="/about" class="navbar-item">About us</router-link>
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="dropdown is-hoverable">
              <div class="dropdown-trigger">
                <div class="navbar-item" aria-haspopup="true" aria-controls="dropdown-menu">
                  <span id="cat-tag">Categories:</span>
                  <span class="icon is-small">
                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                  </span>
                </div>
            </div>
              <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content">
                  <router-link to="/hats" class="navbar-item">Hats</router-link>
                  <router-link to="/jackets" class="navbar-item">Jackets</router-link>
                  <router-link to="/pants" class="navbar-item">Pants</router-link>
                  <router-link to="/shirts" class="navbar-item">Shirts</router-link>
                </div>
              </div>
          </div>
            <div class="buttons">
              <!-- check if authenticated and show either login or myaccount buttons-->
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>

              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
<!--loading bar-->
    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
  <router-view/>
</section>

    <footer class="footer">
      <p class="has-text-centered is-dark">Copyright (c) 2023</p>
      <router-link id="privacy" to="/privacy">Privacy Policy</router-link>
    </footer>

  </div>
</template>


<script>
import axios from 'axios'

  export default {
    data() {
      return{
        showMobileMenu: false,
        cart: {
          items: []
        }
      }
      
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.cart
      //set header for token in browser
      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
    mounted() {
      this.cart = this.$store.state.cart
    },
    computed: {
      cartTotalLength() {
        let totalLength = 0

        for (let i = 0; i < this.cart.items.length; i++) {
          totalLength += this.cart.items[i].quantity
        }

        return totalLength
      }
    }
  }
</script>

<style lang="scss">
@import '../node_modules/bulma';

#cat-tag {
  color: black;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
.navbar {
  background-color: #FFE0B5;
}
.navbar-item { 
  color: #48C78E;
  text-shadow: 0.5px 0.5px black;
}
.footer {
  text-align: center;
  color: #b5e2fa;
  background-color: #586f6b;
}
#privacy {
  text-decoration: none;
}
</style>