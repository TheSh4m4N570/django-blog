from django import forms
from django.contrib.auth.forms import UserCreationForm

from blogs.models import Category, Blog
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured')


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','is_active', 'is_staff', 'is_superuser', 'password1',
                  'password2', 'groups', 'user_permissions')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','is_active', 'is_staff', 'is_superuser',
                  'groups', 'user_permissions')