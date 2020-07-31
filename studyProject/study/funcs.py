from PIL import Image, ImageDraw

def text_To_Image(content):
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
 
    d = ImageDraw.Draw(img)
    d.text((10,10), content, fill=(255,255,0))
 
    return img

import uuid
import os

def get_file_path_1(instance, filename):
    filename = instance.year + "_" + instance.month + "_" + instance.content_grade + "_" + instance.category + "_" + instance.content_number_begin + "_" + instance.content_number_end + ".pdf"
    return os.path.join('images/content_1', filename)

def get_file_path_2(instance, filename):
    filename = object_name = instance.publisher + "_" + instance.author + "_" + instance.content_label + "_" + instance.content_chapter + "_" + instance.category + "_" +  instance.content_number_begin + "_" + instance.content_number_end + ".pdf"
    return os.path.join('images/content_2', filename)