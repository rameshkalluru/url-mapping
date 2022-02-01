from django.shortcuts import render

# Create your views here.


def nag(request):
    return render(request,'nag.html')

def nagu(request):
    return render(request,'nagu.html')

def nagaraju(request):
    return render(request,'nagaraju.html')