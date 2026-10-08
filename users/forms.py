from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Profile

class RegistrationForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta :
        model = User
        fields = [
            'username','email','password'
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone',
            'location',
            'skills',
            'experience',
            'resume',
            'profile_picture'
        ]