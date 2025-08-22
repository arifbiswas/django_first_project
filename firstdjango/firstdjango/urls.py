"""
URL configuration for firstdjango project.
"""
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("home",views.home,name="homeasd"),
    path("about/",views.about ,name="about"),
    path("contact/",views.contact,name="contact"),
    path("test/",include("testapp.urls"))
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    # Include django_browser_reload URLs only in DEBUG mode
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]