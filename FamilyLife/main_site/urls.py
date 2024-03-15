from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_main, name='home'),
    # path('regist/', views.regist, name='regist'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    # path('login/', views.login, name='login'),
    path('post/<slug:slug>/', views.show_post, name='post'),
    path('category/<slug:slug>/', views.category, name='category'),
]

