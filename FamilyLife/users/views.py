from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from .forms import LoginUserForm, RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            user = authenticate(request, username=cd['username'], 
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
        
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))



# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'users/register.html'
#     extra_context = {'title': 'Регистрация'}
#     success_url = reverse_lazy('users:login')

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})
