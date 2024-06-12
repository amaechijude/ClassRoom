from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        
    def save(self,commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user
    
    
class LoginForm(forms.Form):
    email_or_username = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"email or username"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder":"Enter Password"}))
    
    
class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "A ,-separated list of tags"}))
    class Meta:
        model = PostModel
        exclude = ('author', 'slug', 'created_at', 'pid', 'title', 'img')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ('author', 'slug', 'created_at', 'post')
        
