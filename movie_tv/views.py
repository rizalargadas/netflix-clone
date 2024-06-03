from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from movie_tv.models import Movie
from django.urls import reverse
from .models import Vote
from django.db.models import Exists, OuterRef


def browse(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    profiles = Profile.objects.filter(account=profile.account)

    if profile:
        movies = Movie.objects.annotate(
            has_voted=Exists(Vote.objects.filter(
                profile=profile, movie=OuterRef('pk')))
        )
    else:
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


def vote(request, profile_pk, movie_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if not Vote.objects.filter(profile=profile, movie=movie).exists():
        Vote.objects.create(profile=profile, movie=movie)

    return redirect(reverse('movie_tv:browse', args=[profile_pk]))
