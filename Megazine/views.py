from django.shortcuts import render

# Create your views here.

from .models import Contact_Us, AboutFounder

def home(request):
    return render(request, "home.html")

def Contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        temp=Contact_Us(name=name,email=email,phone=phone,message=message)
        temp.save()
    return render(request, "contact.html")  

def Newspage(request):
    return render(request, "newspage.html") 

def About(request):
    about = AboutFounder.objects.all()
    context={
        'about':about
    }
    return render(request, "about.html", context)      

def Articles(request):
    art = Articlespage.objects.all()
    cont={
        'art':art
    }
    return render(request, "articles.html",cont) 