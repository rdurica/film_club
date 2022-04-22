from datetime import date

from django.contrib.auth.models import User
from django.db import models

from .label import Label


class Movie(models.Model):
    name = models.CharField(max_length=50, unique=True)
    img = models.ImageField(upload_to="images")
    labels = models.ManyToManyField(Label)
    year = models.IntegerField(default=date.today().year)
    reference_url = models.URLField(max_length=250)
    author = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def movie_labels(self) -> str:
        """Get labels in one string"""
        return ",\n".join([label.name for label in self.labels.all()])

    def __str__(self) -> str:
        return self.name
