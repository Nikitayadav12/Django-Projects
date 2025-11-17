from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from .permissions import IsOrganizerOrReadOnly

class Eventviewset(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)



def event(request):
    return render(request, 'event/event.html')