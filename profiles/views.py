from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import ProfileImage, Profile


@login_required
def choose_profile(request):
    profiles = Profile.objects.filter(account=request.user)
    return render(request, 'profiles/choose_profile.html', {'profiles': profiles})


@login_required
def manage_profiles(request):
    return render(request, 'profiles/manage_profiles.html')


@login_required
def add_profile(request):
    profiles = Profile.objects.filter(account=request.user)
    if profiles.count() > 5:
        return render(request, 'profiles/choose_profile.html', {
            'form': ProfileForm(),
            'profiles': profiles,
            'error': 'You cannot create more than 5 profiles.'
        })

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            if not profile.is_kid:
                profile.is_kid = False
            profile.account = request.user
            profile.save()
            return redirect('profiles:choose_profile')
        else:
            print(form.errors)
    else:
        form = ProfileForm()
    return render(request, 'profiles/add_profile.html', {'form': form})
