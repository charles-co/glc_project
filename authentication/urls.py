from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers
from rest_framework_simplejwt.views import (TokenRefreshView)

from .views import UserViewSet, PasswordResetConfirm

app_name = 'authentication'

router = routers.DefaultRouter()
router.register(r'auth', UserViewSet, basename='user')


urlpatterns = [
    path('api/', include((router.urls, 'authentication'))),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    # path('api/auth/password/reset/<uidb64>/<token>/', 
    #         PasswordResetConfirm.as_view(), name='password-reset-confirm'),

]