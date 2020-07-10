from music.views import (
    music,
    main,
    detail,
)
from django.contrib import admin, auth

from django.urls import path, include

urlpatterns = [

    path('', main, name="Index"),

    path('admin/', admin.site.urls),

    path('music/', music, name="Music"),

    path('music/<int:album_id>', detail, name="Album"),

]
