from django.shortcuts import render, redirect
from .models import Content_1 ,Content_2
from .funcs import text_To_Image, file_division

# Create your views here.

def home(request):
    return render(request, 'study/index.html')

def upload(request):
    if request.method == 'POST':
        content_index = request.POST.get('content_index')
        if content_index == "simul":
            content = Content_1()
            content.year = request.POST.get('year')
            content.month = request.POST.get('month')
            content.content_grade = request.POST.get('grade')
            content.category = request.POST.get('category')
            if content.category == "handmade":
                content_number_list = request.getlist('content_number_list')
                file_name_prefix = content.year + "_" + content.month + "_" + content.catent_grade + "_" + content.category+ "_"
                content_file = request.FILES.get('content_file')
                file_division("../uploads/images/content_1", file_name_prefix, content_number_list, content_file, '..files/')
                for nums in content_number_list:
                    content.number = nums
                    content.content_file = '..files/' + file_name_prefix + "_" + nums
                    content.save

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
    '''
    if request.method == 'POST'
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
    return render(request, 'study/download.html')