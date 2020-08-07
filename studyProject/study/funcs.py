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

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def file_division(file_name, file_index, original_file, new_path):
    
    pdf = PdfFileReader(originial_file)

    numberPages = pdf.getNumPages()

    for page in range(0, numberPages):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_name = file_name+file_index[page]+".pdf"
        save_path = os.path.join(new_path, output_name)

        with open(save_path, 'wb') as f:
            pdf_writer.write(f)