# Generated by Django 4.0 on 2022-05-26 23:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_usertask_is_examined'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertaskfile',
            name='done_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertaskfile',
            name='too_late',
            field=models.BooleanField(default=False),
        ),
    ]
