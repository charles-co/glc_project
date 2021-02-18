from django.urls import reverse
from django.template.defaultfilters import date

from rest_framework import serializers
from .models import TodaysVerse


class TodaysVerseSerializer(serializers.ModelSerializer):
    
    bible_verse = serializers.CharField(source="get_verse")
    bible_name = serializers.CharField(source="get_bible")

    class Meta:
        model = TodaysVerse
        fields = ['bible_verse', 'bible_name', 'message']
        # read_only_fields = ['bible_verse', 'book_name']