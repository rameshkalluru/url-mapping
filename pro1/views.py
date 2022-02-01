from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def mark(request):
    return render(request,'mark.html')

def mass(request):
    return render(request,'mass.html')

def music(request):
    return render(request,'music.html')

def rock(request):
    return render(request,'rock.html')