from django.db import models

# Create your models here.
#event registration

from django.conf import settings
# from event_management_project.event.models import Event

class EventRegistration(models.Model):
    attendee=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    event=models.ForeignKey('event.Event',on_delete=models.CASCADE)
    registered_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('attendee','event')#prevent duplicate



    def __str__(self):
        return f"{self.attendee.username}--{self.event.title}"