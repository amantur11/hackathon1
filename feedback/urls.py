from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feedback.views import FavoriteModelViewset
from django.views.decorators.cache import cache_page 


router = DefaultRouter()
router.register('', FavoriteModelViewset)
# router.register('comment', CommentModelViewSet)

urlpatterns = [
    path('favorite/', cache_page(60)(include(router.urls)))
]
