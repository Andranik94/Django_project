from django.shortcuts import render
#from home import templates
# Create your views here.
from django.http import HttpResponse


def home_page(request):
    #return HttpResponse("<h4>te55stttt</h4>")
    return render(request, "home.html", {})


def about_as(request):
    return  HttpResponse("<h4>Abou as</h4>")
