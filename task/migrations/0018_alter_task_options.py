# Generated by Django 4.0.5 on 2022-06-21 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0017_alter_usertask_mark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['created_at']},
        ),
    ]
