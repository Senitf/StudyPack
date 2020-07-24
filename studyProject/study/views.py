from django.shortcuts import render, redirect
from .models import Content_1 ,Content_2

# Create your views here.

def home(request):
    return render(request, 'study/index.html')

def upload(request):
    if request.method == 'POST':
        content_index_1 = request.POST.get('content_index_1')
        content_index_2 = request.POST.get('content_index_2')
        if content_index_1 == "simul":
            content = Content_1()
            content.year = request.POST.get('year')
            content.month = request.POST.get('month')
            content.content_grade = request.POST.get('grade')
            content.category = request.POST.get('category')
            if content.category == "handmade":
                content.content_file = request.POST.FILES['content_file']
                content.content_number_begin = request.POST.get('content_number_begin')
                content.content_number_end = request.POST.get('content_number_end')
                content.save()
        else:
            content = Content_1()
            content.year = request.POST.get('year')
            content.month = request.POST.get('month')
            content.content_grade = request.POST.get('grade')
            content.category = request.POST.get('category')
            if content.category == "handmade":
                content.content_file = request.POST.get('content_file')
                content.content_number_begin = request.POST.get('content_number_begin')
                content.content_number_end = request.POST.get('content_number_end')
                content.save()
                return redirect('home')
    else:
        return render(request, 'study/upload.html')

def download(request):
    return render(request, 'study/download.html')