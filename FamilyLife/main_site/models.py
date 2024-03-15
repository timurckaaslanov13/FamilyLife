import random
import string
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.http import request
    

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)
    

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
    
    def __str__(self) -> str:
        return self.name

# Модель поста
class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
    
    objects = models.Manager()
    published = PublishedManager()
        
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Post, self).save(*args, **kwargs)
    

    
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})
    
    def __str__(self) -> str:
        return self.title



class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    text_feed = models.TextField(blank=True, verbose_name='Отзыв')