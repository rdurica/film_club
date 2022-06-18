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
    list_display = ("url", "source", "created_at", "is_approved", "is_processed")
    list_display_links = ("url",)
    search_fields = ("url",)
    list_per_page = 50
