from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Order, OrderItem

from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer


# A View to get the list of all products
class ProductsList(APIView):

	def get(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)


class OrderCreate(APIView):

	def post(self, request):
		if request.method == 'POST':
			new_order = Order(status='NEW')
			new_order.save()
			serializer = OrderSerializer(new_order)
			return Response(serializer.data)

