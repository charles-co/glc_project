from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .models import Audio, Video, Podcast
from .renderers import ContentRenderer
from .pagination import StandardResultsSetPagination
from .serializers import AudioSerializer, VideoSerializer, PodcastSerializer
# Create your views here.


class ContentViewSet(GenericViewSet):
    
    pagination_class = StandardResultsSetPagination
    renderer_classes = (ContentRenderer,)
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
    
        if self.action == 'audios':
            return Audio.objects.all()
        elif self.action == 'videos':
            return Video.objects.all()
        else:
            return Podcast.objects.all()

    def get_serializer_class(self):
        actions = ['audios', 'videos', 'podcasts']
        if self.action == actions[0]:
            return AudioSerializer
        elif self.action == actions[1]:
            return VideoSerializer
        else:
            return PodcastSerializer

    @action(methods=['get'], detail=False)
    def audios(self, request):
        """
        Audios
        
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def videos(self, request):
        """
        Videos
        
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def podcasts(self, request):
        """
        Podcasts
        
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)