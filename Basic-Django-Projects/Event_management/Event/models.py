from django.db import models
from django.conf import settings
# from django.utils import timezone
# Create your models here.


class Event(models.Model):
    CATEGORY_CHOICES=(
        ('tech','Tech'),
        ('cultural','Cultural'),
        ('workshop','Workshop'),
        ('sports','Sports'),
    )

    title=models.CharField(max_length=255)
    description=models.TextField()
    date=models.DateTimeField()
    location=models.CharField(max_length=255)
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='organize_event')

    def __str__(self):
        return self.title