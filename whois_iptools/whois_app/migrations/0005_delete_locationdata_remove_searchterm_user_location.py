# Generated by Django 4.1.6 on 2023-02-10 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whois_app', '0004_locationdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LocationData',
        ),
        migrations.RemoveField(
            model_name='searchterm',
            name='user_location',
        ),
    ]
