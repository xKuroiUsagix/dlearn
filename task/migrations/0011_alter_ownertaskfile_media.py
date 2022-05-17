# Generated by Django 4.0.4 on 2022-05-07 09:24

from django.db import migrations, models
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_alter_ownertaskfile_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownertaskfile',
            name='media',
            field=models.FileField(blank=True, max_length=256, null=True, upload_to=task.models.owner_directory_path, verbose_name='Media'),
        ),
    ]