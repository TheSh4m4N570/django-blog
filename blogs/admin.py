from django.contrib import admin
from .models import Category, Blog, Comment

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status', 'is_featured')


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)