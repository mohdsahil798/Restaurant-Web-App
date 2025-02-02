from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("service/", service, name="service"),
    path("menu/", menu, name="menu"),
    path("contact/", contact, name="contact"),
]