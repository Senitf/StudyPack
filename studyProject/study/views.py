from django.shortcuts import render
from .models import Content_1 ,Content_2

# Create your views here.

def home(request):
    return render(request, 'study/index.html')

def upload(request):
    return render(request, 'study/upload.html')

def create_content_1(request):
    content = Content_1()
    content.grade = request.GET['grade']
    content.month = request.GET['month']
    content.content_type = request.GET['content_type']
    content.content_number = request.GET['content_number']
    content.category = request.GET['category']
    content.content_file = request.FILES['content_file']
    content.save()
    return redirect('')

def create_content_2(request):
    content = Content_2()
    content.publisher = request.GET['publisher']
    content.content_label = request.GET['content_label']
    content.content_type = request.GET['content_type']
    content.content_number = request.GET['content_number']
    content.content_file = request.FILES['content_file']
    content.save()
    return redirect('')