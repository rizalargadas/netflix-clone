from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.urls import reverse
from .models import Vote, Genre, Language, Movie, List
from django.db.models import Exists, OuterRef
from django.utils.timezone import make_aware
from datetime import datetime, timedelta


def browse(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    profiles = Profile.objects.filter(account=profile.account)

    movies = Movie.objects.annotate(
        has_voted=Exists(Vote.objects.filter(
            profile=profile, movie=OuterRef('pk'))),
        on_list=Exists(List.objects.filter(
            profile=profile, movie=OuterRef('pk')))
    )

    featured_movie = movies.get(is_featured=True, show_type='movie')

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


def add_to_list(request, profile_pk, movie_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    my_list, created = List.objects.get_or_create(profile=profile)

    # Add the movie to the list if it's not already there
    if not my_list.movie.filter(pk=movie.pk).exists():
        my_list.movie.add(movie)

    return redirect(reverse('movie_tv:browse', args=[profile_pk]))


def tv_show(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    profiles = Profile.objects.filter(account=profile.account)
    genres = Genre.objects.all()
    query = request.GET.get('q', '')
    message = ''

    if profile and query:
        movies = Movie.objects.filter(show_type='tv_show').annotate(
            has_voted=Exists(Vote.objects.filter(
                profile=profile, movie=OuterRef('pk')))
        )
        movies = movies.filter(genre__name__icontains=query)
        if not movies:
            message = f"No TV show available for {query}."
    else:
        movies = Movie.objects.filter(show_type='tv_show')

    featured_movie = get_object_or_404(
        Movie, is_featured=True, show_type='tv_show')
    context = {
        'profile': profile,
        'profiles': profiles,
        'movies': movies,
        'featured_movie': featured_movie,
        'genres': genres,
        'message': message,
        'query': query
    }
    return render(request, 'movie_tv/tv_show.html', context)


def movies(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    profiles = Profile.objects.filter(account=profile.account)
    genres = Genre.objects.all()
    query = request.GET.get('q', '')
    message = ''

    if profile and query:
        movies = Movie.objects.filter(show_type='movie').annotate(
            has_voted=Exists(Vote.objects.filter(
                profile=profile, movie=OuterRef('pk')))
        )
        movies = movies.filter(genre__name__icontains=query)
        if not movies:
            message = f"No movie available for {query}."
    else:
        movies = Movie.objects.filter(show_type='movie')

    featured_movie = get_object_or_404(
        Movie, is_featured=True, show_type='movie')
    context = {
        'profile': profile,
        'profiles': profiles,
        'movies': movies,
        'featured_movie': featured_movie,
        'genres': genres,
        'message': message,
        'query': query
    }
    return render(request, 'movie_tv/movies.html', context)


def new_popular(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    profiles = Profile.objects.filter(account=profile.account)
    genres = Genre.objects.all()
    query = request.GET.get('q', '')
    message = ''

    one_month_ago = make_aware(datetime.now() - timedelta(days=30))

    if profile and query:
        movies = Movie.objects.filter(show_type='movie').annotate(
            has_voted=Exists(Vote.objects.filter(
                profile=profile, movie=OuterRef('pk')))
        )
        movies = movies.filter(genre__name__icontains=query)
        if not movies:
            message = f"No movie available for {query}."
    else:
        movies = Movie.objects.filter(show_type='movie')

    movies = movies.filter(date_added__gte=one_month_ago)

    featured_movie = get_object_or_404(
        Movie, is_featured=True, show_type='movie')
    context = {
        'profile': profile,
        'profiles': profiles,
        'movies': movies,
        'featured_movie': featured_movie,
        'genres': genres,
        'message': message,
        'query': query
    }
    return render(request, 'movie_tv/new_popular.html', context)


def browse_by_language(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    profiles = Profile.objects.filter(account=profile.account)
    languages = Language.objects.all()
    query = request.GET.get('q', '')
    message = ''

    if profile and query:
        movies = Movie.objects.annotate(
            has_voted=Exists(Vote.objects.filter(
                profile=profile, movie=OuterRef('pk')))
        )
        movies = movies.filter(language__name__icontains=query)
        if not movies:
            message = f"No movie/show available for {query}."
    else:
        movies = Movie.objects.all()

    featured_movie = get_object_or_404(
        Movie, is_featured=True, show_type='movie')
    context = {
        'profile': profile,
        'profiles': profiles,
        'movies': movies,
        'featured_movie': featured_movie,
        'languages': languages,
        'message': message,
        'query': query
    }
    return render(request, 'movie_tv/browse_by_language.html', context)
