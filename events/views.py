from django.conf import settings
from django.db.models import QuerySet, Q

from rest_framework import viewsets, status
from rest_framework.decorators import action
# from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, GenericAPIView
# from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .models import Event
from .renderers import EventRenderer
from .serializers import EventSerializer, ReactSerializer
from .pagination import StandardResultsSetPagination


class EventViewSet(GenericViewSet):
    
    renderer_classes = (EventRenderer,)
    pagination_class = StandardResultsSetPagination
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):

        if self.action == 'upcoming':
            return super().get_queryset().upcoming_events()
        elif self.action == 'current':
            return super().get_queryset().current_events()
        else:
            return super().get_queryset().previous_events()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_serializer_class(self):
        actions = ['react',]
        if self.action == actions[0]:
            return ReactSerializer
        else:
            return EventSerializer

    @action(methods=['get'], detail=False)
    def upcoming(self, request):
        """
        Upcoming Events.
        
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=False)
    def current(self, request):
        """
       Current Events.
        
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=False)
    def previous(self, request):
        """
        Previous Events.
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)
    def react(self, request, pk):
        event = Event.objects.filter(id=pk).prefetch_related('reactions')
        if event.exists():
            event = event.first()
            if request.user not in event.reactions.all():
                event.reactions.add(request.user)
            return Response({'success': True, 'reaction_count': event.reactions.count()}, status=status.HTTP_200_OK)
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)