<template>
  <div class="home">
      <section class="hero is-medium mb-6 is-dark">
        <div class="has-text-centered" id="banner">
        <h1 class="is-size-1">
          Welcome to eStore
        </h1>
        <h2 class="is-size-4">
          The best online store ever!
        </h2>
      </div>
    </section>
  </div>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h3 class="is-size-2 has-text-centered">Latest products</h3>
      </div>

      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />
      </div>
    
</template>

<script>
import axios from 'axios'

import ProductBox from '@/components/ProductBox'


export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox,
},
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Estore'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

    
      await axios
      .get('/api/v1/latest-products/')
      .then(response => {
        this.latestProducts = response.data
      } )
      .catch(error => {
        console.log(error)
      })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
#banner {
  height: 10rem;
  background-image: url('~@/assets/Background.jpg');
  background-repeat: no-repeat;
}
h1 {
  font: italic bold 1.2em Georgia, serif;
  color: #48C78E;
  text-shadow: 2px 2px 2px  black;
  padding-top: 0.5em;
}
h2 {
  color: #48C78E;
  text-shadow: 2px 2px black;
}
h3 {
  color: #48C78E;
  text-shadow: 2px 2px black;
}
@media (max-width: 512px) {
  h2 {
    display: none;
  }
}
</style>