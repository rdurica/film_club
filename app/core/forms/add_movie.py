from django.forms import ModelForm

from app.core.models import Movie


class AddMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ["name", "reference_url", "labels", "year", "img"]
