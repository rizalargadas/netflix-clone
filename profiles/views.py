from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import ProfileImage


@login_required
def choose_profile(request):
    return render(request, 'profiles/choose_profile.html')


@login_required
def manage_profiles(request):
    return render(request, 'profiles/manage_profiles.html')


@login_required
def add_profile(request):
    if request.method == 'POST':
        print(request.POST)
        form = ProfileForm(request.POST, request.FILES)
        print('checkpoint 1')
        if form.is_valid():
            print('checkpoint 2')
            profile = form.save(commit=False)
            if not profile.avatar:
                profile.avatar = ProfileImage.objects.get(
                    name='default_profile')
            if not profile.avatar:
                profile.is_kid = False
            profile.save()
            print('checkpoint 3')
            return redirect('profiles:choose_profile')
        else:
            print(form.errors)
    else:
        form = ProfileForm()
    return render(request, 'profiles/add_profile.html', {'form': form})
