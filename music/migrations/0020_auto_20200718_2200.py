# Generated by Django 3.0.8 on 2020-07-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0019_like_dislike_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dislikes', models.IntegerField(default=1)),
                ('page', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
                ('page', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Like_Dislike',
        ),
    ]
