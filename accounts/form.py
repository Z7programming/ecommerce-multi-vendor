from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class sign_upForm(UserCreationForm):
    class Meta:
        model = User
        # fields= '__all__'
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class profileForm(forms.ModelForm):
    photo = forms.ImageField(label=False,
                             widget=forms.FileInput(attrs={'style': 'display:none;'}))

    class Meta:
        model = Profile
        exclude = ['user', 'spend', 'sall_count', ]
