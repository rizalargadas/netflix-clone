from django.contrib import admin
from .models import Genre, Movie, Actor, Language, Vote, List

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Language)
admin.site.register(Vote)
admin.site.register(List)
