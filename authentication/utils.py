from django.core.mail import EmailMessage

import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()



class Util:

    @staticmethod
    def send_email(payload):
        email = EmailMessage(subject=payload['subject'],
                                body=payload['body'],
                                to=[payload['email']],
                            )
        EmailThread(email).start()