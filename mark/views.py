from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request,'hello.html')

def images(request):
    return render(request,'images.html')

def REELS(request):
    return render(request,'REELS.html')
