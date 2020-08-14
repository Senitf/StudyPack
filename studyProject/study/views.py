from django.shortcuts import render, redirect
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from .models import Content_1 ,Content_2
from .funcs import text_To_Image, file_division, file_mix
from django.core.files.storage import default_storage
import time
import os

# Create your views here.

def home(request):
    return render(request, 'study/index.html')

def upload(request):
    if request.method == 'POST':
        content_index = request.POST.get('content_index')
        if content_index == "simul":
            year = request.POST.get('year')
            month = request.POST.get('month')
            content_grade = request.POST.get('grade')
            category = request.POST.get('category')
            if category == "handmade":
                content_number_list = request.POST.getlist('content_number_list')
                file_name_prefix = year + "_" + month + "_" + content_grade + "_" + category
                content_file = request.FILES.get('content_file')
                default_storage.save(file_name_prefix + ".pdf", content_file)
                file_division('uploads/', file_name_prefix, content_number_list, 'uploads/images/content_1/')
                os.remove('uploads/' + file_name_prefix + ".pdf")
                for nums in content_number_list:
                    new_content = Content_1()
                    new_content.year = year
                    new_content.month = month
                    new_content.content_grade = content_grade
                    new_content.category = category
                    new_content.content_number = nums
                    new_content.content_file = 'uploads/images/cache/' + file_name_prefix + "_" + nums + ".pdf"
                    new_content.save()
                return redirect('home')
            else:
                content.content_number_begin = request.POST.get('content_number')
                content.content_number_end = content.content_number_begin
                content.content_text = request.POST.get('content_text')
                content.save()
                
                return redirect('home')

        else:
            content = Content_2()
            content.year = request.POST.get('year')
            content.content_label = request.POST.get('content_label')
            content.publisher = request.POST.get('publisher')
            content.author = request.POST.get('author')
            content.content_chapter = request.POST.get('content_chapter')
            content.category = request.POST.get('category')
            if content.category == "handmade":
                content.content_file = request.FILES.get('content_file')
                content.content_number_begin = request.POST.get('content_number_begin')
                content.content_number_end = request.POST.get('content_number_end')
                content.save()

                return redirect('home')
            else:
                content.content_number_begin = request.POST.get('content_number')
                content.content_number_end = content.content_number_begin
                content.content_text = request.POST.get('content_text')
                content.save()

                return redirect('home')
    else:
        return render(request, 'study/upload.html')

def download(request):
    if request.method == 'POST':
        if request.POST.get('content_index') == "simul":
            original_file_prefix = str(request.POST.get('year')) + "_" + str(request.POST.get('month')) + "_" + str(request.POST.get('grade')) + "_" + str(request.POST.get('category'))
            original_file_index_list = request.POST.getlist('content_number')
            filename = file_mix('uploads/images/cache/', original_file_prefix, original_file_index_list, 'uploads/images/cache/')
            wrapper = FileWrapper(open('uploads/images/cache/' + filename, 'rb'))
            response = HttpResponse(wrapper, content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename('uploads/images/cache/' + filename)
            return response
    return render(request, 'study/download.html')
    '''
    if request.method == 'POST':
        if request.POST.get('content_index') == "simul":
            data_set_1 = Content_1.objects.all()
            year = request.POST.get('year')
            month = request.POST.get('month')
            grade = request.POST.get('grade')
            if request.POST.get('category') == "handmade":
                number_list = request.POST.getlist('content_number')
            else:
        else:
            data_set_2 = Content_2.objects.all()
            label = request.POST.get('content_label')
            publisher = request.POST.get('publisher')
            chapter = reuquest.POST.get('content_chapter')
            if request.POST.get('category') == "handmade":
                number_list = request.POST.getlist('content_number')
            else:
    else:
    '''