# Generated by Django 4.1.6 on 2023-02-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exhibitor", "0009_moc_category_moc_size"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="moc",
            name="size",
        ),
        migrations.AlterField(
            model_name="moc",
            name="category",
            field=models.CharField(
                choices=[("FR", "Freshman"), ("SO", "Sophomore")],
                default="FR",
                max_length=2,
            ),
        ),
    ]
