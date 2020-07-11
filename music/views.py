from django.shortcuts import (
    render,
    HttpResponse,
    HttpResponseRedirect,
    Http404,
    redirect
)

from .models import (

    Album,

    Song,

)

import time

def music(request):
    context = {
        'album' : Album.objects.all()
    }
    return render(request, 'templates/music.html', context)

def detail(request, album_id):
    #txt = Album.objects.filter(id=album_id)
    try:
        context = {
        'song' : Song.objects.get(id = album_id),#[album_id-1],
        'album' : Album.objects.get(id = album_id),
        'id' : album_id,
        }
        return render(request, 'templates/album.html', context)
    except IndexError:
        raise Http404("Album Dosen't Exists")

def main(request):

    return render(request, 'templates/index.html')

