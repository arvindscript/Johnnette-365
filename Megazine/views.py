from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, "home.html")

def Contact(request):
    return render(request, "contact.html")    

def Page(request):
    return render(request, "page.html")       