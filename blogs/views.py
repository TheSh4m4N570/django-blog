from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category, Comment
from django.db.models import Q


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


def single_post(request, slug):
    post = get_object_or_404(Blog, slug=slug, status=1)
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    # comments
    comments = Comment.objects.filter(blog=post)
    comment_count = len(comments)
    print(comments)
    context = {'post': post, 'comments': comments, 'comment_count': comment_count}
    return render(request, template_name='single_post.html', context=context)


def search(request):
    search_term = request.GET.get('keyword')
    posts = Blog.objects.filter(Q(title__icontains=search_term) | Q(short_description__icontains=search_term)|
                                Q(blog_body__icontains=search_term), status=1)
    context = {'posts': posts, 'search_term': search_term}
    print(search_term)
    return render(request, template_name='search.html', context=context)

