# Generated by Django 3.2.8 on 2021-12-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20211209_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='password',
            field=models.CharField(default=123, max_length=20, verbose_name='Password'),
            preserve_default=False,
        ),
    ]
