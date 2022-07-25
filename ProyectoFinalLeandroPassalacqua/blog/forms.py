from dataclasses import fields
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#import datetime

class Project_Form(forms.ModelForm):
     
    class Meta:
        model= Post
        fields='__all__'



class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1: forms.CharField(label='Constraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirma Constraseña', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password1','password2','email']
        help_texts={k:"" for k in fields}   


class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}