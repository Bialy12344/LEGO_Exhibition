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
    CASTLE = 'Castle/Starożytność'
    ARCHITEKTURA = 'Architektura'
    KOMIKS = 'Komiks/Anime/Manga'
    MILITARIA = 'Militaria'
    POJAZDY_MINIFIG = 'Pojazdy Minifig'
    POJAZDY_TECHNIC = 'Pojazdy technic'
    SPACE = 'Space/Sci-fi'
    KOLEJNICTWO = 'Kolejnictwo'
    CATEGORY = [
        ('Castle/Starożytność', 'Castle/Starożytność'),
        ('Architektura', 'Architektura'),
        ('Komiks/Anime/Manga', 'Komiks/Anime/Manga'),
        ('Militaria', 'Militaria'),
        ('Pojazdy Minifig', 'Pojazdy Minifig'),
        ('Pojazdy technic', 'Pojazdy technic'),
        ('Space/Sci-fi', 'Space/Sci-fi'),
        ('Kolejnictwo', 'Kolejnictwo'),
    ]
    FIRST_SIZE = '0,5 stołu'
    SECOND_SIZE = '1 stół'
    THIRD_SIZE = '2 stoły'
    SIZE = [
        ('0,5 stołu', '0,5 stołu'),
        ('1 stół', '1 stół'),
        ('2 stoły', '2 stoły'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=CATEGORY, default=CASTLE)
    size = models.CharField(max_length=20, choices=SIZE, default=FIRST_SIZE)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)

class exhibition(models.Model):
    presence_User = models.BooleanField(default=False)
    presence_moc = models.BooleanField(default=False)
    acommodation = models.CharField(max_length=20, choices=['FR/SAT' 'SAT/SUN' 'SUN/MON']),

