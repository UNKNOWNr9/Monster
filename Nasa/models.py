from django.db import models
from django.utils import timezone
from django.utils.html import format_html
# Create your models here.
class PostCategory(models.Model):
    Title = models.CharField(max_length=40, verbose_name='عنوان')
    Slug = models.SlugField(max_length=100, unique=True)
    Status = models.BooleanField(default=True, verbose_name='تیک وضعیت')
    Position = models.IntegerField(verbose_name='پوزیشن', unique=True)


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['Position']

    def __str__(self):
        return self.Title



class post(models.Model):
    STATUS_CHOICES = (
        ('p', 'published'),
        ('d', 'draft'),
    )

    Title = models.CharField(max_length=60, verbose_name='عنوان')
    Description = models.TextField(verbose_name='مشخصات')
    Image = models.ImageField(upload_to='Images', verbose_name='تصویر')
    Slug = models.SlugField(max_length=100, unique=True)
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت انتشار')
    Published = models.DateTimeField(default=timezone.now)
    Created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    Category = models.ManyToManyField(PostCategory, verbose_name='دسته بندی')


    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.Title

    def thumbnail_tag(self):
        return format_html("<img width=80 height=50 style='border-radius: 5px;' src='{}'>".format(self.Image.url))

    thumbnail_tag.short_description = "عکس"


