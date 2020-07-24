from django.db import models
from uuid import uuid4
from django.utils import timezone

# Create your models here.

class Content_1(models.Model): #모의고사
    def __str__(self):
        return self.file_name
    
    def file_upload_to(instance, filename):
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        uuid_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])

    year = models.CharField(max_length=5) #발행년도
    month = models.CharField(max_length=10) #월
    content_grade = models.CharField(max_length=10)  #유형
    #content_number = models.CharField(max_length=5) #지문번호
    #category = models.CharField(max_length=10) #교재유형
    content_file = models.ImageField(blank=False, null=False, upload_to=file_upload_to) #파일

class Content_2(models.Model): #교과서
    def __str__(self):
        return self.file_name
    
    def file_upload_to(instance, filename):
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        uuid_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])

    publisher = models.CharField(max_length=10) #출판사
    content_label = models.CharField(max_length=10)#교재종류
    content_type = models.CharField(max_length=10) #유형
    content_number = models.CharField(max_length=5) #지문번호
    content_file = models.ImageField(blank=False, null=False, upload_to=file_upload_to) #파일