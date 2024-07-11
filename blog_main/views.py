# home page views
from django.shortcuts import render
from blogs.models import Category, Blog


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status=1).order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status=1)
    print(posts)
    context = {'featured_posts': featured_posts, 'posts': posts}
    return render(request=request, template_name='home.html', context=context)