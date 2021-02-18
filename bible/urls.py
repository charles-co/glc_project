from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path

from .views import TodaysVerseAPIView

app_name = 'bible'


urlpatterns = [
    path('api/today/verse/', TodaysVerseAPIView.as_view(), name='todays-verse'),
]