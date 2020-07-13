from django.shortcuts import (
    render,
    HttpResponse,
    HttpResponseRedirect,
    Http404,
    redirect,

)

from .models import (

    Album,

    Song,

   Comments,

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
        'comment' : Comments.objects.filter(page=album_id),
        'id' : album_id,
        }
        return render(request, 'templates/album.html', context)
    except IndexError:
        raise Http404("Album Dosen't Exists")
    except:
        context = {
            'song': Song.objects.get(id=album_id),  # [album_id-1],
            'album': Album.objects.get(id=album_id),
            'id': album_id,
        }
        return render(request, 'templates/album.html', context)

def main(request):

    return render(request, 'templates/index.html')

def comment(request, num):

    comments = Comments()

    text = request.POST.get('comment')

    comments.comment = text

    comments.page = num

    comments.save()

    return HttpResponse("Comment Posted")

def search(request):

    """
    a = ['A', 'Al', 'mdm', 'Ali', 'Naser']
    for i in a:
        if "Al" in i:
            print(i)
    """

    albums = Album.objects.all()

    """for i in albums:

        if keyword in i:

            context = {
                'result' : i,
            }"""

    context = {
        'albums' : albums,
        'keyword' : request.POST.get('keyword'),
    }

    return render(request, 'templates/search.html', context)


