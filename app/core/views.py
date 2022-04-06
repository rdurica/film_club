from typing import Union

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader

from app.core.forms.add_movie import AddMovieForm


@login_required
def index_view(request) -> HttpResponse:
    """Index page"""
    if request.method == "POST":
        form = AddMovieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
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
