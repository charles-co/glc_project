from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers
# from rest_framework_simplejwt.views import (TokenRefreshView)

from .views import EventViewSet

app_name = 'events'

router = routers.DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('api/', include((router.urls, 'event'))),
]