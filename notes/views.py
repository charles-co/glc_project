from django.conf import settings
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Note
from .permissions import IsOwner
from .renderers import NoteRenderer
from .serializers import NoteSerializer
from .pagination import StandardResultsSetPagination

class NoteLCAPIView(ListCreateAPIView):
    
    renderer_classes = (NoteRenderer,)
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user).select_related('user')

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class NoteRUDAPIView(RetrieveUpdateDestroyAPIView):
    
    renderer_classes = (NoteRenderer,)
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user).select_related('user')

