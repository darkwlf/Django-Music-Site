from django.db import models

class Album(models.Model):

    artist = models.CharField(max_length=25)

    album_title = models.CharField(max_length=500)

    genre = models.CharField(max_length=100)

    album_logo = models.CharField(max_length=900)

    def __str__(self):

        return self.album_title

class Song(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    file_type = models.CharField(max_length=900, default='mp3')

    song = models.CharField(max_length=250, default='mp3')

    addr = models.CharField(max_length=500, default='https://irsv.upmusics.com/99/Shahab%20Mozaffari%20-%20Rade%20Pa%20(320).mp3')

    def __str__(self):

        return 'Name: ' + str(self.song)

class Comments(models.Model):

    comment = models.TextField(max_length=1000)

    page = models.CharField(max_length=900, default='')

    def __str__(self):

        return self.comment

class Artist(models.Model):

    artist_name = models.CharField(max_length=1000, default='')

    artist_image = models.ImageField(upload_to="static/")

    artist_description = models.CharField(max_length=2000, default='')

    def __str__(self):

        return self.artist_name
