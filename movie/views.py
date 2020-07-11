from django.shortcuts import render

from .models import Movie

def movie(request):

    context = {
        'movie' : Movie.objects.all(),
    }

    return render(request, 'templates/movie.html', context)