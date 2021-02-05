from django.conf import settings
from django.core.mail import send_mail

import threading


class EmailThread(threading.Thread):

    def __init__(self, payload):
        self.payload = payload
        threading.Thread.__init__(self)

    def run(self):
        send_mail(
            self.payload['subject'],
            self.payload['body'],
            settings.DEFAULT_FROM_EMAIL,
            (self.payload['email'],),
            fail_silently=False,
        )



class Util:

    @staticmethod
    def send_email(payload):
        EmailThread(payload).start()