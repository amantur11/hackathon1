from django.urls import path, include
# from .views import (ProductListAPIView, CollectionListAPIView, CollectionDetailAPIView, ProductDetailAPIView, 
# SearchAPIView, MainPageNewAPIVIew, MainPageHitAPIVIew, MainSliderAPIView, MainBenefistAPIView, CallbackAPIView,
# CollectionNewAPIView)
from .views import *
from rest_framework.views import APIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductModelViewSet)
# router.register('comment', CommentModelViewSet)

urlpatterns = [
    # path('api/v1/main/collection/', CollectionListAPIView.as_view()),
    # path('api/v1/products/', ProductListAPIView.as_view()),
    # path('api/v1/products/<int:id>/', ProductDetailAPIView.as_view()),
    # path('api/v1/collection/', CollectionListAPIView.as_view()),
    path('api/v1/main/search/', SearchAPIView.as_view()),
    path('api/v1/main/slider/', MainSliderAPIView.as_view()),
    path('api/v1/main/hit/', MainPageHitAPIVIew.as_view()),
    path('api/v1/main/new1/', MainPageNewAPIVIew.as_view()),
    path('api/v1/main/benefist/', MainBenefistAPIView.as_view()),
    path('api/v1/main/create/', CallbackAPIView.as_view()),
    path('api/v1/collection/<int:id>/', CollectionDetailAPIView.as_view()),
    path('api/v1/collection/new/', CollectionNewAPIView.as_view()),
    path('favorite/', include(router.urls)),
    path('auth/', auth),
    path('', include(router.urls))
]

