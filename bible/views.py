from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import TodaysVerse
from .renderers import BibleRenderer
from .serializers import TodaysVerseSerializer
# Create your views here.


class TodaysVerseAPIView(GenericAPIView):
    
    renderer_classes = (BibleRenderer,)
    queryset = TodaysVerse.objects.today()
    permission_classes = [IsAuthenticated,]
    serializer_class = TodaysVerseSerializer

    def get(self, request):
        """
        Todays Verse
        
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
