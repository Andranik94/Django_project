from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def home_page(request):
    return render(request, "home.html", {})


def about_as(request):
    return HttpResponse("<h4>Abou as</h4>")
