from django.conf import settings
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from django.utils.http import urlencode
from .models import Event

@receiver(pre_save, sender=Event)
def pre_save_user_reciever(sender, instance, *args, **kwargs):
    if not instance.description:
        if instance.title:
            instance.description = instance.title