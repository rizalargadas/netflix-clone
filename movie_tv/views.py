from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.urls import reverse


@login_required
def browse(request):
    return render(request, 'movie_tv/browse.html')
