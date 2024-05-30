from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.urls import reverse


def browse(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'movie_tv/browse.html', {'profile': profile})
