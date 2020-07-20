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

    Artist,

    Like,

    Dislike,

)

from django.core.exceptions import ObjectDoesNotExist

import time

def music(request):

    #ar = Artist.objects.all()



    context = {
        'album' : Album.objects.all(),
        'artist' : Artist.objects.all()
        #'artist_page': page
    }

    return render(request, 'templates/music.html', context)

def detail(request, album_id):

    if Dislike.objects.filter(page=album_id).count() - Like.objects.filter(page=album_id).count() < 0 :

        sd = int(Like.objects.filter(page=album_id).count() - Dislike.objects.filter(page=album_id).count()) / int(Like.objects.filter(page=album_id).count() + Dislike.objects.filter(page=album_id).count()) * 100

    else:

        sd = int(Dislike.objects.filter(page=album_id).count() - Like.objects.filter(page=album_id).count()) / int(Dislike.objects.filter(page=album_id).count() + Like.objects.filter(page=album_id).count()) * 100

    try:

        context = {

        'song' : Song.objects.get(id = album_id),#[album_id-1],

        'album' : Album.objects.get(id = album_id),

        'comment' : Comments.objects.filter(page=album_id),

        'id' : album_id,

        'artist_page' : Artist.objects.get(artist_name=Album.objects.get(id = album_id).artist).id,

        'like' : Like.objects.filter(page=album_id),

        's' : Like.objects.filter(page=album_id).count(),

        'd' : Dislike.objects.filter(page=album_id).count(),

        'sd' : sd

        }

        return render(request, 'templates/album.html', context)

    except IndexError:

        raise Http404("Album Dosen't Exists")

    except ObjectDoesNotExist:

        context = {
            'song': 'در حال حاضر آهنگی موجود نیست',

            #Song.objects.get(id=album_id),  # [album_id-1],
            'album': Album.objects.get(id=album_id),

            'id': album_id,

            'artist_page': Artist.objects.get(artist_name=Album.objects.get(id=album_id).artist).id,

        }

        return render(request, 'templates/album.html', context)

    except:

        context = {
            'song': Song.objects.get(id=album_id),  # [album_id-1],

            'album': Album.objects.get(id=album_id),

            'id': album_id,

            'artist_page': Artist.objects.get(artist_name=Album.objects.get(id = album_id).artist).id,

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

    return redirect('.')

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


def artist(request, name):

    singer = Artist.objects.get(id=name)

    singer_songs = Album.objects.filter(artist=singer.artist_name)

    context = {

        'artist_songs' : singer_songs,

        'artist_name' : singer.artist_name,

        'artist_image' : singer.artist_image,

        'artist_description' : singer.artist_description,

        'id' : Album.objects.filter(id=name),

    }

    return render(request, 'templates/artist.html', context)


def artist_main(request):

    artists = Artist.objects.all()

    context = {

        'artists' : artists,

    }

    return render(request,'templates/artist_main.html', context)

def like(request, page_num):
    try:
        if not request.session['like'] and not request.session['dislike']:

            like = Like()

            new_like = request.POST.get('like')

            like.likes = new_like

            request.session['like'] = page_num

            like.page = page_num

            like.save()

            l = Like.objects.filter(page=page_num)

            return HttpResponse(l.count())
        else:
            return HttpResponse("You Liked Before")

    except KeyError:

        like = Like()

        new_like = request.POST.get('like')

        like.likes = new_like

        request.session['like'] = page_num

        like.page = page_num

        like.save()

        l = Like.objects.filter(page=page_num)

        return HttpResponse(l.count())

def dislike(request, page_number):
    try:

        if not request.session['dislike'] and not request.session['like']:

            dislike = Dislike()

            new_dislike = request.POST.get('dislike')

            dislike.dislikes = new_dislike

            request.session['dislike'] = page_number

            dislike.page = page_number

            dislike.save()

            l = Dislike.objects.filter(page=page_number)

            return HttpResponse(l.count())

        else:

            return HttpResponse("You DisLiked Before")

    except KeyError:

        dislike = Dislike()

        new_dislike = request.POST.get('like')

        dislike.dislikes = new_dislike

        request.session['dislike'] = page_number

        dislike.page = page_number

        dislike.save()

        l = Dislike.objects.filter(page=page_number)

        return HttpResponse(l.count())

def artist_search(request):

    """
    a = ['A', 'Al', 'mdm', 'Ali', 'Naser']
    for i in a:
        if "Al" in i:
            print(i)
    """

    artists = Artist.objects.all()

    """for i in albums:

        if keyword in i:

            context = {
                'result' : i,
            }"""

    context = {
        'artists' : artists,
        'keyword' : request.POST.get('keyword'),
    }

    return render(request, 'templates/artist_search.html', context)