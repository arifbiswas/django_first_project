from django.shortcuts import render

# Create your views here.
def app(request) : 
    return render(request,"app/test.html")
def contact(request) : 
    return render(request,"app/contact.html")