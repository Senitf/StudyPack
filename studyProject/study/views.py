from django.shortcuts import render
from .models import Content_1 ,Content_2

# Create your views here.

def home(request):
    return render(request, 'study/index.html')

def upload(request):
    return render(request, 'study/upload.html')

def download(request):
    return render(request, 'study/download.html')

def create(request):
    content_index = request.GET['content_index']
    if content_index == "모의고사":
        content = Content_1()
        content.year = request.GET['year']
        content.month = request.GET['month']
        content.content_grade = request.GET['grade']
        #content.content_number = request.GET['content_number']
        #content.category = request.GET['category']
        content.content_file = request.FILES['content_file']
        content.save()
    else:
        content = Content_1()
        content.grade = request.GET['grade']
        content.month = request.GET['month']
        content.content_type = request.GET['content_type']
        content.content_number = request.GET['content_number']
        content.category = request.GET['category']
        content.content_file = request.FILES['content_file']
        content.save()

    return redirect('')