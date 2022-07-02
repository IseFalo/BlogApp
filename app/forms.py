# from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms


class PostForm(ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text', 'post_image')

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields =('comment_author', 'text')

class CreateUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']