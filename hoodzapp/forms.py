from django import forms
from .models import Post, UserProfile
from django.contrib.auth.models import User


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['poster', 'pub_date']




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'phone', 'projects', 'pic')
        # exclude = ['user','pub_date']