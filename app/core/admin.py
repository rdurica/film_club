from django.contrib import admin

from app.core.models import Movie, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_display_links = ("user",)
    search_fields = ("user",)
    list_per_page = 50


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "movie_labels", "created_at", "is_approved")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 50
