# Generated by Django 5.0 on 2023-12-12 18:49

import course.models
import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_course_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=pathlib.PureWindowsPath('C:/Users/kodokawai/Desktop/learning/university/IMPORTANT!/dlearn/uploads/default/default_image.png'), max_length=256, upload_to=course.models.course_directory_path),
        ),
    ]
