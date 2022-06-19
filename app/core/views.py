from typing import Union

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.db.utils import IntegrityError
from app.core.forms.add_movie import AddMovieForm
from app.core.services.movie_processor import CSFDProcessor, IMDBProcessor


def process_movie(request):
    """debug processors ToDo: Delete me"""
    imdb = IMDBProcessor()
    imdb.get_content("https://www.imdb.com/title/tt10872600/?ref_=tt_sims_tt_t_1")
    print(imdb.get_movie_name())

    return HttpResponse("Processed")


@login_required
def index_view(request) -> HttpResponse:
    """Index page"""
    if request.method == "POST":
        form = AddMovieForm(request.POST, request.FILES)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            try:
                movie.save()
            except IntegrityError:  # Duplicate entry
                redirect("index")

            redirect("index")
    else:
        form = AddMovieForm()

    return render(request, "index.html", {"form": form})


def login_view(request) -> Union[HttpResponse, HttpResponseRedirect]:
    """Login page"""
    if request.user.is_authenticated:
        return redirect("index")

    template = loader.get_template("login.html")

    return HttpResponse(template.render({}, request))


def logout_link(request) -> HttpResponseRedirect:
    """Logout link"""
    logout(request)

    return redirect("login")
