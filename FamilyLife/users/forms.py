from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', 
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Логин"}))
    password = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-control ', 'id': "password", 'placeholder':"Пароль"}))
    
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
    
    
class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-control ', 'id': "password"}))
    password2 = forms.CharField(label='Повтор пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-control '}))
    
    email = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        
        labels = {
            'email': 'E-mail',
            
        }
        
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password1']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email