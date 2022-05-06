# Generated by Django 3.2.8 on 2022-03-29 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultdetail',
            name='text_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resultdetail',
            name='is_right',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resultdetail',
            name='option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.option'),
        ),
    ]