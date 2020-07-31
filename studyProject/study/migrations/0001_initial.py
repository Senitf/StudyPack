# Generated by Django 3.0.8 on 2020-07-31 05:53

from django.db import migrations, models
import study.funcs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=50)),
                ('content_grade', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('content_number_begin', models.CharField(max_length=50)),
                ('content_number_end', models.CharField(max_length=50)),
                ('content_text', models.TextField(blank=True)),
                ('content_file', models.ImageField(blank=True, upload_to=study.funcs.get_file_path_1)),
            ],
        ),
        migrations.CreateModel(
            name='Content_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('content_label', models.CharField(max_length=50)),
                ('content_chapter', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('content_number_begin', models.CharField(max_length=50)),
                ('content_number_end', models.CharField(max_length=50)),
                ('content_file', models.ImageField(blank=True, upload_to=study.funcs.get_file_path_2)),
                ('content_text', models.TextField(blank=True)),
            ],
        ),
    ]
