from django.urls import path, include

from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet, CartViewSet


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'', CartViewSet)

urlpatterns = [
    path('', include((router.urls, 'cart')))
]
