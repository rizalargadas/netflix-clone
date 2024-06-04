from django.urls import path
from . import views

app_name = 'movie_tv'

urlpatterns = [
    path('<int:profile_pk>/browse/', views.browse, name='browse'),
    path('<int:profile_pk>/tv_show/', views.tv_show, name='tv_show'),
    path('<int:profile_pk>/my_list/', views.list_view, name='my_list'),
    path('<int:profile_pk>/movies/', views.movies, name='movies'),
    path('<int:profile_pk>/new_popular/',
         views.new_popular, name='new_popular'),
    path('<int:profile_pk>/browse_by_language/',
         views.browse_by_language, name='browse_by_language'),
    path('<uuid:movie_pk>/watch/', views.watch, name="watch"),
    path('<int:profile_pk>/<uuid:movie_pk>/vote/', views.vote, name="vote"),
    path('<int:profile_pk>/<uuid:movie_pk>/add_to_list/',
         views.add_to_list, name="list"),
]
