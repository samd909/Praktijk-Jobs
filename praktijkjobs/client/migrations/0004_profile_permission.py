# Generated by Django 5.1.2 on 2024-12-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='permission',
            field=models.IntegerField(default=1),
        ),
    ]