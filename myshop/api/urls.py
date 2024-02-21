
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import *


router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'initial_upload_products', InitialUploadProducts, basename='initial_upload_products')
router.register(r'initial_upload_catalog', InitialUploadCatalog, basename='initial_upload_catalog')
router.register(r'carts', CartsViewSet, basename='carts')
router.register(r'customers', CustomersViewSet, basename='customers')
router.register(r'token', TokenView, basename='token')
router.register(r'order', OrderViewSet, basename='order')


urlpatterns = [
    path('v1/', include(router.urls)),
]
