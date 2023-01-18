from django.core.mail import send_mail
from rest_framework import status, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import EmailSerializer

import os
import threading
from threading import Thread


class EmailThread(threading.Thread):
    """Class to send asynchronous emails with Threading"""
    def __init__(self, subject, body, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.body = body
        threading.Thread.__init__(self)

    def run(self):
        send_mail(
            self.subject,
            self.body,
            os.environ.get('EMAIL_ADDR'),
            [self.recipient_list]
        )


def send_async_mail(subject, body, recipient_list):
    """Static method to send async emails"""
    EmailThread(subject, body, recipient_list).start()


class MailerView(mixins.CreateModelMixin, GenericAPIView):
    """View to send emails"""
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        details = serializer.data
        subject = details['subject']
        body = details['body']
        receiver = details['receiver']

        send_async_mail(subject=subject, body=body, recipient_list=receiver)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
