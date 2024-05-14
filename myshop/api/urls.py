
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
router.register(r'token', GetTokenViewSet, basename='token')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'like', Likes, basename='like')
router.register(r'feedbacks', FeedbackViewSet, basename='feedbacks')
router.register(r'questions', ProductQuestionViewSet, basename='questions')
router.register(r'catalogs', CatalogViewSet, basename='catalogs')
router.register(r'update_leftovers', UpdateLeftovers, basename='update_leftovers')
router.register(r'sliders', MainSliderViewSet, basename='get_sliders')


urlpatterns = [
    path('v1/', include(router.urls)),
]
