from django.urls import path
from . import views

urlpatterns = [
    path("",views.app,name="app"),
    path("/contact/",views.contact ,name="testcontact"),

]
