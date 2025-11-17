from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#create custom user model with their model(Admin,Organizer,Attendee)


class User(AbstractUser):
    ADMIN='admin'
    ORGANIZER='organizer'
    ATTENDEE='attendees'


    ROLE_CHOICES=[
        (ADMIN,'admin'),
        (ORGANIZER,'organizer'),
        (ATTENDEE,'attendees')
    ]
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default=ATTENDEE)
