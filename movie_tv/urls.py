from django.urls import path
from . import views

app_name = 'movie_tv'

urlpatterns = [
    path('<int:profile_pk>/browse/', views.browse, name='browse'),
    path('<uuid:movie_pk>/watch/', views.watch, name="watch"),
    path('<int:profile_pk>/<uuid:movie_pk>/vote/', views.vote, name="vote"),
]
