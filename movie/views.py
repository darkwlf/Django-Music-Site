from django.shortcuts import render, Http404

from .models import Movie

def movie(request):

    context = {
        'movie' : Movie.objects.all(),
    }

    return render(request, 'templates/movie.html', context)
def movie_watch(request, movie_id):
    try:
        video = Movie.objects.get(id=movie_id)

        context = {
            'video' : video
        }

        return render(request, 'templates/movie_watch.html', context)
    except:
        raise Http404("Movie Not Found")
#TODO Write Rate Model And View For Musics And Movies.