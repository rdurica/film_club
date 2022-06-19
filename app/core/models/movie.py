from django.contrib.auth.models import User
from django.db import models

from .label import Label


class Movie(models.Model):
    SOURCE_IMDB = "imdb"
    SOURCE_CSFD = "csfd"
    MOVIE_SOURCE = ((SOURCE_IMDB, "IMDB"), (SOURCE_CSFD, "ČSFD"))

    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200, unique=True)
    source = models.CharField(max_length=10, choices=MOVIE_SOURCE, default=SOURCE_CSFD)
    labels = models.ManyToManyField(Label)
    year = models.IntegerField(null=True, blank=True, default=None)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)

    def movie_labels(self) -> str:
        """Get labels in one string"""
        return ",\n".join([label.name for label in self.labels.all()])

    def __str__(self) -> str:
        return self.name
