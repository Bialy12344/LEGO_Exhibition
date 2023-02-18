from django.conf import settings
from django.db import models
from django.utils import timezone

class User(models.Model):
    nick = models.CharField(max_length=20, default=True)
    password = models.CharField(max_length=20, default=True)
    name = models.CharField(max_length=20, default=True)
    surname = models.CharField(max_length=20, default=True)
    phone_number = models.CharField(max_length=12, default=True)
    email_adress = models.EmailField(max_length=30, default=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class MOC(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=30, choices=['kat1''kat2''kat3''kat4''kat5']),
    size = models.CharField(max_length=20, choices=['1','2','3']),
    poster = models.ImageField(upload_to="posters")

class exhibition(models.Model):
    presence_User = models.BooleanField(default=False)
    presence_moc = models.BooleanField(default=False)
    acommodation = models.CharField(max_length=20, choices=['FR/SAT' 'SAT/SUN' 'SUN/MON']),

