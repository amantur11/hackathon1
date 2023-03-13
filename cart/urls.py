from django.urls import path
from .views import (CartAddAPIView, CartListAPIView, CartDeleteAPIView, FavoritesAddAPIView, FavoritesListAPIView, FavoritesDeleteAPIView,
CartClearAPIVew, CartOrderAPIView, CartUpdateAPIView)


urlpatterns = [
    path('api/v1/cart/', CartListAPIView.as_view()),
    path('api/v1/cart/order/', CartOrderAPIView.as_view()),
    path('api/v1/cart/add/', CartAddAPIView.as_view()),
    path('api/v1/cart/update/', CartUpdateAPIView.as_view()),
    path('api/v1/cart/remove/', CartDeleteAPIView.as_view()),
    path('api/v1/cart/clear/', CartClearAPIVew.as_view()),
    path('api/v1/favorites/', FavoritesListAPIView.as_view()),
    path('api/v1/favorites/add/<int:id>/', FavoritesAddAPIView.as_view()),
    path('api/v1/favorites/delete/<int:id>/', FavoritesDeleteAPIView.as_view()), 
]
