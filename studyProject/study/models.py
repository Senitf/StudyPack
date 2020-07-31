from django.db import models
from uuid import uuid4
from django.utils import timezone
from .funcs import get_file_path_1, get_file_path_2

# Create your models here.

class Content_1(models.Model): #모의고사
    def __str__(self):
        object_name = self.year + "_" + self.month + "_" + self.content_grade + "_" + self.category + "_" + self.content_number_begin + "_" + self.content_number_end
        return object_name

    '''
    def file_upload_to(instance, filename):
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        uuid_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])
    '''

    year = models.CharField(max_length=50) #발행년도
    month = models.CharField(max_length=50) #월
    content_grade = models.CharField(max_length=50)  #유형
    category = models.CharField(max_length=50) #교재유형
    content_number_begin = models.CharField(max_length=50) #지문번호
    content_number_end = models.CharField(max_length=50) #지문번호
    content_text = models.TextField(blank=True)
    content_file = models.ImageField(blank=True, null=False, upload_to=get_file_path_1) #파일

class Content_2(models.Model): #교과서
    def __str__(self):
        object_name = self.publisher + "_" + self.author + "_" + self.content_label + "_" + self.content_chapter + "_" + self.category + "_" +  self.content_number_begin + "_" + self.content_number_end
        return object_name
    
    '''
    def file_upload_to(instance, filename):
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        uuid_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])
    '''

    year = models.CharField(max_length=50) #발행년도
    publisher = models.CharField(max_length=50) #출판사
    author = models.CharField(max_length=50) #저자
    content_label = models.CharField(max_length=50)#교재종류
    content_chapter = models.CharField(max_length=50) #단원
    category = models.CharField(max_length=50) #교재유형
    content_number_begin = models.CharField(max_length=50) #지문번호
    content_number_end = models.CharField(max_length=50) #지문번호
    content_file = models.ImageField(blank=True, null=False, upload_to=get_file_path_2) #파일
    content_text = models.TextField(blank=True)