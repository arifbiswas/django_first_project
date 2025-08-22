from django.http import HttpResponse
from django.shortcuts import render


def home(request) : 
   # return HttpResponse("Hello, World . you're visited on the HOME page . This page made by arifbiswas")
    return render(request, "website/index.html")

def about(request) : 
   return render(request, "website/about.html")

def contact(request) : 
   return render(request, "website/contact/index.html")

