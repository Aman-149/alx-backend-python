from django_filters import rest_framework as filters
from chats.models import Message

class MessageFilter(filters.FilterSet):
    class Meta:
        model = Message
        fields = {
            'sender': ['exact'],
            'receiver': ['exact'],
            'timestamp': ['gte', 'lte'],
        }