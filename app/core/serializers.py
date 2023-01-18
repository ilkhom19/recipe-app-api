from rest_framework import serializers
from .models import Email


class EmailSerializer(serializers.ModelSerializer):
    """Serializer for Email object."""
    class Meta:
        model = Email
        fields = ['receiver', 'subject', 'body']
