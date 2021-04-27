from django.db import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        models=User
        fields = ('username', 'email', 'password1', 'password2')

class InfoProfile(forms.modelForm):
    class Meta():
        model=Profile
        fields = ('country')