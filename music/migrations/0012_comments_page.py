# Generated by Django 3.0.8 on 2020-07-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_remove_comments_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='page',
            field=models.CharField(default=2, max_length=900),
        ),
    ]
