# Generated by Django 3.0.8 on 2020-07-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(default='091234567'),
        ),
    ]
