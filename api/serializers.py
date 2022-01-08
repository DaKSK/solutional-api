from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'price')


class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = ('id', 'order', 'product', 'quantity')

# Tried an different approach to formulating the list of Order Items for Order
# class SlugSerializerField(serializers.SlugRelatedField):
# 	def get_queryset(self):
# 		if hasattr(self.root, 'order_id'):
# 			queryset = self.queryset
# 			return queryset.filter(order=self.root.order_id)


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
		return {
			"discount": "0.00",
			"paid": "0.00",
			"returns": "0.00",
			"total": total
		}

	amount = serializers.SerializerMethodField('get_amount')

	class Meta:
		model = Order
		fields = ('amount', 'id', 'status', 'products')

	products = serializers.SerializerMethodField("get_order_items")


