from django.urls import path
from .views import AboutUsAPIView, NewsListAPIView, HelpAPIViews, OfferAPIView, FooterAPIView


urlpatterns = [
    path('api/v1/info/about/', AboutUsAPIView.as_view()),
    path('api/v1/info/news/', NewsListAPIView.as_view()),
    path('api/v1/info/help/', HelpAPIViews.as_view()),
    path('api/v1/info/offer/', OfferAPIView.as_view()),
    path('api/v1/info/footer/', FooterAPIView.as_view()),
]


