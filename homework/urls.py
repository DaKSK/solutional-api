from django.contrib import admin
from django.urls import path, include
from api.views import ProductViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/products', ProductViewSet)
router.register(r'api/orders', OrderViewSet)

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    # AUTH
    path('api-auth/', include('rest_framework.urls')),
]
# API ENDPOINTS
urlpatterns += router.urls
