from rest_framework import serializers

from .models import Order, OrderItem

from product.serializers import ProductSerializer


class OrderItemSerializer (serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )
    #override create functionality for OrderSerializer
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        #create a new order based on validated data
        order = Order.objects.create(**validated_data)
        #loop through items in list and create new order item and set foreign key order to item data
        #product is already included
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order