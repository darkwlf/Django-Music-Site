# Generated by Django 3.0.8 on 2020-07-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200711_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_cover_url',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
