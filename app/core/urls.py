from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("logout", views.logout_link, name="logout"),
    path("login", views.login_view, name="login"),
]
