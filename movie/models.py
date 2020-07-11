from django.db import models

import jdatetime

year = year = jdatetime.datetime.now().strftime("%Y")

class Movie(models.Model):

    movie_title = models.CharField(max_length=100)

    movie_rate = models.FloatField()

    movie_length = models.CharField(max_length=100)

    movie_genre = models.CharField(max_length=100)

    movie_producer = models.CharField(max_length=100)

    movie_actors = models.CharField(max_length=900)

    movie_country = models.CharField(max_length=100, default='iran')

    movie_year = models.IntegerField(default=year)

    movie_description = models.CharField(max_length=2000)

    movie_cover_url = models.CharField(max_length=5000, default='')

    movie_url = models.CharField(max_length=1000, default='https://hw14.cdn.asset.aparat.com/aparat-video/8f16a9aa423481f45bf8f23dc5e17b1421199695-144p.mp4')

    def __str__(self):
        return self.movie_title