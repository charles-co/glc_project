from rest_framework import serializers
from .models import Audio, Video, Podcast, TV



class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = ['title', 'audio_file', 'created_at']
        read_only_fields = ['created_at', 'audio_file', 'title']
    

class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ['title', 'file', 'created_at']
        read_only_fields = ['created_at', 'file', 'title']


class PodcastSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Podcast
        fields = ['title', 'file', 'created_at']
        read_only_fields = ['created_at', 'file', 'title']
        
class TVSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TV
        fields = "__all__"