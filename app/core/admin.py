from django.contrib import admin

from app.core.models import Profile


@admin.register(Profile)
class ApplicationTypeAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_display_links = ("user",)
    search_fields = ("user",)
    list_per_page = 50
