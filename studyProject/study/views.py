from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'study/index.html')

def upload(request):
    return render(request, 'study/upload.html')