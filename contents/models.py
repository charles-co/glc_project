from django.conf import settings
from django.db import models 
from django.utils.translation import ugettext_lazy as _
from audiofield.fields import AudioField
from glc_project.utils import files_directory_path
import os.path

class Audio(models.Model):

    title = models.CharField(_("Titile"), max_length=100)
    audio_file = AudioField(upload_to=files_directory_path,
                            ext_whitelist=(".mp3", ".wav", ".ogg"),
                            help_text=("Allowed type - .mp3, .wav, .ogg"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<ul class="playlist"><li style="width:250px;">\
            <a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(self.audio_file.name))
            return player_string

    audio_file_player.allow_tags = True
    audio_file_player.short_description = _('Audio file player')

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.title
    
class Podcast(models.Model):

    title = models.CharField(_("Titile"), max_length=100)
    file = models.FileField(_("Podcast"), upload_to=files_directory_path, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.title

class Video(models.Model):

    title = models.CharField(_("Titile"), max_length=100)
    file = models.FileField(_("Video"), upload_to=files_directory_path, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.title