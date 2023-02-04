import hashlib
from random import randint

from django.contrib.sites import requests
from django.core.mail import send_mail
from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import EmailSerializer, TargetMail

import os
import threading


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


@api_view(['POST'])
def sendMail(request):
    targetMail=TargetMail(data=request.data)

    if targetMail.is_valid():
        address = targetMail.data['email']
        password = f'{randint(1000,9999)}'
        salt = "sugar"
        hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        send_async_mail(subject='Book a Room Email Verification', body=f'Your Secret code is: {password}', recipient_list=address)

        return Response([address, hashed_password], status=status.HTTP_200_OK)
    else: return Response(targetMail.errors)
