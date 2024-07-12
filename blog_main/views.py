# home page views
from django.shortcuts import render
from blogs.models import Category, Blog
from social.models import About, SocialMedia


def home(request):
    about = About.objects.get(pk=1)
    social_media = SocialMedia.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status=1).order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status=1)
    print(posts)
    context = {'featured_posts': featured_posts, 'posts': posts, 'about': about, 'social_media':social_media}
    return render(request=request, template_name='home.html', context=context)

