from django.db import models
from uuid import uuid4
from django.utils import timezone

# Create your models here.

class content_1(models.Model):
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

    photo = models.ImageField(upload_to=date_upload_to)

    grade = models.CharField(max_length=5)
    month = models.CharField(max_length=10)
    content_type = models.CharField(max_length=10)
    content_number = models.CharField(max_length=5)
    category = models.CharField(max_length=10)
    content_file = models.ImageField(blank=False, null=False, upload_to=file_upload_to)

class content_2(models.Model):
    def __str__(self):
        return self.file_name
    
    def image_upload_to(instance, filename):
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        uuid_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])

    photo = models.ImageField(upload_to=date_upload_to)

    publisher = models.CharField(max_length=10)
    content_label = models.CharField(max_length=10)
    content_type = models.CharField(max_length=10)
    content_number = models.CharField(max_length=5)
    content_file = models.ImageField(blank=False, null=False, upload_to=file_upload_to)