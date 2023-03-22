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

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.username

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
    FIRST_SIZE = 0.5
    SECOND_SIZE = 1
    THIRD_SIZE = 2
    SIZE = [
        (0.5, '0,5 stołu'),
        (1, '1 stół'),
        (2, '2 stoły'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=CATEGORY, default=CASTLE)
    size = models.FloatField(max_length=20, choices=SIZE)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)

class Organizator(models.Model):
    nazwa = models.CharField(max_length=20)
    imię = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    ulica = models.CharField(max_length=20)
    miasto = models.CharField(max_length=20)
    kod_pocztowy = models.CharField(max_length=20)
    NIP = models.CharField(max_length=20)
    telefon = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

class Exhibition(models.Model):
    date = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    organizator = models.ForeignKey(Organizator, on_delete=models.CASCADE)
    required_area = models.CharField(max_length=20)
    comments = models.CharField(max_length=500)







