from django.db import models
import uuid

SHOW_TYPE_CHOICES = (
    ('movie', 'Movie'),
    ('tv_show', 'TV Show')
)


class Genre(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Actor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Language(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


def default_link():
    return str("https://www.youtube.com/embed/GtL1huin9EE")


class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=1000)
    trailer_link = models.CharField(
        max_length=2000, default=default_link)
    cover = models.ImageField(upload_to='movie_tv/covers', null=True)
    show_type = models.CharField(
        max_length=10, choices=SHOW_TYPE_CHOICES, default='movie')
    description = models.TextField()
    cast = models.ManyToManyField(Actor, related_name='movies')
    genre = models.ManyToManyField(Genre, related_name="movies")
    date_added = models.DateTimeField(null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']
