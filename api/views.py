from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin

from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer


# A ViewSet to get the list of all products
class ProductViewSet(ListModelMixin, GenericViewSet):

	queryset = Product.objects.all()
	serializer_class = ProductSerializer

# The OrderViewSet is a class based view that enables the actions for our objects
# The ViewSet also enables using the router for our urls
# All logic required for Order handling


class OrderViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	# Method for returning and adding products

	@action(detail=True, methods=['get', 'post'])
	def products(self, request, pk=None):
		if request.method == 'GET':
			order_items = OrderItem.objects.filter(order__id=pk)
			return Response(OrderItemSerializer(order_items, many=True).data)
		if request.method == 'POST':
			order = Order.objects.get(id=pk)
			# Disable updating products when status is PAID
			if order.status == 'PAID':
				return Response("Invalid parameters")

			# Generating list of product ids
			products = request.data
			for product_id in products:
				product = Product.objects.get(id=product_id)
				existing_order_item = OrderItem.objects.filter(product=product, order=order)

				# Handling existing product incrementation and setting default quantity to 1
				if existing_order_item.exists():
					order_item = existing_order_item[0]
					order_item.quantity = order_item.quantity + 1
					order_item.save()
				else:
					order_item = OrderItem(product=product, order=order, quantity=1)
					order_item.save()
				return Response("OK")

	# Method for updating specific OrderItems in Order
	# The example API uses the url 'products', for clarity they are renamed to OrderItem elsewhere

	@action(detail=True, methods=['get', 'patch'], url_path='products/(?P<order_item_pk>[^/.]+)')
	def update_products(self, request, pk=None, order_item_pk=None):
		order_item = OrderItem.objects.get(id=order_item_pk)
		quantity = request.data.get('quantity')
		if quantity:
			order_item.quantity = quantity
		order_item.save()
		replaced_with = request.data.get('replaced_with')
		if replaced_with:
			# POSSIBLE SOLUTION TO ISSUE OF REPLACEMENT PRODUCT ADDITION ERROR RESPONSE:
			# product = Product.objects.get(replaced_with)['product_id']
			# order_item.replacement_product = product
			# order_item.quantity = replaced_with['quantity']
			# order_item.save()
			return Response("Invalid parameters")
		return Response("OK")

# First attempt with APIView as a lower level implementation
# Decided in favor of ViewSets

# class ProductsList(APIView):
#
# 	def get(self, request):
# 		products = Product.objects.all()
# 		serializer = ProductSerializer(products, many=True)
# 		return Response(serializer.data)
