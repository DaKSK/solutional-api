"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    # AUTH
    path('api-auth/', include('rest_framework.urls')),
    # API ENDPOINTS
    # path('/api/products', - GET Retrieve Products
    # path('/api/orders', - POST Create New Order
    # path('/api/orders/:order_id', - GET Retrieve Order
    # path('/api/orders/:order_id/products', - GET Retrieve Order Items and PATCH Add Order Item to Order
    # path('/api/orders/:order_id/products/:product_id', - 2x PATCH Update quantity and Add replacement
]
