from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category


# Create your views here.


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(
        category_id=category_id,
        status=1
    )
    try:
        category_name = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect(to="404.html")
    context = {'posts': posts, 'category_name': category_name}
    return render(request, template_name='post_by_category.html', context=context)
