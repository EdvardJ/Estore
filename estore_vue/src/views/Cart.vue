<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cart</h1>  
            </div>

            <div class="column is-12 box" >
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                            v-bind:initialItem="item" 
                            v-on:removeFromCart="removeFromCart"/>
                    </tbody>
                </table>
                
                <p v-else>Cart is empty...</p>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Summary:</h2>
                <!-- display computed values -->
                <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items

                <hr>

                <router-link to="/cart/checkout" class="button is-dark">Proceed to checkout</router-link>
                <hr>
                <h2 class="subtitle">or</h2>
                <button class="button is-danger" @click="clearCart">Clear cart</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'

export default {
    name: "Cart",
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        //remove item from cart by filtering with id
        removeFromCart(item) {
            this.cart.items=this.cart.items.filter(i => i.product.id !== item.product.id)
        },
        //empty cart and reload page
        clearCart(state) {
        state.cart = { items: [] }

        localStorage.setItem('cart', JSON.stringify(state.cart))
        location.reload();
      }
    },
    computed: {
        // product quantity
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        // product price times quantity
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
}
</script>