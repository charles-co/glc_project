from django.conf import settings
from django.contrib import messages
from django.db.models.signals import post_save, pre_save, pre_delete
from django.conf import settings
from django.dispatch import receiver

# from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from .models import Profile

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def post_save_user_create_reciever(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(pre_save, sender=Profile)
def pre_save_user_reciever(sender, instance, *args, **kwargs):
    if not instance.full_name.istitle():
        instance.full_name = instance.full_name.title()