from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Blog


def home_page(request):
    context ={}
    blogs = Blog.objects.all()
    context['blogs']= blogs
    return render(request, "home.html", context)


def about_us(request):
    return render(request, "about_us.html", {})

def contact_us(request):
    return render(request, "contact_us.html", {})

def blog_detail(request,pk):
    print("------------")
    print("------------")

    context = {}
    blog = Blog.objects.get(id=pk)
    context['blog'] = blog
    return render(request, "blog_detail.html", context)