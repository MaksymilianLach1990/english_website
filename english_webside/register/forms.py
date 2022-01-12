from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()
    
    class Meta:
        model = User
        fields = ('username', 'age', 'email', 'password1', 'password2')
