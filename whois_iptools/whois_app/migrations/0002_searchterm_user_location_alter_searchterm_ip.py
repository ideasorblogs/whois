# Generated by Django 4.1.6 on 2023-02-10 21:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('whois_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchterm',
            name='user_location',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='searchterm',
            name='ip',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
    ]
