# Generated by Django 3.0.8 on 2020-07-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0015_auto_20200716_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artist_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
