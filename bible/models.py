from django.conf import settings
from django.db import models 
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey

from datetime import datetime, timedelta
# Create your models here.

class Book(models.Model):
    """
    Example: Gen, Exo
    """
    _id = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=30)
    nameLong = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=15)

    class Meta: 
        ordering = ['id']

    def __str__(self):
        return self.name

class Chapter(models.Model):
    _id = models.CharField(max_length=10, unique=True)
    number = models.PositiveIntegerField(_("Number"))
    position = models.PositiveIntegerField(_("Position"), unique=True)
    book = models.ForeignKey(Book, verbose_name=_("Book"), on_delete=models.CASCADE, related_name="chapters")
    
    class Meta: 
        ordering = ['id']
    
    def __str__(self):
        return self._id

class Verse(models.Model):
    _id = models.CharField(max_length=30, unique=True)
    reference = models.CharField(max_length=30)
    chapter = models.ForeignKey(Chapter, verbose_name=_("Chapter"), on_delete=models.CASCADE, related_name="verses")
    
    class Meta: 
        ordering = ['id']
    
    def __str__(self):
        return self.reference
    
class Bible(models.Model):
    """
    Example: Kjv, Asv
    """    
    _id = models.CharField(max_length=25, unique=True)
    dblId = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=15)
    book = models.ManyToManyField(Book, verbose_name=_("Books"), related_name="books")

    def __str__(self):
        return self.name

class TodaysVerse(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    bible = models.OneToOneField(Bible, verbose_name=_("Bible"), on_delete=models.CASCADE)
    
    book = models.OneToOneField(Book, verbose_name=_("Book"), on_delete=models.CASCADE)

    chapter = ChainedForeignKey(Chapter,
                                auto_choose=True,
                                sort=True,
                                verbose_name="Chapter",
                                chained_field="book",
                                chained_model_field="book")
    
    verse = ChainedForeignKey(Verse,
                                auto_choose=True,
                                sort=True,
                                verbose_name="Verse",
                                chained_field="chapter",
                                chained_model_field="chapter")
    
    date = models.DateField(_("To be posted on?"), auto_now=False, auto_now_add=False, default=timezone.now, unique=True)
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True)

    class Meta:
        verbose_name_plural = "Todays Verse"
        verbose_name = "Todays Verse"
        ordering = ['date']
    
    def __str__(self):
        return self.title