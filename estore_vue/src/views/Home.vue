<template>
  <div class="home">
      <section class="hero is-medium mb-6 is-dark">
        <div class="hero-body has-text-centered" :style="cssProps">
        <h1 class="is-size-1">
          Welcome to eStore
        </h1>
        <h2 class="is-size-2">
          The best online store ever!
        </h2>
      </div>
    </section>
  </div>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
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
      latestProducts: [],
      cssProps: {
          backgroundImage: `url(${require('@/assets/Background.jpg')})`,
          backgroundRepeat: `no-repeat`
        }
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
h1 {
  font: italic bold 12px/30px Georgia, serif;
  color: #48C78E;
  text-shadow: 2px 2px 2px  black;
}
h2 {
  color: #48C78E;
  text-shadow: 2px 2px black;
}
</style>