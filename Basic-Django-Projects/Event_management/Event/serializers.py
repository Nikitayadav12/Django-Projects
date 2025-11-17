from  rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    organizer_username=serializers.CharField(source='organizer.username',read_only=True)


    class Meta:
        model=Event
        fields='__all__'
        read_only_fields=['organizer']