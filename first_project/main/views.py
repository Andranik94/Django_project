from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def home_page(request):
    return render(request, "home.html", {})


def about_us(request):
    return render(request, "about_us.html", {})

def contact_us(request):
    return render(request, "contact_us.html", {})
