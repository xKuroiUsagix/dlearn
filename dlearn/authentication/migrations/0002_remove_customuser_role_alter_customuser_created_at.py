# Generated by Django 5.0.7 on 2024-07-21 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='CreatedAt'),
        ),
    ]
