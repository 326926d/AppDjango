from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime


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



# Create your views here.
