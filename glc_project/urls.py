"""glc_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

from rest_framework import permissions 
from rest_social_auth import views 

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.site.enable_nav_sidebar = False
admin.site.site_header = 'GLC'
admin.site.index_title = 'GLC Administration'
schema_view = get_schema_view(
        openapi.Info(
            title="GLC API",
            default_version='v1',
            description="API Test",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@glc.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    path('', include('authentication.urls')),
    path('', include('events.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    re_path(r'^api/auth/login/social/(?:(?P<provider>[a-zA-Z0-9_-]+)/?)?$',
            views.SocialJWTPairOnlyAuthView.as_view(),
            name='login_social_jwt_pair'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

handler400='rest_framework.exceptions.bad_request'
handler404='utils.views.error_404'
handler500='utils.views.error_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
