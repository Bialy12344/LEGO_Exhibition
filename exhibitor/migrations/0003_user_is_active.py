# Generated by Django 4.1.6 on 2023-02-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exhibitor", "0002_alter_user_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
