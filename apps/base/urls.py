from django.urls import path

from . import views
from .api import (user_view)

from rest_framework import routers

app_name = 'base'

router = routers.DefaultRouter()

router.register(r'api/v1/user', user_view.UserViewSet, basename='user')

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += router.urls
