from django_extensions.management.jobs import BaseJob, DailyJob
from contents.models import TV
from django.utils import timezone
from datetime import timedelta

class Job(DailyJob):
    help = "Deletes TV url over 24 hours"

    def execute(self):
        # executing empty sample job
        print("...running delete tv job.")
        urls = TV.objects.all()
        now = timezone.now()
        for url in urls:
            expiration = url.created_at + timedelta(days=1)
            if expiration < now:
                print("...Deleting", url.title)
                url.delete()
                print("Deleted")
        print("...job terminated.")