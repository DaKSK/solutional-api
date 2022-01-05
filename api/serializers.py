from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'price')


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('id', 'status')


class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = ('id', 'order', 'product', 'quantity')

