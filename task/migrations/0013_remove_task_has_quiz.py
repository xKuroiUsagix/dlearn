# Generated by Django 4.0.4 on 2022-05-09 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_alter_usertask_done_at_alter_usertaskfile_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='has_quiz',
        ),
    ]
