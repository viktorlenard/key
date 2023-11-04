from django.db import models
from django.conf import settings

# Create your models here.

'''
Examples for a moron (me):

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
'''

class Password(models.Model):
    blue = "blue"
    red = "red"
    green = "green"
    yellow = "yellow"
    purple = "purple"
    pw_tags = [
        (blue,"blue"),
        (red, "red"),
        (green, "green"),
        (yellow, "yellow"),
        (purple, "purple"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='user_passwords')
    name = models.CharField(max_length=64)
    hash = models.CharField(max_length=1000)
    url = models.CharField(max_length=64)
    tags = models.CharField(max_length=10, choices=pw_tags)

    def __str__(self):
        return f"{self.user} ({self.name})"