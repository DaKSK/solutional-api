from django.contrib import admin
from django.urls import path, include
from api.views import OrderCreate, OrderView, ProductViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/products', ProductViewSet)
router.register(r'api/orders', OrderViewSet)

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    # AUTH
    path('api-auth/', include('rest_framework.urls')),
    # API ENDPOINTS
    # path('api/products/', ProductsList.as_view()),  # - GET Retrieve Products
    # path('api/orders/', OrderCreate.as_view()),     # - POST Create New Order
    # path('api/orders/:order_id', OrderView.as_view()),  # - GET Retrieve Order
    # path('api/orders/:order_id/products', - GET Retrieve Order Items and PATCH Add Order Item to Order
    # path('api/orders/:order_id/products/:product_id', - 2x PATCH Update quantity and Add replacement
]
urlpatterns += router.urls
