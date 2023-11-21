from django.db import models
from django.conf import settings
from django_cryptography.fields import encrypt


"""
Using django-cryptography I am encrypting the username, password and comment fields.
I do anticipate users saving sensitive information as comments. If someone were to
read the db this is all they get at the moment: 
1|Apple|apple.com|blue|1|�|�|�

Unfortunately as an Admin I will still have access to the information saved, need to
make it clear to the users.
"""
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
    username = encrypt(models.CharField(max_length=1000, null=True, blank=True)) # Encrypted field.
    ciphertext = encrypt(models.CharField(max_length=1000)) # Encrypted field.
    url = models.CharField(max_length=64)
    tags = models.CharField(max_length=10, choices=pw_tags, null=True, blank=True)
    comment = encrypt(models.CharField(max_length=1000, null=True, blank=True)) # Encrypted field.
    def __str__(self):
        return f"{self.user} ({self.name})"