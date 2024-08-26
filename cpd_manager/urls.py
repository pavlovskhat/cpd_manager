"""
cpd_manager URL dispatcher.

admin: Admin backend panel.
records: records URL dispatcher.
users: users URL dispatcher.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("records.urls"), name="records"),
    path("users/", include("users.urls"), name="users"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
