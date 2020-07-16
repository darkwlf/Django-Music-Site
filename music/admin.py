from django.contrib import admin
from .models import Album, Song, Comments, Artist

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Comments)
admin.site.register(Artist)