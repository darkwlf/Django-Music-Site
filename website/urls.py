from music.views import (
    music,
    main,
    detail,

)
from register.views import sign, login, register
from django.contrib import admin, auth
from django.urls import path, include
from movie.views import movie

urlpatterns = [

    path('', main, name="Index"),

    path('admin/', admin.site.urls),

    path('music/', music, name="Music"),

    path('music/<int:album_id>', detail, name="Album"),

    path('Sign/', register, name="sign"),

    path('Sign/Register', sign, name="Register"),

    path('Movie/', movie, name="Movie Index")

]
