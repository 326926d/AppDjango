from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("contacts/", views.contacts, name = "contacts"),
    path("digest/", views.digest, name = "digest"),
    path("tutors/", views.about, name = "tutors"),
    path("vacancies/", views.vacancies, name = "vacancies"),
]
