from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models 
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

class Note(models.Model):

    title = models.CharField(_("Title"), max_length=50, blank=True)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    text = models.TextField(_("Text"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', 'created_at']

    def __str__(self):
        return self.title