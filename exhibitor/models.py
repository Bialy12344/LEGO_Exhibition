from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    email_adress = models.EmailField(max_length=30)

class User(models.Model):
    nick = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    email_adress = models.EmailField(max_length=30)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.nick

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.username

class Moc(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=30, choices=['kat1''kat2''kat3''kat4''kat5']),
    size = models.CharField(max_length=20, choices=['1','2','3']),
    poster = models.ImageField(upload_to="posters", null=True, blank=True)

class exhibition(models.Model):
    presence_User = models.BooleanField(default=False)
    presence_moc = models.BooleanField(default=False)
    acommodation = models.CharField(max_length=20, choices=['FR/SAT' 'SAT/SUN' 'SUN/MON']),

