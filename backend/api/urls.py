from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
urlpatterns = router.urls