from datetime import timedelta
from django.utils import timezone
import json
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from main_site.forms import AddPostForm, CommentForm
from main_site.models import Category, Feedback, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    # {'title': 'Добавить статью', 'url_name': 'add_page'},
    # {'title': 'Войти', 'url_name': 'login'},
    # {'title': 'Регистрация', 'url_name': 'regist'},
    
]

categories = Category.objects.all()

def index_main(request):
    today = timezone.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.all()
    post_new = Post.objects.filter(date_create__gte=last_week)
    best_post = Post.objects.all()[0]
    data = {'title': 'FamilyLife', 
            'menu': menu,
            'posts': posts,
            'best': best_post,
            'categories': categories,
            'post_new': post_new,
            }
    return render(request, 'main_site/home.html', context=data)


# def regist(request):
#     data = {'title': 'Регистрация', 
#             'menu': menu,
#             'categories': categories,
#             }
#     return render(request, 'main_site/registration.html', context=data)

def show_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    feedback = Feedback.objects.filter(post=post)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.user = request.user
            art.post = post
            art.save()
            return redirect('post', slug)
    else:
        form = CommentForm() 
    
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'categories': categories,
        'feedback': feedback,
        'form': form,
    }
    return render(request, 'main_site/post.html', data)



def about(request):
    data = {'title': 'О нас', 
            'menu': menu,
            'categories': categories,
            }
    return render(request, 'main_site/about.html', context=data)

@login_required
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.save()
            return redirect('home')
    else:
        form = AddPostForm()     
    data = {'title': 'Добавить пост', 
            'menu': menu,
            'categories': categories,
            'form': form
            }
    return  render(request, 'main_site/addpage.html', context=data)


# def login(request):
#     data = {'title': 'Войти', 
#             'menu': menu,
#             'categories': categories,
#             }
#     return  render(request, 'main_site/login.html', context=data)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.published.filter(category_id=category.pk)
    
    data = {
        'title': f'Категория: {category.name}',
        'menu': menu,
        'posts': posts,
        # 'categories':categories
        
    }
    return render(request, 'main_site/category.html', context=data)
