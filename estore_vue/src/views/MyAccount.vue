<template>
    <div class="columns is-multiline">
        <div class="column is-12">
            <h1 class="title">My account</h1>
        </div>

        <div class="column is-12">
        <button @click="logout()" class="button is-danger">Log out</button>
        </div>

        <hr>

        <div class="column is-12">
            <h2 class="subtitle">My Orders:</h2>

            <OrderSummary
                v-for='order in orders'
                v-bind:key="order.id"
                v-bind:order="order" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';

import OrderSummary from '@/components/OrderSummary.vue'

export default {
    name: 'MyAccount',
    components:{
        OrderSummary
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'My account | eStore'

        this.getMyOrders()
    },
    methods: {
        logout(){
        axios.defaults.headers.common["Authorization"] = ""

        localStorage.removeItem("token")
        localStorage.removeItem("username")
        localStorage.removeItem("userid")
        
        this.$store.commit('removeToken')

        this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
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
    font: italic small-caps bold Georgia, serif;
    color: #48C78E;
    text-shadow: 2px 2px black;
}

</style>