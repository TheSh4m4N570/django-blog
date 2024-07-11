# Create a context processor to get the categories and display them on all pages
from .models import Category


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}