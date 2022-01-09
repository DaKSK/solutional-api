from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'price')


class OrderItemSerializer(serializers.ModelSerializer):

	name = serializers.ReadOnlyField(source='product.name')
	price = serializers.ReadOnlyField(source='product.price')

	class Meta:
		model = OrderItem
		fields = ('id', 'name', 'price', 'product_id', 'quantity', 'replacement_product')


class OrderSerializer(serializers.ModelSerializer):

	def get_order_items(self, args):
		queryset = OrderItem.objects.filter(order__id=args.id)
		products = OrderItemSerializer(queryset, many=True, read_only=True)
		return products.data

	def get_amount(self, args):
		queryset = OrderItem.objects.filter(order__id=args.id)
		total = 0
		for order_item in queryset:
			total += order_item.product.price * order_item.quantity
		current_order = Order.objects.get(id=args.id)
		paid = total if current_order.status == 'PAID' else 0.00
		return {
			"discount": "0.00",
			"paid": paid,
			"returns": "0.00",
			"total": total
		}

	amount = serializers.SerializerMethodField('get_amount')

	class Meta:
		model = Order
		fields = ('amount', 'id', 'products', 'status')

	products = serializers.SerializerMethodField("get_order_items")
