from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text'}),
        required=True, max_length=20)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'input type': 'text'}),
        max_length=20, required=True)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'input type': 'text'}),
        max_length=20, required=True)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'type': 'email'}),
        required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This email is already taken")
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email has to end with @gmail.com")
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']