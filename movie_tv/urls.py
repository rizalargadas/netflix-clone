from django.urls import path
from . import views

app_name = 'movie_tv'

urlpatterns = [
    path('<int:pk>/browse/', views.browse, name='browse')
]
