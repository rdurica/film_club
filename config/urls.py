import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings

urlpatterns = [
    path("", include("social_django.urls", namespace="social")),
    path("", include("app.core.urls")),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
