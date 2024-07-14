# home page views
from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from social.models import About, SocialMedia
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib import auth


def home(request):
    about = About.objects.get(pk=1)
    social_media = SocialMedia.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status=1).order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status=1)
    print(posts)
    context = {'featured_posts': featured_posts, 'posts': posts, 'about': about, 'social_media':social_media}
    return render(request=request, template_name='home.html', context=context)


# Register Function
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, template_name='register.html', context=context)


# User login
def login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                print("Invalid login credentials")
    form = CustomUserLoginForm()
    context = {'form': form}
    return render(request, template_name='login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('login')