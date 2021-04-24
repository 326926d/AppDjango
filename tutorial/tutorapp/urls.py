from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("contacts/", views.contacts, name = "contacts"),
    path("digest/", views.digest, name = "digest"),
    path("tutors/", views.about, name = "tutors"),
    path("vacancies/", views.vacancies, name = "vacancies"),
    path("search/", SearchResultsView.as_view(), name = "search_results"),
    
]
