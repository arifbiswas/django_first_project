from django.http import HttpResponse
from django.shortcuts import render


def home(request) : 
#    return HttpResponse("Hello, World . you're visited on the HOME page . This page made by arifbiswas")
    return render(request, "website/index.html")

def about(request) : 
   return HttpResponse("Hello, World . you're visited on the ABOUT page . This page made by arifbiswas")

def contact(request) : 
   return HttpResponse("Hello, World . you're visited on the CONTACT page . This page made by arifbiswas")

