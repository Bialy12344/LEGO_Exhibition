# Generated by Django 4.1.6 on 2023-02-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exhibitor", "0010_remove_moc_size_alter_moc_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="moc",
            name="size",
            field=models.CharField(
                choices=[
                    ("0,5 stołu", "0,5 stołu"),
                    ("1 stół", "1 stół"),
                    ("2 stoły", "2 stoły"),
                ],
                default="0,5 stołu",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="moc",
            name="category",
            field=models.CharField(
                choices=[
                    ("Castle/Starożytność", "Castle/Starożytność"),
                    ("Architektura", "Architektura"),
                    ("Komiks/Anime/Manga", "Komiks/Anime/Manga"),
                    ("Militaria", "Militaria"),
                    ("Pojazdy Minifig", "Pojazdy Minifig"),
                    ("Pojazdy technic", "Pojazdy technic"),
                    ("Space/Sci-fi", "Space/Sci-fi"),
                    ("Kolejnictwo", "Kolejnictwo"),
                ],
                default="Castle/Starożytność",
                max_length=20,
            ),
        ),
    ]