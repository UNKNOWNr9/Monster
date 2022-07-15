# Generated by Django 4.0.4 on 2022-07-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nasa', '0005_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Is_Special',
            field=models.BooleanField(default=False, verbose_name='پست ویژه'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('d', 'پیشنویس'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], max_length=1, verbose_name='وضعیت انتشار'),
        ),
    ]
