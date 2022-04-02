from typing import Union

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader


@login_required
def index_view(request) -> HttpResponse:
    """Index page"""
    template = loader.get_template("index.html")

    return HttpResponse(template.render(None, request))


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
