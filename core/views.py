from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmailForm, CustomUserCreationForm, CustomAuthenticationForm


def index(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            return redirect(f"{reverse('core:signup')}?email={email}")
    else:
        form = EmailForm()
    return render(request, 'core/index.html', {'form': form})


def signup(request):
    email = request.GET.get('email', '')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profiles:choose_profile')
    else:
        form = CustomUserCreationForm(initial={'email': email})
    return render(request, 'core/signup.html', {'form': form})


def success(request):
    return render(request, 'core/success.html')


def signin(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect('profiles:choose_profile')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'core/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('core:index')
