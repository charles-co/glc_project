from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers

from .views import NoteLCAPIView, NoteRUDAPIView

app_name = 'notes'


urlpatterns = [
    path('api/notes/', NoteLCAPIView.as_view(), name='notes-lc'),
    path('api/notes/<int:pk>', NoteRUDAPIView.as_view(), name='notes-rud'),
]