from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import EventRegistration
from .serializers import EventRegisterationSerializer
from .permissions import IsAttendee
from django.apps import apps

class RegisterEventView(generics.CreateAPIView):
    serializer_class = EventRegisterationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAttendee]

    def create(self, request, *args, **kwargs):
        event_id = self.kwargs.get('event_id')
        Event = apps.get_model('event', 'Event')
        event = get_object_or_404(Event, id=event_id)
        attendees = request.user

        if EventRegistration.objects.filter(event=event, attendees=attendees).exists():
            return Response({'detail': 'You have already registered for this event.'}, status=status.HTTP_409_CONFLICT)

        registration = EventRegistration.objects.create(event=event, attendees=attendees)
        serializer = self.get_serializer(registration)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# views.py

from django import forms
from django.shortcuts import redirect
# from event.models import Event  # direct import because now you know Event model path

# Form for registration
class EventRegistrationForm(forms.Form):
    event_id = forms.IntegerField(label='Event ID')

    def __init__(self, *args, **kwargs):
        # Check if 'event_id' is passed and handle it
        self.event_id = kwargs.pop('event_id', None)
        super().__init__(*args, **kwargs)

# New view for frontend
def register_event_form(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            return redirect('api_register_event', event_id=event_id)  # Redirect to your API view
    else:
        form = EventRegistrationForm()

    return render(request, 'attendees/register_event.html', {'form': form})

from django.http import JsonResponse
from event.models import Event

def your_api_view(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        # Process the event data
        return JsonResponse({'message': 'Event registered successfully', 'event_id': event.id})
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)
