# Generated by Django 4.0 on 2021-12-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='files',
        ),
        migrations.AddField(
            model_name='task',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='Files'),
        ),
    ]
