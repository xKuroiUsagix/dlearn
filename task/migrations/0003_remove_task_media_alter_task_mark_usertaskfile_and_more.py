# Generated by Django 4.0 on 2021-12-13 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customuser_password'),
        ('task', '0002_remove_task_files_task_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='media',
        ),
        migrations.AlterField(
            model_name='task',
            name='mark',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Mark'),
        ),
        migrations.CreateModel(
            name='UserTaskFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to='media', verbose_name='Media')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='OwnerTaskFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to='media', verbose_name='Media')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
    ]