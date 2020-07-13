from music.views import (
    music,
    main,
    detail,
    comment,
    search,

)

from register.views import sign, login, register

from django.contrib import admin, auth

from django.urls import path, include

from movie.views import movie, movie_watch

urlpatterns = [

    path('', main, name="Index"),

    path('admin/', admin.site.urls),

    path('music/', music, name="Music"),

    path('music/<int:album_id>', detail, name="Album"),

    path('Sign/', register, name="sign"),

    path('Sign/Register', sign, name="Register"),

    path('Movie/', movie, name="Movie Index"),

    path('Movie/<int:movie_id>', movie_watch, name="Movie Watch"),

    path('music/<int:num>/new-comment', comment),

    path('music/search', search, name="search")

]

# TODO Write Rate Model And View For Musics And Movies.

# TODO Write (Like , Dislike) App

# TODO Write Search Application

