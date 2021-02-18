from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import DateTimeRangeField
from django.db import models 
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from datetime import datetime, timedelta

from sorl.thumbnail import ImageField
from glc_project.utils import files_directory_path
# Create your models here.

User = get_user_model()

class EventQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    
    def previous_events(self):
        return self.filter(end__lt=timezone.now())[:10]

    def current_events(self):
        return self.filter(start__lte=timezone.now(), end__gt=timezone.now())

    def upcoming_events(self):
        days = timedelta(days=7)
        now = timezone.now()
        future = now + days
        return self.filter(start__gt=now, end__lte=future)

class EventManager(models.Manager):

    def get_queryset(self):
        return EventQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def upcoming(self):
        return self.get_queryset().active().upcoming_events()

    def current(self):
        return self.get_queryset().active().current_events()
    
    def previous(self):
        return self.get_queryset().active().previous_events()

class Event(models.Model):

    title = models.CharField(_("Title"), max_length=100)
    photo = ImageField(_("Photo"), upload_to=files_directory_path)
    description = models.TextField(_("Short Description"), blank=True)
    location = models.CharField(_("Location"), max_length=50)
    start = models.DateTimeField(_("Start"), auto_now=False, auto_now_add=False)
    end = models.DateTimeField(_("End"), auto_now=False, auto_now_add=False)
    active = models.BooleanField(_("Active"), default=True)
    reactions = models.ManyToManyField(User, verbose_name=_("reactions"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EventManager()

    class Meta:
        ordering = ['start', 'end', 'title']

    def __str__(self):
        return self.title

    def number_of_reactions(self):
        return self.reactions.count()