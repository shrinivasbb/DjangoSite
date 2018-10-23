from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
        email = forms.EmailField()
        first_Name = forms.CharField(required=False)
        last_Name = forms.CharField(required=False)

        class Meta:
            model = User
            fields = ['username', 'first_Name', 'last_Name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

