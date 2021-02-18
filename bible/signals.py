from django.conf import settings
from django.db.models.signals import post_save, pre_save, pre_delete, post_init
from django.dispatch import receiver
from django.utils.http import urlencode
from .models import TodaysVerse

import os
import requests


@receiver(pre_save, sender=TodaysVerse)
def pre_save_todaysverse_reciever(sender, instance, *args, **kwargs):

    if instance.changed_fields:
        print(instance.changed_fields)
        print(instance.message)
        if list(instance.changed_fields) != ['title'] or instance.message == "verse not found.":
            key = os.environ.get("BIBLE_KEY")
            bible = instance.bible._id
            verse = instance.verse._id
            url = "https://api.scripture.api.bible/v1/bibles/{}/verses/{}".format(bible, verse)
            response = requests.get(url,
                                headers = {'api-key': key},
                                params = {'content-type': 'text',
                                            'include-notes': False,
                                            'include-titles': False,
                                            'include-chapter-numbers': False,
                                            'include-chapter-numbers': False,
                                            'include-verse-numbers': False,
                                            'include-verse-spans': False,
                                            'use-org-id': False,
                                        }
                                    )
            if response.status_code == 200:
                instance.message = response.json()['data']['content'].strip()
            else:
                instance.message = "verse not found."