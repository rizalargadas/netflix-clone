from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import ProfileForm
from .models import Profile


@login_required
def choose_profile(request):
    profiles = Profile.objects.filter(
        account=request.user).order_by('created_at')
    return render(request, 'profiles/choose_profile.html', {'profiles': profiles})


@login_required
def manage_profiles(request):
    profiles = Profile.objects.filter(
        account=request.user).order_by('created_at')
    return render(request, 'profiles/manage_profiles.html', {'profiles': profiles})


@login_required
def add_profile(request):
    profiles = Profile.objects.filter(
        account=request.user)
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


@login_required
def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            pin1 = form.cleaned_data['enter_pin']
            pin2 = form.cleaned_data['confirm_pin']
            if pin1 and pin2:
                if pin1 != pin2:
                    error = 'Pin did not match.'
                    return render(request, 'profiles/edit_profile.html', {'profile': profile, 'form': form, 'error': error})
                profile.pin = pin1
            profile.save()
            return redirect('profiles:manage_profiles')
    else:
        form = ProfileForm(
            initial={'name': profile.name,
                     'is_kid': profile.is_kid,
                     'avatar': profile.avatar})
    return render(request, 'profiles/edit_profile.html', {'profile': profile, 'form': form})


def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.delete()
    return redirect('profiles:manage_profiles')


def profile_lock(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        entered_pin = request.POST.get('pin', '')
        if entered_pin == profile.pin:
            return redirect(reverse('movie_tv:browse', args=[pk]))
        else:
            error = 'Wrong pin.'
            return render(request, 'profiles/profile_lock.html', {'error': error})

    return render(request, 'profiles/profile_lock.html')


def check_profile_lock(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if profile.pin:
        return redirect(reverse('profiles:profile_lock', args=[pk]))
    else:
        return redirect(reverse('movie_tv:browse', args=[pk]))
