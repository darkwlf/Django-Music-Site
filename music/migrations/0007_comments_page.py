# Generated by Django 3.0.8 on 2020-07-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='page',
            field=models.IntegerField(default=2),
        ),
    ]