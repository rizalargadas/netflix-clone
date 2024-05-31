from django.urls import path
from . import views

app_name = 'movie_tv'

urlpatterns = [
    path('<int:pk>/browse/', views.browse, name='browse'),
    path('<uuid:movie_pk>/watch/', views.watch, name="watch")
]
