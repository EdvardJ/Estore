import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: '',
    isLoading: false
  },
  mutations: {
    initializeStore(state) {
      if(localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
      //check for token in localstorage and set authenticated if so
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)

      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      } 

      localStorage.setItem('cart', JSON.stringify(state.cart))
      },
      setIsLoading(state, status) {
        state.isLoading = status
      },
      //functions to determine value and authentication for token
      setToken(state, token) {
        state.token = token
        state.isAuthenticated = true
      },
      removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
      }
  },
  actions: {
  },
  modules: {
  }
})
