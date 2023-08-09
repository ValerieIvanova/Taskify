from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from taskify.profileApp.models import UserProfile

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'password-field'
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'password-field'
        }),
    )

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'password-field'
        }),
    )


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'age', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'profile_picture': forms.ClearableFileInput(attrs={'placeholder': 'Choose profile picture'}),
        }