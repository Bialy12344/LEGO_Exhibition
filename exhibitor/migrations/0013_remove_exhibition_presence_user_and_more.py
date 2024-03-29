# Generated by Django 4.1.6 on 2023-03-14 20:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exhibitor", "0012_alter_moc_size_alter_user_email_adress_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exhibition",
            name="presence_User",
        ),
        migrations.RemoveField(
            model_name="exhibition",
            name="presence_moc",
        ),
        migrations.AddField(
            model_name="exhibition",
            name="address",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="exhibition",
            name="city",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="exhibition",
            name="comments",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="exhibition",
            name="date",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="exhibition",
            name="principal",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="exhibition",
            name="required_area",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
