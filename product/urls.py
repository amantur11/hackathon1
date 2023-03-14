from django.urls import path, include
# from .views import (ProductListAPIView, CollectionListAPIView, CollectionDetailAPIView, ProductDetailAPIView, 
# SearchAPIView, MainPageNewAPIVIew, MainPageHitAPIVIew, MainSliderAPIView, MainBenefistAPIView, CallbackAPIView,
# CollectionNewAPIView)
from .views import *
from rest_framework.views import APIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('modelviewset_crud', ProductModelViewSet)
router.register('products_mixin', ProductMixin)


urlpatterns = [
    # path('api/v1/main/collection/', CollectionListAPIView.as_view()),
    path('api/v1/products/', ProductListAPIView.as_view()),
    path('api/v1/products/<int:id>/', ProductDetailAPIView.as_view()),
    # path('api/v1/collection/', CollectionListAPIView.as_view()),
    path('api/v1/main/search/', SearchAPIView.as_view()),
    path('api/v1/main/slider/', MainSliderAPIView.as_view()),
    path('api/v1/main/hit/', MainPageHitAPIVIew.as_view()),
    path('api/v1/main/new/', MainPageNewAPIVIew.as_view()),
    path('api/v1/main/benefist/', MainBenefistAPIView.as_view()),
    path('api/v1/main/create/', CallbackAPIView.as_view()),
    path('api/v1/collection/<int:id>/', CollectionDetailAPIView.as_view()),
    path('api/v1/collection/new/', CollectionNewAPIView.as_view()),
    path('', include(router.urls))
]

