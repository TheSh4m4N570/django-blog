from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blogs.models import Category, Blog
from .forms import CategoryForm, PostForm
from django.template.defaultfilters import slugify


# Create your views here.

@login_required(login_url='/login')
def dashboard(request):
    categories_count = Category.objects.count()
    blogs_count = Blog.objects.count()
    context = {'categories_count': categories_count, 'blogs_count': blogs_count}
    return render(request, template_name="dashboard/dashboard.html", context=context)


def categories(request):
    dash_categories = Category.objects.all()
    context = {'categories': dash_categories}
    return render(request, template_name="dashboard/categories.html", context=context)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    context = {'form': form}
    return render(request, 'dashboard/add_category.html', context=context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(to='categories')
    context = {'category': category, 'form': form}
    return render(request, 'dashboard/edit_category.html', context=context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect(to='categories')


# Posts Views
def posts(request):
    all_posts = Blog.objects.all()
    context = {'all_posts': all_posts}
    return render(request, template_name="dashboard/posts.html", context=context)


# Add Post
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = PostForm
    context = {'form': form}
    return render(request, template_name="dashboard/add_post.html", context=context)


# Edit ost
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = PostForm(instance=post)
    context = {'form': form, 'post': post}
    return render(request, 'dashboard/edit_post.html', context=context)


# Delete post
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect(to='posts')