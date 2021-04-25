from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
from .models import Tutors
from django.db.models import Q
from django.views.generic import ListView


def home(request):
    return render(request, "tutorapp/base.html")

def about(request):
    return render(request, 'tutorapp/about.html')
def contacts(request):
    return render(request, "tutorapp/contacts.html")

def digest(request):
    return render(request, "tutorapp/digest.html")
def promo(request):
    return render(request, "tutorapp/promo.html")

def tutors(request):
    return render(request, "tutorapp/tutors.html")

def vacancies(request):
    return render(request, "tutorapp/vacancies.html")


class SearchResultsView(ListView):
    model = Tutors
    template_name='search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        # if query.islower()():
        #     return query.upper()
        object_list = Tutors.objects.filter(
            Q(name__icontains = query) | Q(disciple__icontains = query)
        )
        return object_list
    
# Create your views here.
