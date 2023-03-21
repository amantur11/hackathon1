"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .yasg import ulrpatterns as doc_urls
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from product.views import ProductModelViewSet, auth
from users.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/spam/', include('spam.urls')),
    path('login_view/', login_view),
    path('auth/', auth),
    path('', include('about_us.urls')),
    path('', include('cart.urls')),
    path('', include('social_django.urls', namespace='social')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_urls
