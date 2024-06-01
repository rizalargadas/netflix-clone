from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from movie_tv.models import Movie
from django.urls import reverse


def browse(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profiles = Profile.objects.filter(account=profile.account)
    movies = Movie.objects.all()
    featured_movie = movies.get(is_featured=True)
    context = {
        'profile': profile,
        'profiles': profiles,
        'movies': movies,
        'featured_movie': featured_movie,
    }
    return render(request, 'movie_tv/browse.html', context)


def watch(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'movie_tv/watch.html', {'movie': movie})
