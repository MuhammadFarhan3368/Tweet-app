from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        # widgets = {
        #     'text': forms.Textarea(attrs={'placeholder': 'What\'s happening?', 'rows': 3, 'cols': 40}),
        #     'photo': forms.ClearableFileInput(attrs={'multiple': True}),
        # }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email Address")
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)