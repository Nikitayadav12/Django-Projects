from rest_framework import serializers
from .models import EventRegistration


class EventRegisterationSerializer(serializers.ModelSerializer):
    event_title=serializers.CharField(source='event.title',read_only=True)
    attendee_username=serializers.CharField(source='attendees.username',read_only=True)


    class Meta:
        models=EventRegistration
        fields='__all__'
        read_only_fields=['attendees']
