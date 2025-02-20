
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.urls import path
from Megazine import views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("contact", views.Contact, name="contact"),
    path("newspage", views.Newspage, name="newspage"),
    path("about", views.About, name="about"),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)