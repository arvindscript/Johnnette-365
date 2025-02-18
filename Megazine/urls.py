
from django.conf import settings
from django.urls import path
from Megazine import views
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.Contact, name="contact"),
    path("page", views.Page, name="page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)