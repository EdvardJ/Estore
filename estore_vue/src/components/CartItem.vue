<template>
    <tr>
        <td><router-link :to="item.product.get_absolute_url"> {{ item.product.name }}</router-link></td>
        <td>${{ item.product.price }}</td>
        <td>
            <a @click="decrementQuantity(item)">-</a>
            {{ item.quantity }}
            <a @click="incrementQuantity(item)">+</a>
        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>

</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        //item total price
        getItemTotal(item){
            return item.quantity * item.product.price
        },
        //decrease/increase item quantity from cart
        decrementQuantity(item) {
            item.quantity -= 1
        //check if item quantity 0 then remove
            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }


            this.updateCart()
        },
        incrementQuantity(item){
            item.quantity += 1

            this.updateCart()
        },
        //update cart in localstorage
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        //call a function from parent
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        }
    },
}
</script>