from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmailForm, CustomUserCreationForm


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
            return redirect('core:success')
    else:
        form = CustomUserCreationForm(initial={'email': email})
    return render(request, 'core/signup.html', {'form': form})


def success(request):
    return render(request, 'core/success.html')

# def signin(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('movie_tv: browse')
#     else:
#         print('not a POST request')
#         form = CustomAuthenticationForm()
#     return render(request, 'core/signin.html', {'form': form})
