from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, "home.html")

def Contact(request):
    return render(request, "contact.html")    

def News(request):
    return render(request, "newspage.html")