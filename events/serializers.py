from django.urls import reverse
from django.template.defaultfilters import date

from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

import json
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    user_can_react = serializers.SerializerMethodField()
    reaction_count = serializers.CharField(source="number_of_reactions")
    
    class Meta:
        model = Event
        exclude = ['end', 'active', 'reactions', 'start', 'created_at', 'updated_at']

    def get_start_time(self, obj):
        return date(obj.start.astimezone(), arg='P T')

    def get_end_time(self, obj):
        return date(obj.end.astimezone(), arg='P T')

    def get_date(self, obj):
        return date(obj.start.date(), arg='D, jS N Y')

    def get_user_can_react(self, obj):
        return self.context['request'].user not in obj.reactions.all() 


class ReactSerializer(serializers.Serializer):
    pass