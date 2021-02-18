from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers

from .views import ContentViewSet

app_name = 'contents'

router = routers.DefaultRouter()
router.register(r'content', ContentViewSet, basename='content')

urlpatterns = [
    path('api/', include((router.urls, 'content'))),
]