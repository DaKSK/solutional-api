from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin
from .models import Product, Order, OrderItem

from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer


# A View to get the list of all products
class ProductViewSet(ListModelMixin, GenericViewSet):

	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	# permission_classes = None

# LOWER LEVEL IMPLEMENT
#
# class ProductsList(APIView):
#
# 	def get(self, request):
# 		products = Product.objects.all()
# 		serializer = ProductSerializer(products, many=True)
# 		return Response(serializer.data)

# All logic required for Order handling


class OrderViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	@action(detail=True, methods=['get', 'post'])
	def products(self, request, pk=None):
		if request.method == 'GET':
			order_items = OrderItem.objects.filter(order__id=pk)
			return Response(OrderItemSerializer(order_items, many=True).data)
		if request.method == 'POST':
			order = Order.objects.get(id=pk)
			if order.status == 'PAID':
				return Response("Invalid parameters")
			products = request.data
			for product_id in products:
				product = Product.objects.get(id=product_id)
				existing_order_item = OrderItem.objects.filter(product=product, order=order)
				if existing_order_item.exists():
					order_item = existing_order_item[0]
					order_item.quantity = order_item.quantity + 1
					order_item.save()
				else:
					order_item = OrderItem(product=product, order=order, quantity=1)
					order_item.save()
				return Response("OK")

	@action(detail=True, methods=['get', 'patch'], url_path='products/(?P<order_item_pk>[^/.]+)')
	def update_products(self, request, pk=None, order_item_pk=None):
		order_item = OrderItem.objects.get(id=order_item_pk)
		quantity = request.data.get('quantity')
		if quantity:
			order_item.quantity = quantity
		order_item.save()
		replaced_with = request.data.get('replaced_with')
		if replaced_with:
			# POSSIBLE SOLUTION TO ISSUE OF REPLACEMENT PRODUCT ERROR:
			# product = Product.objects.get(replaced_with)['product_id']
			# order_item.replacement_product = product
			# order_item.quantity = replaced_with['quantity']
			# order_item.save()
			return Response("Invalid parameters")
		return Response("OK")


class OrderItemViewSet:
	pass

# Lower level implementation
class OrderCreate(APIView):

	def post(self, request):
		if request.method == 'POST':
			new_order = Order(status='NEW')
			new_order.save()
			serializer = OrderSerializer(new_order)
			return Response(serializer.data)


class OrderView(APIView):
	pass


class OrderAdd(APIView):
	# Add product to order item
	# Takes in the product id field as parameter in JSON format e.g. [123]
	@staticmethod
	def post(self, request):
		pass
		# if request.method == 'POST':
		# 	order_id = request.query_params
		# 	product_id = request.data
		# 	products = Product.objects.all()
		# 	for p in products.id:
		# 		if product_id not in p:
		# 			# Returns "invalid parameters" when product not found
		# 			return "invalid parameters"
		# 	product_to_add = Product(id=product_id)
		# 	# Returns "OK" when product added to OrderItem
		# 	return "OK"
	# Returns error - bad request when sending wrong type
