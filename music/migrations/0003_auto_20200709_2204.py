# Generated by Django 3.0.8 on 2020-07-09 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200709_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='type',
            new_name='file_type',
        ),
    ]
